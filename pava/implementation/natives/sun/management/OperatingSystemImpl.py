def add_native_methods(clazz):
    def getTotalSwapSpaceSize____(a0):
        raise NotImplementedError()

    def getFreeSwapSpaceSize____(a0):
        raise NotImplementedError()

    def getProcessCpuTime____(a0):
        raise NotImplementedError()

    def getFreePhysicalMemorySize____(a0):
        raise NotImplementedError()

    def getTotalPhysicalMemorySize____(a0):
        raise NotImplementedError()

    def getSystemCpuLoad____(a0):
        raise NotImplementedError()

    def getProcessCpuLoad____(a0):
        raise NotImplementedError()

    clazz.getTotalSwapSpaceSize____ = getTotalSwapSpaceSize____
    clazz.getFreeSwapSpaceSize____ = getFreeSwapSpaceSize____
    clazz.getProcessCpuTime____ = getProcessCpuTime____
    clazz.getFreePhysicalMemorySize____ = getFreePhysicalMemorySize____
    clazz.getTotalPhysicalMemorySize____ = getTotalPhysicalMemorySize____
    clazz.getSystemCpuLoad____ = getSystemCpuLoad____
    clazz.getProcessCpuLoad____ = getProcessCpuLoad____

