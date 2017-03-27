def add_native_methods(clazz):
    def handle0(a0, a1):
        raise NotImplementedError()

    clazz.handle0 = staticmethod(handle0)

