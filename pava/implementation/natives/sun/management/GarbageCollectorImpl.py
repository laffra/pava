def add_native_methods(clazz):
    def getCollectionCount____(a0):
        raise NotImplementedError()

    def getCollectionTime____(a0):
        raise NotImplementedError()

    def setNotificationEnabled__com_sun_management_GarbageCollectorMXBean__boolean__(a0, a1, a2):
        raise NotImplementedError()

    clazz.getCollectionCount____ = getCollectionCount____
    clazz.getCollectionTime____ = getCollectionTime____
    clazz.setNotificationEnabled__com_sun_management_GarbageCollectorMXBean__boolean__ = setNotificationEnabled__com_sun_management_GarbageCollectorMXBean__boolean__

