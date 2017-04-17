def add_native_methods(clazz):
    def WindowsRegOpenKey__int__byte____int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def WindowsRegCloseKey__int__(a0, a1):
        raise NotImplementedError()

    def WindowsRegCreateKeyEx__int__byte____(a0, a1, a2):
        raise NotImplementedError()

    def WindowsRegDeleteKey__int__byte____(a0, a1, a2):
        raise NotImplementedError()

    def WindowsRegFlushKey__int__(a0, a1):
        raise NotImplementedError()

    def WindowsRegQueryValueEx__int__byte____(a0, a1, a2):
        raise NotImplementedError()

    def WindowsRegSetValueEx__int__byte____byte____(a0, a1, a2, a3):
        raise NotImplementedError()

    def WindowsRegDeleteValue__int__byte____(a0, a1, a2):
        raise NotImplementedError()

    def WindowsRegQueryInfoKey__int__(a0, a1):
        raise NotImplementedError()

    def WindowsRegEnumKeyEx__int__int__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def WindowsRegEnumValue__int__int__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.WindowsRegOpenKey__int__byte____int__ = staticmethod(WindowsRegOpenKey__int__byte____int__)
    clazz.WindowsRegCloseKey__int__ = staticmethod(WindowsRegCloseKey__int__)
    clazz.WindowsRegCreateKeyEx__int__byte____ = staticmethod(WindowsRegCreateKeyEx__int__byte____)
    clazz.WindowsRegDeleteKey__int__byte____ = staticmethod(WindowsRegDeleteKey__int__byte____)
    clazz.WindowsRegFlushKey__int__ = staticmethod(WindowsRegFlushKey__int__)
    clazz.WindowsRegQueryValueEx__int__byte____ = staticmethod(WindowsRegQueryValueEx__int__byte____)
    clazz.WindowsRegSetValueEx__int__byte____byte____ = staticmethod(WindowsRegSetValueEx__int__byte____byte____)
    clazz.WindowsRegDeleteValue__int__byte____ = staticmethod(WindowsRegDeleteValue__int__byte____)
    clazz.WindowsRegQueryInfoKey__int__ = staticmethod(WindowsRegQueryInfoKey__int__)
    clazz.WindowsRegEnumKeyEx__int__int__int__ = staticmethod(WindowsRegEnumKeyEx__int__int__int__)
    clazz.WindowsRegEnumValue__int__int__int__ = staticmethod(WindowsRegEnumValue__int__int__int__)

