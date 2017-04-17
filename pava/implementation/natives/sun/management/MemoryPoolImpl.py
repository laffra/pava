def add_native_methods(clazz):
    def getUsage0____(a0):
        raise NotImplementedError()

    def getPeakUsage0____(a0):
        raise NotImplementedError()

    def getCollectionUsage0____(a0):
        raise NotImplementedError()

    def setUsageThreshold0__long__long__(a0, a1, a2):
        raise NotImplementedError()

    def setCollectionThreshold0__long__long__(a0, a1, a2):
        raise NotImplementedError()

    def resetPeakUsage0____(a0):
        raise NotImplementedError()

    def getMemoryManagers0____(a0):
        raise NotImplementedError()

    def setPoolUsageSensor__sun_management_Sensor__(a0, a1):
        raise NotImplementedError()

    def setPoolCollectionSensor__sun_management_Sensor__(a0, a1):
        raise NotImplementedError()

    clazz.getUsage0____ = getUsage0____
    clazz.getPeakUsage0____ = getPeakUsage0____
    clazz.getCollectionUsage0____ = getCollectionUsage0____
    clazz.setUsageThreshold0__long__long__ = setUsageThreshold0__long__long__
    clazz.setCollectionThreshold0__long__long__ = setCollectionThreshold0__long__long__
    clazz.resetPeakUsage0____ = resetPeakUsage0____
    clazz.getMemoryManagers0____ = getMemoryManagers0____
    clazz.setPoolUsageSensor__sun_management_Sensor__ = setPoolUsageSensor__sun_management_Sensor__
    clazz.setPoolCollectionSensor__sun_management_Sensor__ = setPoolCollectionSensor__sun_management_Sensor__

