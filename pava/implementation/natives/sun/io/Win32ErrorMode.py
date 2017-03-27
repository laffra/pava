def add_native_methods(clazz):
    def setErrorMode(a0):
        raise NotImplementedError()

    clazz.setErrorMode = staticmethod(setErrorMode)

