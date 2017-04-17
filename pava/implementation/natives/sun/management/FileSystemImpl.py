def add_native_methods(clazz):
    def init0____():
        raise NotImplementedError()

    def isSecuritySupported0__java_lang_String__(a0):
        raise NotImplementedError()

    def isAccessUserOnly0__java_lang_String__(a0):
        raise NotImplementedError()

    clazz.init0____ = staticmethod(init0____)
    clazz.isSecuritySupported0__java_lang_String__ = staticmethod(isSecuritySupported0__java_lang_String__)
    clazz.isAccessUserOnly0__java_lang_String__ = staticmethod(isAccessUserOnly0__java_lang_String__)

