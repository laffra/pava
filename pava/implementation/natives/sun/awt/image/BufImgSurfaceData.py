def add_native_methods(clazz):
    def initIDs(a0, a1):
        raise NotImplementedError()

    def initRaster(a0, a1, a2, a3, a4, a5, a6, a7):
        raise NotImplementedError()

    def freeNativeICMData(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.initRaster = initRaster
    clazz.freeNativeICMData = staticmethod(freeNativeICMData)

