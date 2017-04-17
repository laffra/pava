def add_native_methods(clazz):
    def create__sun_awt_windows_WComponentPeer__(a0, a1):
        raise NotImplementedError()

    def getBoundsPrivate____(a0):
        raise NotImplementedError()

    clazz.create__sun_awt_windows_WComponentPeer__ = create__sun_awt_windows_WComponentPeer__
    clazz.getBoundsPrivate____ = getBoundsPrivate____

