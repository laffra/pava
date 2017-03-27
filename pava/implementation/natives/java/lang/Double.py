def add_native_methods(clazz):
    def doubleToRawLongBits(a0):
        raise NotImplementedError()

    def longBitsToDouble(a0):
        raise NotImplementedError()

    clazz.doubleToRawLongBits = staticmethod(doubleToRawLongBits)
    clazz.longBitsToDouble = staticmethod(longBitsToDouble)

