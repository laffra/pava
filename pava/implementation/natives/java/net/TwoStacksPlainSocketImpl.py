def add_native_methods(clazz):
    def initProto():
        raise NotImplementedError()

    def socketCreate(a0):
        raise NotImplementedError()

    def socketConnect(a0, a1, a2):
        raise NotImplementedError()

    def socketBind(a0, a1, a2):
        raise NotImplementedError()

    def socketListen(a0):
        raise NotImplementedError()

    def socketAccept(a0):
        raise NotImplementedError()

    def socketAvailable():
        raise NotImplementedError()

    def socketClose0(a0):
        raise NotImplementedError()

    def socketShutdown(a0):
        raise NotImplementedError()

    def socketNativeSetOption(a0, a1, a2):
        raise NotImplementedError()

    def socketGetOption(a0, a1):
        raise NotImplementedError()

    def socketSendUrgentData(a0):
        raise NotImplementedError()

    clazz.initProto = staticmethod(initProto)
    clazz.socketCreate = socketCreate
    clazz.socketConnect = socketConnect
    clazz.socketBind = socketBind
    clazz.socketListen = socketListen
    clazz.socketAccept = socketAccept
    clazz.socketAvailable = socketAvailable
    clazz.socketClose0 = socketClose0
    clazz.socketShutdown = socketShutdown
    clazz.socketNativeSetOption = socketNativeSetOption
    clazz.socketGetOption = socketGetOption
    clazz.socketSendUrgentData = socketSendUrgentData

