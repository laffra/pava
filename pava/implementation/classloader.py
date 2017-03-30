import datetime
import new
import os
import subprocess
import sys
import traceback
import zipfile
from itertools import islice
from collections import namedtuple

import peak.util.assembler as asm
from javaruntime import decompile_java_class_file
from javaruntime import decompile_java_classes

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

JAVA = 'C:/Program Files/Java/jdk1.8.0_121/bin/java'


def get_boot_path():
    java = subprocess.Popen([JAVA, '-verbose', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in java.stdout.readlines():
        if line.startswith('[Opened'):
            return [ (line[8:-2]) ]


def set_classpath(cp):
    assert isinstance(cp, list), 'classpath should be a list of directories and archives'
    try:
        index_class_path(list(set(get_boot_path() + cp)))
    except Exception as e:
        print '##### ERROR:', traceback.format_exc(e)


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


CLASS_PATH_CHUNK_SIZE = 400

def index_class_path(path):
    classes = []
    for p in path:
        if not os.path.exists(p):
            raise ValueError('Class path entry does not exist: "%s"' % p)
        if classpath_already_marked(p):
            continue
        if os.path.isdir(p):
            classes.extend(add_directory(p))
        else:
            classes.extend(add_jar(p))
        add_classpath_marker(p)
    cp = ';'.join(path)
    count = 0
    for n, class_names in enumerate(chunk(classes, CLASS_PATH_CHUNK_SIZE)):
        for class_file in decompile_java_classes(class_names, cp):
            try:
                save_class(class_file)
            except Exception as e:
                if DEBUG:
                    raise e
        count += len(class_names)
        print 'Loaded %d classes - %d%%' % (count, count * 100 / len(classes))


def get_classpath_marker(p):
    marker = os.path.normpath(p)
    marker = marker.replace('\\', '_').replace(' ', '_').replace(':', '_').replace('.', '_')
    marker = os.path.join(HOME, marker + '.log')
    return marker

def classpath_already_marked(path):
    return os.path.exists(get_classpath_marker(path))

def add_classpath_marker(path):
    marker = get_classpath_marker(path)
    with open(marker, 'w') as fout:
        fout.write('%s' % datetime.datetime.now())


def add_jar(jar_path):
    if DEBUG:
        print 'add classpath: ', jar_path
    class_names = []
    with zipfile.ZipFile(jar_path, 'r') as jar:
        for n, entry in enumerate(jar.infolist()):
            if entry.filename.endswith('.class'):
                class_names.append(entry.filename[:-6].replace('/', '.'))
    return class_names


def add_directory(dir_path):
    if DEBUG:
        print 'add classpath: ', dir_path
    class_names = []
    def visit(arg, dir_name, file_names):
        for file_name in file_names:
            if file_name.endswith('.class'):
                dir_name = dir_name[len(dir_path)+1:]
                class_names.append('%s.%s' % (dir_name.replace('/', '.'), file_name[:-6]))
    os.path.walk(dir_path, visit, '')
    return class_names



def fix_dollar_sign(class_name):
    return class_name.replace('$', '__')


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

def save_class(java_class_file):
    module_name = replace_reserved_names(java_class_file.package)
    class_name = replace_reserved_names(java_class_file.class_name)
    header = get_class_header(class_name)
    module_path = get_module_path(module_name)
    if not os.path.exists(module_path):
        with open(module_path, 'w') as fout:
            fout.write('')
    with open(module_path, 'r') as fin:
        contents = fin.read() or init_module(module_name)
    if not header in contents:
        contents += transpile_class(module_name, class_name, java_class_file)
        with open(module_path, 'w') as fout:
            fout.write(contents)


def replace_reserved_names(name):
    if name in RESERVED_WORDS:
        return '__%s__' % name
    if name == '<init>': return '__init__'
    if name == '<clinit>': return '__clinit__'
    name = name.replace('$', '__')
    name = name.replace('-', '__')
    return name


def transpile_class(module_name, class_name, java_class_file):
    if DEBUG:
        print 'Load Java class %s.%s' % (module_name, class_name)
    class_object = generate_python_class(module_name, class_name, java_class_file)
    lines = ['', get_class_header(class_name)]
    for field in class_object.fields:
        if field.static:
            lines.append('    %s = None # %s' % (replace_reserved_names(field.name), field.type_name))
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
        full_name = '%s.%s' % (module_name, class_name)
        lines.append('pava.load_natives("%s", %s)' % (full_name, class_name))
        lines.append('')
    return '\n'.join(lines)


def run_java_method(input_file, method_name):
    java_class_file = decompile_java_class_file(input_file)
    class_object = generate_python_class('test', 'Test', java_class_file)
    for fn in class_object.functions:
        if fn.name == method_name:
            code = new.code(fn.argcount, fn.nlocals, fn.stacksize, fn.flags, fn.codestring, fn.constants, fn.names,
                            fn.varnames, fn.filename, fn.name, fn.firstlineno, fn.lnotab)
            return code()


Class = namedtuple('Class', [
    'fields', 'functions', 'natives'
])
Field = namedtuple('Field', [
    'name', 'type_name', 'static'
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
    for field in class_file.fields:
        class_object.fields.append(Field(field.name, field.type_name, field.static))
    for method in class_file.methods:
        file_name = class_name + '.java'
        method_name = replace_reserved_names(method.name)
        code, imports = compile_method('%s.%s' % (module_name, class_name), method, file_name, method.static)
        if method.native:
            class_object.natives.append(NativeMethod(method_name, method.args, method.static))
        else:
            method = create_function(code, imports, method.static)
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


def compile_method(class_name, method, filename, is_static):
    if DEBUG:
        print 'compile', class_name, method.name
    code = asm.Code()
    code.co_name = replace_reserved_names(str(method.name))
    code.co_filename = str(filename)

    # parameters added to code by pava
    code.stack_depth = []
    code.java_bytecodes = []
    code.module_names = set()
    code.jumps = []

    first_exception_index = method.exceptions[0].target_index if method.exceptions else -1

    if not method.code:
        asm.Return(None, code)
    else:
        for n,ins in enumerate(method.code):
            if ins.index == first_exception_index:
                break
            try:
                if ins.operands is not None:
                    opcodes.convert(ins.opcode, code, ins.index, ins.operands)
                else:
                    opcodes.convert(ins.opcode, code, ins.index)
            except Exception as e:
                print '%s.%s()' % (class_name, method.name), len(loaded_classes)
                dump(code)
                try:
                    for ins in method.code[n:n+7]:
                        operands = repr(ins.operands) if ins.operands is not None else ''
                        print ' '*51, '###', str(ins.index).rjust(3), ins.opcode, operands
                except Exception:
                    pass
                print '##### ERROR:', traceback.format_exc(e)
                raise e
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
                    ln += ' %s' % (locals()[asm.argtype[op]][arg].ljust(10))
                except:
                    ln += ' %s %s ??????' % (asm.argtype[op], arg)
        ln += ' ' * (52 - len(ln))
        for index, (bytecode, pos, args) in code.java_bytecodes:
            if index == start:
                ln += '### %s %s %s' % (str(pos).rjust(3), bytecode, args)
        print(ln)
        if op in (asm.JUMP_IF_TRUE_OR_POP, asm.JUMP_IF_FALSE_OR_POP):
            print('        '+''.ljust(7) + ' POP_TOP')
        i+=1
