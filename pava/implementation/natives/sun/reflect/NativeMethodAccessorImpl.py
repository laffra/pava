def add_native_methods(clazz):
    def invoke0(a0, a1, a2):
        raise NotImplementedError()

    clazz.invoke0 = staticmethod(invoke0)

