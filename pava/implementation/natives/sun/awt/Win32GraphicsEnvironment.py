def add_native_methods(clazz):
    def initDisplay():
        raise NotImplementedError()

    def getNumScreens():
        raise NotImplementedError()

    def getDefaultScreen():
        raise NotImplementedError()

    def getXResolution():
        raise NotImplementedError()

    def getYResolution():
        raise NotImplementedError()

    def isVistaOS():
        raise NotImplementedError()

    clazz.initDisplay = staticmethod(initDisplay)
    clazz.getNumScreens = getNumScreens
    clazz.getDefaultScreen = getDefaultScreen
    clazz.getXResolution = getXResolution
    clazz.getYResolution = getYResolution
    clazz.isVistaOS = staticmethod(isVistaOS)

