def add_native_methods(clazz):
    def setToolTip(a0):
        raise NotImplementedError()

    def create():
        raise NotImplementedError()

    def _dispose():
        raise NotImplementedError()

    def updateNativeIcon(a0):
        raise NotImplementedError()

    def setNativeIcon(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def _displayMessage(a0, a1, a2):
        raise NotImplementedError()

    clazz.setToolTip = setToolTip
    clazz.create = create
    clazz._dispose = _dispose
    clazz.updateNativeIcon = updateNativeIcon
    clazz.setNativeIcon = setNativeIcon
    clazz._displayMessage = _displayMessage

