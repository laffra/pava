def add_native_methods(clazz):
    def initD3D____(a0):
        raise NotImplementedError()

    def getDeviceCapsNative__int__(a0, a1):
        raise NotImplementedError()

    def getDeviceIdNative__int__(a0, a1):
        raise NotImplementedError()

    def enterFullScreenExclusiveNative__int__long__(a0, a1, a2):
        raise NotImplementedError()

    def exitFullScreenExclusiveNative__int__(a0, a1):
        raise NotImplementedError()

    def getCurrentDisplayModeNative__int__(a0, a1):
        raise NotImplementedError()

    def configDisplayModeNative__int__long__int__int__int__int__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def enumDisplayModesNative__int__java_util_ArrayList__(a0, a1, a2):
        raise NotImplementedError()

    def getAvailableAcceleratedMemoryNative__int__(a0, a1):
        raise NotImplementedError()

    def isD3DAvailableOnDeviceNative__int__(a0, a1):
        raise NotImplementedError()

    clazz.initD3D____ = staticmethod(initD3D____)
    clazz.getDeviceCapsNative__int__ = staticmethod(getDeviceCapsNative__int__)
    clazz.getDeviceIdNative__int__ = staticmethod(getDeviceIdNative__int__)
    clazz.enterFullScreenExclusiveNative__int__long__ = staticmethod(enterFullScreenExclusiveNative__int__long__)
    clazz.exitFullScreenExclusiveNative__int__ = staticmethod(exitFullScreenExclusiveNative__int__)
    clazz.getCurrentDisplayModeNative__int__ = staticmethod(getCurrentDisplayModeNative__int__)
    clazz.configDisplayModeNative__int__long__int__int__int__int__ = staticmethod(configDisplayModeNative__int__long__int__int__int__int__)
    clazz.enumDisplayModesNative__int__java_util_ArrayList__ = staticmethod(enumDisplayModesNative__int__java_util_ArrayList__)
    clazz.getAvailableAcceleratedMemoryNative__int__ = staticmethod(getAvailableAcceleratedMemoryNative__int__)
    clazz.isD3DAvailableOnDeviceNative__int__ = staticmethod(isD3DAvailableOnDeviceNative__int__)

