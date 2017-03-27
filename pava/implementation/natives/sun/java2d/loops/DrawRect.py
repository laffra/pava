def add_native_methods(clazz):
    def DrawRect(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    clazz.DrawRect = DrawRect

