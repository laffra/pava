def add_native_methods(clazz):
    def lazyPaint____(a0):
        raise NotImplementedError()

    def setText__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def setAlignment__int__(a0, a1):
        raise NotImplementedError()

    def create__sun_awt_windows_WComponentPeer__(a0, a1):
        raise NotImplementedError()

    clazz.lazyPaint____ = lazyPaint____
    clazz.setText__java_lang_String__ = setText__java_lang_String__
    clazz.setAlignment__int__ = setAlignment__int__
    clazz.create__sun_awt_windows_WComponentPeer__ = create__sun_awt_windows_WComponentPeer__

