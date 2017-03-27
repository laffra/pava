def add_native_methods(clazz):
    def environmentBlock():
        raise NotImplementedError()

    clazz.environmentBlock = staticmethod(environmentBlock)

