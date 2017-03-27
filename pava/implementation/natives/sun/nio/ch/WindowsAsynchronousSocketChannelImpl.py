def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def connect0(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def updateConnectContext(a0):
        raise NotImplementedError()

    def read0(a0, a1, a2, a3):
        raise NotImplementedError()

    def write0(a0, a1, a2, a3):
        raise NotImplementedError()

    def shutdown0(a0, a1):
        raise NotImplementedError()

    def closesocket0(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.connect0 = staticmethod(connect0)
    clazz.updateConnectContext = staticmethod(updateConnectContext)
    clazz.read0 = staticmethod(read0)
    clazz.write0 = staticmethod(write0)
    clazz.shutdown0 = staticmethod(shutdown0)
    clazz.closesocket0 = staticmethod(closesocket0)

