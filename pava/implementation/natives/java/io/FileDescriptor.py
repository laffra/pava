def add_native_methods(clazz):
    def sync():
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    def __set__(a0):
        raise NotImplementedError()

    clazz.sync = sync
    clazz.initIDs = staticmethod(initIDs)
    clazz.__set__ = staticmethod(__set__)

