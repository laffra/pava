def add_native_methods(clazz):
    def getNumGcExtAttributes(a0):
        raise NotImplementedError()

    def fillGcAttributeInfo(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def getLastGcInfo0(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    clazz.getNumGcExtAttributes = getNumGcExtAttributes
    clazz.fillGcAttributeInfo = fillGcAttributeInfo
    clazz.getLastGcInfo0 = getLastGcInfo0

