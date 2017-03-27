def add_native_methods(clazz):
    def DrawParallelogram(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        raise NotImplementedError()

    clazz.DrawParallelogram = DrawParallelogram

