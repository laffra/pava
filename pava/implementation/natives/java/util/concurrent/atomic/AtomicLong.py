def add_native_methods(clazz):
    def VMSupportsCS8():
        raise NotImplementedError()

    clazz.VMSupportsCS8 = staticmethod(VMSupportsCS8)

