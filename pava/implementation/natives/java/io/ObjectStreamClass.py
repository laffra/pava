def add_native_methods(clazz):
    def initNative():
        raise NotImplementedError()

    def hasStaticInitializer(a0):
        raise NotImplementedError()

    clazz.initNative = staticmethod(initNative)
    clazz.hasStaticInitializer = staticmethod(hasStaticInitializer)

