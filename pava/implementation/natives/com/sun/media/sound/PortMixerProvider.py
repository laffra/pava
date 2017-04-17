def add_native_methods(clazz):
    def nGetNumDevices____(a0):
        raise NotImplementedError()

    def nNewPortMixerInfo__int__(a0, a1):
        raise NotImplementedError()

    clazz.nGetNumDevices____ = staticmethod(nGetNumDevices____)
    clazz.nNewPortMixerInfo__int__ = staticmethod(nNewPortMixerInfo__int__)

