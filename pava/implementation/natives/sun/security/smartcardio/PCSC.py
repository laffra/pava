def add_native_methods(clazz):
    def SCardEstablishContext(a0):
        raise NotImplementedError()

    def SCardListReaders(a0):
        raise NotImplementedError()

    def SCardConnect(a0, a1, a2, a3):
        raise NotImplementedError()

    def SCardTransmit(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def SCardStatus(a0, a1):
        raise NotImplementedError()

    def SCardDisconnect(a0, a1):
        raise NotImplementedError()

    def SCardGetStatusChange(a0, a1, a2, a3):
        raise NotImplementedError()

    def SCardBeginTransaction(a0):
        raise NotImplementedError()

    def SCardEndTransaction(a0, a1):
        raise NotImplementedError()

    def SCardControl(a0, a1, a2):
        raise NotImplementedError()

    clazz.SCardEstablishContext = staticmethod(SCardEstablishContext)
    clazz.SCardListReaders = staticmethod(SCardListReaders)
    clazz.SCardConnect = staticmethod(SCardConnect)
    clazz.SCardTransmit = staticmethod(SCardTransmit)
    clazz.SCardStatus = staticmethod(SCardStatus)
    clazz.SCardDisconnect = staticmethod(SCardDisconnect)
    clazz.SCardGetStatusChange = staticmethod(SCardGetStatusChange)
    clazz.SCardBeginTransaction = staticmethod(SCardBeginTransaction)
    clazz.SCardEndTransaction = staticmethod(SCardEndTransaction)
    clazz.SCardControl = staticmethod(SCardControl)

