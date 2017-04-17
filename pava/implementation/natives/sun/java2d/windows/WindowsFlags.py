def add_native_methods(clazz):
    def initNativeFlags____(a0):
        raise NotImplementedError()

    clazz.initNativeFlags____ = staticmethod(initNativeFlags____)

