def add_native_methods(clazz):
    def getText():
        raise NotImplementedError()

    def setText(a0):
        raise NotImplementedError()

    def getSelectionStart():
        raise NotImplementedError()

    def getSelectionEnd():
        raise NotImplementedError()

    def select(a0, a1):
        raise NotImplementedError()

    def enableEditing(a0):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.getText = getText
    clazz.setText = setText
    clazz.getSelectionStart = getSelectionStart
    clazz.getSelectionEnd = getSelectionEnd
    clazz.select = select
    clazz.enableEditing = enableEditing
    clazz.initIDs = staticmethod(initIDs)

