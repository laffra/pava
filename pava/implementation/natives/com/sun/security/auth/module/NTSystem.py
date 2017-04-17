def add_native_methods(clazz):
    def getCurrent__boolean__(a0, a1):
        raise NotImplementedError()

    def getImpersonationToken0____(a0):
        raise NotImplementedError()

    clazz.getCurrent__boolean__ = getCurrent__boolean__
    clazz.getImpersonationToken0____ = getImpersonationToken0____

