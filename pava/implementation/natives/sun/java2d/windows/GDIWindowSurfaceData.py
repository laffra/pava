def add_native_methods(clazz):
    def initIDs(a0):
        raise NotImplementedError()

    def initOps(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def invalidateSD():
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.initOps = initOps
    clazz.invalidateSD = invalidateSD

