def add_native_methods(clazz):
    def getScrollbarSize__int__(a0):
        raise NotImplementedError()

    def setValues__int__int__int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def setLineIncrement__int__(a0, a1):
        raise NotImplementedError()

    def setPageIncrement__int__(a0, a1):
        raise NotImplementedError()

    def create__sun_awt_windows_WComponentPeer__(a0, a1):
        raise NotImplementedError()

    clazz.getScrollbarSize__int__ = staticmethod(getScrollbarSize__int__)
    clazz.setValues__int__int__int__int__ = setValues__int__int__int__int__
    clazz.setLineIncrement__int__ = setLineIncrement__int__
    clazz.setPageIncrement__int__ = setPageIncrement__int__
    clazz.create__sun_awt_windows_WComponentPeer__ = create__sun_awt_windows_WComponentPeer__

