def add_native_methods(clazz):
    def checkConnect(a0, a1, a2):
        raise NotImplementedError()

    def sendOutOfBandData(a0, a1):
        raise NotImplementedError()

    clazz.checkConnect = staticmethod(checkConnect)
    clazz.sendOutOfBandData = staticmethod(sendOutOfBandData)

