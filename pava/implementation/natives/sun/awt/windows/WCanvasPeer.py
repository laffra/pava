def add_native_methods(clazz):
    def create(a0):
        raise NotImplementedError()

    def setNativeBackgroundErase(a0, a1):
        raise NotImplementedError()

    clazz.create = create
    clazz.setNativeBackgroundErase = setNativeBackgroundErase

