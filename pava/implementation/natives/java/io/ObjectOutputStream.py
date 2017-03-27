def add_native_methods(clazz):
    def floatsToBytes(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def doublesToBytes(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz.floatsToBytes = staticmethod(floatsToBytes)
    clazz.doublesToBytes = staticmethod(doublesToBytes)

