def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def getBounds(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.getBounds = getBounds

