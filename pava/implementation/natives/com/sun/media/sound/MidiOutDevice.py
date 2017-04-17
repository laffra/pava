def add_native_methods(clazz):
    def nOpen__int__(a0, a1):
        raise NotImplementedError()

    def nClose__long__(a0, a1):
        raise NotImplementedError()

    def nSendShortMessage__long__int__long__(a0, a1, a2, a3):
        raise NotImplementedError()

    def nSendLongMessage__long__byte____int__long__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def nGetTimeStamp__long__(a0, a1):
        raise NotImplementedError()

    clazz.nOpen__int__ = nOpen__int__
    clazz.nClose__long__ = nClose__long__
    clazz.nSendShortMessage__long__int__long__ = nSendShortMessage__long__int__long__
    clazz.nSendLongMessage__long__byte____int__long__ = nSendLongMessage__long__byte____int__long__
    clazz.nGetTimeStamp__long__ = nGetTimeStamp__long__

