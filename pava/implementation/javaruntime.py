from collections import namedtuple
import dis
import opcodes
import os
import pava
import re
import sys
import StringIO
import subprocess
import traceback


JDK = 'C:/Program Files/Java/jdk1.8.0_121'
JAVA = JDK + '/bin/java'
JAVAC = JDK + '/bin/javac'
JAVAP = JDK + '/bin/javap'
JAVART = JDK + '/jre/lib/rt.jar'

Field = namedtuple('Field', ['name', 'type_name', 'is_static', 'is_public'])
Method = namedtuple('Method', ['name', 'args', 'return_type', 'code', 'exceptions', 'is_static', 'is_public', 'is_native'])
Instruction = namedtuple('Instruction', ['index', 'opcode', 'operands'])
ExceptionHandler = namedtuple('ExceptionHandler', ['from_index', 'to_index', 'target_index', 'type_name'])
FieldReference = namedtuple('FieldReference', ['class_name', 'field_name', 'signature'])
MethodReference = namedtuple('MethodReference', ['class_name', 'method_name', 'return_type', 'args'])

JAVA_TO_PYTHON_RENAME_RE = re.compile('[^a-zA-Z0-9]|\).*')

JAVA_SIGNATURE_TYPES = {
    'B': 'byte',
    'C': 'char',
    'D': 'double',
    'F': 'float',
    'I': 'int',
    'J': 'long',
    'S': 'short',
    'V': 'void',
    'Z': 'boolean',
    '[': '[',
    ']': ']'
}


def get_python_class_name(class_name):
    python_name = '.'.join(map(get_python_name, class_name.split('.')))
    return python_name


def get_python_method_name(method_name, signature):
    # ()V  or  int   or  ""
    if signature and signature[0] == '(':
        return_type, types = get_types_from_signature(signature)
        python_signature = '__'.join(types)
    else:
        python_signature = signature
    python_name = get_python_name('%s__%s__' % (method_name, python_signature))
    return python_name


def get_python_field_name(field_name):
    python_name = get_python_name(field_name)
    return python_name


def get_python_name(java_name):
    return re.sub(JAVA_TO_PYTHON_RENAME_RE, '_', java_name)


def get_types_from_signature(signature):
    # (I)Ljava/lang/StringBuilder;
    # ([ZII)V
    # ()[Ljava/lang/String;
    return_type = extract_type_list(signature[signature.index(')') + 1:])[0]
    signature_types = extract_type_list(signature[1:signature.index(')')])
    return return_type, signature_types


def extract_type_list(encoded_type_string):
    types = []
    n = 0
    array_count = 0
    while n < len(encoded_type_string):
        long_name = JAVA_SIGNATURE_TYPES.get(encoded_type_string[n])
        if encoded_type_string[n] == '[':
            array_count += 1
        elif long_name:
            types.append(long_name + '[]' * array_count)
            array_count = 0
        else:
            start = n
            while n < len(encoded_type_string) - 1 and encoded_type_string[n] != ';':
                n += 1
            class_name = encoded_type_string[start + 1: n].replace('/', '.')
            types.append(class_name + '[]' * array_count)
            array_count = 0
        n += 1
    return types


class ClassFile(object):
    def __init__(self, file_input):
        details = self.parse_details(file_input)
        self.source_file, self.full_name, self.package, self.class_name, self.super_class = details
        self.fields, self.methods = self.parse_items(file_input)

    def parse_details(self, file_input):
        tokens = file_input.readline().split()
        if tokens[0] == 'Compiled':
            source_file = tokens[2][1:-1]
            tokens = file_input.readline().split()
        else:
            source_file = ''
        full_name = self.get_token_after(tokens, ['class', 'interface'])
        package, _, class_name = full_name.rpartition('.')
        full_name = full_name.split('<')[0]
        class_name = class_name.split('<')[0]
        super_class = 'pava.JavaClass' if full_name == 'java.lang.Object' else 'java.lang.Object'
        if 'extends' in tokens:
            super_class = self.get_token_after(tokens, ['extends']).split('<')[0]
        return source_file, full_name, package, class_name, super_class

    def parse_items(self, file_input):
        fields = []
        methods = []
        found_methods = set()
        lines = iter(file_input)
        try:
            while True:
                line = lines.next().rstrip()
                if not line:
                    continue
                if '(' in line:
                    method = self.parse_method(line, lines)
                    if method.name not in found_methods:
                        found_methods.add(method.name)
                        methods.append(method)
                elif '{}' in line:
                    methods.append(self.parse_clinit(line, lines))
                elif line != '}':
                    fields.append(self.parse_field(line))
        except StopIteration:
            return fields, methods

    def get_token_after(self, tokens, afters):
        for after in afters:
            try:
                index = tokens.index(after)
                if index == len(tokens) -1:
                    return None
                return tokens[index + 1]
            except ValueError:
                pass
        raise ValueError('None from "%s" found in %s' % (afters, tokens))

    def parse_method(self, line, lines):
        prefix, signature = line[:-1].split('(')
        if 'throws' in signature:
            signature,_,_ = signature.partition(' throws ')
        signature = signature[:-1]
        tokens = prefix.split()
        if tokens[-1] == self.full_name:
            name = '__java_init__'
            return_type = 'void'
        else:
            return_type, name = tokens[-2:]
        code, exceptions = self.parse_code(name, lines)
        args = signature.split(', ') if signature else []
        is_static, is_public, is_native = 'static' in prefix, 'public' in prefix, 'native' in prefix
        args = ['cls' if is_static else 'self'] + ['a%d' % (n+1) for n in range(len(args))]
        python_method_name = get_python_method_name(name, signature)
        return Method(python_method_name, args, return_type, code, exceptions, is_static, is_public, is_native)

    def parse_code(self, name, lines):
        code = []
        exceptions = []
        line = lines.next().rstrip() # skip Code: label
        if not line:
            return code, exceptions # this method has no code
        line = lines.next().rstrip()
        while line:
            tokens = line.split()
            if tokens[0] == '}':
                break
            if tokens[0] == 'Exception':
                exceptions = self.parse_exceptions(lines)
                code = code[:exceptions[0].target_index]
                break
            assert tokens[0][-1] == ':', 'unexpected code index: ' + line
            index = int(tokens[0][:-1])
            opcode = tokens[1]
            if opcode == 'lookupswitch' or opcode == 'tableswitch':
                arg = dict()
                line = lines.next().strip()
                while line != '}':
                    value, target = line.split(': ')
                    arg[value] = target
                    line = lines.next().strip()
            elif len(tokens)> 2:
                if '//' in tokens:
                    info = tokens.index('//')
                    try:
                        kind, arg = tokens[info + 1], ' '.join(tokens[info + 2:])
                    except IndexError:
                        kind, arg = tokens[-1], ('',)
                    if kind == 'class':
                        # java/lang/StringBuilder
                        arg = arg.replace('/', '.')
                    elif kind == 'Field':
                        # size:I
                        name, type_signature = arg.split(':')
                        class_name = ''
                        field_name = name
                        if '.' in name:
                            class_name, field_name = name.split('.')
                            class_name = class_name.replace('/', '.')
                        python_class_name = get_python_class_name(class_name) or self.class_name
                        arg = FieldReference(python_class_name, field_name, type_signature)
                    elif kind in ['Method', 'InterfaceMethod', 'InvokeDynamic']:
                        # java/lang/StringBuilder.append:(I)Ljava/lang/StringBuilder;
                        target, _, signature = arg.rpartition(':')
                        class_name, method_name = target.split('.') if '.' in target else ('', target)
                        class_name = class_name.replace('/', '.')
                        method_name = '__java_init__' if method_name == '"<init>"' else method_name
                        return_type, method_args = get_types_from_signature(signature)
                        python_class_name = get_python_class_name(class_name) or self.class_name
                        python_method_name = get_python_method_name(method_name, signature)
                        arg = MethodReference(python_class_name, python_method_name, return_type, method_args)
                    elif kind == '' or kind == 'String':
                        pass
                    elif kind == 'int':
                        arg = int(arg)
                    elif kind == 'long':
                        arg = long(arg)
                    elif kind == 'float':
                        arg = arg[:-1] # strip trailing f
                        if arg == 'Infinity':
                            arg = float('inf')
                        elif arg == '-Infinity':
                            arg = float('inf')
                        else:
                            arg = float(arg)
                    elif kind == 'double':
                        arg = float(arg.replace('d', ''))
                    else:
                        raise NotImplementedError('kind=%s, arg=%s, tokens=%s' % (kind, arg, tokens))
                else:
                    if tokens[2].endswith(','):
                        # ['25:', 'iinc', '2,', '1']
                        arg = int(tokens[2][:-1]), int(tokens[3])
                    else:
                        try:
                            arg = int(tokens[2])
                        except ValueError:
                            arg = tokens[2]
            else:
                arg = None
            code.append(Instruction(index, opcode, arg))
            line = lines.next().rstrip()
        return code, exceptions

    def parse_clinit(self, line, lines):
        code, exceptions = self.parse_code('clinit', lines)
        return Method('__clinit__', ['cls'], 'void', code, exceptions, True, True, False)

    def parse_field(self, line):
        # Example: public static final java.lang.Boolean TRUE;
        tokens = line[:-1].split()
        return Field(tokens[-1], tokens[-2], 'static' in tokens, 'public' in tokens)

    def parse_exceptions(self, lines):
        line = lines.next() # skip "from to target type"
        line = lines.next()
        exceptions = []
        while line and line != '}':
            from_index, to_index, target, exception = line.replace('Class ', '').split()
            exceptions.append(ExceptionHandler(int(from_index), int(to_index), int(target), exception))
            line = lines.next().rstrip()
        return exceptions


def compile_java_source(file_name):
    print subprocess.Popen([JAVAC, file_name], stdout=subprocess.PIPE).stdout.read()


def decompile_java_class(class_name):
    return ClassFile(subprocess.Popen([JAVAP, '-c', '-p', class_name], stdout=subprocess.PIPE).stdout)


def decompile_java_classes(class_names, classpath):
    cmd = [JAVAP, '-cp', classpath, '-c', '-p'] + list(class_names)
    javap_output = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout.readlines()
    class_files = []
    lines = []
    for line in javap_output:
        lines.append(line)
        if line.rstrip() == '}':
            class_files.append(ClassFile(StringIO.StringIO(''.join(lines))))
            lines = []
    return class_files


def run_java_class(class_name):
    return subprocess.Popen([JAVA, class_name], stdout=subprocess.PIPE).stdout.read().rstrip()


def run_java_test(return_type, expression):
    sys.setrecursionlimit(1000)
    opcodes.DEBUG = True
    opcodes.TRACE = False
    opcodes.INTERPRET = True
    expected, actual = compile_and_run_java_test(return_type, expression)
    assert equals(actual, expected), 'Expected test to produce %s, instead got %s' % (repr(expected), repr(actual))


def equals(value1, value2):
    if type(value1) is not type(value2):
        return False
    if isinstance(value1, float):
        return abs(value1 - value2) < 0.000001
    return value1 == value2


def compile_and_run_java_test(return_type, expression):
    from pava.implementation import classloader
    source_path = 'PavaTest.java'
    binary_path = 'PavaTest.class'
    try:
        with open(source_path, 'w') as fout:
            fout.write('public class PavaTest {\n')
            fout.write('  public static %s test() {\n' % return_type)
            fout.write('    %s\n' % expression)
            fout.write('  }\n')
            fout.write('  public static void main(String[] args) {\n')
            fout.write('    System.out.println(PavaTest.test());\n')
            fout.write('  }\n')
            fout.write('}\n')
        compile_java_source(source_path)
        expected = run_java_class('PavaTest')
        try:
            expected = eval(expected)
        except Exception as e:
            pass # Interpret the result as a string
        class_file = decompile_java_class(binary_path)
        python_class_text = classloader.init_module('tests')
        python_class_text += classloader.transpile_class('tests', 'PavaTest', 'java.lang.Object', class_file)
        python_class_text = python_class_text.replace("'PavaTest']", ']')

        globals()['pava'] = __import__('pava')
        try:
            exec(python_class_text, globals())
        except Exception as e:
            print '####### EXEC FAILED:'
            traceback.print_exc()
            raise e
        actual = 'Unknown'
        try:
            classobj = globals()['PavaTest']
            method = getattr(classobj, 'test____')
            setattr(sys.modules[__name__], 'PavaTest', classobj)
            globals()['PavaTest'] = classobj
            actual = method()
        except Exception as e:
            actual = str(e)
            print '##### ERROR:', traceback.format_exc(e)
        finally:
            print '='*100
            print '#### Expression:', expression
            print '####   Expected:', repr(expected)
            print '####     Actual:', repr(actual)
            print '='*100
            return expected, actual
    finally:
        if os.path.exists(source_path):
            os.remove(source_path)
        if os.path.exists(binary_path):
            os.remove(binary_path)

