def add_native_methods(clazz):
    def activate0(a0, a1):
        raise NotImplementedError()

    def dispose0(a0):
        raise NotImplementedError()

    def isEnabled0(a0):
        raise NotImplementedError()

    def isSupported0():
        raise NotImplementedError()

    def defineClass0(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz.activate0 = staticmethod(activate0)
    clazz.dispose0 = staticmethod(dispose0)
    clazz.isEnabled0 = staticmethod(isEnabled0)
    clazz.isSupported0 = staticmethod(isSupported0)
    clazz.defineClass0 = staticmethod(defineClass0)

