def add_native_methods(clazz):
    def initWriterIDs__java_lang_Class__java_lang_Class__(a0, a1, a2):
        raise NotImplementedError()

    def initJPEGImageWriter____(a0):
        raise NotImplementedError()

    def setDest__long__(a0, a1):
        raise NotImplementedError()

    def writeImage__long__byte____int__int__int__int____int__int__int__int__int__javax_imageio_plugins_jpeg_JPEGQTable____boolean__javax_imageio_plugins_jpeg_JPEGHuffmanTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____boolean__boolean__boolean__int__int____int____int____int____int____boolean__int__(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26):
        raise NotImplementedError()

    def writeTables__long__javax_imageio_plugins_jpeg_JPEGQTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def abortWrite__long__(a0, a1):
        raise NotImplementedError()

    def resetWriter__long__(a0, a1):
        raise NotImplementedError()

    def disposeWriter__long__(a0, a1):
        raise NotImplementedError()

    clazz.initWriterIDs__java_lang_Class__java_lang_Class__ = staticmethod(initWriterIDs__java_lang_Class__java_lang_Class__)
    clazz.initJPEGImageWriter____ = initJPEGImageWriter____
    clazz.setDest__long__ = setDest__long__
    clazz.writeImage__long__byte____int__int__int__int____int__int__int__int__int__javax_imageio_plugins_jpeg_JPEGQTable____boolean__javax_imageio_plugins_jpeg_JPEGHuffmanTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____boolean__boolean__boolean__int__int____int____int____int____int____boolean__int__ = writeImage__long__byte____int__int__int__int____int__int__int__int__int__javax_imageio_plugins_jpeg_JPEGQTable____boolean__javax_imageio_plugins_jpeg_JPEGHuffmanTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____boolean__boolean__boolean__int__int____int____int____int____int____boolean__int__
    clazz.writeTables__long__javax_imageio_plugins_jpeg_JPEGQTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____ = writeTables__long__javax_imageio_plugins_jpeg_JPEGQTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____
    clazz.abortWrite__long__ = abortWrite__long__
    clazz.resetWriter__long__ = resetWriter__long__
    clazz.disposeWriter__long__ = staticmethod(disposeWriter__long__)

