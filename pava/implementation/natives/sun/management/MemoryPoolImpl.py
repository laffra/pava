def add_native_methods(clazz):
    def getUsage0():
        raise NotImplementedError()

    def getPeakUsage0():
        raise NotImplementedError()

    def getCollectionUsage0():
        raise NotImplementedError()

    def setUsageThreshold0(a0, a1):
        raise NotImplementedError()

    def setCollectionThreshold0(a0, a1):
        raise NotImplementedError()

    def resetPeakUsage0():
        raise NotImplementedError()

    def getMemoryManagers0():
        raise NotImplementedError()

    def setPoolUsageSensor(a0):
        raise NotImplementedError()

    def setPoolCollectionSensor(a0):
        raise NotImplementedError()

    clazz.getUsage0 = getUsage0
    clazz.getPeakUsage0 = getPeakUsage0
    clazz.getCollectionUsage0 = getCollectionUsage0
    clazz.setUsageThreshold0 = setUsageThreshold0
    clazz.setCollectionThreshold0 = setCollectionThreshold0
    clazz.resetPeakUsage0 = resetPeakUsage0
    clazz.getMemoryManagers0 = getMemoryManagers0
    clazz.setPoolUsageSensor = setPoolUsageSensor
    clazz.setPoolCollectionSensor = setPoolCollectionSensor

