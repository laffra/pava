def add_native_methods(clazz):
    def freeStgMedium(a0):
        raise NotImplementedError()

    clazz.freeStgMedium = freeStgMedium

