def add_native_methods(clazz):
    def read0__java_io_FileDescriptor__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def pread0__java_io_FileDescriptor__long__int__long__(a0, a1, a2, a3):
        raise NotImplementedError()

    def readv0__java_io_FileDescriptor__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def write0__java_io_FileDescriptor__long__int__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def pwrite0__java_io_FileDescriptor__long__int__long__(a0, a1, a2, a3):
        raise NotImplementedError()

    def writev0__java_io_FileDescriptor__long__int__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def force0__java_io_FileDescriptor__boolean__(a0, a1):
        raise NotImplementedError()

    def truncate0__java_io_FileDescriptor__long__(a0, a1):
        raise NotImplementedError()

    def size0__java_io_FileDescriptor__(a0):
        raise NotImplementedError()

    def lock0__java_io_FileDescriptor__boolean__long__long__boolean__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def release0__java_io_FileDescriptor__long__long__(a0, a1, a2):
        raise NotImplementedError()

    def close0__java_io_FileDescriptor__(a0):
        raise NotImplementedError()

    def closeByHandle__long__(a0):
        raise NotImplementedError()

    def duplicateHandle__long__(a0):
        raise NotImplementedError()

    clazz.read0__java_io_FileDescriptor__long__int__ = staticmethod(read0__java_io_FileDescriptor__long__int__)
    clazz.pread0__java_io_FileDescriptor__long__int__long__ = staticmethod(pread0__java_io_FileDescriptor__long__int__long__)
    clazz.readv0__java_io_FileDescriptor__long__int__ = staticmethod(readv0__java_io_FileDescriptor__long__int__)
    clazz.write0__java_io_FileDescriptor__long__int__boolean__ = staticmethod(write0__java_io_FileDescriptor__long__int__boolean__)
    clazz.pwrite0__java_io_FileDescriptor__long__int__long__ = staticmethod(pwrite0__java_io_FileDescriptor__long__int__long__)
    clazz.writev0__java_io_FileDescriptor__long__int__boolean__ = staticmethod(writev0__java_io_FileDescriptor__long__int__boolean__)
    clazz.force0__java_io_FileDescriptor__boolean__ = staticmethod(force0__java_io_FileDescriptor__boolean__)
    clazz.truncate0__java_io_FileDescriptor__long__ = staticmethod(truncate0__java_io_FileDescriptor__long__)
    clazz.size0__java_io_FileDescriptor__ = staticmethod(size0__java_io_FileDescriptor__)
    clazz.lock0__java_io_FileDescriptor__boolean__long__long__boolean__ = staticmethod(lock0__java_io_FileDescriptor__boolean__long__long__boolean__)
    clazz.release0__java_io_FileDescriptor__long__long__ = staticmethod(release0__java_io_FileDescriptor__long__long__)
    clazz.close0__java_io_FileDescriptor__ = staticmethod(close0__java_io_FileDescriptor__)
    clazz.closeByHandle__long__ = staticmethod(closeByHandle__long__)
    clazz.duplicateHandle__long__ = staticmethod(duplicateHandle__long__)

