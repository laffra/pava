def add_native_methods(clazz):
    def createAwtDialog__sun_awt_windows_WComponentPeer__(a0, a1):
        raise NotImplementedError()

    def showModal____(a0):
        raise NotImplementedError()

    def endModal____(a0):
        raise NotImplementedError()

    def pSetIMMOption__java_lang_String__(a0, a1):
        raise NotImplementedError()

    clazz.createAwtDialog__sun_awt_windows_WComponentPeer__ = createAwtDialog__sun_awt_windows_WComponentPeer__
    clazz.showModal____ = showModal____
    clazz.endModal____ = endModal____
    clazz.pSetIMMOption__java_lang_String__ = pSetIMMOption__java_lang_String__

