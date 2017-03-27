def add_native_methods(clazz):
    def socketWrite0(a0, a1, a2, a3):
        raise NotImplementedError()

    def init():
        raise NotImplementedError()

    clazz.socketWrite0 = socketWrite0
    clazz.init = staticmethod(init)

