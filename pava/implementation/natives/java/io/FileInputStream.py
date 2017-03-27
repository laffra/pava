def add_native_methods(clazz):
    def open0(a0):
        raise NotImplementedError()

    def read0():
        raise NotImplementedError()

    def readBytes(a0, a1, a2):
        raise NotImplementedError()

    def skip(a0):
        raise NotImplementedError()

    def available():
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    def close0():
        raise NotImplementedError()

    clazz.open0 = open0
    clazz.read0 = read0
    clazz.readBytes = readBytes
    clazz.skip = skip
    clazz.available = available
    clazz.initIDs = staticmethod(initIDs)
    clazz.close0 = close0

