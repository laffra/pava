def add_native_methods(clazz):
    def nOpen__int__(a0, a1):
        raise NotImplementedError()

    def nClose__long__(a0, a1):
        raise NotImplementedError()

    def nGetPortCount__long__(a0, a1):
        raise NotImplementedError()

    def nGetPortType__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def nGetPortName__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def nGetControls__long__int__java_util_Vector__(a0, a1, a2, a3):
        raise NotImplementedError()

    def nControlSetIntValue__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def nControlGetIntValue__long__(a0, a1):
        raise NotImplementedError()

    def nControlSetFloatValue__long__float__(a0, a1, a2):
        raise NotImplementedError()

    def nControlGetFloatValue__long__(a0, a1):
        raise NotImplementedError()

    clazz.nOpen__int__ = staticmethod(nOpen__int__)
    clazz.nClose__long__ = staticmethod(nClose__long__)
    clazz.nGetPortCount__long__ = staticmethod(nGetPortCount__long__)
    clazz.nGetPortType__long__int__ = staticmethod(nGetPortType__long__int__)
    clazz.nGetPortName__long__int__ = staticmethod(nGetPortName__long__int__)
    clazz.nGetControls__long__int__java_util_Vector__ = staticmethod(nGetControls__long__int__java_util_Vector__)
    clazz.nControlSetIntValue__long__int__ = staticmethod(nControlSetIntValue__long__int__)
    clazz.nControlGetIntValue__long__ = staticmethod(nControlGetIntValue__long__)
    clazz.nControlSetFloatValue__long__float__ = staticmethod(nControlSetFloatValue__long__float__)
    clazz.nControlGetFloatValue__long__ = staticmethod(nControlGetFloatValue__long__)

