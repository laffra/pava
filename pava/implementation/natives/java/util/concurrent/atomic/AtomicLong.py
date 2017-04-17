def add_native_methods(clazz):
    def VMSupportsCS8____(a0):
        raise NotImplementedError()

    clazz.VMSupportsCS8____ = staticmethod(VMSupportsCS8____)

