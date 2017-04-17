def add_native_methods(clazz):
    def initReaderIDs__java_lang_Class__java_lang_Class__java_lang_Class__(a0, a1, a2, a3):
        raise NotImplementedError()

    def initJPEGImageReader____(a0):
        raise NotImplementedError()

    def setSource__long__(a0, a1):
        raise NotImplementedError()

    def readImageHeader__long__boolean__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def setOutColorSpace__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def readImage__long__byte____int__int____int____int__int__int__int__int__int__javax_imageio_plugins_jpeg_JPEGQTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____int__int__boolean__(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17):
        raise NotImplementedError()

    def abortRead__long__(a0, a1):
        raise NotImplementedError()

    def resetLibraryState__long__(a0, a1):
        raise NotImplementedError()

    def resetReader__long__(a0, a1):
        raise NotImplementedError()

    def disposeReader__long__(a0, a1):
        raise NotImplementedError()

    clazz.initReaderIDs__java_lang_Class__java_lang_Class__java_lang_Class__ = staticmethod(initReaderIDs__java_lang_Class__java_lang_Class__java_lang_Class__)
    clazz.initJPEGImageReader____ = initJPEGImageReader____
    clazz.setSource__long__ = setSource__long__
    clazz.readImageHeader__long__boolean__boolean__ = readImageHeader__long__boolean__boolean__
    clazz.setOutColorSpace__long__int__ = setOutColorSpace__long__int__
    clazz.readImage__long__byte____int__int____int____int__int__int__int__int__int__javax_imageio_plugins_jpeg_JPEGQTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____int__int__boolean__ = readImage__long__byte____int__int____int____int__int__int__int__int__int__javax_imageio_plugins_jpeg_JPEGQTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____javax_imageio_plugins_jpeg_JPEGHuffmanTable____int__int__boolean__
    clazz.abortRead__long__ = abortRead__long__
    clazz.resetLibraryState__long__ = resetLibraryState__long__
    clazz.resetReader__long__ = resetReader__long__
    clazz.disposeReader__long__ = staticmethod(disposeReader__long__)

