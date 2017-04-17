def add_native_methods(clazz):
    def init____(a0):
        raise NotImplementedError()

    def getSystemProxy__java_lang_String__java_lang_String__(a0, a1, a2):
        raise NotImplementedError()

    clazz.init____ = staticmethod(init____)
    clazz.getSystemProxy__java_lang_String__java_lang_String__ = getSystemProxy__java_lang_String__java_lang_String__

