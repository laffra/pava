def add_native_methods(clazz):
    def _setLabel__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def create__sun_awt_windows_WMenuPeer__(a0, a1):
        raise NotImplementedError()

    def enable__boolean__(a0, a1):
        raise NotImplementedError()

    clazz._setLabel__java_lang_String__ = _setLabel__java_lang_String__
    clazz.create__sun_awt_windows_WMenuPeer__ = create__sun_awt_windows_WMenuPeer__
    clazz.enable__boolean__ = enable__boolean__

