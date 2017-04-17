def add_native_methods(clazz):
    def setNativeFocusOwner__java_awt_peer_ComponentPeer__(a0):
        raise NotImplementedError()

    def getNativeFocusOwner____():
        raise NotImplementedError()

    def getNativeFocusedWindow____():
        raise NotImplementedError()

    clazz.setNativeFocusOwner__java_awt_peer_ComponentPeer__ = staticmethod(setNativeFocusOwner__java_awt_peer_ComponentPeer__)
    clazz.getNativeFocusOwner____ = staticmethod(getNativeFocusOwner____)
    clazz.getNativeFocusedWindow____ = staticmethod(getNativeFocusedWindow____)

