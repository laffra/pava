def add_native_methods(clazz):
    def initTexture(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def initFBObject(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def initFlipBackbuffer(a0):
        raise NotImplementedError()

    def getTextureTarget(a0):
        raise NotImplementedError()

    def getTextureID(a0):
        raise NotImplementedError()

    clazz.initTexture = initTexture
    clazz.initFBObject = initFBObject
    clazz.initFlipBackbuffer = initFlipBackbuffer
    clazz.getTextureTarget = getTextureTarget
    clazz.getTextureID = getTextureID

