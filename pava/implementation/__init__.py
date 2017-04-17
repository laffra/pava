import imp
import importlib
import os
import sys

DEBUG = False

def pava_to_string(object):
    try:
        return object.toString____()
    except:
        return str(object)


def multianewarray(*dimensions):
    raise NotImplementedError('multianewarray not yet implemented')


def checkcast(obj, cls):
    if not isinstance(obj, cls):
        import java
        raise java.lang.ClassCastException('Object of type "%s" cannot be cast to type "%s"' % (
            type(obj).__name__, cls.__name__)
        )
    return obj


nan = None

inf = sys.maxint


def load_natives(module_name, clazz):
    natives = importlib.import_module('pava.implementation.natives.' + module_name)
    natives.add_native_methods(clazz)


class LazyModule(object):
    def __init__(self, name, file_name):
        self.name = name
        self.file_name = file_name
        self.cache = {}
        sys.modules[name + '_pava'] = sys.modules[__name__]
        sys.modules[name] = self

    def __getattr__(self, item):
        cache = self.__getattribute__('cache')
        if item in cache:
            return cache[item]
        name = self.__getattribute__('name')
        file_name = self.__getattribute__('file_name')
        path = name.split('.')
        if item == '__path__':
            return path
        else:
            item_file_name = os.path.join(os.path.dirname(file_name), item + '.py')
            if not os.path.exists(item_file_name):
                item_file_name = os.path.join(os.path.dirname(file_name), os.path.join(item,  '__init__.py'))
            if os.path.exists(item_file_name):
                name = '%s.%s' % (name, item)
                module = imp.load_source(name, item_file_name)
                sys.modules[name + '.' + item] = module
                if hasattr(module, item):
                    module = getattr(module, item)
                print 'Loaded ', item, module
                cache[item] = module
                return module
            else:
                raise ImportError('Cannot load ' + item_file_name)


class JavaClass(object):
    def __init__(self):
        print 'Init', type(self)
