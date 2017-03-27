def add_native_methods(clazz):
    def getLocalHostName():
        raise NotImplementedError()

    def lookupAllHostAddr(a0):
        raise NotImplementedError()

    def getHostByAddr(a0):
        raise NotImplementedError()

    def isReachable0(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.getLocalHostName = getLocalHostName
    clazz.lookupAllHostAddr = lookupAllHostAddr
    clazz.getHostByAddr = getHostByAddr
    clazz.isReachable0 = isReachable0

