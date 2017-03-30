def add_native_methods(clazz):
    def create_native_tc(a0, a1):
        raise NotImplementedError()

    clazz.create_native_tc = create_native_tc

