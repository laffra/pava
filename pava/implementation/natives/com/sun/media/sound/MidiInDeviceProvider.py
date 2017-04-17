def add_native_methods(clazz):
    def nGetNumDevices____(a0):
        raise NotImplementedError()

    def nGetName__int__(a0, a1):
        raise NotImplementedError()

    def nGetVendor__int__(a0, a1):
        raise NotImplementedError()

    def nGetDescription__int__(a0, a1):
        raise NotImplementedError()

    def nGetVersion__int__(a0, a1):
        raise NotImplementedError()

    clazz.nGetNumDevices____ = staticmethod(nGetNumDevices____)
    clazz.nGetName__int__ = staticmethod(nGetName__int__)
    clazz.nGetVendor__int__ = staticmethod(nGetVendor__int__)
    clazz.nGetDescription__int__ = staticmethod(nGetDescription__int__)
    clazz.nGetVersion__int__ = staticmethod(nGetVersion__int__)

