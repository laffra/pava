def add_native_methods(clazz):
    def setFilterString(a0):
        raise NotImplementedError()

    def _dispose():
        raise NotImplementedError()

    def _show():
        raise NotImplementedError()

    def _hide():
        raise NotImplementedError()

    def toFront():
        raise NotImplementedError()

    def toBack():
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.setFilterString = staticmethod(setFilterString)
    clazz._dispose = _dispose
    clazz._show = _show
    clazz._hide = _hide
    clazz.toFront = toFront
    clazz.toBack = toBack
    clazz.initIDs = staticmethod(initIDs)

