def add_native_methods(clazz):
    def checkConnect__java_io_FileDescriptor__boolean__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def sendOutOfBandData__java_io_FileDescriptor__byte__(a0, a1, a2):
        raise NotImplementedError()

    clazz.checkConnect__java_io_FileDescriptor__boolean__boolean__ = staticmethod(checkConnect__java_io_FileDescriptor__boolean__boolean__)
    clazz.sendOutOfBandData__java_io_FileDescriptor__byte__ = staticmethod(sendOutOfBandData__java_io_FileDescriptor__byte__)

