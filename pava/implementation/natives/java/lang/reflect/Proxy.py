def add_native_methods(clazz):
    def defineClass0(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz.defineClass0 = staticmethod(defineClass0)

