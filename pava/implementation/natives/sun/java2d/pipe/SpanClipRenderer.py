def add_native_methods(clazz):
    def initIDs(a0, a1):
        raise NotImplementedError()

    def fillTile(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def eraseTile(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.fillTile = fillTile
    clazz.eraseTile = eraseTile

