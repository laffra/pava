def add_native_methods(clazz):
    def init(a0, a1):
        raise NotImplementedError()

    def getMechPtr(a0):
        raise NotImplementedError()

    def indicateMechs():
        raise NotImplementedError()

    def inquireNamesForMech():
        raise NotImplementedError()

    def releaseName(a0):
        raise NotImplementedError()

    def importName(a0, a1):
        raise NotImplementedError()

    def compareName(a0, a1):
        raise NotImplementedError()

    def canonicalizeName(a0):
        raise NotImplementedError()

    def exportName(a0):
        raise NotImplementedError()

    def displayName(a0):
        raise NotImplementedError()

    def acquireCred(a0, a1, a2):
        raise NotImplementedError()

    def releaseCred(a0):
        raise NotImplementedError()

    def getCredName(a0):
        raise NotImplementedError()

    def getCredTime(a0):
        raise NotImplementedError()

    def getCredUsage(a0):
        raise NotImplementedError()

    def importContext(a0):
        raise NotImplementedError()

    def initContext(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def acceptContext(a0, a1, a2, a3):
        raise NotImplementedError()

    def inquireContext(a0):
        raise NotImplementedError()

    def getContextMech(a0):
        raise NotImplementedError()

    def getContextName(a0, a1):
        raise NotImplementedError()

    def getContextTime(a0):
        raise NotImplementedError()

    def deleteContext(a0):
        raise NotImplementedError()

    def wrapSizeLimit(a0, a1, a2, a3):
        raise NotImplementedError()

    def exportContext(a0):
        raise NotImplementedError()

    def getMic(a0, a1, a2):
        raise NotImplementedError()

    def verifyMic(a0, a1, a2, a3):
        raise NotImplementedError()

    def wrap(a0, a1, a2):
        raise NotImplementedError()

    def unwrap(a0, a1, a2):
        raise NotImplementedError()

    clazz.init = staticmethod(init)
    clazz.getMechPtr = staticmethod(getMechPtr)
    clazz.indicateMechs = staticmethod(indicateMechs)
    clazz.inquireNamesForMech = inquireNamesForMech
    clazz.releaseName = releaseName
    clazz.importName = importName
    clazz.compareName = compareName
    clazz.canonicalizeName = canonicalizeName
    clazz.exportName = exportName
    clazz.displayName = displayName
    clazz.acquireCred = acquireCred
    clazz.releaseCred = releaseCred
    clazz.getCredName = getCredName
    clazz.getCredTime = getCredTime
    clazz.getCredUsage = getCredUsage
    clazz.importContext = importContext
    clazz.initContext = initContext
    clazz.acceptContext = acceptContext
    clazz.inquireContext = inquireContext
    clazz.getContextMech = getContextMech
    clazz.getContextName = getContextName
    clazz.getContextTime = getContextTime
    clazz.deleteContext = deleteContext
    clazz.wrapSizeLimit = wrapSizeLimit
    clazz.exportContext = exportContext
    clazz.getMic = getMic
    clazz.verifyMic = verifyMic
    clazz.wrap = wrap
    clazz.unwrap = unwrap

