def add_native_methods(clazz):
    def init(a0):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.init = init
    clazz.initIDs = staticmethod(initIDs)

