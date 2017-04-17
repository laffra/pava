def add_native_methods(clazz):
    def toStderr__java_lang_String__(a0):
        raise NotImplementedError()

    def toStdout__java_lang_String__(a0):
        raise NotImplementedError()

    clazz.toStderr__java_lang_String__ = staticmethod(toStderr__java_lang_String__)
    clazz.toStdout__java_lang_String__ = staticmethod(toStdout__java_lang_String__)

