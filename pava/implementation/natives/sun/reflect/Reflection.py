def add_native_methods(clazz):
    def getCallerClass____():
        raise NotImplementedError()

    def getCallerClass__int__(a0):
        raise NotImplementedError()

    def getClassAccessFlags__java_lang_Class_____(a0):
        raise NotImplementedError()

    clazz.getCallerClass____ = staticmethod(getCallerClass____)
    clazz.getCallerClass__int__ = staticmethod(getCallerClass__int__)
    clazz.getClassAccessFlags__java_lang_Class_____ = staticmethod(getClassAccessFlags__java_lang_Class_____)

