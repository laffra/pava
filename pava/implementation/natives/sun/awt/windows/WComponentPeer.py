def add_native_methods(clazz):
    def isObscured():
        raise NotImplementedError()

    def pShow():
        raise NotImplementedError()

    def hide():
        raise NotImplementedError()

    def enable():
        raise NotImplementedError()

    def disable():
        raise NotImplementedError()

    def getLocationOnScreen():
        raise NotImplementedError()

    def reshapeNoCheck(a0, a1, a2, a3):
        raise NotImplementedError()

    def updateWindow():
        raise NotImplementedError()

    def createPrintedPixels(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def reshape(a0, a1, a2, a3):
        raise NotImplementedError()

    def nativeHandleEvent(a0):
        raise NotImplementedError()

    def setFocus(a0):
        raise NotImplementedError()

    def _dispose():
        raise NotImplementedError()

    def _setForeground(a0):
        raise NotImplementedError()

    def _setBackground(a0):
        raise NotImplementedError()

    def _setFont(a0):
        raise NotImplementedError()

    def start():
        raise NotImplementedError()

    def beginValidate():
        raise NotImplementedError()

    def endValidate():
        raise NotImplementedError()

    def addNativeDropTarget():
        raise NotImplementedError()

    def removeNativeDropTarget():
        raise NotImplementedError()

    def nativeHandlesWheelScrolling():
        raise NotImplementedError()

    def pSetParent(a0):
        raise NotImplementedError()

    def setRectangularShape(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def setZOrder(a0):
        raise NotImplementedError()

    clazz.isObscured = isObscured
    clazz.pShow = pShow
    clazz.hide = hide
    clazz.enable = enable
    clazz.disable = disable
    clazz.getLocationOnScreen = getLocationOnScreen
    clazz.reshapeNoCheck = reshapeNoCheck
    clazz.updateWindow = updateWindow
    clazz.createPrintedPixels = createPrintedPixels
    clazz.reshape = reshape
    clazz.nativeHandleEvent = nativeHandleEvent
    clazz.setFocus = setFocus
    clazz._dispose = _dispose
    clazz._setForeground = _setForeground
    clazz._setBackground = _setBackground
    clazz._setFont = _setFont
    clazz.start = start
    clazz.beginValidate = beginValidate
    clazz.endValidate = endValidate
    clazz.addNativeDropTarget = addNativeDropTarget
    clazz.removeNativeDropTarget = removeNativeDropTarget
    clazz.nativeHandlesWheelScrolling = nativeHandlesWheelScrolling
    clazz.pSetParent = pSetParent
    clazz.setRectangularShape = setRectangularShape
    clazz.setZOrder = setZOrder

