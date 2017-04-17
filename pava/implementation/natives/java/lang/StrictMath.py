def add_native_methods(clazz):
    def sin__double__(a0):
        raise NotImplementedError()

    def cos__double__(a0):
        raise NotImplementedError()

    def tan__double__(a0):
        raise NotImplementedError()

    def asin__double__(a0):
        raise NotImplementedError()

    def acos__double__(a0):
        raise NotImplementedError()

    def atan__double__(a0):
        raise NotImplementedError()

    def exp__double__(a0):
        raise NotImplementedError()

    def log__double__(a0):
        raise NotImplementedError()

    def log10__double__(a0):
        raise NotImplementedError()

    def sqrt__double__(a0):
        raise NotImplementedError()

    def cbrt__double__(a0):
        raise NotImplementedError()

    def IEEEremainder__double__double__(a0, a1):
        raise NotImplementedError()

    def atan2__double__double__(a0, a1):
        raise NotImplementedError()

    def pow__double__double__(a0, a1):
        raise NotImplementedError()

    def sinh__double__(a0):
        raise NotImplementedError()

    def cosh__double__(a0):
        raise NotImplementedError()

    def tanh__double__(a0):
        raise NotImplementedError()

    def hypot__double__double__(a0, a1):
        raise NotImplementedError()

    def expm1__double__(a0):
        raise NotImplementedError()

    def log1p__double__(a0):
        raise NotImplementedError()

    clazz.sin__double__ = staticmethod(sin__double__)
    clazz.cos__double__ = staticmethod(cos__double__)
    clazz.tan__double__ = staticmethod(tan__double__)
    clazz.asin__double__ = staticmethod(asin__double__)
    clazz.acos__double__ = staticmethod(acos__double__)
    clazz.atan__double__ = staticmethod(atan__double__)
    clazz.exp__double__ = staticmethod(exp__double__)
    clazz.log__double__ = staticmethod(log__double__)
    clazz.log10__double__ = staticmethod(log10__double__)
    clazz.sqrt__double__ = staticmethod(sqrt__double__)
    clazz.cbrt__double__ = staticmethod(cbrt__double__)
    clazz.IEEEremainder__double__double__ = staticmethod(IEEEremainder__double__double__)
    clazz.atan2__double__double__ = staticmethod(atan2__double__double__)
    clazz.pow__double__double__ = staticmethod(pow__double__double__)
    clazz.sinh__double__ = staticmethod(sinh__double__)
    clazz.cosh__double__ = staticmethod(cosh__double__)
    clazz.tanh__double__ = staticmethod(tanh__double__)
    clazz.hypot__double__double__ = staticmethod(hypot__double__double__)
    clazz.expm1__double__ = staticmethod(expm1__double__)
    clazz.log1p__double__ = staticmethod(log1p__double__)

