def add_native_methods(clazz):
    def init(a0, a1):
        raise NotImplementedError()

    def expand(a0):
        raise NotImplementedError()

    def resolve(a0, a1):
        raise NotImplementedError()

    def getMembers(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def objectFieldOffset(a0):
        raise NotImplementedError()

    def staticFieldOffset(a0):
        raise NotImplementedError()

    def staticFieldBase(a0):
        raise NotImplementedError()

    def getMemberVMInfo(a0):
        raise NotImplementedError()

    def getConstant(a0):
        raise NotImplementedError()

    def setCallSiteTargetNormal(a0, a1):
        raise NotImplementedError()

    def setCallSiteTargetVolatile(a0, a1):
        raise NotImplementedError()

    def registerNatives():
        raise NotImplementedError()

    def getNamedCon(a0, a1):
        raise NotImplementedError()

    clazz.init = staticmethod(init)
    clazz.expand = staticmethod(expand)
    clazz.resolve = staticmethod(resolve)
    clazz.getMembers = staticmethod(getMembers)
    clazz.objectFieldOffset = staticmethod(objectFieldOffset)
    clazz.staticFieldOffset = staticmethod(staticFieldOffset)
    clazz.staticFieldBase = staticmethod(staticFieldBase)
    clazz.getMemberVMInfo = staticmethod(getMemberVMInfo)
    clazz.getConstant = staticmethod(getConstant)
    clazz.setCallSiteTargetNormal = staticmethod(setCallSiteTargetNormal)
    clazz.setCallSiteTargetVolatile = staticmethod(setCallSiteTargetVolatile)
    clazz.registerNatives = staticmethod(registerNatives)
    clazz.getNamedCon = staticmethod(getNamedCon)

