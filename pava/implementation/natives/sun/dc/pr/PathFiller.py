def add_native_methods(clazz):
    def dispose():
        raise NotImplementedError()

    def setFillMode(a0):
        raise NotImplementedError()

    def beginPath():
        raise NotImplementedError()

    def beginSubpath(a0, a1):
        raise NotImplementedError()

    def appendLine(a0, a1):
        raise NotImplementedError()

    def appendQuadratic(a0, a1, a2, a3):
        raise NotImplementedError()

    def appendCubic(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def closedSubpath():
        raise NotImplementedError()

    def endPath():
        raise NotImplementedError()

    def getCPathConsumer():
        raise NotImplementedError()

    def getAlphaBox(a0):
        raise NotImplementedError()

    def setOutputArea(a0, a1, a2, a3):
        raise NotImplementedError()

    def getTileState():
        raise NotImplementedError()

    def writeAlpha8(a0, a1, a2, a3):
        raise NotImplementedError()

    def writeAlpha16(a0, a1, a2, a3):
        raise NotImplementedError()

    def nextTile():
        raise NotImplementedError()

    def reset():
        raise NotImplementedError()

    def cClassInitialize():
        raise NotImplementedError()

    def cClassFinalize():
        raise NotImplementedError()

    def cInitialize():
        raise NotImplementedError()

    clazz.dispose = dispose
    clazz.setFillMode = setFillMode
    clazz.beginPath = beginPath
    clazz.beginSubpath = beginSubpath
    clazz.appendLine = appendLine
    clazz.appendQuadratic = appendQuadratic
    clazz.appendCubic = appendCubic
    clazz.closedSubpath = closedSubpath
    clazz.endPath = endPath
    clazz.getCPathConsumer = getCPathConsumer
    clazz.getAlphaBox = getAlphaBox
    clazz.setOutputArea = setOutputArea
    clazz.getTileState = getTileState
    clazz.writeAlpha8 = writeAlpha8
    clazz.writeAlpha16 = writeAlpha16
    clazz.nextTile = nextTile
    clazz.reset = reset
    clazz.cClassInitialize = staticmethod(cClassInitialize)
    clazz.cClassFinalize = staticmethod(cClassFinalize)
    clazz.cInitialize = cInitialize

