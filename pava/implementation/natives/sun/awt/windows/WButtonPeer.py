def add_native_methods(clazz):
    def setLabel__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def create__sun_awt_windows_WComponentPeer__(a0, a1):
        raise NotImplementedError()

    clazz.setLabel__java_lang_String__ = setLabel__java_lang_String__
    clazz.create__sun_awt_windows_WComponentPeer__ = create__sun_awt_windows_WComponentPeer__

