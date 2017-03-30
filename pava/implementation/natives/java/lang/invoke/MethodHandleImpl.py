def add_native_methods(clazz):
    def selectAlternative(a0, a1, a2):
        raise NotImplementedError()

    clazz.selectAlternative = staticmethod(selectAlternative)

