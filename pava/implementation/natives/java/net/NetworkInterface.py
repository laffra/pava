def add_native_methods(clazz):
    def getAll():
        raise NotImplementedError()

    def getByName0(a0):
        raise NotImplementedError()

    def getByIndex0(a0):
        raise NotImplementedError()

    def getByInetAddress0(a0):
        raise NotImplementedError()

    def isUp0(a0, a1):
        raise NotImplementedError()

    def isLoopback0(a0, a1):
        raise NotImplementedError()

    def supportsMulticast0(a0, a1):
        raise NotImplementedError()

    def isP2P0(a0, a1):
        raise NotImplementedError()

    def getMacAddr0(a0, a1, a2):
        raise NotImplementedError()

    def getMTU0(a0, a1):
        raise NotImplementedError()

    def init():
        raise NotImplementedError()

    clazz.getAll = staticmethod(getAll)
    clazz.getByName0 = staticmethod(getByName0)
    clazz.getByIndex0 = staticmethod(getByIndex0)
    clazz.getByInetAddress0 = staticmethod(getByInetAddress0)
    clazz.isUp0 = staticmethod(isUp0)
    clazz.isLoopback0 = staticmethod(isLoopback0)
    clazz.supportsMulticast0 = staticmethod(supportsMulticast0)
    clazz.isP2P0 = staticmethod(isP2P0)
    clazz.getMacAddr0 = staticmethod(getMacAddr0)
    clazz.getMTU0 = staticmethod(getMTU0)
    clazz.init = staticmethod(init)

