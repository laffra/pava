def add_native_methods(clazz):
    def getWindowsDirectory__boolean__(a0, a1):
        raise NotImplementedError()

    clazz.getWindowsDirectory__boolean__ = staticmethod(getWindowsDirectory__boolean__)

