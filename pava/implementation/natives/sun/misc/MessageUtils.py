def add_native_methods(clazz):
    def toStderr(a0):
        raise NotImplementedError()

    def toStdout(a0):
        raise NotImplementedError()

    clazz.toStderr = staticmethod(toStderr)
    clazz.toStdout = staticmethod(toStdout)

