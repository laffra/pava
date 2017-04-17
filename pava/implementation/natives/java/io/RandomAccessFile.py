def add_native_methods(clazz):
    def getFilePointer____(a0):
        raise NotImplementedError()

    def length____(a0):
        raise NotImplementedError()

    def setLength__long__(a0, a1):
        raise NotImplementedError()

    clazz.getFilePointer____ = getFilePointer____
    clazz.length____ = length____
    clazz.setLength__long__ = setLength__long__

