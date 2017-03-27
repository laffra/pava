def add_native_methods(clazz):
    def maskFill(a0, a1, a2, a3, a4, a5, a6, a7):
        raise NotImplementedError()

    clazz.maskFill = maskFill

