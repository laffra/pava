def add_native_methods(clazz):
    def initIDs__java_lang_Class__(a0, a1):
        raise NotImplementedError()

    def initOps__sun_awt_windows_WComponentPeer__int__int__int__int__int__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def invalidateSD____(a0):
        raise NotImplementedError()

    clazz.initIDs__java_lang_Class__ = staticmethod(initIDs__java_lang_Class__)
    clazz.initOps__sun_awt_windows_WComponentPeer__int__int__int__int__int__ = initOps__sun_awt_windows_WComponentPeer__int__int__int__int__int__
    clazz.invalidateSD____ = invalidateSD____

