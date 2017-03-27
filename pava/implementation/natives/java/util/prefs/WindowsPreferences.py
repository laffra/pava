def add_native_methods(clazz):
    def WindowsRegOpenKey(a0, a1, a2):
        raise NotImplementedError()

    def WindowsRegCloseKey(a0):
        raise NotImplementedError()

    def WindowsRegCreateKeyEx(a0, a1):
        raise NotImplementedError()

    def WindowsRegDeleteKey(a0, a1):
        raise NotImplementedError()

    def WindowsRegFlushKey(a0):
        raise NotImplementedError()

    def WindowsRegQueryValueEx(a0, a1):
        raise NotImplementedError()

    def WindowsRegSetValueEx(a0, a1, a2):
        raise NotImplementedError()

    def WindowsRegDeleteValue(a0, a1):
        raise NotImplementedError()

    def WindowsRegQueryInfoKey(a0):
        raise NotImplementedError()

    def WindowsRegEnumKeyEx(a0, a1, a2):
        raise NotImplementedError()

    def WindowsRegEnumValue(a0, a1, a2):
        raise NotImplementedError()

    clazz.WindowsRegOpenKey = staticmethod(WindowsRegOpenKey)
    clazz.WindowsRegCloseKey = staticmethod(WindowsRegCloseKey)
    clazz.WindowsRegCreateKeyEx = staticmethod(WindowsRegCreateKeyEx)
    clazz.WindowsRegDeleteKey = staticmethod(WindowsRegDeleteKey)
    clazz.WindowsRegFlushKey = staticmethod(WindowsRegFlushKey)
    clazz.WindowsRegQueryValueEx = staticmethod(WindowsRegQueryValueEx)
    clazz.WindowsRegSetValueEx = staticmethod(WindowsRegSetValueEx)
    clazz.WindowsRegDeleteValue = staticmethod(WindowsRegDeleteValue)
    clazz.WindowsRegQueryInfoKey = staticmethod(WindowsRegQueryInfoKey)
    clazz.WindowsRegEnumKeyEx = staticmethod(WindowsRegEnumKeyEx)
    clazz.WindowsRegEnumValue = staticmethod(WindowsRegEnumValue)

