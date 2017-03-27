def add_native_methods(clazz):
    def init():
        raise NotImplementedError()

    def getSystemProxy(a0, a1):
        raise NotImplementedError()

    clazz.init = staticmethod(init)
    clazz.getSystemProxy = getSystemProxy

