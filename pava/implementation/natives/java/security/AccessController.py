def add_native_methods(clazz):
    def doPrivileged(a0):
        raise NotImplementedError()

    def doPrivileged(a0, a1):
        raise NotImplementedError()

    def doPrivileged(a0):
        raise NotImplementedError()

    def doPrivileged(a0, a1):
        raise NotImplementedError()

    def getStackAccessControlContext():
        raise NotImplementedError()

    def getInheritedAccessControlContext():
        raise NotImplementedError()

    clazz.doPrivileged = staticmethod(doPrivileged)
    clazz.doPrivileged = staticmethod(doPrivileged)
    clazz.doPrivileged = staticmethod(doPrivileged)
    clazz.doPrivileged = staticmethod(doPrivileged)
    clazz.getStackAccessControlContext = staticmethod(getStackAccessControlContext)
    clazz.getInheritedAccessControlContext = staticmethod(getInheritedAccessControlContext)

