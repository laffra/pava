def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def initDesktop():
        raise NotImplementedError()

    def initSpecial(a0, a1):
        raise NotImplementedError()

    def getNextPIDLEntry(a0):
        raise NotImplementedError()

    def copyFirstPIDLEntry(a0):
        raise NotImplementedError()

    def combinePIDLs(a0, a1):
        raise NotImplementedError()

    def releasePIDL(a0):
        raise NotImplementedError()

    def releaseIShellFolder(a0):
        raise NotImplementedError()

    def compareIDs(a0, a1, a2):
        raise NotImplementedError()

    def getAttributes0(a0, a1, a2):
        raise NotImplementedError()

    def getFileSystemPath0(a0):
        raise NotImplementedError()

    def getEnumObjects(a0, a1, a2):
        raise NotImplementedError()

    def getNextChild(a0):
        raise NotImplementedError()

    def releaseEnumObjects(a0):
        raise NotImplementedError()

    def bindToObject(a0, a1):
        raise NotImplementedError()

    def getLinkLocation(a0, a1, a2):
        raise NotImplementedError()

    def parseDisplayName0(a0, a1):
        raise NotImplementedError()

    def getDisplayNameOf(a0, a1, a2):
        raise NotImplementedError()

    def getFolderType(a0):
        raise NotImplementedError()

    def getExecutableType(a0):
        raise NotImplementedError()

    def getIShellIcon(a0):
        raise NotImplementedError()

    def getIconIndex(a0, a1):
        raise NotImplementedError()

    def getIcon(a0, a1):
        raise NotImplementedError()

    def extractIcon(a0, a1, a2):
        raise NotImplementedError()

    def getSystemIcon(a0):
        raise NotImplementedError()

    def getIconResource(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def getIconBits(a0, a1):
        raise NotImplementedError()

    def disposeIcon(a0):
        raise NotImplementedError()

    def getStandardViewButton0(a0):
        raise NotImplementedError()

    def doGetColumnInfo(a0):
        raise NotImplementedError()

    def doGetColumnValue(a0, a1, a2):
        raise NotImplementedError()

    def compareIDsByColumn(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.initDesktop = initDesktop
    clazz.initSpecial = initSpecial
    clazz.getNextPIDLEntry = staticmethod(getNextPIDLEntry)
    clazz.copyFirstPIDLEntry = staticmethod(copyFirstPIDLEntry)
    clazz.combinePIDLs = staticmethod(combinePIDLs)
    clazz.releasePIDL = staticmethod(releasePIDL)
    clazz.releaseIShellFolder = staticmethod(releaseIShellFolder)
    clazz.compareIDs = staticmethod(compareIDs)
    clazz.getAttributes0 = staticmethod(getAttributes0)
    clazz.getFileSystemPath0 = staticmethod(getFileSystemPath0)
    clazz.getEnumObjects = getEnumObjects
    clazz.getNextChild = getNextChild
    clazz.releaseEnumObjects = releaseEnumObjects
    clazz.bindToObject = staticmethod(bindToObject)
    clazz.getLinkLocation = staticmethod(getLinkLocation)
    clazz.parseDisplayName0 = staticmethod(parseDisplayName0)
    clazz.getDisplayNameOf = staticmethod(getDisplayNameOf)
    clazz.getFolderType = staticmethod(getFolderType)
    clazz.getExecutableType = getExecutableType
    clazz.getIShellIcon = staticmethod(getIShellIcon)
    clazz.getIconIndex = staticmethod(getIconIndex)
    clazz.getIcon = staticmethod(getIcon)
    clazz.extractIcon = staticmethod(extractIcon)
    clazz.getSystemIcon = staticmethod(getSystemIcon)
    clazz.getIconResource = staticmethod(getIconResource)
    clazz.getIconBits = staticmethod(getIconBits)
    clazz.disposeIcon = staticmethod(disposeIcon)
    clazz.getStandardViewButton0 = staticmethod(getStandardViewButton0)
    clazz.doGetColumnInfo = doGetColumnInfo
    clazz.doGetColumnValue = doGetColumnValue
    clazz.compareIDsByColumn = staticmethod(compareIDsByColumn)

