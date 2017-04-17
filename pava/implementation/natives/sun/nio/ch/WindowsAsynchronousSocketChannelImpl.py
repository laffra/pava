def add_native_methods(clazz):
    def initIDs____(a0):
        raise NotImplementedError()

    def connect0__long__boolean__java_net_InetAddress__int__long__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def updateConnectContext__long__(a0, a1):
        raise NotImplementedError()

    def read0__long__int__long__long__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def write0__long__int__long__long__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def shutdown0__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def closesocket0__long__(a0, a1):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.connect0__long__boolean__java_net_InetAddress__int__long__ = staticmethod(connect0__long__boolean__java_net_InetAddress__int__long__)
    clazz.updateConnectContext__long__ = staticmethod(updateConnectContext__long__)
    clazz.read0__long__int__long__long__ = staticmethod(read0__long__int__long__long__)
    clazz.write0__long__int__long__long__ = staticmethod(write0__long__int__long__long__)
    clazz.shutdown0__long__int__ = staticmethod(shutdown0__long__int__)
    clazz.closesocket0__long__ = staticmethod(closesocket0__long__)

