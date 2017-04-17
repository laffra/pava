def add_native_methods(clazz):
    def isInstance__java_lang_Object__(a0, a1):
        raise NotImplementedError()

    def isAssignableFrom__java_lang_Class_____(a0, a1):
        raise NotImplementedError()

    def isInterface____(a0):
        raise NotImplementedError()

    def isArray____(a0):
        raise NotImplementedError()

    def isPrimitive____(a0):
        raise NotImplementedError()

    def getSuperclass____(a0):
        raise NotImplementedError()

    def getComponentType____(a0):
        raise NotImplementedError()

    def getModifiers____(a0):
        raise NotImplementedError()

    def getSigners____(a0):
        raise NotImplementedError()

    def setSigners__java_lang_Object____(a0, a1):
        raise NotImplementedError()

    def getPrimitiveClass__java_lang_String__(a0):
        raise NotImplementedError()

    def getRawAnnotations____(a0):
        raise NotImplementedError()

    def getRawTypeAnnotations____(a0):
        raise NotImplementedError()

    def getConstantPool____(a0):
        raise NotImplementedError()

    clazz.isInstance__java_lang_Object__ = isInstance__java_lang_Object__
    clazz.isAssignableFrom__java_lang_Class_____ = isAssignableFrom__java_lang_Class_____
    clazz.isInterface____ = isInterface____
    clazz.isArray____ = isArray____
    clazz.isPrimitive____ = isPrimitive____
    clazz.getSuperclass____ = getSuperclass____
    clazz.getComponentType____ = getComponentType____
    clazz.getModifiers____ = getModifiers____
    clazz.getSigners____ = getSigners____
    clazz.setSigners__java_lang_Object____ = setSigners__java_lang_Object____
    clazz.getPrimitiveClass__java_lang_String__ = staticmethod(getPrimitiveClass__java_lang_String__)
    clazz.getRawAnnotations____ = getRawAnnotations____
    clazz.getRawTypeAnnotations____ = getRawTypeAnnotations____
    clazz.getConstantPool____ = getConstantPool____

