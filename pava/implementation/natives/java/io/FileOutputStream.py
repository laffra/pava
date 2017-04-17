def add_native_methods(clazz):
    def open0__java_lang_String__boolean__(a0, a1, a2):
        raise NotImplementedError()

    def write__int__boolean__(a0, a1, a2):
        raise NotImplementedError()

    def writeBytes__byte____int__int__boolean__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def close0____(a0):
        raise NotImplementedError()

    def initIDs____(a0):
        raise NotImplementedError()

    clazz.open0__java_lang_String__boolean__ = open0__java_lang_String__boolean__
    clazz.write__int__boolean__ = write__int__boolean__
    clazz.writeBytes__byte____int__int__boolean__ = writeBytes__byte____int__int__boolean__
    clazz.close0____ = close0____
    clazz.initIDs____ = staticmethod(initIDs____)

