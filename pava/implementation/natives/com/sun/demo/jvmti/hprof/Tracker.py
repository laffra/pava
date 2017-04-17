def add_native_methods(clazz):
    def nativeObjectInit__java_lang_Object__java_lang_Object__(a0, a1, a2):
        raise NotImplementedError()

    def nativeNewArray__java_lang_Object__java_lang_Object__(a0, a1, a2):
        raise NotImplementedError()

    def nativeCallSite__java_lang_Object__int__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def nativeReturnSite__java_lang_Object__int__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.nativeObjectInit__java_lang_Object__java_lang_Object__ = staticmethod(nativeObjectInit__java_lang_Object__java_lang_Object__)
    clazz.nativeNewArray__java_lang_Object__java_lang_Object__ = staticmethod(nativeNewArray__java_lang_Object__java_lang_Object__)
    clazz.nativeCallSite__java_lang_Object__int__int__ = staticmethod(nativeCallSite__java_lang_Object__int__int__)
    clazz.nativeReturnSite__java_lang_Object__int__int__ = staticmethod(nativeReturnSite__java_lang_Object__int__int__)

