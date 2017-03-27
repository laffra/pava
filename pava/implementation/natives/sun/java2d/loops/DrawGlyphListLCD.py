def add_native_methods(clazz):
    def DrawGlyphListLCD(a0, a1, a2):
        raise NotImplementedError()

    clazz.DrawGlyphListLCD = DrawGlyphListLCD

