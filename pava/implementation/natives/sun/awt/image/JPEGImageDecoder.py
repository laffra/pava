def add_native_methods(clazz):
    def initIDs__java_lang_Class__(a0, a1):
        raise NotImplementedError()

    def readImage__java_io_InputStream__byte____(a0, a1, a2):
        raise NotImplementedError()

    clazz.initIDs__java_lang_Class__ = staticmethod(initIDs__java_lang_Class__)
    clazz.readImage__java_io_InputStream__byte____ = readImage__java_io_InputStream__byte____

