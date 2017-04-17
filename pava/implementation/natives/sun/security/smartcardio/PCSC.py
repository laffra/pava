def add_native_methods(clazz):
    def SCardEstablishContext__int__(a0):
        raise NotImplementedError()

    def SCardListReaders__long__(a0):
        raise NotImplementedError()

    def SCardConnect__long__java_lang_String__int__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def SCardTransmit__long__int__byte____int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def SCardStatus__long__byte____(a0, a1):
        raise NotImplementedError()

    def SCardDisconnect__long__int__(a0, a1):
        raise NotImplementedError()

    def SCardGetStatusChange__long__long__int____java_lang_String____(a0, a1, a2, a3):
        raise NotImplementedError()

    def SCardBeginTransaction__long__(a0):
        raise NotImplementedError()

    def SCardEndTransaction__long__int__(a0, a1):
        raise NotImplementedError()

    def SCardControl__long__int__byte____(a0, a1, a2):
        raise NotImplementedError()

    clazz.SCardEstablishContext__int__ = staticmethod(SCardEstablishContext__int__)
    clazz.SCardListReaders__long__ = staticmethod(SCardListReaders__long__)
    clazz.SCardConnect__long__java_lang_String__int__int__ = staticmethod(SCardConnect__long__java_lang_String__int__int__)
    clazz.SCardTransmit__long__int__byte____int__int__ = staticmethod(SCardTransmit__long__int__byte____int__int__)
    clazz.SCardStatus__long__byte____ = staticmethod(SCardStatus__long__byte____)
    clazz.SCardDisconnect__long__int__ = staticmethod(SCardDisconnect__long__int__)
    clazz.SCardGetStatusChange__long__long__int____java_lang_String____ = staticmethod(SCardGetStatusChange__long__long__int____java_lang_String____)
    clazz.SCardBeginTransaction__long__ = staticmethod(SCardBeginTransaction__long__)
    clazz.SCardEndTransaction__long__int__ = staticmethod(SCardEndTransaction__long__int__)
    clazz.SCardControl__long__int__byte____ = staticmethod(SCardControl__long__int__byte____)

