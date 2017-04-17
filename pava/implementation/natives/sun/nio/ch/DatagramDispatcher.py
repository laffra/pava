def add_native_methods(clazz):
    def read0__java_io_FileDescriptor__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def readv0__java_io_FileDescriptor__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def write0__java_io_FileDescriptor__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def writev0__java_io_FileDescriptor__long__int__(a0, a1, a2):
        raise NotImplementedError()

    clazz.read0__java_io_FileDescriptor__long__int__ = staticmethod(read0__java_io_FileDescriptor__long__int__)
    clazz.readv0__java_io_FileDescriptor__long__int__ = staticmethod(readv0__java_io_FileDescriptor__long__int__)
    clazz.write0__java_io_FileDescriptor__long__int__ = staticmethod(write0__java_io_FileDescriptor__long__int__)
    clazz.writev0__java_io_FileDescriptor__long__int__ = staticmethod(writev0__java_io_FileDescriptor__long__int__)

