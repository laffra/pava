def add_native_methods(clazz):
    def doPrivileged__java_security_PrivilegedAction_T___(a0):
        raise NotImplementedError()

    def doPrivileged__java_security_PrivilegedAction_T___java_security_AccessControlContext__(a0, a1):
        raise NotImplementedError()

    def doPrivileged__java_security_PrivilegedExceptionAction_T___(a0):
        raise NotImplementedError()

    def doPrivileged__java_security_PrivilegedExceptionAction_T___java_security_AccessControlContext__(a0, a1):
        raise NotImplementedError()

    def getInheritedAccessControlContext____():
        raise NotImplementedError()

    clazz.doPrivileged__java_security_PrivilegedAction_T___ = staticmethod(doPrivileged__java_security_PrivilegedAction_T___)
    clazz.doPrivileged__java_security_PrivilegedAction_T___java_security_AccessControlContext__ = staticmethod(doPrivileged__java_security_PrivilegedAction_T___java_security_AccessControlContext__)
    clazz.doPrivileged__java_security_PrivilegedExceptionAction_T___ = staticmethod(doPrivileged__java_security_PrivilegedExceptionAction_T___)
    clazz.doPrivileged__java_security_PrivilegedExceptionAction_T___java_security_AccessControlContext__ = staticmethod(doPrivileged__java_security_PrivilegedExceptionAction_T___java_security_AccessControlContext__)
    clazz.getInheritedAccessControlContext____ = staticmethod(getInheritedAccessControlContext____)

