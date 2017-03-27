def add_native_methods(clazz):
    def nativeObjectInit(a0, a1):
        raise NotImplementedError()

    def nativeNewArray(a0, a1):
        raise NotImplementedError()

    def nativeCallSite(a0, a1, a2):
        raise NotImplementedError()

    def nativeReturnSite(a0, a1, a2):
        raise NotImplementedError()

    clazz.nativeObjectInit = staticmethod(nativeObjectInit)
    clazz.nativeNewArray = staticmethod(nativeNewArray)
    clazz.nativeCallSite = staticmethod(nativeCallSite)
    clazz.nativeReturnSite = staticmethod(nativeReturnSite)

