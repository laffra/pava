def add_native_methods(clazz):
    def openClipboard(a0):
        raise NotImplementedError()

    def closeClipboard():
        raise NotImplementedError()

    def publishClipboardData(a0, a1):
        raise NotImplementedError()

    def init():
        raise NotImplementedError()

    def getClipboardFormats():
        raise NotImplementedError()

    def getClipboardData(a0):
        raise NotImplementedError()

    def registerClipboardViewer():
        raise NotImplementedError()

    clazz.openClipboard = openClipboard
    clazz.closeClipboard = closeClipboard
    clazz.publishClipboardData = publishClipboardData
    clazz.init = staticmethod(init)
    clazz.getClipboardFormats = getClipboardFormats
    clazz.getClipboardData = getClipboardData
    clazz.registerClipboardViewer = registerClipboardViewer

