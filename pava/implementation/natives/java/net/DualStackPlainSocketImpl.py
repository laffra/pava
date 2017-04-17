def add_native_methods(clazz):
    def initIDs____():
        raise NotImplementedError()

    def socket0__boolean__boolean__(a0, a1):
        raise NotImplementedError()

    def bind0__int__java_net_InetAddress__int__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def connect0__int__java_net_InetAddress__int__(a0, a1, a2):
        raise NotImplementedError()

    def waitForConnect__int__int__(a0, a1):
        raise NotImplementedError()

    def localPort0__int__(a0):
        raise NotImplementedError()

    def localAddress__int__java_net_InetAddressContainer__(a0, a1):
        raise NotImplementedError()

    def listen0__int__int__(a0, a1):
        raise NotImplementedError()

    def accept0__int__java_net_InetSocketAddress____(a0, a1):
        raise NotImplementedError()

    def waitForNewConnection__int__int__(a0, a1):
        raise NotImplementedError()

    def available0__int__(a0):
        raise NotImplementedError()

    def close0__int__(a0):
        raise NotImplementedError()

    def shutdown0__int__int__(a0, a1):
        raise NotImplementedError()

    def setIntOption__int__int__int__(a0, a1, a2):
        raise NotImplementedError()

    def getIntOption__int__int__(a0, a1):
        raise NotImplementedError()

    def sendOOB__int__int__(a0, a1):
        raise NotImplementedError()

    def configureBlocking__int__boolean__(a0, a1):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.socket0__boolean__boolean__ = staticmethod(socket0__boolean__boolean__)
    clazz.bind0__int__java_net_InetAddress__int__boolean__ = staticmethod(bind0__int__java_net_InetAddress__int__boolean__)
    clazz.connect0__int__java_net_InetAddress__int__ = staticmethod(connect0__int__java_net_InetAddress__int__)
    clazz.waitForConnect__int__int__ = staticmethod(waitForConnect__int__int__)
    clazz.localPort0__int__ = staticmethod(localPort0__int__)
    clazz.localAddress__int__java_net_InetAddressContainer__ = staticmethod(localAddress__int__java_net_InetAddressContainer__)
    clazz.listen0__int__int__ = staticmethod(listen0__int__int__)
    clazz.accept0__int__java_net_InetSocketAddress____ = staticmethod(accept0__int__java_net_InetSocketAddress____)
    clazz.waitForNewConnection__int__int__ = staticmethod(waitForNewConnection__int__int__)
    clazz.available0__int__ = staticmethod(available0__int__)
    clazz.close0__int__ = staticmethod(close0__int__)
    clazz.shutdown0__int__int__ = staticmethod(shutdown0__int__int__)
    clazz.setIntOption__int__int__int__ = staticmethod(setIntOption__int__int__int__)
    clazz.getIntOption__int__int__ = staticmethod(getIntOption__int__int__)
    clazz.sendOOB__int__int__ = staticmethod(sendOOB__int__int__)
    clazz.configureBlocking__int__boolean__ = staticmethod(configureBlocking__int__boolean__)

