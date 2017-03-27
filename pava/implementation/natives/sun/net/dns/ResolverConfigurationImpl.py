def add_native_methods(clazz):
    def init0():
        raise NotImplementedError()

    def loadDNSconfig0():
        raise NotImplementedError()

    def notifyAddrChange0():
        raise NotImplementedError()

    clazz.init0 = staticmethod(init0)
    clazz.loadDNSconfig0 = staticmethod(loadDNSconfig0)
    clazz.notifyAddrChange0 = staticmethod(notifyAddrChange0)

