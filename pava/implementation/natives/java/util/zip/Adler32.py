def add_native_methods(clazz):
    def update(a0, a1):
        raise NotImplementedError()

    def updateBytes(a0, a1, a2, a3):
        raise NotImplementedError()

    def updateByteBuffer(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.update = staticmethod(update)
    clazz.updateBytes = staticmethod(updateBytes)
    clazz.updateByteBuffer = staticmethod(updateByteBuffer)

