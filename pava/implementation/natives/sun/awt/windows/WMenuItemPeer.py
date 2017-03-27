def add_native_methods(clazz):
    def _dispose():
        raise NotImplementedError()

    def _setLabel(a0):
        raise NotImplementedError()

    def create(a0):
        raise NotImplementedError()

    def enable(a0):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    def _setFont(a0):
        raise NotImplementedError()

    clazz._dispose = _dispose
    clazz._setLabel = _setLabel
    clazz.create = create
    clazz.enable = enable
    clazz.initIDs = staticmethod(initIDs)
    clazz._setFont = _setFont

