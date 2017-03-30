def add_native_methods(clazz):
    def nativeOrder():
        raise NotImplementedError()

    clazz.nativeOrder = staticmethod(nativeOrder)

