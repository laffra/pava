def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def _toFront():
        raise NotImplementedError()

    def toBack():
        raise NotImplementedError()

    def setAlwaysOnTopNative(a0):
        raise NotImplementedError()

    def setFocusableWindow(a0):
        raise NotImplementedError()

    def _setTitle(a0):
        raise NotImplementedError()

    def _setResizable(a0):
        raise NotImplementedError()

    def createAwtWindow(a0):
        raise NotImplementedError()

    def updateInsets(a0):
        raise NotImplementedError()

    def getSysMinWidth():
        raise NotImplementedError()

    def getSysMinHeight():
        raise NotImplementedError()

    def getSysIconWidth():
        raise NotImplementedError()

    def getSysIconHeight():
        raise NotImplementedError()

    def getSysSmIconWidth():
        raise NotImplementedError()

    def getSysSmIconHeight():
        raise NotImplementedError()

    def setIconImagesData(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def reshapeFrame(a0, a1, a2, a3):
        raise NotImplementedError()

    def requestWindowFocus(a0):
        raise NotImplementedError()

    def setMinSize(a0, a1):
        raise NotImplementedError()

    def modalDisable(a0, a1):
        raise NotImplementedError()

    def modalEnable(a0):
        raise NotImplementedError()

    def getScreenImOn():
        raise NotImplementedError()

    def setFullScreenExclusiveModeState(a0):
        raise NotImplementedError()

    def nativeGrab():
        raise NotImplementedError()

    def nativeUngrab():
        raise NotImplementedError()

    def repositionSecurityWarning():
        raise NotImplementedError()

    def setOpacity(a0):
        raise NotImplementedError()

    def setOpaqueImpl(a0):
        raise NotImplementedError()

    def updateWindowImpl(a0, a1, a2):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz._toFront = _toFront
    clazz.toBack = toBack
    clazz.setAlwaysOnTopNative = setAlwaysOnTopNative
    clazz.setFocusableWindow = setFocusableWindow
    clazz._setTitle = _setTitle
    clazz._setResizable = _setResizable
    clazz.createAwtWindow = createAwtWindow
    clazz.updateInsets = updateInsets
    clazz.getSysMinWidth = staticmethod(getSysMinWidth)
    clazz.getSysMinHeight = staticmethod(getSysMinHeight)
    clazz.getSysIconWidth = staticmethod(getSysIconWidth)
    clazz.getSysIconHeight = staticmethod(getSysIconHeight)
    clazz.getSysSmIconWidth = staticmethod(getSysSmIconWidth)
    clazz.getSysSmIconHeight = staticmethod(getSysSmIconHeight)
    clazz.setIconImagesData = setIconImagesData
    clazz.reshapeFrame = reshapeFrame
    clazz.requestWindowFocus = requestWindowFocus
    clazz.setMinSize = setMinSize
    clazz.modalDisable = modalDisable
    clazz.modalEnable = modalEnable
    clazz.getScreenImOn = getScreenImOn
    clazz.setFullScreenExclusiveModeState = setFullScreenExclusiveModeState
    clazz.nativeGrab = nativeGrab
    clazz.nativeUngrab = nativeUngrab
    clazz.repositionSecurityWarning = repositionSecurityWarning
    clazz.setOpacity = setOpacity
    clazz.setOpaqueImpl = setOpaqueImpl
    clazz.updateWindowImpl = updateWindowImpl

