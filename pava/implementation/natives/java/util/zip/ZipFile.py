def add_native_methods(clazz):
    def initIDs____(a0):
        raise NotImplementedError()

    def getEntry__long__byte____boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def freeEntry__long__long__(a0, a1, a2):
        raise NotImplementedError()

    def getNextEntry__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def close__long__(a0, a1):
        raise NotImplementedError()

    def open__java_lang_String__int__long__boolean__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def getTotal__long__(a0, a1):
        raise NotImplementedError()

    def startsWithLOC__long__(a0, a1):
        raise NotImplementedError()

    def read__long__long__long__byte____int__int__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def getEntryTime__long__(a0, a1):
        raise NotImplementedError()

    def getEntryCrc__long__(a0, a1):
        raise NotImplementedError()

    def getEntryCSize__long__(a0, a1):
        raise NotImplementedError()

    def getEntrySize__long__(a0, a1):
        raise NotImplementedError()

    def getEntryMethod__long__(a0, a1):
        raise NotImplementedError()

    def getEntryFlag__long__(a0, a1):
        raise NotImplementedError()

    def getCommentBytes__long__(a0, a1):
        raise NotImplementedError()

    def getEntryBytes__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def getZipMessage__long__(a0, a1):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.getEntry__long__byte____boolean__ = staticmethod(getEntry__long__byte____boolean__)
    clazz.freeEntry__long__long__ = staticmethod(freeEntry__long__long__)
    clazz.getNextEntry__long__int__ = staticmethod(getNextEntry__long__int__)
    clazz.close__long__ = staticmethod(close__long__)
    clazz.open__java_lang_String__int__long__boolean__ = staticmethod(open__java_lang_String__int__long__boolean__)
    clazz.getTotal__long__ = staticmethod(getTotal__long__)
    clazz.startsWithLOC__long__ = staticmethod(startsWithLOC__long__)
    clazz.read__long__long__long__byte____int__int__ = staticmethod(read__long__long__long__byte____int__int__)
    clazz.getEntryTime__long__ = staticmethod(getEntryTime__long__)
    clazz.getEntryCrc__long__ = staticmethod(getEntryCrc__long__)
    clazz.getEntryCSize__long__ = staticmethod(getEntryCSize__long__)
    clazz.getEntrySize__long__ = staticmethod(getEntrySize__long__)
    clazz.getEntryMethod__long__ = staticmethod(getEntryMethod__long__)
    clazz.getEntryFlag__long__ = staticmethod(getEntryFlag__long__)
    clazz.getCommentBytes__long__ = staticmethod(getCommentBytes__long__)
    clazz.getEntryBytes__long__int__ = staticmethod(getEntryBytes__long__int__)
    clazz.getZipMessage__long__ = staticmethod(getZipMessage__long__)

