def add_native_methods(clazz):
    def initIDs____(a0):
        raise NotImplementedError()

    def finalizeImpl__long__(a0, a1):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.finalizeImpl__long__ = staticmethod(finalizeImpl__long__)

