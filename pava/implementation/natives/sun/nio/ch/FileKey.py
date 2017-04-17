def add_native_methods(clazz):
    def init__java_io_FileDescriptor__(a0, a1):
        raise NotImplementedError()

    def initIDs____(a0):
        raise NotImplementedError()

    clazz.init__java_io_FileDescriptor__ = init__java_io_FileDescriptor__
    clazz.initIDs____ = staticmethod(initIDs____)

