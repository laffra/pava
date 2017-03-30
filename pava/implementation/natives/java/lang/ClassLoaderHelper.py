def add_native_methods(clazz):
    def mapAlternativeName(a0):
        raise NotImplementedError()

    clazz.mapAlternativeName = staticmethod(mapAlternativeName)

