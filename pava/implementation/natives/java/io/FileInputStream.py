def add_native_methods(clazz):
    def skip__long__(a0, a1):
        raise NotImplementedError()

    def available____(a0):
        raise NotImplementedError()

    clazz.skip__long__ = skip__long__
    clazz.available____ = available____

