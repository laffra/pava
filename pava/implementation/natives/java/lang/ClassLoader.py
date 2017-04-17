def add_native_methods(clazz):
    def registerNatives____(a0):
        raise NotImplementedError()

    def defineClass0__java_lang_String__byte____int__int__java_security_ProtectionDomain__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def defineClass1__java_lang_String__byte____int__int__java_security_ProtectionDomain__java_lang_String__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def defineClass2__java_lang_String__java_nio_ByteBuffer__int__int__java_security_ProtectionDomain__java_lang_String__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def resolveClass0__java_lang_Class_____(a0, a1):
        raise NotImplementedError()

    def findBootstrapClass__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def findLoadedClass0__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def findBuiltinLib__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def retrieveDirectives____(a0):
        raise NotImplementedError()

    clazz.registerNatives____ = staticmethod(registerNatives____)
    clazz.defineClass0__java_lang_String__byte____int__int__java_security_ProtectionDomain__ = defineClass0__java_lang_String__byte____int__int__java_security_ProtectionDomain__
    clazz.defineClass1__java_lang_String__byte____int__int__java_security_ProtectionDomain__java_lang_String__ = defineClass1__java_lang_String__byte____int__int__java_security_ProtectionDomain__java_lang_String__
    clazz.defineClass2__java_lang_String__java_nio_ByteBuffer__int__int__java_security_ProtectionDomain__java_lang_String__ = defineClass2__java_lang_String__java_nio_ByteBuffer__int__int__java_security_ProtectionDomain__java_lang_String__
    clazz.resolveClass0__java_lang_Class_____ = resolveClass0__java_lang_Class_____
    clazz.findBootstrapClass__java_lang_String__ = findBootstrapClass__java_lang_String__
    clazz.findLoadedClass0__java_lang_String__ = findLoadedClass0__java_lang_String__
    clazz.findBuiltinLib__java_lang_String__ = staticmethod(findBuiltinLib__java_lang_String__)
    clazz.retrieveDirectives____ = staticmethod(retrieveDirectives____)

