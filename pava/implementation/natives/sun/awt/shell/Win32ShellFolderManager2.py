def add_native_methods(clazz):
    def initializeCom____():
        raise NotImplementedError()

    def uninitializeCom____():
        raise NotImplementedError()

    clazz.initializeCom____ = staticmethod(initializeCom____)
    clazz.uninitializeCom____ = staticmethod(uninitializeCom____)

