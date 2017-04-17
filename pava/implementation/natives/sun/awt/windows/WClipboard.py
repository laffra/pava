def add_native_methods(clazz):
    def openClipboard__sun_awt_datatransfer_SunClipboard__(a0, a1):
        raise NotImplementedError()

    def closeClipboard____(a0):
        raise NotImplementedError()

    def getClipboardFormats____(a0):
        raise NotImplementedError()

    def getClipboardData__long__(a0, a1):
        raise NotImplementedError()

    clazz.openClipboard__sun_awt_datatransfer_SunClipboard__ = openClipboard__sun_awt_datatransfer_SunClipboard__
    clazz.closeClipboard____ = closeClipboard____
    clazz.getClipboardFormats____ = getClipboardFormats____
    clazz.getClipboardData__long__ = getClipboardData__long__

