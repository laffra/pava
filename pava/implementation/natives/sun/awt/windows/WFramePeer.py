def add_native_methods(clazz):
    def setState__int__(a0, a1):
        raise NotImplementedError()

    def getState____(a0):
        raise NotImplementedError()

    def createAwtFrame__sun_awt_windows_WComponentPeer__(a0, a1):
        raise NotImplementedError()

    def pSetIMMOption__java_lang_String__(a0, a1):
        raise NotImplementedError()

    clazz.setState__int__ = setState__int__
    clazz.getState____ = getState____
    clazz.createAwtFrame__sun_awt_windows_WComponentPeer__ = createAwtFrame__sun_awt_windows_WComponentPeer__
    clazz.pSetIMMOption__java_lang_String__ = pSetIMMOption__java_lang_String__

