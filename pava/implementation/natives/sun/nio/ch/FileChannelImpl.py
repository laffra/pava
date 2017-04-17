def add_native_methods(clazz):
    def map0__int__long__long__(a0, a1, a2, a3):
        raise NotImplementedError()

    def unmap0__long__long__(a0, a1, a2):
        raise NotImplementedError()

    def transferTo0__java_io_FileDescriptor__long__long__java_io_FileDescriptor__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def position0__java_io_FileDescriptor__long__(a0, a1, a2):
        raise NotImplementedError()

    def initIDs____(a0):
        raise NotImplementedError()

    clazz.map0__int__long__long__ = map0__int__long__long__
    clazz.unmap0__long__long__ = staticmethod(unmap0__long__long__)
    clazz.transferTo0__java_io_FileDescriptor__long__long__java_io_FileDescriptor__ = transferTo0__java_io_FileDescriptor__long__long__java_io_FileDescriptor__
    clazz.position0__java_io_FileDescriptor__long__ = position0__java_io_FileDescriptor__long__
    clazz.initIDs____ = staticmethod(initIDs____)

