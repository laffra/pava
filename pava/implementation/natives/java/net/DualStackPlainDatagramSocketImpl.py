def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def socketCreate(a0):
        raise NotImplementedError()

    def socketBind(a0, a1, a2, a3):
        raise NotImplementedError()

    def socketConnect(a0, a1, a2):
        raise NotImplementedError()

    def socketDisconnect(a0):
        raise NotImplementedError()

    def socketClose(a0):
        raise NotImplementedError()

    def socketLocalPort(a0):
        raise NotImplementedError()

    def socketLocalAddress(a0):
        raise NotImplementedError()

    def socketReceiveOrPeekData(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def socketSend(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def socketSetIntOption(a0, a1, a2):
        raise NotImplementedError()

    def socketGetIntOption(a0, a1):
        raise NotImplementedError()

    def dataAvailable():
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.socketCreate = staticmethod(socketCreate)
    clazz.socketBind = staticmethod(socketBind)
    clazz.socketConnect = staticmethod(socketConnect)
    clazz.socketDisconnect = staticmethod(socketDisconnect)
    clazz.socketClose = staticmethod(socketClose)
    clazz.socketLocalPort = staticmethod(socketLocalPort)
    clazz.socketLocalAddress = staticmethod(socketLocalAddress)
    clazz.socketReceiveOrPeekData = staticmethod(socketReceiveOrPeekData)
    clazz.socketSend = staticmethod(socketSend)
    clazz.socketSetIntOption = staticmethod(socketSetIntOption)
    clazz.socketGetIntOption = staticmethod(socketGetIntOption)
    clazz.dataAvailable = dataAvailable

