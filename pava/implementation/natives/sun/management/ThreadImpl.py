def add_native_methods(clazz):
    def getThreads____(a0):
        raise NotImplementedError()

    def getThreadInfo1__long____int__java_lang_management_ThreadInfo____(a0, a1, a2, a3):
        raise NotImplementedError()

    def getThreadTotalCpuTime0__long__(a0, a1):
        raise NotImplementedError()

    def getThreadTotalCpuTime1__long____long____(a0, a1, a2):
        raise NotImplementedError()

    def getThreadUserCpuTime0__long__(a0, a1):
        raise NotImplementedError()

    def getThreadUserCpuTime1__long____long____(a0, a1, a2):
        raise NotImplementedError()

    def getThreadAllocatedMemory1__long____long____(a0, a1, a2):
        raise NotImplementedError()

    def setThreadCpuTimeEnabled0__boolean__(a0, a1):
        raise NotImplementedError()

    def setThreadAllocatedMemoryEnabled0__boolean__(a0, a1):
        raise NotImplementedError()

    def setThreadContentionMonitoringEnabled0__boolean__(a0, a1):
        raise NotImplementedError()

    def findMonitorDeadlockedThreads0____(a0):
        raise NotImplementedError()

    def findDeadlockedThreads0____(a0):
        raise NotImplementedError()

    def resetPeakThreadCount0____(a0):
        raise NotImplementedError()

    def dumpThreads0__long____boolean__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def resetContentionTimes0__long__(a0, a1):
        raise NotImplementedError()

    clazz.getThreads____ = staticmethod(getThreads____)
    clazz.getThreadInfo1__long____int__java_lang_management_ThreadInfo____ = staticmethod(getThreadInfo1__long____int__java_lang_management_ThreadInfo____)
    clazz.getThreadTotalCpuTime0__long__ = staticmethod(getThreadTotalCpuTime0__long__)
    clazz.getThreadTotalCpuTime1__long____long____ = staticmethod(getThreadTotalCpuTime1__long____long____)
    clazz.getThreadUserCpuTime0__long__ = staticmethod(getThreadUserCpuTime0__long__)
    clazz.getThreadUserCpuTime1__long____long____ = staticmethod(getThreadUserCpuTime1__long____long____)
    clazz.getThreadAllocatedMemory1__long____long____ = staticmethod(getThreadAllocatedMemory1__long____long____)
    clazz.setThreadCpuTimeEnabled0__boolean__ = staticmethod(setThreadCpuTimeEnabled0__boolean__)
    clazz.setThreadAllocatedMemoryEnabled0__boolean__ = staticmethod(setThreadAllocatedMemoryEnabled0__boolean__)
    clazz.setThreadContentionMonitoringEnabled0__boolean__ = staticmethod(setThreadContentionMonitoringEnabled0__boolean__)
    clazz.findMonitorDeadlockedThreads0____ = staticmethod(findMonitorDeadlockedThreads0____)
    clazz.findDeadlockedThreads0____ = staticmethod(findDeadlockedThreads0____)
    clazz.resetPeakThreadCount0____ = staticmethod(resetPeakThreadCount0____)
    clazz.dumpThreads0__long____boolean__boolean__ = staticmethod(dumpThreads0__long____boolean__boolean__)
    clazz.resetContentionTimes0__long__ = staticmethod(resetContentionTimes0__long__)

