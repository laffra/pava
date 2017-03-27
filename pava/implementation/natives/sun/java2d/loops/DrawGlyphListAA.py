def add_native_methods(clazz):
    def DrawGlyphListAA(a0, a1, a2):
        raise NotImplementedError()

    clazz.DrawGlyphListAA = DrawGlyphListAA

