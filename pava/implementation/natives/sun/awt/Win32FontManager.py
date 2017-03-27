def add_native_methods(clazz):
    def getEUDCFontFile():
        raise NotImplementedError()

    def populateFontFileNameMap0(a0, a1, a2, a3):
        raise NotImplementedError()

    def getFontPath(a0):
        raise NotImplementedError()

    def registerFontWithPlatform(a0):
        raise NotImplementedError()

    def deRegisterFontWithPlatform(a0):
        raise NotImplementedError()

    clazz.getEUDCFontFile = staticmethod(getEUDCFontFile)
    clazz.populateFontFileNameMap0 = staticmethod(populateFontFileNameMap0)
    clazz.getFontPath = getFontPath
    clazz.registerFontWithPlatform = staticmethod(registerFontWithPlatform)
    clazz.deRegisterFontWithPlatform = staticmethod(deRegisterFontWithPlatform)

