def add_native_methods(clazz):
    def initIDs(a0):
        raise NotImplementedError()

    def getDrawBuffer(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.getDrawBuffer = staticmethod(getDrawBuffer)

