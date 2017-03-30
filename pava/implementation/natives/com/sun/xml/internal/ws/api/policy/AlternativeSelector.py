def add_native_methods(clazz):
    def __init__():
        raise NotImplementedError()

    clazz.__init__ = __init__

