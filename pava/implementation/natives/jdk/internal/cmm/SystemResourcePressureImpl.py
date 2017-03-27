def add_native_methods(clazz):
    def setVmMemoryPressure(a0):
        raise NotImplementedError()

    def getVmMemoryPressure():
        raise NotImplementedError()

    clazz.setVmMemoryPressure = setVmMemoryPressure
    clazz.getVmMemoryPressure = getVmMemoryPressure

