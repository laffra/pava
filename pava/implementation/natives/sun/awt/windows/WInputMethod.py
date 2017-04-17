def add_native_methods(clazz):
    def getNativeLocale____():
        raise NotImplementedError()

    def setNativeLocale__java_lang_String__boolean__(a0, a1):
        raise NotImplementedError()

    clazz.getNativeLocale____ = staticmethod(getNativeLocale____)
    clazz.setNativeLocale__java_lang_String__boolean__ = staticmethod(setNativeLocale__java_lang_String__boolean__)

