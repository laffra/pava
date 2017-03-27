def add_native_methods(clazz):
    def startPrintRawData(a0, a1):
        raise NotImplementedError()

    def printRawData(a0, a1):
        raise NotImplementedError()

    def endPrintRawData():
        raise NotImplementedError()

    clazz.startPrintRawData = startPrintRawData
    clazz.printRawData = printRawData
    clazz.endPrintRawData = endPrintRawData

