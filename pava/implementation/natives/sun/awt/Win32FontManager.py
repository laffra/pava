def add_native_methods(clazz):
    def getFontPath__boolean__(a0, a1):
        raise NotImplementedError()

    def registerFontWithPlatform__java_lang_String__(a0):
        raise NotImplementedError()

    def deRegisterFontWithPlatform__java_lang_String__(a0):
        raise NotImplementedError()

    clazz.getFontPath__boolean__ = getFontPath__boolean__
    clazz.registerFontWithPlatform__java_lang_String__ = staticmethod(registerFontWithPlatform__java_lang_String__)
    clazz.deRegisterFontWithPlatform__java_lang_String__ = staticmethod(deRegisterFontWithPlatform__java_lang_String__)

