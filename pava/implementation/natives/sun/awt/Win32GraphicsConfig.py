def add_native_methods(clazz):
    def initIDs____(a0):
        raise NotImplementedError()

    def getBounds__int__(a0, a1):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.getBounds__int__ = getBounds__int__

