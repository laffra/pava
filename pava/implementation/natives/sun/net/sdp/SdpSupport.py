def add_native_methods(clazz):
    def create0____(a0):
        raise NotImplementedError()

    def convert0__int__(a0, a1):
        raise NotImplementedError()

    clazz.create0____ = staticmethod(create0____)
    clazz.convert0__int__ = staticmethod(convert0__int__)

