def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def isOpaqueGray(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.isOpaqueGray = staticmethod(isOpaqueGray)

