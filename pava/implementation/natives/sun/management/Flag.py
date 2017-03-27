def add_native_methods(clazz):
    def getAllFlagNames():
        raise NotImplementedError()

    def getFlags(a0, a1, a2):
        raise NotImplementedError()

    def getInternalFlagCount():
        raise NotImplementedError()

    def setLongValue(a0, a1):
        raise NotImplementedError()

    def setBooleanValue(a0, a1):
        raise NotImplementedError()

    def setStringValue(a0, a1):
        raise NotImplementedError()

    def initialize():
        raise NotImplementedError()

    clazz.getAllFlagNames = staticmethod(getAllFlagNames)
    clazz.getFlags = staticmethod(getFlags)
    clazz.getInternalFlagCount = staticmethod(getInternalFlagCount)
    clazz.setLongValue = staticmethod(setLongValue)
    clazz.setBooleanValue = staticmethod(setBooleanValue)
    clazz.setStringValue = staticmethod(setStringValue)
    clazz.initialize = staticmethod(initialize)

