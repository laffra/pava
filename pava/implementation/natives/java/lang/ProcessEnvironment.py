def add_native_methods(clazz):
    def environmentBlock____(a0):
        raise NotImplementedError()

    clazz.environmentBlock____ = staticmethod(environmentBlock____)

