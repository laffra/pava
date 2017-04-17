def add_native_methods(clazz):
    def getLocalHostName____(a0):
        raise NotImplementedError()

    def lookupAllHostAddr__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def getHostByAddr__byte____(a0, a1):
        raise NotImplementedError()

    clazz.getLocalHostName____ = getLocalHostName____
    clazz.lookupAllHostAddr__java_lang_String__ = lookupAllHostAddr__java_lang_String__
    clazz.getHostByAddr__byte____ = getHostByAddr__byte____

