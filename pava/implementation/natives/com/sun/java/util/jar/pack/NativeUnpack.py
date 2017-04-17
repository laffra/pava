def add_native_methods(clazz):
    def setOption__java_lang_String__java_lang_String__(a0, a1, a2):
        raise NotImplementedError()

    def getOption__java_lang_String__(a0, a1):
        raise NotImplementedError()

    clazz.setOption__java_lang_String__java_lang_String__ = setOption__java_lang_String__java_lang_String__
    clazz.getOption__java_lang_String__ = getOption__java_lang_String__

