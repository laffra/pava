def add_native_methods(clazz):
    def FillRect(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    clazz.FillRect = FillRect

