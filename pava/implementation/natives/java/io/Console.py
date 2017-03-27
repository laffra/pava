def add_native_methods(clazz):
    def encoding():
        raise NotImplementedError()

    def echo(a0):
        raise NotImplementedError()

    def istty():
        raise NotImplementedError()

    clazz.encoding = staticmethod(encoding)
    clazz.echo = staticmethod(echo)
    clazz.istty = staticmethod(istty)

