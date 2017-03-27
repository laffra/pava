def add_native_methods(clazz):
    def getLength(a0):
        raise NotImplementedError()

    def get(a0, a1):
        raise NotImplementedError()

    def getBoolean(a0, a1):
        raise NotImplementedError()

    def getByte(a0, a1):
        raise NotImplementedError()

    def getChar(a0, a1):
        raise NotImplementedError()

    def getShort(a0, a1):
        raise NotImplementedError()

    def getInt(a0, a1):
        raise NotImplementedError()

    def getLong(a0, a1):
        raise NotImplementedError()

    def getFloat(a0, a1):
        raise NotImplementedError()

    def getDouble(a0, a1):
        raise NotImplementedError()

    def __set__(a0, a1, a2):
        raise NotImplementedError()

    def setBoolean(a0, a1, a2):
        raise NotImplementedError()

    def setByte(a0, a1, a2):
        raise NotImplementedError()

    def setChar(a0, a1, a2):
        raise NotImplementedError()

    def setShort(a0, a1, a2):
        raise NotImplementedError()

    def setInt(a0, a1, a2):
        raise NotImplementedError()

    def setLong(a0, a1, a2):
        raise NotImplementedError()

    def setFloat(a0, a1, a2):
        raise NotImplementedError()

    def setDouble(a0, a1, a2):
        raise NotImplementedError()

    def newArray(a0, a1):
        raise NotImplementedError()

    def multiNewArray(a0, a1):
        raise NotImplementedError()

    clazz.getLength = staticmethod(getLength)
    clazz.get = staticmethod(get)
    clazz.getBoolean = staticmethod(getBoolean)
    clazz.getByte = staticmethod(getByte)
    clazz.getChar = staticmethod(getChar)
    clazz.getShort = staticmethod(getShort)
    clazz.getInt = staticmethod(getInt)
    clazz.getLong = staticmethod(getLong)
    clazz.getFloat = staticmethod(getFloat)
    clazz.getDouble = staticmethod(getDouble)
    clazz.__set__ = staticmethod(__set__)
    clazz.setBoolean = staticmethod(setBoolean)
    clazz.setByte = staticmethod(setByte)
    clazz.setChar = staticmethod(setChar)
    clazz.setShort = staticmethod(setShort)
    clazz.setInt = staticmethod(setInt)
    clazz.setLong = staticmethod(setLong)
    clazz.setFloat = staticmethod(setFloat)
    clazz.setDouble = staticmethod(setDouble)
    clazz.newArray = staticmethod(newArray)
    clazz.multiNewArray = staticmethod(multiNewArray)

