def add_native_methods(clazz):
    def initIDs__java_lang_Class__java_lang_Class__(a0, a1):
        raise NotImplementedError()

    def fillTile__sun_java2d_pipe_RegionIterator__byte____int__int__int____(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def eraseTile__sun_java2d_pipe_RegionIterator__byte____int__int__int____(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    clazz.initIDs__java_lang_Class__java_lang_Class__ = staticmethod(initIDs__java_lang_Class__java_lang_Class__)
    clazz.fillTile__sun_java2d_pipe_RegionIterator__byte____int__int__int____ = fillTile__sun_java2d_pipe_RegionIterator__byte____int__int__int____
    clazz.eraseTile__sun_java2d_pipe_RegionIterator__byte____int__int__int____ = eraseTile__sun_java2d_pipe_RegionIterator__byte____int__int__int____

