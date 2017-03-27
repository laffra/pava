def add_native_methods(clazz):
    def create(a0):
        raise NotImplementedError()

    def getBoundsPrivate():
        raise NotImplementedError()

    clazz.create = create
    clazz.getBoundsPrivate = getBoundsPrivate

