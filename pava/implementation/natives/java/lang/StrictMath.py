def add_native_methods(clazz):
    def sin(a0):
        raise NotImplementedError()

    def cos(a0):
        raise NotImplementedError()

    def tan(a0):
        raise NotImplementedError()

    def asin(a0):
        raise NotImplementedError()

    def acos(a0):
        raise NotImplementedError()

    def atan(a0):
        raise NotImplementedError()

    def exp(a0):
        raise NotImplementedError()

    def log(a0):
        raise NotImplementedError()

    def log10(a0):
        raise NotImplementedError()

    def sqrt(a0):
        raise NotImplementedError()

    def cbrt(a0):
        raise NotImplementedError()

    def IEEEremainder(a0, a1):
        raise NotImplementedError()

    def atan2(a0, a1):
        raise NotImplementedError()

    def pow(a0, a1):
        raise NotImplementedError()

    def sinh(a0):
        raise NotImplementedError()

    def cosh(a0):
        raise NotImplementedError()

    def tanh(a0):
        raise NotImplementedError()

    def hypot(a0, a1):
        raise NotImplementedError()

    def expm1(a0):
        raise NotImplementedError()

    def log1p(a0):
        raise NotImplementedError()

    clazz.sin = staticmethod(sin)
    clazz.cos = staticmethod(cos)
    clazz.tan = staticmethod(tan)
    clazz.asin = staticmethod(asin)
    clazz.acos = staticmethod(acos)
    clazz.atan = staticmethod(atan)
    clazz.exp = staticmethod(exp)
    clazz.log = staticmethod(log)
    clazz.log10 = staticmethod(log10)
    clazz.sqrt = staticmethod(sqrt)
    clazz.cbrt = staticmethod(cbrt)
    clazz.IEEEremainder = staticmethod(IEEEremainder)
    clazz.atan2 = staticmethod(atan2)
    clazz.pow = staticmethod(pow)
    clazz.sinh = staticmethod(sinh)
    clazz.cosh = staticmethod(cosh)
    clazz.tanh = staticmethod(tanh)
    clazz.hypot = staticmethod(hypot)
    clazz.expm1 = staticmethod(expm1)
    clazz.log1p = staticmethod(log1p)

