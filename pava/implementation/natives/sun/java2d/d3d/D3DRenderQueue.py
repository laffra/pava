def add_native_methods(clazz):
    def flushBuffer(a0, a1, a2):
        raise NotImplementedError()

    clazz.flushBuffer = flushBuffer

