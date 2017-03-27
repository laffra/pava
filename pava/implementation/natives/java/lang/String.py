def add_native_methods(clazz):
    def intern():
        raise NotImplementedError()

    clazz.intern = intern

