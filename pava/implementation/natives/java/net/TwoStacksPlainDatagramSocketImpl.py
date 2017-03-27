def add_native_methods(clazz):
    def bind0(a0, a1, a2):
        raise NotImplementedError()

    def send(a0):
        raise NotImplementedError()

    def peek(a0):
        raise NotImplementedError()

    def peekData(a0):
        raise NotImplementedError()

    def receive0(a0):
        raise NotImplementedError()

    def setTimeToLive(a0):
        raise NotImplementedError()

    def getTimeToLive():
        raise NotImplementedError()

    def setTTL(a0):
        raise NotImplementedError()

    def getTTL():
        raise NotImplementedError()

    def join(a0, a1):
        raise NotImplementedError()

    def leave(a0, a1):
        raise NotImplementedError()

    def datagramSocketCreate():
        raise NotImplementedError()

    def datagramSocketClose():
        raise NotImplementedError()

    def socketNativeSetOption(a0, a1):
        raise NotImplementedError()

    def socketGetOption(a0):
        raise NotImplementedError()

    def connect0(a0, a1):
        raise NotImplementedError()

    def socketLocalAddress(a0):
        raise NotImplementedError()

    def disconnect0(a0):
        raise NotImplementedError()

    def dataAvailable():
        raise NotImplementedError()

    def init():
        raise NotImplementedError()

    clazz.bind0 = bind0
    clazz.send = send
    clazz.peek = peek
    clazz.peekData = peekData
    clazz.receive0 = receive0
    clazz.setTimeToLive = setTimeToLive
    clazz.getTimeToLive = getTimeToLive
    clazz.setTTL = setTTL
    clazz.getTTL = getTTL
    clazz.join = join
    clazz.leave = leave
    clazz.datagramSocketCreate = datagramSocketCreate
    clazz.datagramSocketClose = datagramSocketClose
    clazz.socketNativeSetOption = socketNativeSetOption
    clazz.socketGetOption = socketGetOption
    clazz.connect0 = connect0
    clazz.socketLocalAddress = socketLocalAddress
    clazz.disconnect0 = disconnect0
    clazz.dataAvailable = dataAvailable
    clazz.init = staticmethod(init)

