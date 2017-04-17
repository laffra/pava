def add_native_methods(clazz):
    def initIDs____(a0):
        raise NotImplementedError()

    def disconnect0__java_io_FileDescriptor__boolean__(a0, a1, a2):
        raise NotImplementedError()

    def receive0__java_io_FileDescriptor__long__int__boolean__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def send0__boolean__java_io_FileDescriptor__long__int__java_net_InetAddress__int__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.disconnect0__java_io_FileDescriptor__boolean__ = staticmethod(disconnect0__java_io_FileDescriptor__boolean__)
    clazz.receive0__java_io_FileDescriptor__long__int__boolean__ = receive0__java_io_FileDescriptor__long__int__boolean__
    clazz.send0__boolean__java_io_FileDescriptor__long__int__java_net_InetAddress__int__ = send0__boolean__java_io_FileDescriptor__long__int__java_net_InetAddress__int__

