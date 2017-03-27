def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def init(a0, a1, a2):
        raise NotImplementedError()

    def setDictionary(a0, a1, a2, a3):
        raise NotImplementedError()

    def deflateBytes(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def getAdler(a0):
        raise NotImplementedError()

    def reset(a0):
        raise NotImplementedError()

    def end(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.init = staticmethod(init)
    clazz.setDictionary = staticmethod(setDictionary)
    clazz.deflateBytes = deflateBytes
    clazz.getAdler = staticmethod(getAdler)
    clazz.reset = staticmethod(reset)
    clazz.end = staticmethod(end)

