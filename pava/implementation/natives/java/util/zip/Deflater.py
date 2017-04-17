def add_native_methods(clazz):
    def initIDs____(a0):
        raise NotImplementedError()

    def init__int__int__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def setDictionary__long__byte____int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def deflateBytes__long__byte____int__int__int__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def getAdler__long__(a0, a1):
        raise NotImplementedError()

    def reset__long__(a0, a1):
        raise NotImplementedError()

    def end__long__(a0, a1):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.init__int__int__boolean__ = staticmethod(init__int__int__boolean__)
    clazz.setDictionary__long__byte____int__int__ = staticmethod(setDictionary__long__byte____int__int__)
    clazz.deflateBytes__long__byte____int__int__int__ = deflateBytes__long__byte____int__int__int__
    clazz.getAdler__long__ = staticmethod(getAdler__long__)
    clazz.reset__long__ = staticmethod(reset__long__)
    clazz.end__long__ = staticmethod(end__long__)

