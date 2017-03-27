def add_native_methods(clazz):
    def getNullScalerContext():
        raise NotImplementedError()

    def getGlyphImage(a0, a1):
        raise NotImplementedError()

    clazz.getNullScalerContext = staticmethod(getNullScalerContext)
    clazz.getGlyphImage = getGlyphImage

