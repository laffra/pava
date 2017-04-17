def add_native_methods(clazz):
    def floatToRawIntBits__float__(a0):
        raise NotImplementedError()

    def intBitsToFloat__int__(a0):
        raise NotImplementedError()

    clazz.floatToRawIntBits__float__ = staticmethod(floatToRawIntBits__float__)
    clazz.intBitsToFloat__int__ = staticmethod(intBitsToFloat__int__)

