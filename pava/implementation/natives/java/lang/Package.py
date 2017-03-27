def add_native_methods(clazz):
    def getSystemPackage0(a0):
        raise NotImplementedError()

    def getSystemPackages0():
        raise NotImplementedError()

    clazz.getSystemPackage0 = staticmethod(getSystemPackage0)
    clazz.getSystemPackages0 = staticmethod(getSystemPackages0)

