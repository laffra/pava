def add_native_methods(clazz):
    def isThemed():
        raise NotImplementedError()

    def paintBackground(a0, a1, a2, a3, a4, a5, a6, a7, a8):
        raise NotImplementedError()

    def getThemeMargins(a0, a1, a2, a3):
        raise NotImplementedError()

    def isThemePartDefined(a0, a1, a2):
        raise NotImplementedError()

    def getColor(a0, a1, a2, a3):
        raise NotImplementedError()

    def getInt(a0, a1, a2, a3):
        raise NotImplementedError()

    def getEnum(a0, a1, a2, a3):
        raise NotImplementedError()

    def getBoolean(a0, a1, a2, a3):
        raise NotImplementedError()

    def getSysBoolean(a0, a1):
        raise NotImplementedError()

    def getPoint(a0, a1, a2, a3):
        raise NotImplementedError()

    def getPosition(a0, a1, a2, a3):
        raise NotImplementedError()

    def getPartSize(a0, a1, a2):
        raise NotImplementedError()

    def openTheme(a0):
        raise NotImplementedError()

    def closeTheme(a0):
        raise NotImplementedError()

    def setWindowTheme(a0):
        raise NotImplementedError()

    def getThemeTransitionDuration(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def isGetThemeTransitionDurationDefined():
        raise NotImplementedError()

    def getThemeBackgroundContentMargins(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz.isThemed = staticmethod(isThemed)
    clazz.paintBackground = staticmethod(paintBackground)
    clazz.getThemeMargins = staticmethod(getThemeMargins)
    clazz.isThemePartDefined = staticmethod(isThemePartDefined)
    clazz.getColor = staticmethod(getColor)
    clazz.getInt = staticmethod(getInt)
    clazz.getEnum = staticmethod(getEnum)
    clazz.getBoolean = staticmethod(getBoolean)
    clazz.getSysBoolean = staticmethod(getSysBoolean)
    clazz.getPoint = staticmethod(getPoint)
    clazz.getPosition = staticmethod(getPosition)
    clazz.getPartSize = staticmethod(getPartSize)
    clazz.openTheme = staticmethod(openTheme)
    clazz.closeTheme = staticmethod(closeTheme)
    clazz.setWindowTheme = staticmethod(setWindowTheme)
    clazz.getThemeTransitionDuration = staticmethod(getThemeTransitionDuration)
    clazz.isGetThemeTransitionDurationDefined = staticmethod(isGetThemeTransitionDurationDefined)
    clazz.getThemeBackgroundContentMargins = staticmethod(getThemeBackgroundContentMargins)

