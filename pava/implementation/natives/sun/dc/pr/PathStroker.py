def add_native_methods(clazz):
    def dispose____(a0):
        raise NotImplementedError()

    def setPenDiameter__float__(a0, a1):
        raise NotImplementedError()

    def setPenT4__float____(a0, a1):
        raise NotImplementedError()

    def setPenFitting__float__int__(a0, a1, a2):
        raise NotImplementedError()

    def setCaps__int__(a0, a1):
        raise NotImplementedError()

    def setCorners__int__float__(a0, a1, a2):
        raise NotImplementedError()

    def setOutputT6__float____(a0, a1):
        raise NotImplementedError()

    def setOutputConsumer__sun_dc_path_PathConsumer__(a0, a1):
        raise NotImplementedError()

    def reset____(a0):
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

    clazz.dispose____ = dispose____
    clazz.setPenDiameter__float__ = setPenDiameter__float__
    clazz.setPenT4__float____ = setPenT4__float____
    clazz.setPenFitting__float__int__ = setPenFitting__float__int__
    clazz.setCaps__int__ = setCaps__int__
    clazz.setCorners__int__float__ = setCorners__int__float__
    clazz.setOutputT6__float____ = setOutputT6__float____
    clazz.setOutputConsumer__sun_dc_path_PathConsumer__ = setOutputConsumer__sun_dc_path_PathConsumer__
    clazz.reset____ = reset____
    clazz.beginPath____ = beginPath____
    clazz.beginSubpath__float__float__ = beginSubpath__float__float__
    clazz.appendLine__float__float__ = appendLine__float__float__
    clazz.appendQuadratic__float__float__float__float__ = appendQuadratic__float__float__float__float__
    clazz.appendCubic__float__float__float__float__float__float__ = appendCubic__float__float__float__float__float__float__
    clazz.closedSubpath____ = closedSubpath____
    clazz.endPath____ = endPath____
    clazz.getCPathConsumer____ = getCPathConsumer____

