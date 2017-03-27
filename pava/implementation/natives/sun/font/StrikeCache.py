def add_native_methods(clazz):
    def getGlyphCacheDescription(a0):
        raise NotImplementedError()

    def freeIntPointer(a0):
        raise NotImplementedError()

    def freeLongPointer(a0):
        raise NotImplementedError()

    def freeIntMemory(a0, a1):
        raise NotImplementedError()

    def freeLongMemory(a0, a1):
        raise NotImplementedError()

    clazz.getGlyphCacheDescription = staticmethod(getGlyphCacheDescription)
    clazz.freeIntPointer = staticmethod(freeIntPointer)
    clazz.freeLongPointer = staticmethod(freeLongPointer)
    clazz.freeIntMemory = staticmethod(freeIntMemory)
    clazz.freeLongMemory = staticmethod(freeLongMemory)

