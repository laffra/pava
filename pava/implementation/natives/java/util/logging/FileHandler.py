def add_native_methods(clazz):
    def isSetUID____(a0):
        raise NotImplementedError()

    clazz.isSetUID____ = staticmethod(isSetUID____)

