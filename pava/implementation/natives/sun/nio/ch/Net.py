def add_native_methods(clazz):
    def isIPv6Available0():
        raise NotImplementedError()

    def isExclusiveBindAvailable():
        raise NotImplementedError()

    def canIPv6SocketJoinIPv4Group0():
        raise NotImplementedError()

    def canJoin6WithIPv4Group0():
        raise NotImplementedError()

    def socket0(a0, a1, a2, a3):
        raise NotImplementedError()

    def bind0(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def listen(a0, a1):
        raise NotImplementedError()

    def connect0(a0, a1, a2, a3):
        raise NotImplementedError()

    def shutdown(a0, a1):
        raise NotImplementedError()

    def localPort(a0):
        raise NotImplementedError()

    def localInetAddress(a0):
        raise NotImplementedError()

    def remotePort(a0):
        raise NotImplementedError()

    def remoteInetAddress(a0):
        raise NotImplementedError()

    def getIntOption0(a0, a1, a2, a3):
        raise NotImplementedError()

    def setIntOption0(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def poll(a0, a1, a2):
        raise NotImplementedError()

    def joinOrDrop4(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def blockOrUnblock4(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def joinOrDrop6(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def blockOrUnblock6(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def setInterface4(a0, a1):
        raise NotImplementedError()

    def getInterface4(a0):
        raise NotImplementedError()

    def setInterface6(a0, a1):
        raise NotImplementedError()

    def getInterface6(a0):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    def pollinValue():
        raise NotImplementedError()

    def polloutValue():
        raise NotImplementedError()

    def pollerrValue():
        raise NotImplementedError()

    def pollhupValue():
        raise NotImplementedError()

    def pollnvalValue():
        raise NotImplementedError()

    def pollconnValue():
        raise NotImplementedError()

    clazz.isIPv6Available0 = staticmethod(isIPv6Available0)
    clazz.isExclusiveBindAvailable = staticmethod(isExclusiveBindAvailable)
    clazz.canIPv6SocketJoinIPv4Group0 = staticmethod(canIPv6SocketJoinIPv4Group0)
    clazz.canJoin6WithIPv4Group0 = staticmethod(canJoin6WithIPv4Group0)
    clazz.socket0 = staticmethod(socket0)
    clazz.bind0 = staticmethod(bind0)
    clazz.listen = staticmethod(listen)
    clazz.connect0 = staticmethod(connect0)
    clazz.shutdown = staticmethod(shutdown)
    clazz.localPort = staticmethod(localPort)
    clazz.localInetAddress = staticmethod(localInetAddress)
    clazz.remotePort = staticmethod(remotePort)
    clazz.remoteInetAddress = staticmethod(remoteInetAddress)
    clazz.getIntOption0 = staticmethod(getIntOption0)
    clazz.setIntOption0 = staticmethod(setIntOption0)
    clazz.poll = staticmethod(poll)
    clazz.joinOrDrop4 = staticmethod(joinOrDrop4)
    clazz.blockOrUnblock4 = staticmethod(blockOrUnblock4)
    clazz.joinOrDrop6 = staticmethod(joinOrDrop6)
    clazz.blockOrUnblock6 = staticmethod(blockOrUnblock6)
    clazz.setInterface4 = staticmethod(setInterface4)
    clazz.getInterface4 = staticmethod(getInterface4)
    clazz.setInterface6 = staticmethod(setInterface6)
    clazz.getInterface6 = staticmethod(getInterface6)
    clazz.initIDs = staticmethod(initIDs)
    clazz.pollinValue = staticmethod(pollinValue)
    clazz.polloutValue = staticmethod(polloutValue)
    clazz.pollerrValue = staticmethod(pollerrValue)
    clazz.pollhupValue = staticmethod(pollhupValue)
    clazz.pollnvalValue = staticmethod(pollnvalValue)
    clazz.pollconnValue = staticmethod(pollconnValue)

