def add_native_methods(clazz):
    def getSystemTimeZoneID(a0):
        raise NotImplementedError()

    def getSystemGMTOffsetID():
        raise NotImplementedError()

    clazz.getSystemTimeZoneID = staticmethod(getSystemTimeZoneID)
    clazz.getSystemGMTOffsetID = staticmethod(getSystemGMTOffsetID)

