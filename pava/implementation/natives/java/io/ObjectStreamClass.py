def add_native_methods(clazz):
    def initNative____(a0):
        raise NotImplementedError()

    def hasStaticInitializer__java_lang_Class_____(a0, a1):
        raise NotImplementedError()

    clazz.initNative____ = staticmethod(initNative____)
    clazz.hasStaticInitializer__java_lang_Class_____ = staticmethod(hasStaticInitializer__java_lang_Class_____)

