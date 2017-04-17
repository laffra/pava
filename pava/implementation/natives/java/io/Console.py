def add_native_methods(clazz):
    def encoding____(a0):
        raise NotImplementedError()

    def echo__boolean__(a0, a1):
        raise NotImplementedError()

    def istty____(a0):
        raise NotImplementedError()

    clazz.encoding____ = staticmethod(encoding____)
    clazz.echo__boolean__ = staticmethod(echo__boolean__)
    clazz.istty____ = staticmethod(istty____)

