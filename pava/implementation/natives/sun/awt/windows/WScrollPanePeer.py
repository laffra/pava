def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def create(a0):
        raise NotImplementedError()

    def getOffset(a0):
        raise NotImplementedError()

    def setInsets():
        raise NotImplementedError()

    def setScrollPosition(a0, a1):
        raise NotImplementedError()

    def _getHScrollbarHeight():
        raise NotImplementedError()

    def _getVScrollbarWidth():
        raise NotImplementedError()

    def setSpans(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.create = create
    clazz.getOffset = getOffset
    clazz.setInsets = setInsets
    clazz.setScrollPosition = setScrollPosition
    clazz._getHScrollbarHeight = _getHScrollbarHeight
    clazz._getVScrollbarWidth = _getVScrollbarWidth
    clazz.setSpans = setSpans

