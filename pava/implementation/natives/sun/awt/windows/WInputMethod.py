def add_native_methods(clazz):
    def createNativeContext():
        raise NotImplementedError()

    def destroyNativeContext(a0):
        raise NotImplementedError()

    def enableNativeIME(a0, a1, a2):
        raise NotImplementedError()

    def disableNativeIME(a0):
        raise NotImplementedError()

    def handleNativeIMEEvent(a0, a1):
        raise NotImplementedError()

    def endCompositionNative(a0, a1):
        raise NotImplementedError()

    def setConversionStatus(a0, a1):
        raise NotImplementedError()

    def getConversionStatus(a0):
        raise NotImplementedError()

    def setOpenStatus(a0, a1):
        raise NotImplementedError()

    def getOpenStatus(a0):
        raise NotImplementedError()

    def setStatusWindowVisible(a0, a1):
        raise NotImplementedError()

    def getNativeIMMDescription():
        raise NotImplementedError()

    def getNativeLocale():
        raise NotImplementedError()

    def setNativeLocale(a0, a1):
        raise NotImplementedError()

    def openCandidateWindow(a0, a1, a2):
        raise NotImplementedError()

    clazz.createNativeContext = createNativeContext
    clazz.destroyNativeContext = destroyNativeContext
    clazz.enableNativeIME = enableNativeIME
    clazz.disableNativeIME = disableNativeIME
    clazz.handleNativeIMEEvent = handleNativeIMEEvent
    clazz.endCompositionNative = endCompositionNative
    clazz.setConversionStatus = setConversionStatus
    clazz.getConversionStatus = getConversionStatus
    clazz.setOpenStatus = setOpenStatus
    clazz.getOpenStatus = getOpenStatus
    clazz.setStatusWindowVisible = setStatusWindowVisible
    clazz.getNativeIMMDescription = getNativeIMMDescription
    clazz.getNativeLocale = staticmethod(getNativeLocale)
    clazz.setNativeLocale = staticmethod(setNativeLocale)
    clazz.openCandidateWindow = openCandidateWindow

