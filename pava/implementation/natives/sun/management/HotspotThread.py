def add_native_methods(clazz):
    def getInternalThreadCount____(a0):
        raise NotImplementedError()

    def getInternalThreadTimes0__java_lang_String____long____(a0, a1, a2):
        raise NotImplementedError()

    clazz.getInternalThreadCount____ = getInternalThreadCount____
    clazz.getInternalThreadTimes0__java_lang_String____long____ = getInternalThreadTimes0__java_lang_String____long____

