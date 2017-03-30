import importlib
import os
from pava.implementation import classloader
from pava.implementation import javaruntime

set_classpath = classloader.set_classpath

method = implementation.method
nan = implementation.nan
inf = implementation.inf
load_natives = implementation.load_natives

run_java_test = javaruntime.run_java_test


class JavaPackage(object):
    def __init__(self, name):
        self.name = name
        self.module = None

    def __getattribute__(self, item):
        name = object.__getattribute__(self, 'name')
        module = object.__getattribute__(self, 'module')
        if not module:
            self.module =  module = importlib.import_module(name)
        try:
            return getattr(module, item)
        except:
            raise AttributeError('Module %s has no attribute "%s"' % (name, item))



