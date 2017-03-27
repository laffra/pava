def add_native_methods(clazz):
    def readFile(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def writeFile(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def lockFile(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def close0(a0):
        raise NotImplementedError()

    clazz.readFile = staticmethod(readFile)
    clazz.writeFile = staticmethod(writeFile)
    clazz.lockFile = staticmethod(lockFile)
    clazz.close0 = staticmethod(close0)

