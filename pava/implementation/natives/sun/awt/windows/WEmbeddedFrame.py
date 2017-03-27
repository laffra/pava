def add_native_methods(clazz):
    def isPrinterDC(a0):
        raise NotImplementedError()

    def printBand(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    def notifyModalBlockedImpl(a0, a1, a2):
        raise NotImplementedError()

    clazz.isPrinterDC = isPrinterDC
    clazz.printBand = printBand
    clazz.initIDs = staticmethod(initIDs)
    clazz.notifyModalBlockedImpl = notifyModalBlockedImpl

