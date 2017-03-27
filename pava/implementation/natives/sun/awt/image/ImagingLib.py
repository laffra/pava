def add_native_methods(clazz):
    def init():
        raise NotImplementedError()

    def transformBI(a0, a1, a2, a3):
        raise NotImplementedError()

    def transformRaster(a0, a1, a2, a3):
        raise NotImplementedError()

    def convolveBI(a0, a1, a2, a3):
        raise NotImplementedError()

    def convolveRaster(a0, a1, a2, a3):
        raise NotImplementedError()

    def lookupByteBI(a0, a1, a2):
        raise NotImplementedError()

    def lookupByteRaster(a0, a1, a2):
        raise NotImplementedError()

    clazz.init = staticmethod(init)
    clazz.transformBI = staticmethod(transformBI)
    clazz.transformRaster = staticmethod(transformRaster)
    clazz.convolveBI = staticmethod(convolveBI)
    clazz.convolveRaster = staticmethod(convolveRaster)
    clazz.lookupByteBI = staticmethod(lookupByteBI)
    clazz.lookupByteRaster = staticmethod(lookupByteRaster)

