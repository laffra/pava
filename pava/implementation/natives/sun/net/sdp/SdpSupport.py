def add_native_methods(clazz):
    def create0():
        raise NotImplementedError()

    def convert0(a0):
        raise NotImplementedError()

    clazz.create0 = staticmethod(create0)
    clazz.convert0 = staticmethod(convert0)

