def add_native_methods(clazz):
    def setState(a0):
        raise NotImplementedError()

    clazz.setState = setState

