def add_native_methods(clazz):
    def getBooleanAttributes__java_io_File__(a0, a1):
        raise NotImplementedError()

    def checkAccess__java_io_File__int__(a0, a1, a2):
        raise NotImplementedError()

    def getLastModifiedTime__java_io_File__(a0, a1):
        raise NotImplementedError()

    def getLength__java_io_File__(a0, a1):
        raise NotImplementedError()

    def setPermission__java_io_File__int__boolean__boolean__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def createFileExclusively__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def list__java_io_File__(a0, a1):
        raise NotImplementedError()

    def createDirectory__java_io_File__(a0, a1):
        raise NotImplementedError()

    def setLastModifiedTime__java_io_File__long__(a0, a1, a2):
        raise NotImplementedError()

    def setReadOnly__java_io_File__(a0, a1):
        raise NotImplementedError()

    clazz.getBooleanAttributes__java_io_File__ = getBooleanAttributes__java_io_File__
    clazz.checkAccess__java_io_File__int__ = checkAccess__java_io_File__int__
    clazz.getLastModifiedTime__java_io_File__ = getLastModifiedTime__java_io_File__
    clazz.getLength__java_io_File__ = getLength__java_io_File__
    clazz.setPermission__java_io_File__int__boolean__boolean__ = setPermission__java_io_File__int__boolean__boolean__
    clazz.createFileExclusively__java_lang_String__ = createFileExclusively__java_lang_String__
    clazz.list__java_io_File__ = list__java_io_File__
    clazz.createDirectory__java_io_File__ = createDirectory__java_io_File__
    clazz.setLastModifiedTime__java_io_File__long__ = setLastModifiedTime__java_io_File__long__
    clazz.setReadOnly__java_io_File__ = setReadOnly__java_io_File__

