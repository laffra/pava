def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)

