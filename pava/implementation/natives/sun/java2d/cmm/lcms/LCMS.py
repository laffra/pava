def add_native_methods(clazz):
    def loadProfileNative(a0, a1):
        raise NotImplementedError()

    def getProfileSizeNative(a0):
        raise NotImplementedError()

    def getProfileDataNative(a0, a1):
        raise NotImplementedError()

    def getTagNative(a0, a1):
        raise NotImplementedError()

    def setTagDataNative(a0, a1, a2):
        raise NotImplementedError()

    def getProfileID(a0):
        raise NotImplementedError()

    def createNativeTransform(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def colorConvert(a0, a1, a2):
        raise NotImplementedError()

    def freeTransform(a0):
        raise NotImplementedError()

    def initLCMS(a0, a1, a2):
        raise NotImplementedError()

    clazz.loadProfileNative = loadProfileNative
    clazz.getProfileSizeNative = getProfileSizeNative
    clazz.getProfileDataNative = getProfileDataNative
    clazz.getTagNative = staticmethod(getTagNative)
    clazz.setTagDataNative = setTagDataNative
    clazz.getProfileID = staticmethod(getProfileID)
    clazz.createNativeTransform = staticmethod(createNativeTransform)
    clazz.colorConvert = staticmethod(colorConvert)
    clazz.freeTransform = staticmethod(freeTransform)
    clazz.initLCMS = staticmethod(initLCMS)

