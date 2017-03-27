def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def initDevice(a0):
        raise NotImplementedError()

    def getMaxConfigsImpl(a0):
        raise NotImplementedError()

    def isPixFmtSupported(a0, a1):
        raise NotImplementedError()

    def getDefaultPixIDImpl(a0):
        raise NotImplementedError()

    def enterFullScreenExclusive(a0, a1):
        raise NotImplementedError()

    def exitFullScreenExclusive(a0, a1):
        raise NotImplementedError()

    def getCurrentDisplayMode(a0):
        raise NotImplementedError()

    def configDisplayMode(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def enumDisplayModes(a0, a1):
        raise NotImplementedError()

    def makeColorModel(a0, a1):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.initDevice = initDevice
    clazz.getMaxConfigsImpl = getMaxConfigsImpl
    clazz.isPixFmtSupported = isPixFmtSupported
    clazz.getDefaultPixIDImpl = getDefaultPixIDImpl
    clazz.enterFullScreenExclusive = enterFullScreenExclusive
    clazz.exitFullScreenExclusive = exitFullScreenExclusive
    clazz.getCurrentDisplayMode = getCurrentDisplayMode
    clazz.configDisplayMode = configDisplayMode
    clazz.enumDisplayModes = enumDisplayModes
    clazz.makeColorModel = makeColorModel

