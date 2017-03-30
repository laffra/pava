from collections import namedtuple
import new
import os
import StringIO
import subprocess

DEBUG = False

JDK = 'C:/Program Files/Java/jdk1.8.0_121'
JAVA = JDK + '/bin/java'
JAVAC = JDK + '/bin/javac'
JAVAP = JDK + '/bin/javap'
JAVART = JDK + '/jre/lib/rt.jar'

Field = namedtuple('Field', ['name', 'type_name', 'static', 'public'])
Method = namedtuple('Method', ['name', 'args', 'return_type', 'code', 'exceptions', 'static', 'public', 'native'])
Instruction = namedtuple('Instruction', ['index', 'opcode', 'operands'])
ExceptionHandler = namedtuple('ExceptionHandler', ['from_index', 'to_index', 'target_index', 'type_name'])
FieldReference = namedtuple('FieldReference', ['class_name', 'field_name', 'signature'])
MethodReference = namedtuple('MethodReference', ['class_name', 'method_name', 'return_type', 'args'])


class ClassFile(object):
    def __init__(self, file_input):
        details = self.parse_details(file_input)
        self.source_file, self.full_name, self.package, self.class_name, self.super_classes = details
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
        super_classes = []
        return source_file, full_name, package, class_name, super_classes

    def parse_items(self, file_input):
        fields = []
        methods = []
        lines = iter(file_input)
        try:
            while True:
                line = lines.next().rstrip()
                if not line:
                    continue
                if '(' in line:
                    methods.append(self.parse_method(line, lines))
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
        raise ValueError('"%s" is not in %s' % (after, tokens))

    def parse_method(self, line, lines):
        prefix, signature = line[:-1].split('(')
        if 'throws' in signature:
            signature,_,_ = signature.partition(' throws ')
        signature = signature[:-1]
        tokens = prefix.split()
        if tokens[-1] == self.full_name:
            name = '__init__'
            return_type = 'void'
        else:
            return_type, name = tokens[-2:]
        code, exceptions = self.parse_code(name, lines)
        args = signature.split(', ') if signature else []
        static, public, native = 'static' in prefix, 'public' in prefix, 'native' in prefix
        if not static:
            args = ['self'] + args
        return Method(name, args, return_type, code, exceptions, static, public, native)

    def parse_code(self, name, lines):
        if DEBUG:
            print 'parse code for ', name
        code = []
        exceptions = []
        line = lines.next().rstrip() # skip Code: label
        if not line:
            return code, exceptions # this method has no code
        line = lines.next().rstrip()
        while line:
            tokens = line.split()
            if DEBUG:
                print '  parse ins', tokens
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
                        arg = FieldReference(class_name, field_name, type_signature)
                    elif kind in ['Method', 'InterfaceMethod', 'InvokeDynamic']:
                        # java/lang/StringBuilder.append:(I)Ljava/lang/StringBuilder;
                        target, _, signature = arg.rpartition(':')
                        class_name, method_name = target.split('.') if '.' in target else ('', target)
                        class_name = class_name.replace('/', '.')
                        method_name = '__init__' if method_name == '"<init>"' else method_name
                        operands, return_type = signature[1:].split(')')
                        operands = operands.split(', ') if operands else []
                        arg = MethodReference(class_name, method_name, return_type, operands)
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
        return Method('__clinit__', [], 'void', code, exceptions, True, True, False)

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

def decompile_java_class_file(fin):
    path = 'pava_class_file.class'
    with open(path, 'wb') as fout:
        fout.write(fin.read())
    return ClassFile(subprocess.Popen([JAVAP, '-c', path], stdout=subprocess.PIPE).stdout)

def javap(fin):
    path = 'pava_class_file.class'
    with open(path, 'wb') as fout:
        fout.write(fin.read())
    return subprocess.Popen([JAVAP, '-c', path], stdout=subprocess.PIPE).stdout.read()

def decompile_java_class(class_name):
    return ClassFile(subprocess.Popen([JAVAP, '-c', class_name], stdout=subprocess.PIPE).stdout)

def decompile_java_classes(class_names, classpath):
    cmd = [JAVAP, '-cp', classpath, '-c'] + list(class_names)
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
        except:
            pass
        class_file = decompile_java_class(binary_path)
        test_method = class_file.methods[1]
        code, imports = classloader.compile_method('PavaTest', test_method, source_path, True)
        modules = {}
        for module_name in imports:
            if module_name and not '[' in module_name and not '.' in module_name:
                if DEBUG:
                    print 'IMPORT', module_name
                modules[module_name] = __import__(module_name, {})
            method = new.function(code.code(), modules, 'test')
        if DEBUG:
            print '################ Compiled method %s with imports %s' % (test_method, imports)
        actual = 'Unknown'
        try:
            actual = eval(code.code(), modules)
        except Exception as e:
            actual = str(e)
            print open(source_path).read()
        finally:
            print '='*100
            print '#### Expression:', expression
            print '####   Expected:', repr(expected)
            print '####     Actual:', repr(actual)
            print '-'*100
            classloader.dump(code)
            print '='*100
            return expected, actual
    finally:
        if os.path.exists(source_path):
            os.remove(source_path)
        if os.path.exists(binary_path):
            os.remove(binary_path)

