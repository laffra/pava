def add_native_methods(clazz):
    def __init__():
        raise NotImplementedError()

    def selectAlternatives(a0, a1):
        raise NotImplementedError()

    clazz.__init__ = __init__
    clazz.selectAlternatives = staticmethod(selectAlternatives)

