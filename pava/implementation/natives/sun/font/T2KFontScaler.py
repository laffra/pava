def add_native_methods(clazz):
    def initIDs(a0):
        raise NotImplementedError()

    def initNativeScaler(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def getFontMetricsNative(a0, a1, a2):
        raise NotImplementedError()

    def getGlyphAdvanceNative(a0, a1, a2, a3):
        raise NotImplementedError()

    def getGlyphMetricsNative(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def getGlyphImageNative(a0, a1, a2, a3):
        raise NotImplementedError()

    def getGlyphOutlineBoundsNative(a0, a1, a2, a3):
        raise NotImplementedError()

    def getGlyphOutlineNative(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def getGlyphVectorOutlineNative(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def getGlyphCodeNative(a0, a1):
        raise NotImplementedError()

    def getLayoutTableCacheNative(a0):
        raise NotImplementedError()

    def disposeNativeScaler(a0, a1):
        raise NotImplementedError()

    def getNumGlyphsNative(a0):
        raise NotImplementedError()

    def getMissingGlyphCodeNative(a0):
        raise NotImplementedError()

    def getUnitsPerEMNative(a0):
        raise NotImplementedError()

    def createScalerContextNative(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def getGlyphPointNative(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.initNativeScaler = initNativeScaler
    clazz.getFontMetricsNative = getFontMetricsNative
    clazz.getGlyphAdvanceNative = getGlyphAdvanceNative
    clazz.getGlyphMetricsNative = getGlyphMetricsNative
    clazz.getGlyphImageNative = getGlyphImageNative
    clazz.getGlyphOutlineBoundsNative = getGlyphOutlineBoundsNative
    clazz.getGlyphOutlineNative = getGlyphOutlineNative
    clazz.getGlyphVectorOutlineNative = getGlyphVectorOutlineNative
    clazz.getGlyphCodeNative = getGlyphCodeNative
    clazz.getLayoutTableCacheNative = getLayoutTableCacheNative
    clazz.disposeNativeScaler = disposeNativeScaler
    clazz.getNumGlyphsNative = getNumGlyphsNative
    clazz.getMissingGlyphCodeNative = getMissingGlyphCodeNative
    clazz.getUnitsPerEMNative = getUnitsPerEMNative
    clazz.createScalerContextNative = createScalerContextNative
    clazz.getGlyphPointNative = getGlyphPointNative

