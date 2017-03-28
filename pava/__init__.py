import importlib
from pava.implementation import classloader

set_classpath = classloader.set_classpath
method = implementation.method
nan = implementation.nan
inf = implementation.inf

class JavaPackage(object):
    def __init__(self, name):
        self.name = name
        self.module = None

    def __getattribute__(self, item):
        name = object.__getattribute__(self, 'name')
        module = object.__getattribute__(self, 'module')
        if not module:
            self.module = module = importlib.import_module(name)
        try:
            return getattr(module, item)
        except:
            raise AttributeError('Module %s has no attribute "%s"' % (name, item))