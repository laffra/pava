def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def init():
        raise NotImplementedError()

    def getWindowsParameters():
        raise NotImplementedError()

    def playWindowsSound(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.init = init
    clazz.getWindowsParameters = getWindowsParameters
    clazz.playWindowsSound = playWindowsSound

