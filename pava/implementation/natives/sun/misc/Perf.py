def add_native_methods(clazz):
    def attach(a0, a1, a2):
        raise NotImplementedError()

    def detach(a0):
        raise NotImplementedError()

    def createLong(a0, a1, a2, a3):
        raise NotImplementedError()

    def createByteArray(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def highResCounter():
        raise NotImplementedError()

    def highResFrequency():
        raise NotImplementedError()

    def registerNatives():
        raise NotImplementedError()

    clazz.attach = attach
    clazz.detach = detach
    clazz.createLong = createLong
    clazz.createByteArray = createByteArray
    clazz.highResCounter = highResCounter
    clazz.highResFrequency = highResFrequency
    clazz.registerNatives = staticmethod(registerNatives)

