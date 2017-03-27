def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def appendPoly(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def setNormalize(a0):
        raise NotImplementedError()

    def setOutputAreaXYXY(a0, a1, a2, a3):
        raise NotImplementedError()

    def setRule(a0):
        raise NotImplementedError()

    def addSegment(a0, a1):
        raise NotImplementedError()

    def getPathBox(a0):
        raise NotImplementedError()

    def intersectClipBox(a0, a1, a2, a3):
        raise NotImplementedError()

    def nextSpan(a0):
        raise NotImplementedError()

    def skipDownTo(a0):
        raise NotImplementedError()

    def getNativeIterator():
        raise NotImplementedError()

    def dispose():
        raise NotImplementedError()

    def moveTo(a0, a1):
        raise NotImplementedError()

    def lineTo(a0, a1):
        raise NotImplementedError()

    def quadTo(a0, a1, a2, a3):
        raise NotImplementedError()

    def curveTo(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def closePath():
        raise NotImplementedError()

    def pathDone():
        raise NotImplementedError()

    def getNativeConsumer():
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.appendPoly = appendPoly
    clazz.setNormalize = setNormalize
    clazz.setOutputAreaXYXY = setOutputAreaXYXY
    clazz.setRule = setRule
    clazz.addSegment = addSegment
    clazz.getPathBox = getPathBox
    clazz.intersectClipBox = intersectClipBox
    clazz.nextSpan = nextSpan
    clazz.skipDownTo = skipDownTo
    clazz.getNativeIterator = getNativeIterator
    clazz.dispose = dispose
    clazz.moveTo = moveTo
    clazz.lineTo = lineTo
    clazz.quadTo = quadTo
    clazz.curveTo = curveTo
    clazz.closePath = closePath
    clazz.pathDone = pathDone
    clazz.getNativeConsumer = getNativeConsumer

