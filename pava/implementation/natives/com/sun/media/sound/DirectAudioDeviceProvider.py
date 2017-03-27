def add_native_methods(clazz):
    def nGetNumDevices():
        raise NotImplementedError()

    def nNewDirectAudioDeviceInfo(a0):
        raise NotImplementedError()

    clazz.nGetNumDevices = staticmethod(nGetNumDevices)
    clazz.nNewDirectAudioDeviceInfo = staticmethod(nNewDirectAudioDeviceInfo)

