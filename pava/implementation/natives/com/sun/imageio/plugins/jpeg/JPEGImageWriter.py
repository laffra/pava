def add_native_methods(clazz):
    def initWriterIDs(a0, a1):
        raise NotImplementedError()

    def initJPEGImageWriter():
        raise NotImplementedError()

    def setDest(a0):
        raise NotImplementedError()

    def writeImage(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25):
        raise NotImplementedError()

    def writeTables(a0, a1, a2, a3):
        raise NotImplementedError()

    def abortWrite(a0):
        raise NotImplementedError()

    def resetWriter(a0):
        raise NotImplementedError()

    def disposeWriter(a0):
        raise NotImplementedError()

    clazz.initWriterIDs = staticmethod(initWriterIDs)
    clazz.initJPEGImageWriter = initJPEGImageWriter
    clazz.setDest = setDest
    clazz.writeImage = writeImage
    clazz.writeTables = writeTables
    clazz.abortWrite = abortWrite
    clazz.resetWriter = resetWriter
    clazz.disposeWriter = staticmethod(disposeWriter)

