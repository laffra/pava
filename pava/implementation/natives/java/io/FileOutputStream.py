def add_native_methods(clazz):
    def open0(a0, a1):
        raise NotImplementedError()

    def write(a0, a1):
        raise NotImplementedError()

    def writeBytes(a0, a1, a2, a3):
        raise NotImplementedError()

    def close0():
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.open0 = open0
    clazz.write = write
    clazz.writeBytes = writeBytes
    clazz.close0 = close0
    clazz.initIDs = staticmethod(initIDs)

