def add_native_methods(clazz):
    def bind0__int__java_net_InetAddress__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def send__java_net_DatagramPacket__(a0, a1):
        raise NotImplementedError()

    def peek__java_net_InetAddress__(a0, a1):
        raise NotImplementedError()

    def peekData__java_net_DatagramPacket__(a0, a1):
        raise NotImplementedError()

    def receive0__java_net_DatagramPacket__(a0, a1):
        raise NotImplementedError()

    def setTimeToLive__int__(a0, a1):
        raise NotImplementedError()

    def getTimeToLive____(a0):
        raise NotImplementedError()

    def setTTL__byte__(a0, a1):
        raise NotImplementedError()

    def getTTL____(a0):
        raise NotImplementedError()

    def join__java_net_InetAddress__java_net_NetworkInterface__(a0, a1, a2):
        raise NotImplementedError()

    def leave__java_net_InetAddress__java_net_NetworkInterface__(a0, a1, a2):
        raise NotImplementedError()

    def datagramSocketCreate____(a0):
        raise NotImplementedError()

    def datagramSocketClose____(a0):
        raise NotImplementedError()

    def socketNativeSetOption__int__java_lang_Object__(a0, a1, a2):
        raise NotImplementedError()

    def socketGetOption__int__(a0, a1):
        raise NotImplementedError()

    def connect0__java_net_InetAddress__int__(a0, a1, a2):
        raise NotImplementedError()

    def socketLocalAddress__int__(a0, a1):
        raise NotImplementedError()

    def disconnect0__int__(a0, a1):
        raise NotImplementedError()

    def dataAvailable____(a0):
        raise NotImplementedError()

    clazz.bind0__int__java_net_InetAddress__boolean__ = bind0__int__java_net_InetAddress__boolean__
    clazz.send__java_net_DatagramPacket__ = send__java_net_DatagramPacket__
    clazz.peek__java_net_InetAddress__ = peek__java_net_InetAddress__
    clazz.peekData__java_net_DatagramPacket__ = peekData__java_net_DatagramPacket__
    clazz.receive0__java_net_DatagramPacket__ = receive0__java_net_DatagramPacket__
    clazz.setTimeToLive__int__ = setTimeToLive__int__
    clazz.getTimeToLive____ = getTimeToLive____
    clazz.setTTL__byte__ = setTTL__byte__
    clazz.getTTL____ = getTTL____
    clazz.join__java_net_InetAddress__java_net_NetworkInterface__ = join__java_net_InetAddress__java_net_NetworkInterface__
    clazz.leave__java_net_InetAddress__java_net_NetworkInterface__ = leave__java_net_InetAddress__java_net_NetworkInterface__
    clazz.datagramSocketCreate____ = datagramSocketCreate____
    clazz.datagramSocketClose____ = datagramSocketClose____
    clazz.socketNativeSetOption__int__java_lang_Object__ = socketNativeSetOption__int__java_lang_Object__
    clazz.socketGetOption__int__ = socketGetOption__int__
    clazz.connect0__java_net_InetAddress__int__ = connect0__java_net_InetAddress__int__
    clazz.socketLocalAddress__int__ = socketLocalAddress__int__
    clazz.disconnect0__int__ = disconnect0__int__
    clazz.dataAvailable____ = dataAvailable____

