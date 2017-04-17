def add_native_methods(clazz):
    def getLower0____():
        raise NotImplementedError()

    def getUpper0____():
        raise NotImplementedError()

    clazz.getLower0____ = staticmethod(getLower0____)
    clazz.getUpper0____ = staticmethod(getUpper0____)

