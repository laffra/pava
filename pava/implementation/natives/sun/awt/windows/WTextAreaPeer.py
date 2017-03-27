def add_native_methods(clazz):
    def replaceRange(a0, a1, a2):
        raise NotImplementedError()

    def create(a0):
        raise NotImplementedError()

    clazz.replaceRange = replaceRange
    clazz.create = create

