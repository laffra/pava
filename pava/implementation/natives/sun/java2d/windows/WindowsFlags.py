def add_native_methods(clazz):
    def initNativeFlags():
        raise NotImplementedError()

    clazz.initNativeFlags = staticmethod(initNativeFlags)

