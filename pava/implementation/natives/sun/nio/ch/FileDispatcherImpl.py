def add_native_methods(clazz):
    def read0(a0, a1, a2):
        raise NotImplementedError()

    def pread0(a0, a1, a2, a3):
        raise NotImplementedError()

    def readv0(a0, a1, a2):
        raise NotImplementedError()

    def write0(a0, a1, a2, a3):
        raise NotImplementedError()

    def pwrite0(a0, a1, a2, a3):
        raise NotImplementedError()

    def writev0(a0, a1, a2, a3):
        raise NotImplementedError()

    def force0(a0, a1):
        raise NotImplementedError()

    def truncate0(a0, a1):
        raise NotImplementedError()

    def size0(a0):
        raise NotImplementedError()

    def lock0(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def release0(a0, a1, a2):
        raise NotImplementedError()

    def close0(a0):
        raise NotImplementedError()

    def closeByHandle(a0):
        raise NotImplementedError()

    def duplicateHandle(a0):
        raise NotImplementedError()

    clazz.read0 = staticmethod(read0)
    clazz.pread0 = staticmethod(pread0)
    clazz.readv0 = staticmethod(readv0)
    clazz.write0 = staticmethod(write0)
    clazz.pwrite0 = staticmethod(pwrite0)
    clazz.writev0 = staticmethod(writev0)
    clazz.force0 = staticmethod(force0)
    clazz.truncate0 = staticmethod(truncate0)
    clazz.size0 = staticmethod(size0)
    clazz.lock0 = staticmethod(lock0)
    clazz.release0 = staticmethod(release0)
    clazz.close0 = staticmethod(close0)
    clazz.closeByHandle = staticmethod(closeByHandle)
    clazz.duplicateHandle = staticmethod(duplicateHandle)

