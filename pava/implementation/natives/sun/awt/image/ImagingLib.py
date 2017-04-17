def add_native_methods(clazz):
    def transformBI__java_awt_image_BufferedImage__java_awt_image_BufferedImage__double____int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def transformRaster__java_awt_image_Raster__java_awt_image_Raster__double____int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def convolveBI__java_awt_image_BufferedImage__java_awt_image_BufferedImage__java_awt_image_Kernel__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def convolveRaster__java_awt_image_Raster__java_awt_image_Raster__java_awt_image_Kernel__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def lookupByteBI__java_awt_image_BufferedImage__java_awt_image_BufferedImage__byte______(a0, a1, a2):
        raise NotImplementedError()

    def lookupByteRaster__java_awt_image_Raster__java_awt_image_Raster__byte______(a0, a1, a2):
        raise NotImplementedError()

    clazz.transformBI__java_awt_image_BufferedImage__java_awt_image_BufferedImage__double____int__ = staticmethod(transformBI__java_awt_image_BufferedImage__java_awt_image_BufferedImage__double____int__)
    clazz.transformRaster__java_awt_image_Raster__java_awt_image_Raster__double____int__ = staticmethod(transformRaster__java_awt_image_Raster__java_awt_image_Raster__double____int__)
    clazz.convolveBI__java_awt_image_BufferedImage__java_awt_image_BufferedImage__java_awt_image_Kernel__int__ = staticmethod(convolveBI__java_awt_image_BufferedImage__java_awt_image_BufferedImage__java_awt_image_Kernel__int__)
    clazz.convolveRaster__java_awt_image_Raster__java_awt_image_Raster__java_awt_image_Kernel__int__ = staticmethod(convolveRaster__java_awt_image_Raster__java_awt_image_Raster__java_awt_image_Kernel__int__)
    clazz.lookupByteBI__java_awt_image_BufferedImage__java_awt_image_BufferedImage__byte______ = staticmethod(lookupByteBI__java_awt_image_BufferedImage__java_awt_image_BufferedImage__byte______)
    clazz.lookupByteRaster__java_awt_image_Raster__java_awt_image_Raster__byte______ = staticmethod(lookupByteRaster__java_awt_image_Raster__java_awt_image_Raster__byte______)

