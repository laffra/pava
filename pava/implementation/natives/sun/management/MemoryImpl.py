def add_native_methods(clazz):
    def getMemoryPools0____(a0):
        raise NotImplementedError()

    def getMemoryManagers0____(a0):
        raise NotImplementedError()

    def getMemoryUsage0__boolean__(a0, a1):
        raise NotImplementedError()

    def setVerboseGC__boolean__(a0, a1):
        raise NotImplementedError()

    clazz.getMemoryPools0____ = staticmethod(getMemoryPools0____)
    clazz.getMemoryManagers0____ = staticmethod(getMemoryManagers0____)
    clazz.getMemoryUsage0__boolean__ = getMemoryUsage0__boolean__
    clazz.setVerboseGC__boolean__ = setVerboseGC__boolean__

