def add_native_methods(clazz):
    def dispose____(a0):
        raise NotImplementedError()

    def setFillMode__int__(a0, a1):
        raise NotImplementedError()

    def beginPath____(a0):
        raise NotImplementedError()

    def beginSubpath__float__float__(a0, a1, a2):
        raise NotImplementedError()

    def appendLine__float__float__(a0, a1, a2):
        raise NotImplementedError()

    def appendQuadratic__float__float__float__float__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def appendCubic__float__float__float__float__float__float__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def closedSubpath____(a0):
        raise NotImplementedError()

    def endPath____(a0):
        raise NotImplementedError()

    def getCPathConsumer____(a0):
        raise NotImplementedError()

    def getAlphaBox__int____(a0, a1):
        raise NotImplementedError()

    def setOutputArea__float__float__int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def getTileState____(a0):
        raise NotImplementedError()

    def nextTile____(a0):
        raise NotImplementedError()

    def reset____(a0):
        raise NotImplementedError()

    clazz.dispose____ = dispose____
    clazz.setFillMode__int__ = setFillMode__int__
    clazz.beginPath____ = beginPath____
    clazz.beginSubpath__float__float__ = beginSubpath__float__float__
    clazz.appendLine__float__float__ = appendLine__float__float__
    clazz.appendQuadratic__float__float__float__float__ = appendQuadratic__float__float__float__float__
    clazz.appendCubic__float__float__float__float__float__float__ = appendCubic__float__float__float__float__float__float__
    clazz.closedSubpath____ = closedSubpath____
    clazz.endPath____ = endPath____
    clazz.getCPathConsumer____ = getCPathConsumer____
    clazz.getAlphaBox__int____ = getAlphaBox__int____
    clazz.setOutputArea__float__float__int__int__ = setOutputArea__float__float__int__int__
    clazz.getTileState____ = getTileState____
    clazz.nextTile____ = nextTile____
    clazz.reset____ = reset____

