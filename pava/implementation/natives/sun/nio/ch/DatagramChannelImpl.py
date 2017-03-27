def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def disconnect0(a0, a1):
        raise NotImplementedError()

    def receive0(a0, a1, a2, a3):
        raise NotImplementedError()

    def send0(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.disconnect0 = staticmethod(disconnect0)
    clazz.receive0 = receive0
    clazz.send0 = send0

