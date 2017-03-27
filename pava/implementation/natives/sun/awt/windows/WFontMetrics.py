def add_native_methods(clazz):
    def stringWidth(a0):
        raise NotImplementedError()

    def charsWidth(a0, a1, a2):
        raise NotImplementedError()

    def bytesWidth(a0, a1, a2):
        raise NotImplementedError()

    def init():
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.stringWidth = stringWidth
    clazz.charsWidth = charsWidth
    clazz.bytesWidth = bytesWidth
    clazz.init = init
    clazz.initIDs = staticmethod(initIDs)

