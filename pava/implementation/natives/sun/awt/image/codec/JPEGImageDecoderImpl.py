def add_native_methods(clazz):
    def initDecoder(a0):
        raise NotImplementedError()

    def readJPEGStream(a0, a1, a2):
        raise NotImplementedError()

    clazz.initDecoder = initDecoder
    clazz.readJPEGStream = readJPEGStream

