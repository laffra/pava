def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def start(a0, a1):
        raise NotImplementedError()

    def getNextFile(a0):
        raise NotImplementedError()

    def getUnusedInput():
        raise NotImplementedError()

    def finish():
        raise NotImplementedError()

    def setOption(a0, a1):
        raise NotImplementedError()

    def getOption(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.start = start
    clazz.getNextFile = getNextFile
    clazz.getUnusedInput = getUnusedInput
    clazz.finish = finish
    clazz.setOption = setOption
    clazz.getOption = getOption

