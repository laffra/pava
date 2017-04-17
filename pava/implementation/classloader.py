import datetime
import new
import os
import profiler
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

HOME = os.path.join(os.path.expanduser("~"), os.path.join('pava', 'classes'))

CLASS_PATH_CHUNK_SIZE = 400

sys.path.append(HOME)
loaded_classes = set()

INDENT = '    '

JAVA = 'C:/Program Files/Java/jdk1.8.0_121/bin/java'

def get_boot_path():
    java = subprocess.Popen([JAVA, '-verbose', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in java.stdout.readlines():
        if line.startswith('[Opened'):
            return [ (line[8:-2]) ]


def set_classpath(cp, debug_class=None):
    assert isinstance(cp, list), 'classpath should be a list of directories and archives'
    try:
        classpath_elements = list(set(get_boot_path() + cp))
        profiler.profile('index_class_path(classpath_elements, debug_class)', globals(), locals())
    except Exception as e:
        print '##### ERROR:', traceback.format_exc(e)


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def index_class_path(path, debug_class):
    compile_class_files(find_class_files(path, debug_class), ';'.join(path))
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


def compile_class_files(classes, cp):
    count = 0
    start = time.time()
    print 'Loading %d classes:' % len(classes)
    for n, class_names in enumerate(chunk(classes, CLASS_PATH_CHUNK_SIZE)):
        for class_file in decompile_java_classes(class_names, cp):
            if DEBUG:
                print('%s %s' % (class_file.package, class_file.class_name))
            save_class(class_file)
        count += len(class_names)
        seconds = time.time() - start
        print 'Loaded %d classes - %d%% - %s' % (count, count * 100 / len(classes), "%02d:%02d" % divmod(seconds, 60))


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
    print 'Loading ', jar_path
    class_names = []
    with zipfile.ZipFile(jar_path, 'r') as jar:
        for n, entry in enumerate(jar.infolist()):
            if entry.filename.endswith('.class'):
                class_names.append(entry.filename[:-6].replace('/', '.'))
    return class_names


def add_directory(dir_path):
    print 'Loading ', dir_path
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


def replace_reserved_names(name):
    return opcodes.replace_reserved_names(name)


def transpile_class(module_name, class_name, super_class, java_class_file):
    if DEBUG:
        print 'Load Java class %s.%s' % (module_name, class_name)
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

        class_def = '%sclass %s(%s):\n%s\n%s' % (
            INDENT * indent,
            self.class_name,
            self.super_class_name,
            '\n'.join('%s' % field.get_source(indent + 1) for field in self.fields),
            '\n\n'.join('%s' % method.get_source(indent + 1) for method in self.methods),
        )
        if self.has_natives:
            class_def += '\nimport implementation.natives.%s\nimplementation.natives.%s.add_native_methods(%s)\n' % (
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
    if '# ' in line:
        line = line[:line.index('# ')]
    return line.strip()


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

    def format(self, indent=1):
        if DEBUG:
            print 'format ', self.name
            print '-'*120
            for key in sorted(self.java_bytecodes.keys()):
                print '    ', key, self.java_bytecodes[key]
            print '-'*120
        lines = []
        n = 0
        last_java_index = -1
        while n < len(self.stack):
            java_index, line, is_static = self.stack[n]
            line = str(line)
            if DEBUG:
                print ' '*8, java_index, ' ', line
            indent, line = self.compute_indent_before(indent, line)
            output_line = cleanup(line)
            for missing_index in range(last_java_index + 1, java_index):
                if missing_index in self.java_bytecodes:
                    lines.append(add_indent(indent - 1, self.add_java_bytecode('', missing_index, indent)))
            if output_line:
                lines.append(add_indent(indent - 1, self.add_java_bytecode(output_line, java_index, indent)))
            indent, line = self.compute_indent_after(indent, line)
            last_java_index = java_index
            n += 1
        return '\n'.join([add_indent(indent + 1, line) for line in lines])

    def get_indent_for_if(self, if_, indent, line):
        try:
            indent = min(indent, self.if_indents[if_])
        except KeyError as e:
            line = 'raise NotImplementedError("do-while loops not yet implemented")'
        return indent, line

    def extract_if(self, line, label):
        fragments = line[line.index(label):].split('=')[:4]
        return fragments[1], fragments[2], fragments[3]

    def compute_indent_before(self, indent, line):
        if '# IF=' in line:
            if_, else_, end_ = self.extract_if(line, '# IF=')
            self.if_indents[if_] = indent
        elif '# ELSE=' in line:
            if_, else_, end_ = self.extract_if(line, '# ELSE=')
            indent, line = self.get_indent_for_if(if_, indent, 'else: ' + line)
        elif '# ENDIF=' in line:
            if_, else_, end_ = self.extract_if(line, '# ENDIF=')
            indent, line = self.get_indent_for_if(if_, indent, line)
        elif '# CASE=' in line:
            if_, key, tmp = self.extract_if(line, '# CASE=')
            indent, line = self.get_indent_for_if(if_, indent, 'elif %s == %s: ' % (tmp, key) + line)
        elif '# DEFAULT=' in line:
            if_, key, tmp = self.extract_if(line, '# DEFAULT=')
            indent, line = self.get_indent_for_if(if_, indent, 'else: ' + line)
        elif '# WHILE=' in line:
            if_, else_, end_ = self.extract_if(line, '# WHILE=')
            indent, line = self.get_indent_for_if(if_, indent, 'while' + line[2:])
        elif '# ENDWHILE=' in line:
            if_, _, _ = self.extract_if(line, '# ENDWHILE=')
            indent, line = self.get_indent_for_if(if_, indent, line)
        return indent, line

    def compute_indent_after(self, indent, line):
        if '# IF=' in line:
            indent += 1
            if not DEBUG:
                line = line[:line.index('# IF=')]
        elif '# ELSE=' in line:
            indent += 1
            if not DEBUG:
                line = line[:line.index('# ELSE=')]
        elif '# ENDIF=' in line:
            if not DEBUG:
                line = ''
        elif '# CASE=' in line:
            indent += 1
            if not DEBUG:
                line = line[:line.index('# CASE=')]
        elif '# DEFAULT=' in line:
            indent += 1
            if not DEBUG:
                line = line[:line.index('# DEFAULT=')]
        elif '# WHILE=' in line:
            indent += 1
            if not DEBUG:
                line = line[:line.index('# WHILE=')]
        elif line.startswith('raise '):
            indent -= 1
        return indent, line

    def check_if(self, java_index):
        for if_, else_, end_ in self.ifs:
            if else_ != end_ and end_ == java_index:
                self.push(-1, '# ENDIF=%d=%d=%d' % (if_, else_, end_), True)


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
        if label == 'WHILE' and end_index not in self.if_indents:
            index = self.find_instruction(end_index)
            tmp = self.next_temp()
            self.stack.insert(index, Instruction(-1, '%s = True  # condition for %d' % (tmp, end_index), None))
            self.stack.insert(index, Instruction(-1, 'while %s:  # condition for %d' % (tmp, end_index), None))
        return '# %s=%d=%d=%d' % (label, if_index, else_index, end_index)

    def add_else(self, else_index, end_index):
        for if_, else_, end_ in self.ifs:
            if else_ == else_index + 3 and end_ == end_index:
                return '# ELSE=%d=%d=%d' % (if_, else_, end_)
        return '# GOTO=%d' % end_index

    def add_loop(self, java_index, while_index):
        for if_, else_, end_ in self.ifs:
            if end_ == while_index:
                return '# ENDWHILE=%d=%d=%d' % (if_, else_, end_)
        return '# ENDWHILE=%d=%d=%d' % (while_index, while_index, while_index)


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
            if n == 0:
                label = self.add_if(java_index, int(java_target_index))
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
        self.stack.append((java_index, expression, is_statement))
        if DEBUG:
            print '=' * 120
            print 'push', java_index, is_statement, expression
            for n, item in enumerate(self.stack):
                print '  ', n, item
            print '=' * 120

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
                    print '=' * 120
                    print 'POP', index, value
                    for n, item in enumerate(self.stack):
                        print '  ', n, item
                    print '=' * 120
                return value

    def pop_expression(self, index):
        top = self.stack.pop(index)[1]
        if index > 2:
            pos_1, value_1, is_stmt_1 = self.stack[index - 1]
            pos_2, value_2, is_stmt_2 = self.stack[index - 2]
            pos_3, value_3, is_stmt_3 = self.stack[index - 3]
            if isinstance(value_1, str) and value_1.startswith('# ELSE=') and \
                           isinstance(value_3, str) and ': # IF=' in value_3 and not is_stmt_2:
                self.stack.pop()
                self.stack.pop()
                self.stack.pop()
                value_3 = value_3[:value_3.index(': # IF=')]
                top = '%s %s else %s' % (value_2, value_3, top)
        return top

    def next_temp(self):
        self.temp_index += 1
        return 't%d' % self.temp_index


