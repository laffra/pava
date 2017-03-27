def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def nativeSetSource(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.nativeSetSource = nativeSetSource

