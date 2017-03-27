def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def socket0(a0, a1):
        raise NotImplementedError()

    def bind0(a0, a1, a2, a3):
        raise NotImplementedError()

    def connect0(a0, a1, a2):
        raise NotImplementedError()

    def waitForConnect(a0, a1):
        raise NotImplementedError()

    def localPort0(a0):
        raise NotImplementedError()

    def localAddress(a0, a1):
        raise NotImplementedError()

    def listen0(a0, a1):
        raise NotImplementedError()

    def accept0(a0, a1):
        raise NotImplementedError()

    def waitForNewConnection(a0, a1):
        raise NotImplementedError()

    def available0(a0):
        raise NotImplementedError()

    def close0(a0):
        raise NotImplementedError()

    def shutdown0(a0, a1):
        raise NotImplementedError()

    def setIntOption(a0, a1, a2):
        raise NotImplementedError()

    def getIntOption(a0, a1):
        raise NotImplementedError()

    def sendOOB(a0, a1):
        raise NotImplementedError()

    def configureBlocking(a0, a1):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.socket0 = staticmethod(socket0)
    clazz.bind0 = staticmethod(bind0)
    clazz.connect0 = staticmethod(connect0)
    clazz.waitForConnect = staticmethod(waitForConnect)
    clazz.localPort0 = staticmethod(localPort0)
    clazz.localAddress = staticmethod(localAddress)
    clazz.listen0 = staticmethod(listen0)
    clazz.accept0 = staticmethod(accept0)
    clazz.waitForNewConnection = staticmethod(waitForNewConnection)
    clazz.available0 = staticmethod(available0)
    clazz.close0 = staticmethod(close0)
    clazz.shutdown0 = staticmethod(shutdown0)
    clazz.setIntOption = staticmethod(setIntOption)
    clazz.getIntOption = staticmethod(getIntOption)
    clazz.sendOOB = staticmethod(sendOOB)
    clazz.configureBlocking = staticmethod(configureBlocking)

