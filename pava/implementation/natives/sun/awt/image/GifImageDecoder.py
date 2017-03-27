def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def parseImage(a0, a1, a2, a3, a4, a5, a6, a7, a8):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.parseImage = parseImage

