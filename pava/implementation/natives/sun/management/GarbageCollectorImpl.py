def add_native_methods(clazz):
    def getCollectionCount():
        raise NotImplementedError()

    def getCollectionTime():
        raise NotImplementedError()

    def setNotificationEnabled(a0, a1):
        raise NotImplementedError()

    clazz.getCollectionCount = getCollectionCount
    clazz.getCollectionTime = getCollectionTime
    clazz.setNotificationEnabled = setNotificationEnabled

