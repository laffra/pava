def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def finalizeImpl(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.finalizeImpl = staticmethod(finalizeImpl)

