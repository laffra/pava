def add_native_methods(clazz):
    def toFront____(a0):
        raise NotImplementedError()

    def toBack____(a0):
        raise NotImplementedError()

    clazz.toFront____ = toFront____
    clazz.toBack____ = toBack____

