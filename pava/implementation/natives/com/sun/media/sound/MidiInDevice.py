def add_native_methods(clazz):
    def nOpen__int__(a0, a1):
        raise NotImplementedError()

    def nClose__long__(a0, a1):
        raise NotImplementedError()

    def nStart__long__(a0, a1):
        raise NotImplementedError()

    def nStop__long__(a0, a1):
        raise NotImplementedError()

    def nGetTimeStamp__long__(a0, a1):
        raise NotImplementedError()

    clazz.nOpen__int__ = nOpen__int__
    clazz.nClose__long__ = nClose__long__
    clazz.nStart__long__ = nStart__long__
    clazz.nStop__long__ = nStop__long__
    clazz.nGetTimeStamp__long__ = nGetTimeStamp__long__

