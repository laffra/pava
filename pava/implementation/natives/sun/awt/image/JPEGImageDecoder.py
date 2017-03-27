def add_native_methods(clazz):
    def initIDs(a0):
        raise NotImplementedError()

    def readImage(a0, a1):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.readImage = readImage

