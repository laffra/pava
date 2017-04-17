def add_native_methods(clazz):
    def doubleToRawLongBits__double__(a0):
        raise NotImplementedError()

    def longBitsToDouble__long__(a0):
        raise NotImplementedError()

    clazz.doubleToRawLongBits__double__ = staticmethod(doubleToRawLongBits__double__)
    clazz.longBitsToDouble__long__ = staticmethod(longBitsToDouble__long__)

