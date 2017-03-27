def add_native_methods(clazz):
    def initReaderIDs(a0, a1, a2):
        raise NotImplementedError()

    def initJPEGImageReader():
        raise NotImplementedError()

    def setSource(a0):
        raise NotImplementedError()

    def readImageHeader(a0, a1, a2):
        raise NotImplementedError()

    def setOutColorSpace(a0, a1):
        raise NotImplementedError()

    def readImage(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16):
        raise NotImplementedError()

    def abortRead(a0):
        raise NotImplementedError()

    def resetLibraryState(a0):
        raise NotImplementedError()

    def resetReader(a0):
        raise NotImplementedError()

    def disposeReader(a0):
        raise NotImplementedError()

    clazz.initReaderIDs = staticmethod(initReaderIDs)
    clazz.initJPEGImageReader = initJPEGImageReader
    clazz.setSource = setSource
    clazz.readImageHeader = readImageHeader
    clazz.setOutColorSpace = setOutColorSpace
    clazz.readImage = readImage
    clazz.abortRead = abortRead
    clazz.resetLibraryState = resetLibraryState
    clazz.resetReader = resetReader
    clazz.disposeReader = staticmethod(disposeReader)

