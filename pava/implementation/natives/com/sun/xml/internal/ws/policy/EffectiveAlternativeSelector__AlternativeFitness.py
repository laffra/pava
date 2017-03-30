def add_native_methods(clazz):
    def values():
        raise NotImplementedError()

    def valueOf(a0):
        raise NotImplementedError()

    def combine(a0):
        raise NotImplementedError()

    def __init__(a0, a1, a2):
        raise NotImplementedError()

    clazz.values = staticmethod(values)
    clazz.valueOf = staticmethod(valueOf)
    clazz.combine = combine
    clazz.__init__ = __init__

