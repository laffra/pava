def add_native_methods(clazz):
    def getThreads():
        raise NotImplementedError()

    def getThreadInfo1(a0, a1, a2):
        raise NotImplementedError()

    def getThreadTotalCpuTime0(a0):
        raise NotImplementedError()

    def getThreadTotalCpuTime1(a0, a1):
        raise NotImplementedError()

    def getThreadUserCpuTime0(a0):
        raise NotImplementedError()

    def getThreadUserCpuTime1(a0, a1):
        raise NotImplementedError()

    def getThreadAllocatedMemory1(a0, a1):
        raise NotImplementedError()

    def setThreadCpuTimeEnabled0(a0):
        raise NotImplementedError()

    def setThreadAllocatedMemoryEnabled0(a0):
        raise NotImplementedError()

    def setThreadContentionMonitoringEnabled0(a0):
        raise NotImplementedError()

    def findMonitorDeadlockedThreads0():
        raise NotImplementedError()

    def findDeadlockedThreads0():
        raise NotImplementedError()

    def resetPeakThreadCount0():
        raise NotImplementedError()

    def dumpThreads0(a0, a1, a2):
        raise NotImplementedError()

    def resetContentionTimes0(a0):
        raise NotImplementedError()

    clazz.getThreads = staticmethod(getThreads)
    clazz.getThreadInfo1 = staticmethod(getThreadInfo1)
    clazz.getThreadTotalCpuTime0 = staticmethod(getThreadTotalCpuTime0)
    clazz.getThreadTotalCpuTime1 = staticmethod(getThreadTotalCpuTime1)
    clazz.getThreadUserCpuTime0 = staticmethod(getThreadUserCpuTime0)
    clazz.getThreadUserCpuTime1 = staticmethod(getThreadUserCpuTime1)
    clazz.getThreadAllocatedMemory1 = staticmethod(getThreadAllocatedMemory1)
    clazz.setThreadCpuTimeEnabled0 = staticmethod(setThreadCpuTimeEnabled0)
    clazz.setThreadAllocatedMemoryEnabled0 = staticmethod(setThreadAllocatedMemoryEnabled0)
    clazz.setThreadContentionMonitoringEnabled0 = staticmethod(setThreadContentionMonitoringEnabled0)
    clazz.findMonitorDeadlockedThreads0 = staticmethod(findMonitorDeadlockedThreads0)
    clazz.findDeadlockedThreads0 = staticmethod(findDeadlockedThreads0)
    clazz.resetPeakThreadCount0 = staticmethod(resetPeakThreadCount0)
    clazz.dumpThreads0 = staticmethod(dumpThreads0)
    clazz.resetContentionTimes0 = staticmethod(resetContentionTimes0)

