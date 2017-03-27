def add_native_methods(clazz):
    def findSignal(a0):
        raise NotImplementedError()

    def handle0(a0, a1):
        raise NotImplementedError()

    def raise0(a0):
        raise NotImplementedError()

    clazz.findSignal = staticmethod(findSignal)
    clazz.handle0 = staticmethod(handle0)
    clazz.raise0 = staticmethod(raise0)

