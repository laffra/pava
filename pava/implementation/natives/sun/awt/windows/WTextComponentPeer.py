def add_native_methods(clazz):
    def getText____(a0):
        raise NotImplementedError()

    def setText__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def getSelectionStart____(a0):
        raise NotImplementedError()

    def getSelectionEnd____(a0):
        raise NotImplementedError()

    def select__int__int__(a0, a1, a2):
        raise NotImplementedError()

    def enableEditing__boolean__(a0, a1):
        raise NotImplementedError()

    clazz.getText____ = getText____
    clazz.setText__java_lang_String__ = setText__java_lang_String__
    clazz.getSelectionStart____ = getSelectionStart____
    clazz.getSelectionEnd____ = getSelectionEnd____
    clazz.select__int__int__ = select__int__int__
    clazz.enableEditing__boolean__ = enableEditing__boolean__

