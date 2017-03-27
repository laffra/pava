def add_native_methods(clazz):
    def setLabel(a0):
        raise NotImplementedError()

    def create(a0):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.setLabel = setLabel
    clazz.create = create
    clazz.initIDs = staticmethod(initIDs)

