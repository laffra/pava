def add_native_methods(clazz):
    def floatToRawIntBits(a0):
        raise NotImplementedError()

    def intBitsToFloat(a0):
        raise NotImplementedError()

    clazz.floatToRawIntBits = staticmethod(floatToRawIntBits)
    clazz.intBitsToFloat = staticmethod(intBitsToFloat)

