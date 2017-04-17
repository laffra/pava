def add_native_methods(clazz):
    def getSystemTimeZoneID__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def getSystemGMTOffsetID____(a0):
        raise NotImplementedError()

    clazz.getSystemTimeZoneID__java_lang_String__ = staticmethod(getSystemTimeZoneID__java_lang_String__)
    clazz.getSystemGMTOffsetID____ = staticmethod(getSystemGMTOffsetID____)

