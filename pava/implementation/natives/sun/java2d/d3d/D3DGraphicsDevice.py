def add_native_methods(clazz):
    def initD3D():
        raise NotImplementedError()

    def getDeviceCapsNative(a0):
        raise NotImplementedError()

    def getDeviceIdNative(a0):
        raise NotImplementedError()

    def enterFullScreenExclusiveNative(a0, a1):
        raise NotImplementedError()

    def exitFullScreenExclusiveNative(a0):
        raise NotImplementedError()

    def getCurrentDisplayModeNative(a0):
        raise NotImplementedError()

    def configDisplayModeNative(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def enumDisplayModesNative(a0, a1):
        raise NotImplementedError()

    def getAvailableAcceleratedMemoryNative(a0):
        raise NotImplementedError()

    def isD3DAvailableOnDeviceNative(a0):
        raise NotImplementedError()

    clazz.initD3D = staticmethod(initD3D)
    clazz.getDeviceCapsNative = staticmethod(getDeviceCapsNative)
    clazz.getDeviceIdNative = staticmethod(getDeviceIdNative)
    clazz.enterFullScreenExclusiveNative = staticmethod(enterFullScreenExclusiveNative)
    clazz.exitFullScreenExclusiveNative = staticmethod(exitFullScreenExclusiveNative)
    clazz.getCurrentDisplayModeNative = staticmethod(getCurrentDisplayModeNative)
    clazz.configDisplayModeNative = staticmethod(configDisplayModeNative)
    clazz.enumDisplayModesNative = staticmethod(enumDisplayModesNative)
    clazz.getAvailableAcceleratedMemoryNative = staticmethod(getAvailableAcceleratedMemoryNative)
    clazz.isD3DAvailableOnDeviceNative = staticmethod(isD3DAvailableOnDeviceNative)

