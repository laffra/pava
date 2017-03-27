def add_native_methods(clazz):
    def getVersion0():
        raise NotImplementedError()

    def initOptionalSupportFields():
        raise NotImplementedError()

    def isThreadContentionMonitoringEnabled():
        raise NotImplementedError()

    def isThreadCpuTimeEnabled():
        raise NotImplementedError()

    def isThreadAllocatedMemoryEnabled():
        raise NotImplementedError()

    def getTotalClassCount():
        raise NotImplementedError()

    def getUnloadedClassCount():
        raise NotImplementedError()

    def getVerboseClass():
        raise NotImplementedError()

    def getVerboseGC():
        raise NotImplementedError()

    def getProcessId():
        raise NotImplementedError()

    def getVmArguments0():
        raise NotImplementedError()

    def getStartupTime():
        raise NotImplementedError()

    def getUptime0():
        raise NotImplementedError()

    def getAvailableProcessors():
        raise NotImplementedError()

    def getTotalCompileTime():
        raise NotImplementedError()

    def getTotalThreadCount():
        raise NotImplementedError()

    def getLiveThreadCount():
        raise NotImplementedError()

    def getPeakThreadCount():
        raise NotImplementedError()

    def getDaemonThreadCount():
        raise NotImplementedError()

    def getSafepointCount():
        raise NotImplementedError()

    def getTotalSafepointTime():
        raise NotImplementedError()

    def getSafepointSyncTime():
        raise NotImplementedError()

    def getTotalApplicationNonStoppedTime():
        raise NotImplementedError()

    def getLoadedClassSize():
        raise NotImplementedError()

    def getUnloadedClassSize():
        raise NotImplementedError()

    def getClassLoadingTime():
        raise NotImplementedError()

    def getMethodDataSize():
        raise NotImplementedError()

    def getInitializedClassCount():
        raise NotImplementedError()

    def getClassInitializationTime():
        raise NotImplementedError()

    def getClassVerificationTime():
        raise NotImplementedError()

    clazz.getVersion0 = staticmethod(getVersion0)
    clazz.initOptionalSupportFields = staticmethod(initOptionalSupportFields)
    clazz.isThreadContentionMonitoringEnabled = isThreadContentionMonitoringEnabled
    clazz.isThreadCpuTimeEnabled = isThreadCpuTimeEnabled
    clazz.isThreadAllocatedMemoryEnabled = isThreadAllocatedMemoryEnabled
    clazz.getTotalClassCount = getTotalClassCount
    clazz.getUnloadedClassCount = getUnloadedClassCount
    clazz.getVerboseClass = getVerboseClass
    clazz.getVerboseGC = getVerboseGC
    clazz.getProcessId = getProcessId
    clazz.getVmArguments0 = getVmArguments0
    clazz.getStartupTime = getStartupTime
    clazz.getUptime0 = getUptime0
    clazz.getAvailableProcessors = getAvailableProcessors
    clazz.getTotalCompileTime = getTotalCompileTime
    clazz.getTotalThreadCount = getTotalThreadCount
    clazz.getLiveThreadCount = getLiveThreadCount
    clazz.getPeakThreadCount = getPeakThreadCount
    clazz.getDaemonThreadCount = getDaemonThreadCount
    clazz.getSafepointCount = getSafepointCount
    clazz.getTotalSafepointTime = getTotalSafepointTime
    clazz.getSafepointSyncTime = getSafepointSyncTime
    clazz.getTotalApplicationNonStoppedTime = getTotalApplicationNonStoppedTime
    clazz.getLoadedClassSize = getLoadedClassSize
    clazz.getUnloadedClassSize = getUnloadedClassSize
    clazz.getClassLoadingTime = getClassLoadingTime
    clazz.getMethodDataSize = getMethodDataSize
    clazz.getInitializedClassCount = getInitializedClassCount
    clazz.getClassInitializationTime = getClassInitializationTime
    clazz.getClassVerificationTime = getClassVerificationTime

