def add_native_methods(clazz):
    def getLookupCacheURLs__java_lang_ClassLoader__(a0, a1):
        raise NotImplementedError()

    def getLookupCacheForClassLoader__java_lang_ClassLoader__java_lang_String__(a0, a1, a2):
        raise NotImplementedError()

    def knownToNotExist0__java_lang_ClassLoader__java_lang_String__(a0, a1, a2):
        raise NotImplementedError()

    clazz.getLookupCacheURLs__java_lang_ClassLoader__ = staticmethod(getLookupCacheURLs__java_lang_ClassLoader__)
    clazz.getLookupCacheForClassLoader__java_lang_ClassLoader__java_lang_String__ = staticmethod(getLookupCacheForClassLoader__java_lang_ClassLoader__java_lang_String__)
    clazz.knownToNotExist0__java_lang_ClassLoader__java_lang_String__ = staticmethod(knownToNotExist0__java_lang_ClassLoader__java_lang_String__)

