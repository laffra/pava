def add_native_methods(clazz):
    def getLower0():
        raise NotImplementedError()

    def getUpper0():
        raise NotImplementedError()

    clazz.getLower0 = staticmethod(getLower0)
    clazz.getUpper0 = staticmethod(getUpper0)

