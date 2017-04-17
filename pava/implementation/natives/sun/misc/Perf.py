def add_native_methods(clazz):
    def createLong__java_lang_String__int__int__long__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def createByteArray__java_lang_String__int__int__byte____int__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def highResCounter____(a0):
        raise NotImplementedError()

    def highResFrequency____(a0):
        raise NotImplementedError()

    clazz.createLong__java_lang_String__int__int__long__ = createLong__java_lang_String__int__int__long__
    clazz.createByteArray__java_lang_String__int__int__byte____int__ = createByteArray__java_lang_String__int__int__byte____int__
    clazz.highResCounter____ = highResCounter____
    clazz.highResFrequency____ = highResFrequency____

