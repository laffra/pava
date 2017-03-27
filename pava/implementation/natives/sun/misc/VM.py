def add_native_methods(clazz):
    def latestUserDefinedLoader():
        raise NotImplementedError()

    def initialize():
        raise NotImplementedError()

    clazz.latestUserDefinedLoader = staticmethod(latestUserDefinedLoader)
    clazz.initialize = staticmethod(initialize)

