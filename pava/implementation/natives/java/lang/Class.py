def add_native_methods(clazz):
    def registerNatives():
        raise NotImplementedError()

    def forName0(a0, a1, a2, a3):
        raise NotImplementedError()

    def isInstance(a0):
        raise NotImplementedError()

    def isAssignableFrom(a0):
        raise NotImplementedError()

    def isInterface():
        raise NotImplementedError()

    def isArray():
        raise NotImplementedError()

    def isPrimitive():
        raise NotImplementedError()

    def getName0():
        raise NotImplementedError()

    def getSuperclass():
        raise NotImplementedError()

    def getInterfaces0():
        raise NotImplementedError()

    def getComponentType():
        raise NotImplementedError()

    def getModifiers():
        raise NotImplementedError()

    def getSigners():
        raise NotImplementedError()

    def setSigners(a0):
        raise NotImplementedError()

    def getEnclosingMethod0():
        raise NotImplementedError()

    def getDeclaringClass0():
        raise NotImplementedError()

    def getProtectionDomain0():
        raise NotImplementedError()

    def getPrimitiveClass(a0):
        raise NotImplementedError()

    def getGenericSignature0():
        raise NotImplementedError()

    def getRawAnnotations():
        raise NotImplementedError()

    def getRawTypeAnnotations():
        raise NotImplementedError()

    def getConstantPool():
        raise NotImplementedError()

    def getDeclaredFields0(a0):
        raise NotImplementedError()

    def getDeclaredMethods0(a0):
        raise NotImplementedError()

    def getDeclaredConstructors0(a0):
        raise NotImplementedError()

    def getDeclaredClasses0():
        raise NotImplementedError()

    def desiredAssertionStatus0(a0):
        raise NotImplementedError()

    clazz.registerNatives = staticmethod(registerNatives)
    clazz.forName0 = staticmethod(forName0)
    clazz.isInstance = isInstance
    clazz.isAssignableFrom = isAssignableFrom
    clazz.isInterface = isInterface
    clazz.isArray = isArray
    clazz.isPrimitive = isPrimitive
    clazz.getName0 = getName0
    clazz.getSuperclass = getSuperclass
    clazz.getInterfaces0 = getInterfaces0
    clazz.getComponentType = getComponentType
    clazz.getModifiers = getModifiers
    clazz.getSigners = getSigners
    clazz.setSigners = setSigners
    clazz.getEnclosingMethod0 = getEnclosingMethod0
    clazz.getDeclaringClass0 = getDeclaringClass0
    clazz.getProtectionDomain0 = getProtectionDomain0
    clazz.getPrimitiveClass = staticmethod(getPrimitiveClass)
    clazz.getGenericSignature0 = getGenericSignature0
    clazz.getRawAnnotations = getRawAnnotations
    clazz.getRawTypeAnnotations = getRawTypeAnnotations
    clazz.getConstantPool = getConstantPool
    clazz.getDeclaredFields0 = getDeclaredFields0
    clazz.getDeclaredMethods0 = getDeclaredMethods0
    clazz.getDeclaredConstructors0 = getDeclaredConstructors0
    clazz.getDeclaredClasses0 = getDeclaredClasses0
    clazz.desiredAssertionStatus0 = staticmethod(desiredAssertionStatus0)

