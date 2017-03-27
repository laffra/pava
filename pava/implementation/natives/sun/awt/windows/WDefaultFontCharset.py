def add_native_methods(clazz):
    def canConvert(a0):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.canConvert = canConvert
    clazz.initIDs = staticmethod(initIDs)

