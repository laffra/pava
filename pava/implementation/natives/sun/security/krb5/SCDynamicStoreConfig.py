def add_native_methods(clazz):
    def installNotificationCallback():
        raise NotImplementedError()

    def getKerberosConfig():
        raise NotImplementedError()

    clazz.installNotificationCallback = staticmethod(installNotificationCallback)
    clazz.getKerberosConfig = staticmethod(getKerberosConfig)

