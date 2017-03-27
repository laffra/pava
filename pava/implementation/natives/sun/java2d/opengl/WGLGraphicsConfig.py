def add_native_methods(clazz):
    def getDefaultPixFmt(a0):
        raise NotImplementedError()

    def initWGL():
        raise NotImplementedError()

    def getWGLConfigInfo(a0, a1):
        raise NotImplementedError()

    def getOGLCapabilities(a0):
        raise NotImplementedError()

    clazz.getDefaultPixFmt = staticmethod(getDefaultPixFmt)
    clazz.initWGL = staticmethod(initWGL)
    clazz.getWGLConfigInfo = staticmethod(getWGLConfigInfo)
    clazz.getOGLCapabilities = staticmethod(getOGLCapabilities)

