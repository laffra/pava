def add_native_methods(clazz):
    def nativeGenerateSeed(a0):
        raise NotImplementedError()

    clazz.nativeGenerateSeed = staticmethod(nativeGenerateSeed)

