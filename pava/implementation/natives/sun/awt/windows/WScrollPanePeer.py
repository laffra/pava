def add_native_methods(clazz):
    def initIDs____():
        raise NotImplementedError()

    def create__sun_awt_windows_WComponentPeer__(a0, a1):
        raise NotImplementedError()

    def getOffset__int__(a0, a1):
        raise NotImplementedError()

    def setScrollPosition__int__int__(a0, a1, a2):
        raise NotImplementedError()

    def setSpans__int__int__int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.create__sun_awt_windows_WComponentPeer__ = create__sun_awt_windows_WComponentPeer__
    clazz.getOffset__int__ = getOffset__int__
    clazz.setScrollPosition__int__int__ = setScrollPosition__int__int__
    clazz.setSpans__int__int__int__int__ = setSpans__int__int__int__int__

