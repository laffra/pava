def add_native_methods(clazz):
    def getCurrent(a0):
        raise NotImplementedError()

    def getImpersonationToken0():
        raise NotImplementedError()

    clazz.getCurrent = getCurrent
    clazz.getImpersonationToken0 = getImpersonationToken0

