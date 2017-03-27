def add_native_methods(clazz):
    def newInstance0(a0, a1):
        raise NotImplementedError()

    clazz.newInstance0 = staticmethod(newInstance0)

