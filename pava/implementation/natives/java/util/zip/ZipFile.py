def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def getEntry(a0, a1, a2):
        raise NotImplementedError()

    def freeEntry(a0, a1):
        raise NotImplementedError()

    def getNextEntry(a0, a1):
        raise NotImplementedError()

    def close(a0):
        raise NotImplementedError()

    def open(a0, a1, a2, a3):
        raise NotImplementedError()

    def getTotal(a0):
        raise NotImplementedError()

    def startsWithLOC(a0):
        raise NotImplementedError()

    def read(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def getEntryTime(a0):
        raise NotImplementedError()

    def getEntryCrc(a0):
        raise NotImplementedError()

    def getEntryCSize(a0):
        raise NotImplementedError()

    def getEntrySize(a0):
        raise NotImplementedError()

    def getEntryMethod(a0):
        raise NotImplementedError()

    def getEntryFlag(a0):
        raise NotImplementedError()

    def getCommentBytes(a0):
        raise NotImplementedError()

    def getEntryBytes(a0, a1):
        raise NotImplementedError()

    def getZipMessage(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.getEntry = staticmethod(getEntry)
    clazz.freeEntry = staticmethod(freeEntry)
    clazz.getNextEntry = staticmethod(getNextEntry)
    clazz.close = staticmethod(close)
    clazz.open = staticmethod(open)
    clazz.getTotal = staticmethod(getTotal)
    clazz.startsWithLOC = staticmethod(startsWithLOC)
    clazz.read = staticmethod(read)
    clazz.getEntryTime = staticmethod(getEntryTime)
    clazz.getEntryCrc = staticmethod(getEntryCrc)
    clazz.getEntryCSize = staticmethod(getEntryCSize)
    clazz.getEntrySize = staticmethod(getEntrySize)
    clazz.getEntryMethod = staticmethod(getEntryMethod)
    clazz.getEntryFlag = staticmethod(getEntryFlag)
    clazz.getCommentBytes = staticmethod(getCommentBytes)
    clazz.getEntryBytes = staticmethod(getEntryBytes)
    clazz.getZipMessage = staticmethod(getZipMessage)

