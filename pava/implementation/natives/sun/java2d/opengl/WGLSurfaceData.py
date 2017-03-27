def add_native_methods(clazz):
    def initOps(a0, a1, a2):
        raise NotImplementedError()

    def initPbuffer(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def updateWindowAccelImpl(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.initOps = initOps
    clazz.initPbuffer = initPbuffer
    clazz.updateWindowAccelImpl = staticmethod(updateWindowAccelImpl)

