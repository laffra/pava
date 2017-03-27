def add_native_methods(clazz):
    def setVerboseClass(a0):
        raise NotImplementedError()

    clazz.setVerboseClass = staticmethod(setVerboseClass)

