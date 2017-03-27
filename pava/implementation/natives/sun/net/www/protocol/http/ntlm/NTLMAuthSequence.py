def add_native_methods(clazz):
    def initFirst(a0):
        raise NotImplementedError()

    def getCredentialsHandle(a0, a1, a2):
        raise NotImplementedError()

    def getNextToken(a0, a1, a2):
        raise NotImplementedError()

    clazz.initFirst = staticmethod(initFirst)
    clazz.getCredentialsHandle = getCredentialsHandle
    clazz.getNextToken = getNextToken

