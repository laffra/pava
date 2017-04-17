def add_native_methods(clazz):
    def getDefaultPixFmt__int__(a0):
        raise NotImplementedError()

    clazz.getDefaultPixFmt__int__ = staticmethod(getDefaultPixFmt__int__)

