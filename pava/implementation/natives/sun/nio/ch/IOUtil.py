def add_native_methods(clazz):
    def randomBytes__byte____(a0):
        raise NotImplementedError()

    def makePipe__boolean__(a0):
        raise NotImplementedError()

    def drain__int__(a0):
        raise NotImplementedError()

    def configureBlocking__java_io_FileDescriptor__boolean__(a0, a1):
        raise NotImplementedError()

    def fdVal__java_io_FileDescriptor__(a0):
        raise NotImplementedError()

    def setfdVal__java_io_FileDescriptor__int__(a0, a1):
        raise NotImplementedError()

    def fdLimit____():
        raise NotImplementedError()

    def iovMax____():
        raise NotImplementedError()

    def initIDs____():
        raise NotImplementedError()

    clazz.randomBytes__byte____ = staticmethod(randomBytes__byte____)
    clazz.makePipe__boolean__ = staticmethod(makePipe__boolean__)
    clazz.drain__int__ = staticmethod(drain__int__)
    clazz.configureBlocking__java_io_FileDescriptor__boolean__ = staticmethod(configureBlocking__java_io_FileDescriptor__boolean__)
    clazz.fdVal__java_io_FileDescriptor__ = staticmethod(fdVal__java_io_FileDescriptor__)
    clazz.setfdVal__java_io_FileDescriptor__int__ = staticmethod(setfdVal__java_io_FileDescriptor__int__)
    clazz.fdLimit____ = staticmethod(fdLimit____)
    clazz.iovMax____ = staticmethod(iovMax____)
    clazz.initIDs____ = staticmethod(initIDs____)

