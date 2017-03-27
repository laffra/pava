def add_native_methods(clazz):
    def getCallerClass():
        raise NotImplementedError()

    def getCallerClass(a0):
        raise NotImplementedError()

    def getClassAccessFlags(a0):
        raise NotImplementedError()

    clazz.getCallerClass = staticmethod(getCallerClass)
    clazz.getCallerClass = staticmethod(getCallerClass)
    clazz.getClassAccessFlags = staticmethod(getClassAccessFlags)

