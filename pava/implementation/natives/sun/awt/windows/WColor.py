def add_native_methods(clazz):
    def getDefaultColor(a0):
        raise NotImplementedError()

    clazz.getDefaultColor = staticmethod(getDefaultColor)

