def add_native_methods(clazz):
    def installNotificationCallback____(a0):
        raise NotImplementedError()

    def getKerberosConfig____(a0):
        raise NotImplementedError()

    clazz.installNotificationCallback____ = staticmethod(installNotificationCallback____)
    clazz.getKerberosConfig____ = staticmethod(getKerberosConfig____)

