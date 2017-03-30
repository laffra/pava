def add_native_methods(clazz):
    def rejectAlternatives(a0):
        raise NotImplementedError()

    clazz.rejectAlternatives = staticmethod(rejectAlternatives)

