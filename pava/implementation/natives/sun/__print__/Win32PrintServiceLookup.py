def add_native_methods(clazz):
    def getDefaultPrinterName():
        raise NotImplementedError()

    def getAllPrinterNames():
        raise NotImplementedError()

    def notifyFirstPrinterChange(a0):
        raise NotImplementedError()

    def notifyClosePrinterChange(a0):
        raise NotImplementedError()

    def notifyPrinterChange(a0):
        raise NotImplementedError()

    clazz.getDefaultPrinterName = getDefaultPrinterName
    clazz.getAllPrinterNames = getAllPrinterNames
    clazz.notifyFirstPrinterChange = notifyFirstPrinterChange
    clazz.notifyClosePrinterChange = notifyClosePrinterChange
    clazz.notifyPrinterChange = notifyPrinterChange

