def add_native_methods(clazz):
    def init():
        raise NotImplementedError()

    clazz.init = staticmethod(init)

