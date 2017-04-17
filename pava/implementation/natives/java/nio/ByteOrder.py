def add_native_methods(clazz):
    def nativeOrder____():
        raise NotImplementedError()

    clazz.nativeOrder____ = staticmethod(nativeOrder____)

