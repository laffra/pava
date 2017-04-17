def add_native_methods(clazz):
    def getDefaultPrinterName____(a0):
        raise NotImplementedError()

    def getAllPrinterNames____(a0):
        raise NotImplementedError()

    def notifyFirstPrinterChange__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def notifyClosePrinterChange__long__(a0, a1):
        raise NotImplementedError()

    def notifyPrinterChange__long__(a0, a1):
        raise NotImplementedError()

    clazz.getDefaultPrinterName____ = getDefaultPrinterName____
    clazz.getAllPrinterNames____ = getAllPrinterNames____
    clazz.notifyFirstPrinterChange__java_lang_String__ = notifyFirstPrinterChange__java_lang_String__
    clazz.notifyClosePrinterChange__long__ = notifyClosePrinterChange__long__
    clazz.notifyPrinterChange__long__ = notifyPrinterChange__long__

