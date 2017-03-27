def add_native_methods(clazz):
    def init0():
        raise NotImplementedError()

    def isSecuritySupported0(a0):
        raise NotImplementedError()

    def isAccessUserOnly0(a0):
        raise NotImplementedError()

    clazz.init0 = staticmethod(init0)
    clazz.isSecuritySupported0 = staticmethod(isSecuritySupported0)
    clazz.isAccessUserOnly0 = staticmethod(isAccessUserOnly0)

