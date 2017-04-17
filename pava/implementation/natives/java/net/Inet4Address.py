def add_native_methods(clazz):
    def init____(a0):
        raise NotImplementedError()

    clazz.init____ = staticmethod(init____)

