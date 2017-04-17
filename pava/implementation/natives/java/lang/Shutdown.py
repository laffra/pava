def add_native_methods(clazz):
    def halt0__int__(a0):
        raise NotImplementedError()

    clazz.halt0__int__ = staticmethod(halt0__int__)

