def add_native_methods(clazz):
    def registerNatives():
        raise NotImplementedError()

    def getInt(a0, a1):
        raise NotImplementedError()

    def putInt(a0, a1, a2):
        raise NotImplementedError()

    def getObject(a0, a1):
        raise NotImplementedError()

    def putObject(a0, a1, a2):
        raise NotImplementedError()

    def getBoolean(a0, a1):
        raise NotImplementedError()

    def putBoolean(a0, a1, a2):
        raise NotImplementedError()

    def getByte(a0, a1):
        raise NotImplementedError()

    def putByte(a0, a1, a2):
        raise NotImplementedError()

    def getShort(a0, a1):
        raise NotImplementedError()

    def putShort(a0, a1, a2):
        raise NotImplementedError()

    def getChar(a0, a1):
        raise NotImplementedError()

    def putChar(a0, a1, a2):
        raise NotImplementedError()

    def getLong(a0, a1):
        raise NotImplementedError()

    def putLong(a0, a1, a2):
        raise NotImplementedError()

    def getFloat(a0, a1):
        raise NotImplementedError()

    def putFloat(a0, a1, a2):
        raise NotImplementedError()

    def getDouble(a0, a1):
        raise NotImplementedError()

    def putDouble(a0, a1, a2):
        raise NotImplementedError()

    def getByte(a0):
        raise NotImplementedError()

    def putByte(a0, a1):
        raise NotImplementedError()

    def getShort(a0):
        raise NotImplementedError()

    def putShort(a0, a1):
        raise NotImplementedError()

    def getChar(a0):
        raise NotImplementedError()

    def putChar(a0, a1):
        raise NotImplementedError()

    def getInt(a0):
        raise NotImplementedError()

    def putInt(a0, a1):
        raise NotImplementedError()

    def getLong(a0):
        raise NotImplementedError()

    def putLong(a0, a1):
        raise NotImplementedError()

    def getFloat(a0):
        raise NotImplementedError()

    def putFloat(a0, a1):
        raise NotImplementedError()

    def getDouble(a0):
        raise NotImplementedError()

    def putDouble(a0, a1):
        raise NotImplementedError()

    def getAddress(a0):
        raise NotImplementedError()

    def putAddress(a0, a1):
        raise NotImplementedError()

    def allocateMemory(a0):
        raise NotImplementedError()

    def reallocateMemory(a0, a1):
        raise NotImplementedError()

    def setMemory(a0, a1, a2, a3):
        raise NotImplementedError()

    def copyMemory(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def freeMemory(a0):
        raise NotImplementedError()

    def staticFieldOffset(a0):
        raise NotImplementedError()

    def objectFieldOffset(a0):
        raise NotImplementedError()

    def staticFieldBase(a0):
        raise NotImplementedError()

    def shouldBeInitialized(a0):
        raise NotImplementedError()

    def ensureClassInitialized(a0):
        raise NotImplementedError()

    def arrayBaseOffset(a0):
        raise NotImplementedError()

    def arrayIndexScale(a0):
        raise NotImplementedError()

    def addressSize():
        raise NotImplementedError()

    def pageSize():
        raise NotImplementedError()

    def defineClass(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def defineAnonymousClass(a0, a1, a2):
        raise NotImplementedError()

    def allocateInstance(a0):
        raise NotImplementedError()

    def monitorEnter(a0):
        raise NotImplementedError()

    def monitorExit(a0):
        raise NotImplementedError()

    def tryMonitorEnter(a0):
        raise NotImplementedError()

    def throwException(a0):
        raise NotImplementedError()

    def compareAndSwapObject(a0, a1, a2, a3):
        raise NotImplementedError()

    def compareAndSwapInt(a0, a1, a2, a3):
        raise NotImplementedError()

    def compareAndSwapLong(a0, a1, a2, a3):
        raise NotImplementedError()

    def getObjectVolatile(a0, a1):
        raise NotImplementedError()

    def putObjectVolatile(a0, a1, a2):
        raise NotImplementedError()

    def getIntVolatile(a0, a1):
        raise NotImplementedError()

    def putIntVolatile(a0, a1, a2):
        raise NotImplementedError()

    def getBooleanVolatile(a0, a1):
        raise NotImplementedError()

    def putBooleanVolatile(a0, a1, a2):
        raise NotImplementedError()

    def getByteVolatile(a0, a1):
        raise NotImplementedError()

    def putByteVolatile(a0, a1, a2):
        raise NotImplementedError()

    def getShortVolatile(a0, a1):
        raise NotImplementedError()

    def putShortVolatile(a0, a1, a2):
        raise NotImplementedError()

    def getCharVolatile(a0, a1):
        raise NotImplementedError()

    def putCharVolatile(a0, a1, a2):
        raise NotImplementedError()

    def getLongVolatile(a0, a1):
        raise NotImplementedError()

    def putLongVolatile(a0, a1, a2):
        raise NotImplementedError()

    def getFloatVolatile(a0, a1):
        raise NotImplementedError()

    def putFloatVolatile(a0, a1, a2):
        raise NotImplementedError()

    def getDoubleVolatile(a0, a1):
        raise NotImplementedError()

    def putDoubleVolatile(a0, a1, a2):
        raise NotImplementedError()

    def putOrderedObject(a0, a1, a2):
        raise NotImplementedError()

    def putOrderedInt(a0, a1, a2):
        raise NotImplementedError()

    def putOrderedLong(a0, a1, a2):
        raise NotImplementedError()

    def unpark(a0):
        raise NotImplementedError()

    def park(a0, a1):
        raise NotImplementedError()

    def getLoadAverage(a0, a1):
        raise NotImplementedError()

    def loadFence():
        raise NotImplementedError()

    def storeFence():
        raise NotImplementedError()

    def fullFence():
        raise NotImplementedError()

    clazz.registerNatives = staticmethod(registerNatives)
    clazz.getInt = getInt
    clazz.putInt = putInt
    clazz.getObject = getObject
    clazz.putObject = putObject
    clazz.getBoolean = getBoolean
    clazz.putBoolean = putBoolean
    clazz.getByte = getByte
    clazz.putByte = putByte
    clazz.getShort = getShort
    clazz.putShort = putShort
    clazz.getChar = getChar
    clazz.putChar = putChar
    clazz.getLong = getLong
    clazz.putLong = putLong
    clazz.getFloat = getFloat
    clazz.putFloat = putFloat
    clazz.getDouble = getDouble
    clazz.putDouble = putDouble
    clazz.getByte = getByte
    clazz.putByte = putByte
    clazz.getShort = getShort
    clazz.putShort = putShort
    clazz.getChar = getChar
    clazz.putChar = putChar
    clazz.getInt = getInt
    clazz.putInt = putInt
    clazz.getLong = getLong
    clazz.putLong = putLong
    clazz.getFloat = getFloat
    clazz.putFloat = putFloat
    clazz.getDouble = getDouble
    clazz.putDouble = putDouble
    clazz.getAddress = getAddress
    clazz.putAddress = putAddress
    clazz.allocateMemory = allocateMemory
    clazz.reallocateMemory = reallocateMemory
    clazz.setMemory = setMemory
    clazz.copyMemory = copyMemory
    clazz.freeMemory = freeMemory
    clazz.staticFieldOffset = staticFieldOffset
    clazz.objectFieldOffset = objectFieldOffset
    clazz.staticFieldBase = staticFieldBase
    clazz.shouldBeInitialized = shouldBeInitialized
    clazz.ensureClassInitialized = ensureClassInitialized
    clazz.arrayBaseOffset = arrayBaseOffset
    clazz.arrayIndexScale = arrayIndexScale
    clazz.addressSize = addressSize
    clazz.pageSize = pageSize
    clazz.defineClass = defineClass
    clazz.defineAnonymousClass = defineAnonymousClass
    clazz.allocateInstance = allocateInstance
    clazz.monitorEnter = monitorEnter
    clazz.monitorExit = monitorExit
    clazz.tryMonitorEnter = tryMonitorEnter
    clazz.throwException = throwException
    clazz.compareAndSwapObject = compareAndSwapObject
    clazz.compareAndSwapInt = compareAndSwapInt
    clazz.compareAndSwapLong = compareAndSwapLong
    clazz.getObjectVolatile = getObjectVolatile
    clazz.putObjectVolatile = putObjectVolatile
    clazz.getIntVolatile = getIntVolatile
    clazz.putIntVolatile = putIntVolatile
    clazz.getBooleanVolatile = getBooleanVolatile
    clazz.putBooleanVolatile = putBooleanVolatile
    clazz.getByteVolatile = getByteVolatile
    clazz.putByteVolatile = putByteVolatile
    clazz.getShortVolatile = getShortVolatile
    clazz.putShortVolatile = putShortVolatile
    clazz.getCharVolatile = getCharVolatile
    clazz.putCharVolatile = putCharVolatile
    clazz.getLongVolatile = getLongVolatile
    clazz.putLongVolatile = putLongVolatile
    clazz.getFloatVolatile = getFloatVolatile
    clazz.putFloatVolatile = putFloatVolatile
    clazz.getDoubleVolatile = getDoubleVolatile
    clazz.putDoubleVolatile = putDoubleVolatile
    clazz.putOrderedObject = putOrderedObject
    clazz.putOrderedInt = putOrderedInt
    clazz.putOrderedLong = putOrderedLong
    clazz.unpark = unpark
    clazz.park = park
    clazz.getLoadAverage = getLoadAverage
    clazz.loadFence = loadFence
    clazz.storeFence = storeFence
    clazz.fullFence = fullFence

