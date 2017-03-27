def add_native_methods(clazz):
    def nGetFormats(a0, a1, a2, a3):
        raise NotImplementedError()

    def nOpen(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
        raise NotImplementedError()

    def nStart(a0, a1):
        raise NotImplementedError()

    def nStop(a0, a1):
        raise NotImplementedError()

    def nClose(a0, a1):
        raise NotImplementedError()

    def nWrite(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def nRead(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def nGetBufferSize(a0, a1):
        raise NotImplementedError()

    def nIsStillDraining(a0, a1):
        raise NotImplementedError()

    def nFlush(a0, a1):
        raise NotImplementedError()

    def nAvailable(a0, a1):
        raise NotImplementedError()

    def nGetBytePosition(a0, a1, a2):
        raise NotImplementedError()

    def nSetBytePosition(a0, a1, a2):
        raise NotImplementedError()

    def nRequiresServicing(a0, a1):
        raise NotImplementedError()

    def nService(a0, a1):
        raise NotImplementedError()

    clazz.nGetFormats = staticmethod(nGetFormats)
    clazz.nOpen = staticmethod(nOpen)
    clazz.nStart = staticmethod(nStart)
    clazz.nStop = staticmethod(nStop)
    clazz.nClose = staticmethod(nClose)
    clazz.nWrite = staticmethod(nWrite)
    clazz.nRead = staticmethod(nRead)
    clazz.nGetBufferSize = staticmethod(nGetBufferSize)
    clazz.nIsStillDraining = staticmethod(nIsStillDraining)
    clazz.nFlush = staticmethod(nFlush)
    clazz.nAvailable = staticmethod(nAvailable)
    clazz.nGetBytePosition = staticmethod(nGetBytePosition)
    clazz.nSetBytePosition = staticmethod(nSetBytePosition)
    clazz.nRequiresServicing = staticmethod(nRequiresServicing)
    clazz.nService = staticmethod(nService)

