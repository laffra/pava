def add_native_methods(clazz):
    def nativeGenerateSeed__byte____(a0, a1):
        raise NotImplementedError()

    clazz.nativeGenerateSeed__byte____ = staticmethod(nativeGenerateSeed__byte____)

