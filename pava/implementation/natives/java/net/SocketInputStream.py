def add_native_methods(clazz):
    def socketRead0(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def init():
        raise NotImplementedError()

    clazz.socketRead0 = socketRead0
    clazz.init = staticmethod(init)

