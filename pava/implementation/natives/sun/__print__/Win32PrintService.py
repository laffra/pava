def add_native_methods(clazz):
    def getAllMediaIDs(a0, a1):
        raise NotImplementedError()

    def getAllMediaSizes(a0, a1):
        raise NotImplementedError()

    def getAllMediaTrays(a0, a1):
        raise NotImplementedError()

    def getMediaPrintableArea(a0, a1):
        raise NotImplementedError()

    def getAllMediaNames(a0, a1):
        raise NotImplementedError()

    def getAllMediaTrayNames(a0, a1):
        raise NotImplementedError()

    def getCopiesSupported(a0, a1):
        raise NotImplementedError()

    def getAllResolutions(a0, a1):
        raise NotImplementedError()

    def getCapabilities(a0, a1):
        raise NotImplementedError()

    def getDefaultSettings(a0, a1):
        raise NotImplementedError()

    def getJobStatus(a0, a1):
        raise NotImplementedError()

    def getPrinterPort(a0):
        raise NotImplementedError()

    clazz.getAllMediaIDs = getAllMediaIDs
    clazz.getAllMediaSizes = getAllMediaSizes
    clazz.getAllMediaTrays = getAllMediaTrays
    clazz.getMediaPrintableArea = getMediaPrintableArea
    clazz.getAllMediaNames = getAllMediaNames
    clazz.getAllMediaTrayNames = getAllMediaTrayNames
    clazz.getCopiesSupported = getCopiesSupported
    clazz.getAllResolutions = getAllResolutions
    clazz.getCapabilities = getCapabilities
    clazz.getDefaultSettings = getDefaultSettings
    clazz.getJobStatus = getJobStatus
    clazz.getPrinterPort = getPrinterPort

