def add_native_methods(clazz):
    def initIDs____(a0):
        raise NotImplementedError()

    def accept0__long__long__long__long__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def updateAcceptContext__long__long__(a0, a1, a2):
        raise NotImplementedError()

    def closesocket0__long__(a0, a1):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.accept0__long__long__long__long__ = staticmethod(accept0__long__long__long__long__)
    clazz.updateAcceptContext__long__long__ = staticmethod(updateAcceptContext__long__long__)
    clazz.closesocket0__long__ = staticmethod(closesocket0__long__)

