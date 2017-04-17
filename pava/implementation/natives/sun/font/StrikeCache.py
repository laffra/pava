def add_native_methods(clazz):
    def getGlyphCacheDescription__long____(a0):
        raise NotImplementedError()

    def freeIntPointer__int__(a0):
        raise NotImplementedError()

    def freeLongPointer__long__(a0):
        raise NotImplementedError()

    clazz.getGlyphCacheDescription__long____ = staticmethod(getGlyphCacheDescription__long____)
    clazz.freeIntPointer__int__ = staticmethod(freeIntPointer__int__)
    clazz.freeLongPointer__long__ = staticmethod(freeLongPointer__long__)

