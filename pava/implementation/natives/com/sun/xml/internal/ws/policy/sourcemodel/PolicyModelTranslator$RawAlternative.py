def add_native_methods(clazz):
    def __init__(a0, a1):
        raise NotImplementedError()

    clazz.__init__ = __init__

