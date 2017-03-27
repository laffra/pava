def add_native_methods(clazz):
    def read0(a0, a1, a2):
        raise NotImplementedError()

    def readv0(a0, a1, a2):
        raise NotImplementedError()

    def write0(a0, a1, a2):
        raise NotImplementedError()

    def writev0(a0, a1, a2):
        raise NotImplementedError()

    clazz.read0 = staticmethod(read0)
    clazz.readv0 = staticmethod(readv0)
    clazz.write0 = staticmethod(write0)
    clazz.writev0 = staticmethod(writev0)

