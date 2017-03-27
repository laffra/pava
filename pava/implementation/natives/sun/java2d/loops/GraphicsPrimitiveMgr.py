def add_native_methods(clazz):
    def initIDs(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
        raise NotImplementedError()

    def registerNativeLoops():
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.registerNativeLoops = staticmethod(registerNativeLoops)

