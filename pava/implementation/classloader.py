import datetime
import os
import subprocess
import sys
import traceback
import zipfile
from collections import namedtuple

import jawa
import peak.util.assembler as asm

import opcodes

VERBOSE = opcodes.VERBOSE
DEBUG = opcodes.DEBUG
HOME = os.path.join(os.path.expanduser("~"), os.path.join('pava', 'classes'))

sys.path.append(HOME)
loaded_classes = set()

RESERVED_WORDS = {
    'and', 'assert', 'break', 'class', 'continue',
    'def', 'del', 'elif', 'else', 'except',
    'exec', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda',
    'not', 'or', 'pass', 'print', 'raise',
    'return', 'try', 'while',
    # some specific ones for pava
    'set', 'dict', 'with', 'yield'
}


def get_boot_path():
    java = subprocess.Popen(['java', '-verbose', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in java.stdout.readlines():
        if line.startswith('[Opened'):
            return [ (line[8:-2]) ]


def set_classpath(cp):
    assert isinstance(cp, list), 'classpath should be a list of directories and archives'
    try:
        index_class_path(get_boot_path() + cp)
    except Exception as e:
        print '##### ERROR:', traceback.format_exc(e)


def index_class_path(path):
    for p in path:
        if not os.path.exists(p):
            continue
        marker = os.path.normpath(p)
        marker = marker.replace('\\', '_').replace(' ', '_').replace(':', '_').replace('.', '_')
        marker = os.path.join(HOME, marker + '.log')
        if os.path.exists(marker):
            return
        if os.path.isdir(p):
            add_directory(p)
        else:
            add_jar(p)
        with open(marker, 'w') as fout:
            fout.write('%s' % datetime.datetime.now())


def add_jar(jar_path):
    if DEBUG:
        print 'add classpath: ', jar_path
    with zipfile.ZipFile(jar_path, 'r') as jar:
        for n, entry in enumerate(jar.infolist()):
            if entry.filename.endswith('.class'):
                fragments = map(replace_reserved_names, entry.filename[:-6].split('/'))
                module_name = str('.'.join(fragments[:-1]))
                class_name = replace_reserved_names(str(fragments[-1]))
                with jar.open(entry) as file:
                    add_class(module_name, class_name, file)


def add_directory(dir_path):
    if DEBUG:
        print 'add classpath: ', dir_path
    def visit(arg, dir_name, file_names):
        for file_name in file_names:
            if file_name.endswith('.class'):
                module_path = os.path.normpath(dir_name[len(dir_path) + 1:])
                fragments = map(replace_reserved_names, module_path.replace('/', '.').replace('\\', '.').split('.'))
                module_name = str('.'.join(fragments))
                class_name = fix_dollar_sign(file_name[:-6])
                with open(os.path.join(dir_name, file_name)) as fin:
                    add_class(module_name, class_name, fin)
    os.path.walk(dir_path, visit, '')


def fix_dollar_sign(class_name):
    return class_name.replace('$', '__')


def add_class(module_name, class_name, fin):
    loaded_classes.add((module_name, class_name))
    if VERBOSE and len(loaded_classes)%100 == 0:
        print 'loaded', len(loaded_classes), 'classes'
    try:
        save_class(module_name, class_name, fin)
    except Exception as e:
        print '##### ERROR:', traceback.format_exc(e)


def get_module_path(module_name, home=HOME):
    path = os.path.join(home)
    parent_path = None
    package_name = ''
    for fragment in module_name.split('.'):
        fragment = replace_reserved_names(fragment)
        package_name = '.'.join([package_name, fragment]) if package_name else fragment
        path = os.path.join(path, fragment)
        if not os.path.exists(path):
            os.makedirs(path)
            init = os.path.join(path, '__init__.py')
            with open(init, 'w') as fout:
                fout.write('')
        if parent_path:
            init = os.path.join(parent_path, '__init__.py')
            with open(init, 'r') as fin:
                contents = fin.read() or init_module(module_name)
                package = '%s = pava.JavaPackage("%s")\n\n' % (fragment, package_name)
                if not package in contents:
                    with open(init, 'w') as fout:
                        fout.write(contents + '\n' + package)
        parent_path = path
    return os.path.join(path, '__init__.py')


def get_class_header(class_name):
    return 'class %s(object):' % class_name


def init_module(module_name):
    return '# This is Java package %s\n\nimport pava\nfrom pava import nan, inf\n\n' % module_name

def save_class(module_name, class_name, java_input_file):
    header = get_class_header(class_name)
    path = get_module_path(module_name)
    with open(path, 'r') as fin:
        contents = fin.read() or init_module(module_name)
    if not header in contents:
        contents += transpile_class(module_name, class_name, java_input_file)
        with open(path, 'w') as fout:
            fout.write(contents)


def replace_reserved_names(name):
    if name in RESERVED_WORDS:
        return '__%s__' % name
    if name == '<init>': return '__init__'
    if name == '<clinit>': return '__clinit__'
    name = name.replace('$', '__')
    name = name.replace('-', '__')
    return name


def transpile_class(module_name, class_name, input_file):
    if DEBUG:
        print 'Load Java class %s.%s' % (module_name, class_name)
    java_class_file = jawa.ClassFile(input_file)
    class_object = generate_python_class(module_name, class_name, java_class_file)
    lines = ['', get_class_header(class_name)]
    for field in class_object.fields:
        if field.static:
            lines.append('    %s = None # %s' % (replace_reserved_names(field.name), field.type))
    for fn in class_object.functions:
        name = replace_reserved_names(fn.name)
        definition = ', '.join(repr(value)for value in [
            fn.argcount, fn.nlocals, fn.stacksize, fn.flags, fn.codestring, fn.constants,
            fn.names, fn.varnames, fn.filename, name, fn.firstlineno, fn.lnotab,
            fn.modules, fn.static
        ])
        lines.append('    %s = pava.method(%s)' % (name, definition))
    if len(lines) == 2:
        lines.append('    pass')
    lines.append('')
    if class_object.natives:
        lines.append('from implementation.natives.%s.%s import add_native_methods' % (module_name, class_name))
        lines.append('add_native_methods(%s)' % class_name)
        lines.append('')
    return '\n'.join(lines)


Class = namedtuple('Class', [
    'fields', 'functions', 'natives'
])
Field = namedtuple('Field', [
    'name', 'type', 'static'
])
Function = namedtuple('Function', [
    'argcount', 'nlocals', 'stacksize', 'flags', 'codestring',
    'constants', 'names', 'varnames', 'filename', 'name',
    'firstlineno', 'lnotab', 'modules', 'static'
])
NativeMethod = namedtuple('NativeMethod', [
    'name', 'args', 'static'
])


def generate_python_class(module_name, class_name, class_file):
    class_object = Class([], [], [])
    constants = dict((c.index, c) for c in class_file.constants)
    for field in class_file.fields:
        is_static = field.access_flags.get('acc_static')
        class_object.fields.append(Field(field.name.value, field.descriptor.value, is_static))
    for method in class_file.methods:
        is_static = method.access_flags.get('acc_static')
        is_native = method.access_flags.get('acc_native')
        file_name = class_name + '.java'
        method_name = replace_reserved_names(method.name.value)
        code, imports = compile_method('%s.%s' % (module_name, class_name), method, constants, file_name, is_static)
        if is_native:
            class_object.natives.append(NativeMethod(method_name, method.args, is_static))
        else:
            method = create_function(code, imports, is_static)
            class_object.functions.append(method)
    add_native_methods(module_name, class_name, class_object.natives)
    return class_object


def create_function(code, imports, is_static):
    return Function(
        code.co_argcount, len(code.co_varnames),
        code.co_stacksize, code.co_flags, code.co_code.tostring(),
        tuple(code.co_consts), tuple(code.co_names),
        tuple(code.co_varnames), code.co_filename,
        code.co_name, code.co_firstlineno, code.co_lnotab.tostring(),
        imports, is_static
    )


def add_native_methods(module_name, class_name, methods):
    if not methods:
        return
    natives = os.path.join(os.path.dirname(__file__), 'natives')
    dirname = os.path.dirname(get_module_path(module_name, home=natives))
    native_path = os.path.join(dirname, class_name + '.py')
    if os.path.exists(native_path):
        return
    with open(native_path, 'a') as fout:
        fout.write('def add_native_methods(clazz):\n')
        for method in methods:
            fout.write('    def %s(%s):\n' % (method.name, ', '.join(['a%d' %n for n in range(len(method.args))])))
            fout.write('        raise NotImplementedError()\n\n')
        for method in methods:
            target = 'staticmethod(%s)' % method.name if method.static else method.name
            fout.write('    clazz.%s = %s\n' % (method.name, target))
        fout.write('\n')

if False:
    # Custom initialization code

    class PythonPrintStream(object):
        def println(self, s):
            print s
    clazz.setOut0(PythonPrintStream())

def compile_method(class_name, method, constants, filename, is_static):
    if DEBUG:
        print 'compile', class_name, method
    code = asm.Code()
    code.co_name = replace_reserved_names(str(method.name.value))
    code.co_filename = str(filename)

    # parameters added to code by pava
    code.stack_depth = []
    code.java_bytecodes = []
    code.module_names = set()
    code.jumps = []

    if not method.code:
        asm.Return(None, code)
    else:
        exception_table = method.code.exception_table
        instructions = list(method.code.disassemble())
        first_exception_index = sys.maxint
        if exception_table:
            first_exception_index = min(handler for _, _, handler, _ in exception_table)
            # TODO: properly handle exception ranges
        flags = method.access_flags
        flags = ', '.join([k for k,v in flags.to_dict().iteritems() if v])
        args =  [] if is_static else ['self']
        for n in xrange(method.code.max_locals):
            args.append('a%d' % n)
        for n,ins in enumerate(instructions):
            if ins.pos >= first_exception_index:
                break
            try:
                operands = opcodes.resolve_operands(constants, ins.operands)
                opcodes.convert(ins.mnemonic, code, ins.pos, args, *operands)
            except Exception as e:
                print flags, '%s.%s()' % (class_name, method.name.value), method.args, len(loaded_classes)
                if VERBOSE:
                    print 'Exception handlers start at', first_exception_index
                dump(code)
                try:
                    for ins in instructions[n:n+7]:
                        print ' '*51, '###', str(ins.pos).rjust(3), ins.mnemonic,
                        print opcodes.resolve_operands(constants, ins.operands)
                except Exception:
                    pass
                print '##### ERROR:', traceback.format_exc(e)
                # raise e
    if DEBUG:
        dump(code)
    return code, code.module_names

def dump(code):
    """Disassemble code in a symbolic manner, i.e., without offsets"""
    co_names = code.co_names
    co_consts = [repr(x) for x in code.co_consts]
    co_varnames = code.co_varnames
    cmp_ops = asm.cmp_op
    free = code.co_cellvars + code.co_freevars
    labels = {}
    instructions = list(asm.iter_code(code.co_code.tostring()))
    lbl = [jump for start, op, arg, jump, end in instructions if jump is not None]
    lbl.sort()
    for jump in lbl:
        labels.setdefault(jump, "L%d:" % (len(labels)+1))

    i = 0
    while i<len(instructions):
        start, op, arg, jump, end = instructions[i]
        ln = labels.get(start, '').ljust(4)
        if i<len(instructions)-1 and op==asm.DUP_TOP and instructions[i+1][1] in (asm.POP_JUMP_IF_FALSE, asm.POP_JUMP_IF_TRUE):
            s, op, arg, jump, end = instructions[i+1]
            ln+=' '+str(start).rjust(3)+' '+['JUMP_IF_FALSE', 'JUMP_IF_TRUE'][op==asm.POP_JUMP_IF_TRUE].ljust(13)
            i+=1
        elif op in (asm.JUMP_IF_TRUE_OR_POP, asm.JUMP_IF_FALSE_OR_POP):
            ln += ' ' + str(start).rjust(3) + ' ' + asm.opname[op][:-7].ljust(13)
        else:
            ln += ' ' + str(start).rjust(3) + ' ' + asm.opname[op].ljust(13)
        if jump is not None:
            ln += ' ' + (labels[jump][:-1] + '(%d)' % jump).rjust(12)
        elif arg is not None:
            ln += ' ' + repr(arg).rjust(10)
            if op in asm.argtype:
                try:
                    ln += ' %s' % (locals()[asm.argtype[op]][arg].ljust(20))
                except:
                    ln += ' %s %s ??????' % (asm.argtype[op], arg)
        ln += ' ' * (50 - len(ln))
        for index, (bytecode, pos, args) in code.java_bytecodes:
            if index == start:
                ln += '  ### %s %s %s' % (str(pos).rjust(3), bytecode, args)
        print(ln)
        if op in (asm.JUMP_IF_TRUE_OR_POP, asm.JUMP_IF_FALSE_OR_POP):
            print('        '+''.ljust(7) + ' POP_TOP')
        i+=1
