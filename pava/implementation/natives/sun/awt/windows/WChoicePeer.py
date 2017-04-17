def add_native_methods(clazz):
    def select__int__(a0, a1):
        raise NotImplementedError()

    def removeAll____(a0):
        raise NotImplementedError()

    def remove__int__(a0, a1):
        raise NotImplementedError()

    def addItems__java_lang_String____int__(a0, a1, a2):
        raise NotImplementedError()

    def reshape__int__int__int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def create__sun_awt_windows_WComponentPeer__(a0, a1):
        raise NotImplementedError()

    clazz.select__int__ = select__int__
    clazz.removeAll____ = removeAll____
    clazz.remove__int__ = remove__int__
    clazz.addItems__java_lang_String____int__ = addItems__java_lang_String____int__
    clazz.reshape__int__int__int__int__ = reshape__int__int__int__int__
    clazz.create__sun_awt_windows_WComponentPeer__ = create__sun_awt_windows_WComponentPeer__

