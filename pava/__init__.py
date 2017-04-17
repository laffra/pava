import importlib
import os
from pava.implementation import classloader
from pava.implementation import javaruntime

set_classpath = classloader.set_classpath

nan = implementation.nan
inf = implementation.inf
load_natives = implementation.load_natives
multianewarray = implementation.multianewarray
checkcast = implementation.checkcast

def JavaPackage(name): pass

run_java_test = javaruntime.run_java_test

LazyModule = implementation.LazyModule
JavaClass = implementation.JavaClass

