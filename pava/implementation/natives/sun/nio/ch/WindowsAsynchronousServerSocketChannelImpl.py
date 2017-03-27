def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def accept0(a0, a1, a2, a3):
        raise NotImplementedError()

    def updateAcceptContext(a0, a1):
        raise NotImplementedError()

    def closesocket0(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.accept0 = staticmethod(accept0)
    clazz.updateAcceptContext = staticmethod(updateAcceptContext)
    clazz.closesocket0 = staticmethod(closesocket0)

