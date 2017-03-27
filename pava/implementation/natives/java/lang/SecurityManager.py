def add_native_methods(clazz):
    def getClassContext():
        raise NotImplementedError()

    def currentClassLoader0():
        raise NotImplementedError()

    def classDepth(a0):
        raise NotImplementedError()

    def classLoaderDepth0():
        raise NotImplementedError()

    def currentLoadedClass0():
        raise NotImplementedError()

    clazz.getClassContext = getClassContext
    clazz.currentClassLoader0 = currentClassLoader0
    clazz.classDepth = classDepth
    clazz.classLoaderDepth0 = classLoaderDepth0
    clazz.currentLoadedClass0 = currentLoadedClass0

