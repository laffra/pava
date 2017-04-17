def add_native_methods(clazz):
    def floatsToBytes__float____int__byte____int__int__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def doublesToBytes__double____int__byte____int__int__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    clazz.floatsToBytes__float____int__byte____int__int__ = staticmethod(floatsToBytes__float____int__byte____int__int__)
    clazz.doublesToBytes__double____int__byte____int__int__ = staticmethod(doublesToBytes__double____int__byte____int__int__)

