def add_native_methods(clazz):
    def startSecondaryEventLoop():
        raise NotImplementedError()

    clazz.startSecondaryEventLoop = startSecondaryEventLoop

