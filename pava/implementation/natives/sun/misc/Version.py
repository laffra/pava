def add_native_methods(clazz):
    def getJvmSpecialVersion():
        raise NotImplementedError()

    def getJdkSpecialVersion():
        raise NotImplementedError()

    def getJvmVersionInfo():
        raise NotImplementedError()

    def getJdkVersionInfo():
        raise NotImplementedError()

    clazz.getJvmSpecialVersion = staticmethod(getJvmSpecialVersion)
    clazz.getJdkSpecialVersion = staticmethod(getJdkSpecialVersion)
    clazz.getJvmVersionInfo = staticmethod(getJvmVersionInfo)
    clazz.getJdkVersionInfo = staticmethod(getJdkVersionInfo)

