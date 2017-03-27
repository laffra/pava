def add_native_methods(clazz):
    def nGetNumDevices():
        raise NotImplementedError()

    def nGetName(a0):
        raise NotImplementedError()

    def nGetVendor(a0):
        raise NotImplementedError()

    def nGetDescription(a0):
        raise NotImplementedError()

    def nGetVersion(a0):
        raise NotImplementedError()

    clazz.nGetNumDevices = staticmethod(nGetNumDevices)
    clazz.nGetName = staticmethod(nGetName)
    clazz.nGetVendor = staticmethod(nGetVendor)
    clazz.nGetDescription = staticmethod(nGetDescription)
    clazz.nGetVersion = staticmethod(nGetVersion)

