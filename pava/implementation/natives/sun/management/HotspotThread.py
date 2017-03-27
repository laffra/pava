def add_native_methods(clazz):
    def getInternalThreadCount():
        raise NotImplementedError()

    def getInternalThreadTimes0(a0, a1):
        raise NotImplementedError()

    clazz.getInternalThreadCount = getInternalThreadCount
    clazz.getInternalThreadTimes0 = getInternalThreadTimes0

