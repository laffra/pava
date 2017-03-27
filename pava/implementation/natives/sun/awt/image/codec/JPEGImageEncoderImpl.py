def add_native_methods(clazz):
    def initEncoder(a0):
        raise NotImplementedError()

    def writeJPEGStream(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    clazz.initEncoder = initEncoder
    clazz.writeJPEGStream = writeJPEGStream

