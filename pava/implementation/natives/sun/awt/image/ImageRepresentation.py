def add_native_methods(clazz):
    def initIDs____(a0):
        raise NotImplementedError()

    def setICMpixels__int__int__int__int__int____byte____int__int__sun_awt_image_IntegerComponentRaster__(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        raise NotImplementedError()

    def setDiffICM__int__int__int__int__int____int__int__java_awt_image_IndexColorModel__byte____int__int__sun_awt_image_ByteComponentRaster__int__(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.setICMpixels__int__int__int__int__int____byte____int__int__sun_awt_image_IntegerComponentRaster__ = setICMpixels__int__int__int__int__int____byte____int__int__sun_awt_image_IntegerComponentRaster__
    clazz.setDiffICM__int__int__int__int__int____int__int__java_awt_image_IndexColorModel__byte____int__int__sun_awt_image_ByteComponentRaster__int__ = setDiffICM__int__int__int__int__int____int__int__java_awt_image_IndexColorModel__byte____int__int__sun_awt_image_ByteComponentRaster__int__

