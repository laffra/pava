def add_native_methods(clazz):
    def registerClipboardFormat(a0):
        raise NotImplementedError()

    def getClipboardFormatName(a0):
        raise NotImplementedError()

    def imageDataToPlatformImageBytes(a0, a1, a2, a3):
        raise NotImplementedError()

    def platformImageBytesToImageData(a0, a1):
        raise NotImplementedError()

    def dragQueryFile(a0):
        raise NotImplementedError()

    clazz.registerClipboardFormat = staticmethod(registerClipboardFormat)
    clazz.getClipboardFormatName = staticmethod(getClipboardFormatName)
    clazz.imageDataToPlatformImageBytes = imageDataToPlatformImageBytes
    clazz.platformImageBytesToImageData = platformImageBytesToImageData
    clazz.dragQueryFile = dragQueryFile

