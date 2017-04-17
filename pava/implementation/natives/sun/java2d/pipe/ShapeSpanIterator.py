def add_native_methods(clazz):
    def initIDs____():
        raise NotImplementedError()

    def appendPoly__int____int____int__int__int__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def setOutputAreaXYXY__int__int__int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def setRule__int__(a0, a1):
        raise NotImplementedError()

    def addSegment__int__float____(a0, a1, a2):
        raise NotImplementedError()

    def getPathBox__int____(a0, a1):
        raise NotImplementedError()

    def intersectClipBox__int__int__int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def nextSpan__int____(a0, a1):
        raise NotImplementedError()

    def skipDownTo__int__(a0, a1):
        raise NotImplementedError()

    def getNativeIterator____(a0):
        raise NotImplementedError()

    def dispose____(a0):
        raise NotImplementedError()

    def moveTo__float__float__(a0, a1, a2):
        raise NotImplementedError()

    def lineTo__float__float__(a0, a1, a2):
        raise NotImplementedError()

    def quadTo__float__float__float__float__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def curveTo__float__float__float__float__float__float__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def closePath____(a0):
        raise NotImplementedError()

    def pathDone____(a0):
        raise NotImplementedError()

    def getNativeConsumer____(a0):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.appendPoly__int____int____int__int__int__ = appendPoly__int____int____int__int__int__
    clazz.setOutputAreaXYXY__int__int__int__int__ = setOutputAreaXYXY__int__int__int__int__
    clazz.setRule__int__ = setRule__int__
    clazz.addSegment__int__float____ = addSegment__int__float____
    clazz.getPathBox__int____ = getPathBox__int____
    clazz.intersectClipBox__int__int__int__int__ = intersectClipBox__int__int__int__int__
    clazz.nextSpan__int____ = nextSpan__int____
    clazz.skipDownTo__int__ = skipDownTo__int__
    clazz.getNativeIterator____ = getNativeIterator____
    clazz.dispose____ = dispose____
    clazz.moveTo__float__float__ = moveTo__float__float__
    clazz.lineTo__float__float__ = lineTo__float__float__
    clazz.quadTo__float__float__float__float__ = quadTo__float__float__float__float__
    clazz.curveTo__float__float__float__float__float__float__ = curveTo__float__float__float__float__float__float__
    clazz.closePath____ = closePath____
    clazz.pathDone____ = pathDone____
    clazz.getNativeConsumer____ = getNativeConsumer____

