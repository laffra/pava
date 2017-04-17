def add_native_methods(clazz):
    def setVmMemoryPressure__int__(a0, a1):
        raise NotImplementedError()

    def getVmMemoryPressure____(a0):
        raise NotImplementedError()

    clazz.setVmMemoryPressure__int__ = setVmMemoryPressure__int__
    clazz.getVmMemoryPressure____ = getVmMemoryPressure____

