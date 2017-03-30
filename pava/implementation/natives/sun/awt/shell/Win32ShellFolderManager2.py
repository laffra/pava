def add_native_methods(clazz):
    def initializeCom():
        raise NotImplementedError()

    def uninitializeCom():
        raise NotImplementedError()

    clazz.initializeCom = staticmethod(initializeCom)
    clazz.uninitializeCom = staticmethod(uninitializeCom)

