def add_native_methods(clazz):
    def initProto____():
        raise NotImplementedError()

    def socketCreate__boolean__(a0, a1):
        raise NotImplementedError()

    def socketConnect__java_net_InetAddress__int__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def socketBind__java_net_InetAddress__int__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def socketListen__int__(a0, a1):
        raise NotImplementedError()

    def socketAccept__java_net_SocketImpl__(a0, a1):
        raise NotImplementedError()

    def socketAvailable____(a0):
        raise NotImplementedError()

    def socketClose0__boolean__(a0, a1):
        raise NotImplementedError()

    def socketShutdown__int__(a0, a1):
        raise NotImplementedError()

    def socketNativeSetOption__int__boolean__java_lang_Object__(a0, a1, a2, a3):
        raise NotImplementedError()

    def socketGetOption__int__java_lang_Object__(a0, a1, a2):
        raise NotImplementedError()

    def socketSendUrgentData__int__(a0, a1):
        raise NotImplementedError()

    clazz.initProto____ = staticmethod(initProto____)
    clazz.socketCreate__boolean__ = socketCreate__boolean__
    clazz.socketConnect__java_net_InetAddress__int__int__ = socketConnect__java_net_InetAddress__int__int__
    clazz.socketBind__java_net_InetAddress__int__boolean__ = socketBind__java_net_InetAddress__int__boolean__
    clazz.socketListen__int__ = socketListen__int__
    clazz.socketAccept__java_net_SocketImpl__ = socketAccept__java_net_SocketImpl__
    clazz.socketAvailable____ = socketAvailable____
    clazz.socketClose0__boolean__ = socketClose0__boolean__
    clazz.socketShutdown__int__ = socketShutdown__int__
    clazz.socketNativeSetOption__int__boolean__java_lang_Object__ = socketNativeSetOption__int__boolean__java_lang_Object__
    clazz.socketGetOption__int__java_lang_Object__ = socketGetOption__int__java_lang_Object__
    clazz.socketSendUrgentData__int__ = socketSendUrgentData__int__

