from __future__ import print_function

import datetime
import re
import os
import subprocess
import sys
import time
import traceback
import zipfile

from itertools import islice

from javaruntime import decompile_java_classes
from javaruntime import Instruction

import opcodes

DEBUG = False
VERIFY_OUTPUT = DEBUG

HOME = os.path.join(os.path.expanduser("~"), os.path.join('pava', 'classes'))

CLASS_PATH_CHUNK_SIZE = 400

sys.path.append(HOME)
loaded_classes = set()

INDENT = '    '

JAVA = '/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home/bin/java'

RETURN_OPCODES = [
    'areturn',
    'ireturn',
    'dreturn',
    'freturn',
    'lreturn',
    'return',
]

def get_already_compiled_classes():
    class_names = []
    def visit(arg, dir_name, file_names):
        for file_name in file_names:
            if file_name.endswith('.py'):
                dir_name = dir_name[len(HOME)+1:]
                class_names.append('%s%s%s' % (dir_name.replace('/', '.'), "." if dir_name else "", file_name[:-3]))
    os.path.walk(HOME, visit, '')
    return class_names

COMPILED_CLASSES = set(get_already_compiled_classes())


def get_boot_path():
    java = subprocess.Popen([JAVA, '-verbose', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in java.stdout.readlines():
        if line.startswith('[Opened'):
            return [ (line[8:-2]) ]


def set_classpath(cp, debug_class=None):
    print("Java classpath:", cp)
    assert isinstance(cp, list), 'classpath should be a list of directories and archives'
    try:
        classpath_elements = list(set(get_boot_path() + cp))
        # profiler.profile('index_class_path(classpath_elements, debug_class)', globals(), locals())
        index_class_path(classpath_elements, debug_class)
    except Exception as e:
        print('##### ERROR:', traceback.format_exc(e))
        raise e


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def index_class_path(path, debug_class):
    compile_class_files(find_class_files(path, debug_class), ';'.join(p for p in path if not p.endswith(".jar")))
    for p in path:
        add_classpath_marker(p)


def find_class_files(path, debug_class):
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
    if debug_class:
        classes = [debug_class]
    if DEBUG:
        print('Found %d Java classes' % len(classes))
    return classes


def is_already_compiled(full_class_name):
    parts = full_class_name.split(".")
    module_name = ".".join(parts[:-1])
    class_name = parts[-1]
    class_file_path = os.path.join(os.path.dirname(get_module_path(module_name)), '%s.py' % class_name.replace('$', '_'))
    return os.path.exists(class_file_path)

def compile_class_files(classes, cp):
    count = 0
    start = time.time()
    print('Loading %d classes:' % len(classes))
    for n, class_names in enumerate(chunk(classes, CLASS_PATH_CHUNK_SIZE)):
        new_class_names = [name for name in class_names if not is_already_compiled(name)]
        for class_file in decompile_java_classes(new_class_names, cp):
            if DEBUG:
                print('%s %s' % (class_file.package, class_file.class_name))
            save_class(class_file)
        count += len(class_names)
        seconds = time.time() - start
        print('Loaded %d classes - %d%% - %s' % (count, count * 100 / len(classes), "%02d:%02d" % divmod(seconds, 60)))


def get_classpath_marker(p):
    marker = os.path.normpath(p)
    marker = marker.replace(os.path.sep, '_').replace(' ', '_').replace(':', '_').replace('.', '_')
    marker = os.path.join(HOME, marker + '.log')
    print(marker)
    return marker


def classpath_already_marked(path):
    return os.path.exists(get_classpath_marker(path))


def add_classpath_marker(path):
    marker = get_classpath_marker(path)
    with open(marker, 'w') as fout:
        fout.write('%s' % datetime.datetime.now())


def add_jar(jar_path):
    print('Loading ', jar_path)
    class_names = []
    try:
        with zipfile.ZipFile(jar_path, 'r') as jar:
            for n, entry in enumerate(jar.infolist()):
                if entry.filename.endswith('.class'):
                    class_name = entry.filename[:-6].replace('/', '.')
                    class_names.append(class_name)
    except Exception as e:
        print("#### Skip %s: %s" % (jar_path, e))
    return class_names


def add_directory(dir_path):
    print('Loading ', dir_path)
    class_names = []
    def visit(arg, dir_name, file_names):
        for file_name in file_names:
            if file_name.endswith('.class'):
                dir_name = dir_name[len(dir_path)+1:]
                class_names.append('%s.%s' % (dir_name.replace('/', '.'), file_name[:-6]))
    os.path.walk(dir_path, visit, '')
    return class_names



def fix_dollar_sign(class_name):
    return class_name.replace('$', '_')


def get_module_path(module_name, home=HOME):
    path = os.path.join(home)
    package_name = ''
    for fragment in module_name.split('.'):
        fragment = replace_reserved_names(fragment)
        package_name = '.'.join([package_name, fragment]) if package_name else fragment
        path = os.path.join(path, fragment)
        if not os.path.exists(path):
            os.makedirs(path)
            init = os.path.join(path, '__init__.py')
            with open(init, 'w') as fout:
                fout.write(init_module(module_name))
    return os.path.join(path, '__init__.py')


def get_class_header(class_name, super_class):
    return 'from %s import %s\n' % (class_name, class_name)


def get_super_class_header(super_class):
    return 'class %s(' % (super_class)


def init_module(module_name):
    return '''"""
This is the Python implementation for the Java package "%s", compiled by Pava.
"""

import pava
pava.LazyModule(__name__, __file__)

''' % module_name


def save_class(java_class_file, force=False):
    module_name = replace_reserved_names(java_class_file.package)
    class_name = replace_reserved_names(java_class_file.class_name)
    super_class = replace_reserved_names(java_class_file.super_class)
    if module_name == 'java.lang' and class_name == 'String':
        super_class = "str"
    class_header = get_class_header(class_name, super_class)
    module_path = get_module_path(module_name)
    with open(module_path, 'r') as fin:
        contents = fin.read()
    if force or not class_header in contents:
        # with open(module_path, 'a') as fout: fout.write(class_header)
        class_file_path = os.path.join(os.path.dirname(get_module_path(module_name)), '%s.py' % class_name)
        with open(class_file_path, 'w') as fout:
            fout.write(transpile_class(module_name, class_name, super_class, java_class_file))
        # if module_name == 'java.lang' and class_name == 'Object' or VERIFY_OUTPUT:
        if VERIFY_OUTPUT:
            pythonOutput = subprocess.Popen(["python", class_file_path], stderr=subprocess.PIPE).stderr.read()
            if "IndentationError" in pythonOutput:
                raise RuntimeError("Bad file: %s" % pythonOutput)


def replace_reserved_names(name):
    return opcodes.replace_reserved_names(name)


def transpile_class(module_name, class_name, super_class, java_class_file):
    if DEBUG:
        print("@" * 80)
        print('Load Java class %s.%s' % (module_name, class_name))
        print(len(java_class_file.methods), len(java_class_file.fields))
        print("@" * 80)
    return PythonClass(module_name, class_name, super_class, java_class_file).get_source()


JAVA_DEFAULT_VALUE_BY_TYPE = {
    'byte': 0,
    'char' : 0,
    'double' : 0.0,
    'float' : float(0.0),
    'int' : 0,
    'long' : 0,
    'short' : 0,
    'boolean' : False,
    'java.lang.String': '""',
}


def get_default_value(type_name):
    return JAVA_DEFAULT_VALUE_BY_TYPE.get(type_name)


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
            fout.write('%sdef %s(%s):\n' % (INDENT, method.name, ', '.join(['a%d' %n for n in range(len(method.args))])))
            fout.write('%sraise NotImplementedError()\n\n' % (INDENT * 2))
        for method in methods:
            target = 'classmethod(%s)' % method.name if method.is_static else method.name
            fout.write('%sclazz.%s = %s\n' % (INDENT, method.name, target))
        fout.write('\n')


class PythonModule(object):
    def __init__(self, file_name):
        self.file_name = file_name


class PythonClass(object):
    def __init__(self, module_name, class_name, super_class_name, java_class):
        self.module_name = module_name
        self.class_name = class_name
        self.full_name = '%s.%s' % (module_name, class_name)
        self.super_class_name = super_class_name
        self.fields = map(self.compile_field, java_class.fields)
        self.has_natives = False
        self.methods = filter(None, map(self.compile_method, java_class.methods))

    def get_source(self, indent=0):
        modules = set()
        for method in self.methods:
            modules.update(method.imports)
        modules = [m for m in modules if m and not '[' in m and m != self.class_name]
        if self.super_class_name == 'pava.JavaClass':
            modules.append('pava')
        imports = '\n'.join('import %s' % module for module in sorted(modules))

        if not self.fields and not self.methods:
            body = "%spass" % (INDENT * (indent + 1))
        else:
            body = "\n".join([
                '\n'.join('%s' % field.get_source(indent + 1) for field in self.fields),
                '\n\n'.join('%s' % method.get_source(indent + 1) for method in self.methods)
            ])
        class_def = '%sclass %s(%s):\n\n%s' % (
            INDENT * indent,
            self.class_name,
            self.super_class_name,
            body
        )
        if self.has_natives:
            class_def += '\nimport pava.implementation.natives.%s\npava.implementation.natives.%s.add_native_methods(%s)\n' % (
                self.full_name, self.full_name, self.class_name
            )
        return imports + '\n\n\n' + class_def

    def compile_field(self, java_field):
        return PythonField(java_field.type_name, java_field.name)

    def compile_method(self, java_method):
        if DEBUG:
            print(INDENT + java_method.name)
        python_method = PythonMethod(self, java_method)
        first_exception_index = java_method.exceptions[0].target_index if java_method.exceptions else -1
        python_method.previous_ins = None
        if java_method.is_native:
            self.has_natives = True
            return None
        if not java_method.code:
            python_method.code = 'pass'
        else:
            n = 0
            while n < len(java_method.code):  # the code array grows while we process it
                ins = java_method.code[n]
                python_method.java_bytecode = (n, ins)
                if ins.index == first_exception_index:
                    break
                if ins.operands is not None:
                    opcodes.convert(ins.opcode, python_method, ins.index, ins.operands)
                else:
                    opcodes.convert(ins.opcode, python_method, ins.index)
                while java_method.code[n] != ins:
                    n += 1
                n += 1
                python_method.previous_ins = ins
        return python_method


class PythonField(object):
    def __init__(self, type_name, name):
        self.type_name = type_name
        self.name = replace_reserved_names(name)

    def get_source(self, indent=1):
        return '%s%s = %s # %s' % (
            INDENT * indent,
            self.name,
            'None',
            self.type_name,
        )


def add_indent(indent, line):
    return '%s%s' % (INDENT * max(0, indent), line)

def cleanup(line):
    if DEBUG:
        return line
    line = re.sub("#[A-Z]+[=0-9]* ", "", line)
    try:
        expression, comment = line.split('#')
        line = '%s#%s' % (expression.rstrip().ljust(45), comment)
    except ValueError:
        pass
    return line


class PythonMethod(object):
    def __init__(self, python_class, java_method):
        self.name = replace_reserved_names(str(java_method.name))
        self.args = java_method.args
        self.java_method = java_method
        self.is_static = java_method.is_static
        self.java_bytecodes = {}
        self.java_bytecode = ''
        self.module_names = set()
        self.python_class = python_class
        self.stack = []
        self.ifs = []
        self.if_indents = {}
        self.elses = []
        self.temp_index = 0
        self.imports = set()

    def get_source(self, indent=1):
        return '%s%sdef %s(%s):\n%s\n%s' % (
            INDENT * indent + '@classmethod\n' if self.is_static else '',
            INDENT * indent,
            self.name,
            ', '.join(self.args),
            self.format(indent),
            self.format_exceptions(indent + 1)
        )

    def format_exceptions(self, indent):
        return '\n'.join([
            '%s# %s' % (INDENT * indent, exc) for exc in self.java_method.exceptions
        ])

    def add_class_reference(self, class_name):
        module_name, _, _ = class_name.partition('.')
        self.imports.add(module_name)

    def add_java_bytecode(self, line, java_index, indent):
        if java_index != -1:
            bytecode = self.java_bytecodes.get(java_index)
            if bytecode:
                line = '%s # %s %s' % (line.ljust(55 - len(INDENT)*indent), str(java_index).rjust(4), bytecode)
        return line

    def format(self, format_indent=1):
        if DEBUG:
            print('format ', self.name)
            print('-'*120)
            for key in sorted(self.java_bytecodes.keys()):
                print('    ', key, self.java_bytecodes[key])
            print('-'*120)
        lines = []
        n = 0
        last_java_index = -1
        indent = format_indent
        previous_line = ""
        while n < len(self.stack):
            java_index, line, is_statement = self.stack[n]
            line = str(line)
            if DEBUG:
                print("compare", n, java_index)
                print("  ", line)
                print("  ", previous_line)
            if line.startswith("# ELSE=") and previous_line.startswith("if "):
                if DEBUG:
                    print("YES, insert pass")
                lines.append(add_indent(indent - 1, "pass"))
            indent, line = self.compute_indent_before(indent, line)
            output_line = line
            for missing_index in range(last_java_index + 1, java_index):
                if missing_index in self.java_bytecodes:
                    lines.append(add_indent(indent - 1, self.add_java_bytecode('', missing_index, indent)))
            if output_line:
                lines.append(add_indent(indent - 1, self.add_java_bytecode(output_line, java_index, indent)))
            if DEBUG:
                print(INDENT * indent, java_index, ' ', output_line, "# indent:", indent)
            indent, line = self.compute_indent_after(indent, output_line)
            if DEBUG:
                print(INDENT * indent, java_index, ' ', output_line, "# indent:", indent)
            last_java_index = java_index
            previous_line = line
            n += 1

        if not lines:
            lines = ["pass"]

        return '\n'.join([add_indent(format_indent + 1, cleanup(line)) for line in lines])

    def get_indent_for_if(self, if_, indent, line):
        try:
            indent = min(indent, self.if_indents[if_])
            if DEBUG:
                print('INDENT %d for %s %s' % (indent, if_, self.if_indents[if_]))
        except KeyError as e:
            if DEBUG:
                print('do-while loops not yet implemented')
        return indent, line

    def extract_if(self, line, label):
        fragments = line[line.index(label):].split('=')[:4]
        try:
            return int(fragments[1]), int(fragments[2]), int(fragments[3])
        except ValueError as e:
            return fragments[1], fragments[2], fragments[3]


    def compute_indent_before(self, indent, line):
        if '#IF=' in line:
            if_, else_, end_ = self.extract_if(line, '#IF=')
            self.if_indents[if_] = indent
        elif '#ELSE=' in line:
            if_, else_, end_ = self.extract_if(line, '#ELSE=')
            if end_ > else_:
                indent, line = self.get_indent_for_if(if_, indent, "else: %s" % line)
        elif '#ENDIF=' in line:
            if_, else_, end_ = self.extract_if(line, '#ENDIF=')
            indent, line = self.get_indent_for_if(if_, indent, line)
        elif '#CASE=' in line:
            if_, key, tmp = self.extract_if(line, '#CASE=')
            indent, line = self.get_indent_for_if(if_, indent, 'elif %s == %s: ' % (tmp, key) + line)
        elif '#DEFAULT=' in line:
            if_, key, tmp = self.extract_if(line, '#DEFAULT=')
            indent, line = self.get_indent_for_if(if_, indent, 'else: ' + line)
        elif '#WHILE=' in line:
            while_, _, _ = self.extract_if(line, '#WHILE=')
            indent, line = self.get_indent_for_if(while_, indent, line)
        elif '#ENDWHILE=' in line:
            if_, _, _ = self.extract_if(line, '#ENDWHILE=')
            indent, line = self.get_indent_for_if(if_, indent, line)
        return indent, line

    def compute_indent_after(self, indent, line):
        original = line
        if '#IF=' in line:
            indent += 1
            if not DEBUG:
                line = line[:line.index('#IF=')]
        elif '#ELSE=' in line:
            _, else_, end_ = self.extract_if(line, '#ELSE=')
            if end_ > else_:
                indent += 1
            if not DEBUG:
                line = line[:line.index('#ELSE=')]
        elif '#ENDIF=' in line:
            if not DEBUG:
                line = ''
        elif '#CASE=' in line:
            indent += 1
            if not DEBUG:
                line = line[:line.index('#CASE=')]
        elif '#DEFAULT=' in line:
            indent += 1
            if not DEBUG:
                line = line[:line.index('#DEFAULT=')]
        elif '#WHILE=' in line:
            indent += 1
            if not DEBUG:
                line = line[:line.index('#WHILE=')]
        elif line.startswith("return "):
            indent -= 1
        elif line.startswith('raise '):
            indent -= 1
        if DEBUG:
            print("compute indent", original)
        return indent, line

    def is_return_instruction(self, java_index):
        if java_index < 1:
            return False
        instruction = self.java_method.code[self.find_instruction(java_index)]
        return instruction.opcode in RETURN_OPCODES

    def check_endif(self, java_index):
        for if_, else_, end_ in self.ifs:
            # if not self.is_return_instruction(java_index - 1) and end_ == java_index:
            if end_ == java_index:
                index, expression, is_statement = self.stack[-1]
                expression +=  ' #%s=%d=%d=%d= ' % ("ENDIF", if_, else_, end_)
                self.stack[-1] = index, expression, is_statement 


    #
    # The following Java if-statements:
    #
    #  if (a) { stmt-1; }       if (a) { stmt-1; } else { stmt-2; }
    #
    # Become this in bytecodes:
    #
    #  if not a: goto L1        if not a: goto L1
    #  stmt-1                   stmt-1
    #  L1: ...                  goto L2
    #                           L1: stmt-2
    #                           L2: ...
    #
    def add_if(self, if_index, else_index):
        before = self.java_method.code[self.find_instruction(else_index) - 1]
        end_index = before.operands if before.opcode == 'goto' else else_index
        self.ifs.append([if_index, else_index, end_index])
        label = 'IF' if end_index > if_index else 'WHILE'
        if DEBUG:
            print("add_if", if_index, else_index, end_index, label)
        if before.opcode in RETURN_OPCODES:
            index = self.find_instruction(else_index)
            ins = Instruction(else_index, 'ifreturn', (if_index, else_index, end_index))
            self.java_method.code.insert(index, ins)
        if label == 'WHILE' and end_index not in self.if_indents:
            index = self.find_instruction(end_index)
            tmp = self.next_temp()
            self.stack.insert(index, Instruction(end_index, '%s = False' % tmp, None))
            self.stack.insert(index, Instruction(end_index, 'while %s:  # WHILE=%d=%s=%s' % (tmp, index, tmp, tmp), None))
            self.stack.insert(index, Instruction(end_index, '%s = True' % tmp, None))
        return '#%s=%d=%d=%d=' % (label, if_index, else_index, end_index)


    def add_else(self, else_index, end_index):
        for if_, else_, end_ in self.ifs:
            if (else_ == else_index or else_ == else_index + 3) and end_ == end_index:
                return '#ELSE=%d=%d=%d=' % (if_, else_, end_)
        return '#GOTO=%d' % end_index

    def add_loop(self, java_index, while_index):
        for if_, else_, end_ in self.ifs:
            if end_ == while_index:
                return '#ENDWHILE=%d=%d=%d=' % (if_, else_, end_)
        return '#ENDWHILE=%d=%d=%d=' % (while_index, while_index, while_index)


    def find_end_switch(self, java_index):
        index = self.find_instruction(int(java_index) - 3)
        if index != -1:
            ins = self.java_method.code[index]
            if ins.opcode == 'goto':
                return ins.operands
        return -1

    def add_lookup_switch(self, java_index, lookup_dict):
        # key is on the stack
        # lookup_dict looks like {0: 68, 1: 74, 2: 80, 5: 86, 'default': 107, 47: 92, 59: 98, 61: 104}
        # keys compared with the top of the stack, values are target indexes
        tmp = self.next_temp()
        self.push(java_index, '%s = %s' % (tmp, self.pop()), is_statement=True)
        cases = sorted(lookup_dict.iteritems(), key=lambda item: item[1])
        for n, (key, java_target_index) in enumerate(cases):
            index = self.find_instruction(java_target_index)
            operands = (java_index, key, tmp)
            next_java_target_index = cases[n+1][1] if n < len(cases) - 1 else -1
            if n == 0:
                label = self.add_if(int(java_target_index), int(next_java_target_index))
                self.push(java_index, 'if %s == %s: %s' % (tmp, key, label), is_statement=True)
            elif n == len(cases) - 1:
                self.java_method.code.insert(index, Instruction(-1, 'default', operands))
            else:
                self.java_method.code.insert(index, Instruction(-1, 'case', operands))
                end_switch_index = self.find_end_switch(java_target_index)
                if end_switch_index != -1:
                    for if_statement in self.ifs:
                        if if_statement[0] == java_index:
                            if_statement[2] = end_switch_index
                            index = self.find_instruction(end_switch_index)
                            ins = Instruction(-1, 'switchend', operands)
                            if self.java_method.code[index - 1] != ins:
                                self.java_method.code.insert(index, ins)

    def find_instruction(self, java_index):
        for n, ins in enumerate(self.java_method.code):
            if ins.index == int(java_index):
                return n
        return -1

    def push(self, java_index, expression, is_statement=False):
        expression = str(expression)
        self.stack.append((java_index, expression, is_statement))
        if DEBUG:
            self.dump_stack('PUSH %d %s' % (java_index, expression))

    def pop_args(self, count=1):
        if count > 1:
            return self.pop(count)
        elif count == 1:
            return [self.pop(1)]
        else:
            return []

    def pop(self, count=1):
        if count > 1:
            return list(reversed([self.pop() for _ in range(count)]))
        else:
            index = len(self.stack) - 1
            while index > 0 and self.stack[index][2]: # search for the first real expression on the stack
                index -= 1
            if self.stack:
                value = self.pop_expression(index)
                if DEBUG:
                    self.dump_stack('POP %d %s' % (index, value))
                return value

    def pop_expression(self, index):
        top = self.stack.pop(index)[1]
        if index > 2:
            pos_1, value_1, is_stmt_1 = self.stack[index - 1]
            pos_2, value_2, is_stmt_2 = self.stack[index - 2]
            pos_3, value_3, is_stmt_3 = self.stack[index - 3]
            if isinstance(value_1, str) and value_1.startswith('#ELSE=') and \
                           isinstance(value_3, str) and ': # IF=' in value_3 and not is_stmt_2:
                self.stack.pop(index - 1)
                self.stack.pop(index - 2)
                self.stack.pop(index - 3)
                value_3 = value_3[:value_3.index(': # IF=')]
                top = '%s %s else %s' % (value_2, value_3, top)
                try:
                    if self.stack and self.stack[-1][1].startswith('#ENDIF='):
                        self.stack.pop()
                except Exception as e:
                    self.dump_stack('POP expression %d %s %s' % (index, top, e))
        return top

    def dump_stack(self, label):
        print('-' * 80)
        print(label)
        for n, item in enumerate(self.stack):
            print(str(n).rjust(4), item)
        print('-' * 80)

    def next_temp(self):
        self.temp_index += 1
        return 't%d' % self.temp_index


