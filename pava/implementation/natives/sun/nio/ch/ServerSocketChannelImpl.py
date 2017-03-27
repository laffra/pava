def add_native_methods(clazz):
    def accept0(a0, a1, a2):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.accept0 = accept0
    clazz.initIDs = staticmethod(initIDs)

