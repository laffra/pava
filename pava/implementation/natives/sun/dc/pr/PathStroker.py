def add_native_methods(clazz):
    def dispose():
        raise NotImplementedError()

    def setPenDiameter(a0):
        raise NotImplementedError()

    def setPenT4(a0):
        raise NotImplementedError()

    def setPenFitting(a0, a1):
        raise NotImplementedError()

    def setCaps(a0):
        raise NotImplementedError()

    def setCorners(a0, a1):
        raise NotImplementedError()

    def setOutputT6(a0):
        raise NotImplementedError()

    def setOutputConsumer(a0):
        raise NotImplementedError()

    def reset():
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

    def cClassInitialize():
        raise NotImplementedError()

    def cClassFinalize():
        raise NotImplementedError()

    def cInitialize(a0):
        raise NotImplementedError()

    def cInitialize2D(a0):
        raise NotImplementedError()

    clazz.dispose = dispose
    clazz.setPenDiameter = setPenDiameter
    clazz.setPenT4 = setPenT4
    clazz.setPenFitting = setPenFitting
    clazz.setCaps = setCaps
    clazz.setCorners = setCorners
    clazz.setOutputT6 = setOutputT6
    clazz.setOutputConsumer = setOutputConsumer
    clazz.reset = reset
    clazz.beginPath = beginPath
    clazz.beginSubpath = beginSubpath
    clazz.appendLine = appendLine
    clazz.appendQuadratic = appendQuadratic
    clazz.appendCubic = appendCubic
    clazz.closedSubpath = closedSubpath
    clazz.endPath = endPath
    clazz.getCPathConsumer = getCPathConsumer
    clazz.cClassInitialize = staticmethod(cClassInitialize)
    clazz.cClassFinalize = staticmethod(cClassFinalize)
    clazz.cInitialize = cInitialize
    clazz.cInitialize2D = cInitialize2D

