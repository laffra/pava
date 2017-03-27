def add_native_methods(clazz):
    def initTexture(a0, a1, a2):
        raise NotImplementedError()

    def initFlipBackbuffer(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def initRTSurface(a0, a1):
        raise NotImplementedError()

    def initOps(a0, a1, a2):
        raise NotImplementedError()

    def dbGetPixelNative(a0, a1, a2):
        raise NotImplementedError()

    def dbSetPixelNative(a0, a1, a2, a3):
        raise NotImplementedError()

    def getNativeResourceNative(a0, a1):
        raise NotImplementedError()

    def updateWindowAccelImpl(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.initTexture = initTexture
    clazz.initFlipBackbuffer = initFlipBackbuffer
    clazz.initRTSurface = initRTSurface
    clazz.initOps = initOps
    clazz.dbGetPixelNative = staticmethod(dbGetPixelNative)
    clazz.dbSetPixelNative = staticmethod(dbSetPixelNative)
    clazz.getNativeResourceNative = staticmethod(getNativeResourceNative)
    clazz.updateWindowAccelImpl = staticmethod(updateWindowAccelImpl)

