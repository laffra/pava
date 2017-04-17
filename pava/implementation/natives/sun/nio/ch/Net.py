def add_native_methods(clazz):
    def listen__java_io_FileDescriptor__int__(a0, a1):
        raise NotImplementedError()

    def shutdown__java_io_FileDescriptor__int__(a0, a1):
        raise NotImplementedError()

    def poll__java_io_FileDescriptor__int__long__(a0, a1, a2):
        raise NotImplementedError()

    def blockOrUnblock6__boolean__java_io_FileDescriptor__byte____int__byte____(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def setInterface4__java_io_FileDescriptor__int__(a0, a1):
        raise NotImplementedError()

    def getInterface4__java_io_FileDescriptor__(a0):
        raise NotImplementedError()

    def setInterface6__java_io_FileDescriptor__int__(a0, a1):
        raise NotImplementedError()

    def getInterface6__java_io_FileDescriptor__(a0):
        raise NotImplementedError()

    def pollinValue____():
        raise NotImplementedError()

    def polloutValue____():
        raise NotImplementedError()

    def pollerrValue____():
        raise NotImplementedError()

    def pollhupValue____():
        raise NotImplementedError()

    def pollnvalValue____():
        raise NotImplementedError()

    def pollconnValue____():
        raise NotImplementedError()

    clazz.listen__java_io_FileDescriptor__int__ = staticmethod(listen__java_io_FileDescriptor__int__)
    clazz.shutdown__java_io_FileDescriptor__int__ = staticmethod(shutdown__java_io_FileDescriptor__int__)
    clazz.poll__java_io_FileDescriptor__int__long__ = staticmethod(poll__java_io_FileDescriptor__int__long__)
    clazz.blockOrUnblock6__boolean__java_io_FileDescriptor__byte____int__byte____ = staticmethod(blockOrUnblock6__boolean__java_io_FileDescriptor__byte____int__byte____)
    clazz.setInterface4__java_io_FileDescriptor__int__ = staticmethod(setInterface4__java_io_FileDescriptor__int__)
    clazz.getInterface4__java_io_FileDescriptor__ = staticmethod(getInterface4__java_io_FileDescriptor__)
    clazz.setInterface6__java_io_FileDescriptor__int__ = staticmethod(setInterface6__java_io_FileDescriptor__int__)
    clazz.getInterface6__java_io_FileDescriptor__ = staticmethod(getInterface6__java_io_FileDescriptor__)
    clazz.pollinValue____ = staticmethod(pollinValue____)
    clazz.polloutValue____ = staticmethod(polloutValue____)
    clazz.pollerrValue____ = staticmethod(pollerrValue____)
    clazz.pollhupValue____ = staticmethod(pollhupValue____)
    clazz.pollnvalValue____ = staticmethod(pollnvalValue____)
    clazz.pollconnValue____ = staticmethod(pollconnValue____)

