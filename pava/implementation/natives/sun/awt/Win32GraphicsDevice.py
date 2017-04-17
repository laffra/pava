def add_native_methods(clazz):
    def initDevice__int__(a0, a1):
        raise NotImplementedError()

    def isPixFmtSupported__int__int__(a0, a1, a2):
        raise NotImplementedError()

    def enterFullScreenExclusive__int__java_awt_peer_WindowPeer__(a0, a1, a2):
        raise NotImplementedError()

    def exitFullScreenExclusive__int__java_awt_peer_WindowPeer__(a0, a1, a2):
        raise NotImplementedError()

    def getCurrentDisplayMode__int__(a0, a1):
        raise NotImplementedError()

    def configDisplayMode__int__java_awt_peer_WindowPeer__int__int__int__int__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def enumDisplayModes__int__java_util_ArrayList__(a0, a1, a2):
        raise NotImplementedError()

    clazz.initDevice__int__ = initDevice__int__
    clazz.isPixFmtSupported__int__int__ = isPixFmtSupported__int__int__
    clazz.enterFullScreenExclusive__int__java_awt_peer_WindowPeer__ = enterFullScreenExclusive__int__java_awt_peer_WindowPeer__
    clazz.exitFullScreenExclusive__int__java_awt_peer_WindowPeer__ = exitFullScreenExclusive__int__java_awt_peer_WindowPeer__
    clazz.getCurrentDisplayMode__int__ = getCurrentDisplayMode__int__
    clazz.configDisplayMode__int__java_awt_peer_WindowPeer__int__int__int__int__ = configDisplayMode__int__java_awt_peer_WindowPeer__int__int__int__int__
    clazz.enumDisplayModes__int__java_util_ArrayList__ = enumDisplayModes__int__java_util_ArrayList__

