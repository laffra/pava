def add_native_methods(clazz):
    def isModifiableClass0__long__java_lang_Class_____(a0, a1, a2):
        raise NotImplementedError()

    def isRetransformClassesSupported0__long__(a0, a1):
        raise NotImplementedError()

    def setHasRetransformableTransformers__long__boolean__(a0, a1, a2):
        raise NotImplementedError()

    def retransformClasses0__long__java_lang_Class_______(a0, a1, a2):
        raise NotImplementedError()

    def redefineClasses0__long__java_lang_instrument_ClassDefinition____(a0, a1, a2):
        raise NotImplementedError()

    def getAllLoadedClasses0__long__(a0, a1):
        raise NotImplementedError()

    def getInitiatedClasses0__long__java_lang_ClassLoader__(a0, a1, a2):
        raise NotImplementedError()

    def getObjectSize0__long__java_lang_Object__(a0, a1, a2):
        raise NotImplementedError()

    def appendToClassLoaderSearch0__long__java_lang_String__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def setNativeMethodPrefixes__long__java_lang_String____boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.isModifiableClass0__long__java_lang_Class_____ = isModifiableClass0__long__java_lang_Class_____
    clazz.isRetransformClassesSupported0__long__ = isRetransformClassesSupported0__long__
    clazz.setHasRetransformableTransformers__long__boolean__ = setHasRetransformableTransformers__long__boolean__
    clazz.retransformClasses0__long__java_lang_Class_______ = retransformClasses0__long__java_lang_Class_______
    clazz.redefineClasses0__long__java_lang_instrument_ClassDefinition____ = redefineClasses0__long__java_lang_instrument_ClassDefinition____
    clazz.getAllLoadedClasses0__long__ = getAllLoadedClasses0__long__
    clazz.getInitiatedClasses0__long__java_lang_ClassLoader__ = getInitiatedClasses0__long__java_lang_ClassLoader__
    clazz.getObjectSize0__long__java_lang_Object__ = getObjectSize0__long__java_lang_Object__
    clazz.appendToClassLoaderSearch0__long__java_lang_String__boolean__ = appendToClassLoaderSearch0__long__java_lang_String__boolean__
    clazz.setNativeMethodPrefixes__long__java_lang_String____boolean__ = setNativeMethodPrefixes__long__java_lang_String____boolean__

