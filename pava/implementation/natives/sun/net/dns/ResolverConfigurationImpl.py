def add_native_methods(clazz):
    def init0____():
        raise NotImplementedError()

    def loadDNSconfig0____():
        raise NotImplementedError()

    def notifyAddrChange0____():
        raise NotImplementedError()

    clazz.init0____ = staticmethod(init0____)
    clazz.loadDNSconfig0____ = staticmethod(loadDNSconfig0____)
    clazz.notifyAddrChange0____ = staticmethod(notifyAddrChange0____)

