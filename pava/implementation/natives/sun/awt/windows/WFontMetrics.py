def add_native_methods(clazz):
    def stringWidth__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def charsWidth__char____int__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def bytesWidth__byte____int__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def init____(a0):
        raise NotImplementedError()

    clazz.stringWidth__java_lang_String__ = stringWidth__java_lang_String__
    clazz.charsWidth__char____int__int__ = charsWidth__char____int__int__
    clazz.bytesWidth__byte____int__int__ = bytesWidth__byte____int__int__
    clazz.init____ = init____

