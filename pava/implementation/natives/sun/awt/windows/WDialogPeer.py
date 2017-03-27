def add_native_methods(clazz):
    def createAwtDialog(a0):
        raise NotImplementedError()

    def showModal():
        raise NotImplementedError()

    def endModal():
        raise NotImplementedError()

    def pSetIMMOption(a0):
        raise NotImplementedError()

    clazz.createAwtDialog = createAwtDialog
    clazz.showModal = showModal
    clazz.endModal = endModal
    clazz.pSetIMMOption = pSetIMMOption

