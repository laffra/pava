def add_native_methods(clazz):
    def initIDs____(a0):
        raise NotImplementedError()

    def init____(a0):
        raise NotImplementedError()

    def getWindowsParameters____(a0):
        raise NotImplementedError()

    def playWindowsSound__java_lang_String__(a0, a1):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.init____ = init____
    clazz.getWindowsParameters____ = getWindowsParameters____
    clazz.playWindowsSound__java_lang_String__ = playWindowsSound__java_lang_String__

