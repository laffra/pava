def add_native_methods(clazz):
    def getLookupCacheURLs(a0):
        raise NotImplementedError()

    def getLookupCacheForClassLoader(a0, a1):
        raise NotImplementedError()

    def knownToNotExist0(a0, a1):
        raise NotImplementedError()

    clazz.getLookupCacheURLs = staticmethod(getLookupCacheURLs)
    clazz.getLookupCacheForClassLoader = staticmethod(getLookupCacheForClassLoader)
    clazz.knownToNotExist0 = staticmethod(knownToNotExist0)

