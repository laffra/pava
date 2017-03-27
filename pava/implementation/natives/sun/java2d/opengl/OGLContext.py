def add_native_methods(clazz):
    def getOGLIdString():
        raise NotImplementedError()

    clazz.getOGLIdString = staticmethod(getOGLIdString)

