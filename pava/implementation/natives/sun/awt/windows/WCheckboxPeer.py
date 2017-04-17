def add_native_methods(clazz):
    def setState__boolean__(a0, a1):
        raise NotImplementedError()

    def setCheckboxGroup__java_awt_CheckboxGroup__(a0, a1):
        raise NotImplementedError()

    def setLabel__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def create__sun_awt_windows_WComponentPeer__(a0, a1):
        raise NotImplementedError()

    clazz.setState__boolean__ = setState__boolean__
    clazz.setCheckboxGroup__java_awt_CheckboxGroup__ = setCheckboxGroup__java_awt_CheckboxGroup__
    clazz.setLabel__java_lang_String__ = setLabel__java_lang_String__
    clazz.create__sun_awt_windows_WComponentPeer__ = create__sun_awt_windows_WComponentPeer__

