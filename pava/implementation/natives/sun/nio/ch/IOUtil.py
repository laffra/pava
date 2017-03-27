def add_native_methods(clazz):
    def randomBytes(a0):
        raise NotImplementedError()

    def makePipe(a0):
        raise NotImplementedError()

    def drain(a0):
        raise NotImplementedError()

    def configureBlocking(a0, a1):
        raise NotImplementedError()

    def fdVal(a0):
        raise NotImplementedError()

    def setfdVal(a0, a1):
        raise NotImplementedError()

    def fdLimit():
        raise NotImplementedError()

    def iovMax():
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.randomBytes = staticmethod(randomBytes)
    clazz.makePipe = staticmethod(makePipe)
    clazz.drain = staticmethod(drain)
    clazz.configureBlocking = staticmethod(configureBlocking)
    clazz.fdVal = staticmethod(fdVal)
    clazz.setfdVal = staticmethod(setfdVal)
    clazz.fdLimit = staticmethod(fdLimit)
    clazz.iovMax = staticmethod(iovMax)
    clazz.initIDs = staticmethod(initIDs)

