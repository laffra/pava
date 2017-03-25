import os
import subprocess
import sys
import zipfile
import traceback

import jawa
import peak.util.assembler as asm

from collections import namedtuple

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
        if os.path.isdir(p):
            add_directory(p)
        else:
            add_jar(p)


def add_jar(jarpath):
    # return
    with zipfile.ZipFile(jarpath, 'r') as jar:
        for n, entry in enumerate(jar.infolist()):
            if entry.filename.endswith('.class'):
                fragments = entry.filename[:-6].split('/')
                module_name = str('.'.join(fragments[:-1]))
                class_name = replace_reserved_names(str(fragments[-1]))
                with jar.open(entry) as file:
                    add_class(module_name, class_name, file)


def add_directory(dir_path):
    def visit(arg, dir_name, file_names):
        for file_name in file_names:
            if file_name.endswith('.class'):
                module_path = os.path.normpath(dir_name[len(dir_path) + 1:])
                module_name = module_path.replace('/', '.').replace('\\', '.')
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


def get_module_path(module_name):
    path = os.path.join(HOME)
    parent_path = None
    for fragment in module_name.split('.'):
        fragment = replace_reserved_names(fragment)
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
                import_statement = 'import %s\n\n' % fragment
                if not import_statement in contents:
                    with open(init, 'w') as fout:
                        fout.write(contents + '\n' + import_statement)
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
    lines = [ get_class_header(class_name) ]
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
    if len(lines) == 1:
        lines.append('    pass')
    lines.append('')
    return '\n'.join(lines)


Class = namedtuple('Class', [
    'fields', 'functions'
])
Field = namedtuple('Field', [
    'name', 'type', 'static'
])
Function = namedtuple('Function', [
    'argcount', 'nlocals', 'stacksize', 'flags', 'codestring',
    'constants', 'names', 'varnames', 'filename', 'name',
    'firstlineno', 'lnotab', 'modules', 'static'
])


def generate_python_class(module_name, class_name, class_file):
    class_object = Class([], [])
    for field in class_file.fields:
        is_static = field.access_flags.get('acc_static')
        class_object.fields.append(Field(field.name.value, field.descriptor.value, is_static))
    for method in class_file.methods:
        is_static = method.access_flags.get('acc_static')
        is_native = method.access_flags.get('acc_native')
        if is_native:
            print 'missing native method: %s.%s.%s() %s' % (module_name, class_name, method.name.value, method.args)
        filename = class_name + '.java'
        constants = dict((c.index, c) for c in class_file.constants)
        code, imports = compile_method('%s.%s' % (module_name, class_name), method, constants, filename, is_static)
        class_object.functions.append(Function(
            code.co_argcount, len(code.co_varnames),
            code.co_stacksize, code.co_flags, code.co_code.tostring(),
            tuple(code.co_consts), tuple(code.co_names),
            tuple(code.co_varnames), code.co_filename,
            code.co_name, code.co_firstlineno, code.co_lnotab.tostring(),
            imports, is_static
        ))
    return class_object


def compile_method(class_name, method, constants, filename, is_static):
    code = asm.Code()
    code.co_name = str(method.name.value)
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
