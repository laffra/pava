def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def setICMpixels(a0, a1, a2, a3, a4, a5, a6, a7, a8):
        raise NotImplementedError()

    def setDiffICM(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.setICMpixels = setICMpixels
    clazz.setDiffICM = setDiffICM

