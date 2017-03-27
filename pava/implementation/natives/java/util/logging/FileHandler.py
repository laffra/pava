def add_native_methods(clazz):
    def isSetUID():
        raise NotImplementedError()

    clazz.isSetUID = staticmethod(isSetUID)

