def add_native_methods(clazz):
    def Transform(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):
        raise NotImplementedError()

    clazz.Transform = Transform

