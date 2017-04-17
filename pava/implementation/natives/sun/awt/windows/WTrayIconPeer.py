def add_native_methods(clazz):
    def setToolTip__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def create____(a0):
        raise NotImplementedError()

    def _dispose____(a0):
        raise NotImplementedError()

    def updateNativeIcon__boolean__(a0, a1):
        raise NotImplementedError()

    def setNativeIcon__int____byte____int__int__int__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    clazz.setToolTip__java_lang_String__ = setToolTip__java_lang_String__
    clazz.create____ = create____
    clazz._dispose____ = _dispose____
    clazz.updateNativeIcon__boolean__ = updateNativeIcon__boolean__
    clazz.setNativeIcon__int____byte____int__int__int__ = setNativeIcon__int____byte____int__int__int__

