def add_native_methods(clazz):
    def getSize0(a0):
        raise NotImplementedError()

    def getClassAt0(a0, a1):
        raise NotImplementedError()

    def getClassAtIfLoaded0(a0, a1):
        raise NotImplementedError()

    def getMethodAt0(a0, a1):
        raise NotImplementedError()

    def getMethodAtIfLoaded0(a0, a1):
        raise NotImplementedError()

    def getFieldAt0(a0, a1):
        raise NotImplementedError()

    def getFieldAtIfLoaded0(a0, a1):
        raise NotImplementedError()

    def getMemberRefInfoAt0(a0, a1):
        raise NotImplementedError()

    def getIntAt0(a0, a1):
        raise NotImplementedError()

    def getLongAt0(a0, a1):
        raise NotImplementedError()

    def getFloatAt0(a0, a1):
        raise NotImplementedError()

    def getDoubleAt0(a0, a1):
        raise NotImplementedError()

    def getStringAt0(a0, a1):
        raise NotImplementedError()

    def getUTF8At0(a0, a1):
        raise NotImplementedError()

    clazz.getSize0 = getSize0
    clazz.getClassAt0 = getClassAt0
    clazz.getClassAtIfLoaded0 = getClassAtIfLoaded0
    clazz.getMethodAt0 = getMethodAt0
    clazz.getMethodAtIfLoaded0 = getMethodAtIfLoaded0
    clazz.getFieldAt0 = getFieldAt0
    clazz.getFieldAtIfLoaded0 = getFieldAtIfLoaded0
    clazz.getMemberRefInfoAt0 = getMemberRefInfoAt0
    clazz.getIntAt0 = getIntAt0
    clazz.getLongAt0 = getLongAt0
    clazz.getFloatAt0 = getFloatAt0
    clazz.getDoubleAt0 = getDoubleAt0
    clazz.getStringAt0 = getStringAt0
    clazz.getUTF8At0 = getUTF8At0

