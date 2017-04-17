def add_native_methods(clazz):
    def getNumScreens____(a0):
        raise NotImplementedError()

    def getDefaultScreen____(a0):
        raise NotImplementedError()

    def getXResolution____(a0):
        raise NotImplementedError()

    def getYResolution____(a0):
        raise NotImplementedError()

    def isVistaOS____():
        raise NotImplementedError()

    clazz.getNumScreens____ = getNumScreens____
    clazz.getDefaultScreen____ = getDefaultScreen____
    clazz.getXResolution____ = getXResolution____
    clazz.getYResolution____ = getYResolution____
    clazz.isVistaOS____ = staticmethod(isVistaOS____)

