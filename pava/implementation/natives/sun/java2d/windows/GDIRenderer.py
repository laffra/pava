def add_native_methods(clazz):
    def doDrawLine(a0, a1, a2, a3, a4, a5, a6, a7):
        raise NotImplementedError()

    def doDrawRect(a0, a1, a2, a3, a4, a5, a6, a7):
        raise NotImplementedError()

    def doDrawRoundRect(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        raise NotImplementedError()

    def doDrawOval(a0, a1, a2, a3, a4, a5, a6, a7):
        raise NotImplementedError()

    def doDrawArc(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        raise NotImplementedError()

    def doDrawPoly(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        raise NotImplementedError()

    def doFillRect(a0, a1, a2, a3, a4, a5, a6, a7):
        raise NotImplementedError()

    def doFillRoundRect(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        raise NotImplementedError()

    def doFillOval(a0, a1, a2, a3, a4, a5, a6, a7):
        raise NotImplementedError()

    def doFillArc(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        raise NotImplementedError()

    def doFillPoly(a0, a1, a2, a3, a4, a5, a6, a7, a8):
        raise NotImplementedError()

    def doShape(a0, a1, a2, a3, a4, a5, a6, a7):
        raise NotImplementedError()

    def devCopyArea(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    clazz.doDrawLine = doDrawLine
    clazz.doDrawRect = doDrawRect
    clazz.doDrawRoundRect = doDrawRoundRect
    clazz.doDrawOval = doDrawOval
    clazz.doDrawArc = doDrawArc
    clazz.doDrawPoly = doDrawPoly
    clazz.doFillRect = doFillRect
    clazz.doFillRoundRect = doFillRoundRect
    clazz.doFillOval = doFillOval
    clazz.doFillArc = doFillArc
    clazz.doFillPoly = doFillPoly
    clazz.doShape = doShape
    clazz.devCopyArea = devCopyArea

