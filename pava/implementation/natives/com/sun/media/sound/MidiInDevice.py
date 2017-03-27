def add_native_methods(clazz):
    def nOpen(a0):
        raise NotImplementedError()

    def nClose(a0):
        raise NotImplementedError()

    def nStart(a0):
        raise NotImplementedError()

    def nStop(a0):
        raise NotImplementedError()

    def nGetTimeStamp(a0):
        raise NotImplementedError()

    def nGetMessages(a0):
        raise NotImplementedError()

    clazz.nOpen = nOpen
    clazz.nClose = nClose
    clazz.nStart = nStart
    clazz.nStop = nStop
    clazz.nGetTimeStamp = nGetTimeStamp
    clazz.nGetMessages = nGetMessages

