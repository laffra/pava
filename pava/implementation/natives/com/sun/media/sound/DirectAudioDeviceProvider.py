def add_native_methods(clazz):
    def nGetNumDevices____(a0):
        raise NotImplementedError()

    def nNewDirectAudioDeviceInfo__int__(a0, a1):
        raise NotImplementedError()

    clazz.nGetNumDevices____ = staticmethod(nGetNumDevices____)
    clazz.nNewDirectAudioDeviceInfo__int__ = staticmethod(nNewDirectAudioDeviceInfo__int__)

