def add_native_methods(clazz):
    def getSystemPackage0__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def getSystemPackages0____(a0):
        raise NotImplementedError()

    clazz.getSystemPackage0__java_lang_String__ = staticmethod(getSystemPackage0__java_lang_String__)
    clazz.getSystemPackages0____ = staticmethod(getSystemPackages0____)

