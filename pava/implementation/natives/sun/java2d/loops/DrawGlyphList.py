def add_native_methods(clazz):
    def DrawGlyphList(a0, a1, a2):
        raise NotImplementedError()

    clazz.DrawGlyphList = DrawGlyphList

