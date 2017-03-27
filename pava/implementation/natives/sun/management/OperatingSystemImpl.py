def add_native_methods(clazz):
    def getCommittedVirtualMemorySize0():
        raise NotImplementedError()

    def getTotalSwapSpaceSize():
        raise NotImplementedError()

    def getFreeSwapSpaceSize():
        raise NotImplementedError()

    def getProcessCpuTime():
        raise NotImplementedError()

    def getFreePhysicalMemorySize():
        raise NotImplementedError()

    def getTotalPhysicalMemorySize():
        raise NotImplementedError()

    def getSystemCpuLoad():
        raise NotImplementedError()

    def getProcessCpuLoad():
        raise NotImplementedError()

    def initialize():
        raise NotImplementedError()

    clazz.getCommittedVirtualMemorySize0 = getCommittedVirtualMemorySize0
    clazz.getTotalSwapSpaceSize = getTotalSwapSpaceSize
    clazz.getFreeSwapSpaceSize = getFreeSwapSpaceSize
    clazz.getProcessCpuTime = getProcessCpuTime
    clazz.getFreePhysicalMemorySize = getFreePhysicalMemorySize
    clazz.getTotalPhysicalMemorySize = getTotalPhysicalMemorySize
    clazz.getSystemCpuLoad = getSystemCpuLoad
    clazz.getProcessCpuLoad = getProcessCpuLoad
    clazz.initialize = staticmethod(initialize)

