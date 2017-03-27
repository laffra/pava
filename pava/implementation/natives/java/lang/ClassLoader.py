def add_native_methods(clazz):
    def registerNatives():
        raise NotImplementedError()

    def defineClass0(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def defineClass1(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def defineClass2(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def resolveClass0(a0):
        raise NotImplementedError()

    def findBootstrapClass(a0):
        raise NotImplementedError()

    def findLoadedClass0(a0):
        raise NotImplementedError()

    def findBuiltinLib(a0):
        raise NotImplementedError()

    def retrieveDirectives():
        raise NotImplementedError()

    clazz.registerNatives = staticmethod(registerNatives)
    clazz.defineClass0 = defineClass0
    clazz.defineClass1 = defineClass1
    clazz.defineClass2 = defineClass2
    clazz.resolveClass0 = resolveClass0
    clazz.findBootstrapClass = findBootstrapClass
    clazz.findLoadedClass0 = findLoadedClass0
    clazz.findBuiltinLib = staticmethod(findBuiltinLib)
    clazz.retrieveDirectives = staticmethod(retrieveDirectives)

