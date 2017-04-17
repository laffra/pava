def add_native_methods(clazz):
    def initIDs____(a0):
        raise NotImplementedError()

    def nativeSetSource__java_awt_peer_ComponentPeer__(a0, a1):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.nativeSetSource__java_awt_peer_ComponentPeer__ = nativeSetSource__java_awt_peer_ComponentPeer__

