def add_native_methods(clazz):
    def _show():
        raise NotImplementedError()

    def toFront():
        raise NotImplementedError()

    def toBack():
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz._show = _show
    clazz.toFront = toFront
    clazz.toBack = toBack
    clazz.initIDs = staticmethod(initIDs)

