def add_native_methods(clazz):
    def initDecoder__java_lang_Class__(a0, a1):
        raise NotImplementedError()

    def readJPEGStream__java_io_InputStream__com_sun_image_codec_jpeg_JPEGDecodeParam__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.initDecoder__java_lang_Class__ = initDecoder__java_lang_Class__
    clazz.readJPEGStream__java_io_InputStream__com_sun_image_codec_jpeg_JPEGDecodeParam__boolean__ = readJPEGStream__java_io_InputStream__com_sun_image_codec_jpeg_JPEGDecodeParam__boolean__

