def add_native_methods(clazz):
    def initEncoder__java_lang_Class__(a0, a1):
        raise NotImplementedError()

    def writeJPEGStream__com_sun_image_codec_jpeg_JPEGEncodeParam__java_awt_image_ColorModel__java_io_OutputStream__java_lang_Object__int__int__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    clazz.initEncoder__java_lang_Class__ = initEncoder__java_lang_Class__
    clazz.writeJPEGStream__com_sun_image_codec_jpeg_JPEGEncodeParam__java_awt_image_ColorModel__java_io_OutputStream__java_lang_Object__int__int__ = writeJPEGStream__com_sun_image_codec_jpeg_JPEGEncodeParam__java_awt_image_ColorModel__java_io_OutputStream__java_lang_Object__int__int__

