def add_native_methods(clazz):
    def nOpen(a0):
        raise NotImplementedError()

    def nClose(a0):
        raise NotImplementedError()

    def nGetPortCount(a0):
        raise NotImplementedError()

    def nGetPortType(a0, a1):
        raise NotImplementedError()

    def nGetPortName(a0, a1):
        raise NotImplementedError()

    def nGetControls(a0, a1, a2):
        raise NotImplementedError()

    def nControlSetIntValue(a0, a1):
        raise NotImplementedError()

    def nControlGetIntValue(a0):
        raise NotImplementedError()

    def nControlSetFloatValue(a0, a1):
        raise NotImplementedError()

    def nControlGetFloatValue(a0):
        raise NotImplementedError()

    clazz.nOpen = staticmethod(nOpen)
    clazz.nClose = staticmethod(nClose)
    clazz.nGetPortCount = staticmethod(nGetPortCount)
    clazz.nGetPortType = staticmethod(nGetPortType)
    clazz.nGetPortName = staticmethod(nGetPortName)
    clazz.nGetControls = staticmethod(nGetControls)
    clazz.nControlSetIntValue = staticmethod(nControlSetIntValue)
    clazz.nControlGetIntValue = staticmethod(nControlGetIntValue)
    clazz.nControlSetFloatValue = staticmethod(nControlSetFloatValue)
    clazz.nControlGetFloatValue = staticmethod(nControlGetFloatValue)

