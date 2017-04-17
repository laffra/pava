def add_native_methods(clazz):
    def canConvert__char__(a0, a1):
        raise NotImplementedError()

    def initIDs____(a0):
        raise NotImplementedError()

    clazz.canConvert__char__ = canConvert__char__
    clazz.initIDs____ = staticmethod(initIDs____)

