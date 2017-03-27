def add_native_methods(clazz):
    def open0(a0, a1):
        raise NotImplementedError()

    def read0():
        raise NotImplementedError()

    def readBytes(a0, a1, a2):
        raise NotImplementedError()

    def write0(a0):
        raise NotImplementedError()

    def writeBytes(a0, a1, a2):
        raise NotImplementedError()

    def getFilePointer():
        raise NotImplementedError()

    def seek0(a0):
        raise NotImplementedError()

    def length():
        raise NotImplementedError()

    def setLength(a0):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    def close0():
        raise NotImplementedError()

    clazz.open0 = open0
    clazz.read0 = read0
    clazz.readBytes = readBytes
    clazz.write0 = write0
    clazz.writeBytes = writeBytes
    clazz.getFilePointer = getFilePointer
    clazz.seek0 = seek0
    clazz.length = length
    clazz.setLength = setLength
    clazz.initIDs = staticmethod(initIDs)
    clazz.close0 = close0

