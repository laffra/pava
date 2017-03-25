import sys

method_count = 0

def method(argcount, nlocals, stacksize, flags, codestring, constants, names,
             varnames, filename, name, firstlineno, lnotab, modules, static):
    global method_count
    print 'define', name, method_count
    method_count += 1
    globals_dict = {}
    for module_name in modules:
        if not '[' in module_name and not '.' in module_name:
            globals_dict[module_name] = __import__(module_name, {})
    code = new.code(argcount, nlocals, stacksize, flags, codestring, constants, names,
             varnames, filename, name, firstlineno, lnotab)
    method = new.function(code, globals_dict, name)
    return staticmethod(method) if static else method

nan = None

inf = sys.maxint
