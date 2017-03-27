def add_native_methods(clazz):
    def retransformClasses0(a0):
        raise NotImplementedError()

    def init():
        raise NotImplementedError()

    clazz.retransformClasses0 = staticmethod(retransformClasses0)
    clazz.init = staticmethod(init)

