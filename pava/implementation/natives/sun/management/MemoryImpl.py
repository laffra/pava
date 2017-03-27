def add_native_methods(clazz):
    def getMemoryPools0():
        raise NotImplementedError()

    def getMemoryManagers0():
        raise NotImplementedError()

    def getMemoryUsage0(a0):
        raise NotImplementedError()

    def setVerboseGC(a0):
        raise NotImplementedError()

    clazz.getMemoryPools0 = staticmethod(getMemoryPools0)
    clazz.getMemoryManagers0 = staticmethod(getMemoryManagers0)
    clazz.getMemoryUsage0 = getMemoryUsage0
    clazz.setVerboseGC = setVerboseGC

