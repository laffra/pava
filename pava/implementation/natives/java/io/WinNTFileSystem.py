def add_native_methods(clazz):
    def getDriveDirectory(a0):
        raise NotImplementedError()

    def canonicalize0(a0):
        raise NotImplementedError()

    def canonicalizeWithPrefix0(a0, a1):
        raise NotImplementedError()

    def getBooleanAttributes(a0):
        raise NotImplementedError()

    def checkAccess(a0, a1):
        raise NotImplementedError()

    def getLastModifiedTime(a0):
        raise NotImplementedError()

    def getLength(a0):
        raise NotImplementedError()

    def setPermission(a0, a1, a2, a3):
        raise NotImplementedError()

    def createFileExclusively(a0):
        raise NotImplementedError()

    def list(a0):
        raise NotImplementedError()

    def createDirectory(a0):
        raise NotImplementedError()

    def setLastModifiedTime(a0, a1):
        raise NotImplementedError()

    def setReadOnly(a0):
        raise NotImplementedError()

    def delete0(a0):
        raise NotImplementedError()

    def rename0(a0, a1):
        raise NotImplementedError()

    def listRoots0():
        raise NotImplementedError()

    def getSpace0(a0, a1):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.getDriveDirectory = getDriveDirectory
    clazz.canonicalize0 = canonicalize0
    clazz.canonicalizeWithPrefix0 = canonicalizeWithPrefix0
    clazz.getBooleanAttributes = getBooleanAttributes
    clazz.checkAccess = checkAccess
    clazz.getLastModifiedTime = getLastModifiedTime
    clazz.getLength = getLength
    clazz.setPermission = setPermission
    clazz.createFileExclusively = createFileExclusively
    clazz.list = list
    clazz.createDirectory = createDirectory
    clazz.setLastModifiedTime = setLastModifiedTime
    clazz.setReadOnly = setReadOnly
    clazz.delete0 = delete0
    clazz.rename0 = rename0
    clazz.listRoots0 = staticmethod(listRoots0)
    clazz.getSpace0 = getSpace0
    clazz.initIDs = staticmethod(initIDs)

