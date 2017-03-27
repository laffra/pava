def add_native_methods(clazz):
    def initNative():
        raise NotImplementedError()

    def _getGlyphImageFromWindows(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz.initNative = staticmethod(initNative)
    clazz._getGlyphImageFromWindows = _getGlyphImageFromWindows

