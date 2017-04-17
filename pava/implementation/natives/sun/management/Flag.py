def add_native_methods(clazz):
    def setLongValue__java_lang_String__long__(a0, a1):
        raise NotImplementedError()

    def setBooleanValue__java_lang_String__boolean__(a0, a1):
        raise NotImplementedError()

    def setStringValue__java_lang_String__java_lang_String__(a0, a1):
        raise NotImplementedError()

    clazz.setLongValue__java_lang_String__long__ = staticmethod(setLongValue__java_lang_String__long__)
    clazz.setBooleanValue__java_lang_String__boolean__ = staticmethod(setBooleanValue__java_lang_String__boolean__)
    clazz.setStringValue__java_lang_String__java_lang_String__ = staticmethod(setStringValue__java_lang_String__java_lang_String__)

