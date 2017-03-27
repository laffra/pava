def add_native_methods(clazz):
    def isModifiableClass0(a0, a1):
        raise NotImplementedError()

    def isRetransformClassesSupported0(a0):
        raise NotImplementedError()

    def setHasRetransformableTransformers(a0, a1):
        raise NotImplementedError()

    def retransformClasses0(a0, a1):
        raise NotImplementedError()

    def redefineClasses0(a0, a1):
        raise NotImplementedError()

    def getAllLoadedClasses0(a0):
        raise NotImplementedError()

    def getInitiatedClasses0(a0, a1):
        raise NotImplementedError()

    def getObjectSize0(a0, a1):
        raise NotImplementedError()

    def appendToClassLoaderSearch0(a0, a1, a2):
        raise NotImplementedError()

    def setNativeMethodPrefixes(a0, a1, a2):
        raise NotImplementedError()

    clazz.isModifiableClass0 = isModifiableClass0
    clazz.isRetransformClassesSupported0 = isRetransformClassesSupported0
    clazz.setHasRetransformableTransformers = setHasRetransformableTransformers
    clazz.retransformClasses0 = retransformClasses0
    clazz.redefineClasses0 = redefineClasses0
    clazz.getAllLoadedClasses0 = getAllLoadedClasses0
    clazz.getInitiatedClasses0 = getInitiatedClasses0
    clazz.getObjectSize0 = getObjectSize0
    clazz.appendToClassLoaderSearch0 = appendToClassLoaderSearch0
    clazz.setNativeMethodPrefixes = setNativeMethodPrefixes

