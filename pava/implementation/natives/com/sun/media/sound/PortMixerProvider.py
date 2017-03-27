def add_native_methods(clazz):
    def nGetNumDevices():
        raise NotImplementedError()

    def nNewPortMixerInfo(a0):
        raise NotImplementedError()

    clazz.nGetNumDevices = staticmethod(nGetNumDevices)
    clazz.nNewPortMixerInfo = staticmethod(nNewPortMixerInfo)

