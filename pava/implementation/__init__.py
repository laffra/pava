import importlib
import new
import sys

DEBUG = False

method_count = 0

def method(argcount, nlocals, stacksize, flags, codestring, constants, names,
             varnames, filename, name, firstlineno, lnotab, modules, static):
    global method_count
    if DEBUG:
        print 'define', name, method_count
    method_count += 1
    globals_dict = {}
    for module_name in modules:
        if module_name and not '[' in module_name and not '.' in module_name:
            globals_dict[module_name] = __import__(module_name, {})
    code = new.code(argcount, nlocals, stacksize, flags, codestring, constants, names,
             varnames, filename, name, firstlineno, lnotab)
    method = new.function(code, globals_dict, name)
    return staticmethod(method) if static else method

nan = None

inf = sys.maxint

def load_natives(module_name, clazz):
    natives = importlib.import_module('pava.implementation.natives.' + module_name)
    natives.add_native_methods(clazz)
