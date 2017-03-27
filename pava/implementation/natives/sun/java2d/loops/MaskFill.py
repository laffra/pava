def add_native_methods(clazz):
    def MaskFill(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        raise NotImplementedError()

    def FillAAPgram(a0, a1, a2, a3, a4, a5, a6, a7, a8):
        raise NotImplementedError()

    def DrawAAPgram(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
        raise NotImplementedError()

    clazz.MaskFill = MaskFill
    clazz.FillAAPgram = FillAAPgram
    clazz.DrawAAPgram = DrawAAPgram

