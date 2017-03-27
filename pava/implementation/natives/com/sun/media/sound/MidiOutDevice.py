def add_native_methods(clazz):
    def nOpen(a0):
        raise NotImplementedError()

    def nClose(a0):
        raise NotImplementedError()

    def nSendShortMessage(a0, a1, a2):
        raise NotImplementedError()

    def nSendLongMessage(a0, a1, a2, a3):
        raise NotImplementedError()

    def nGetTimeStamp(a0):
        raise NotImplementedError()

    clazz.nOpen = nOpen
    clazz.nClose = nClose
    clazz.nSendShortMessage = nSendShortMessage
    clazz.nSendLongMessage = nSendLongMessage
    clazz.nGetTimeStamp = nGetTimeStamp

