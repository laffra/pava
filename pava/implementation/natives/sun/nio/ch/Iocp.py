def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def createIoCompletionPort(a0, a1, a2, a3):
        raise NotImplementedError()

    def close0(a0):
        raise NotImplementedError()

    def getQueuedCompletionStatus(a0, a1):
        raise NotImplementedError()

    def postQueuedCompletionStatus(a0, a1):
        raise NotImplementedError()

    def getErrorMessage(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.createIoCompletionPort = staticmethod(createIoCompletionPort)
    clazz.close0 = staticmethod(close0)
    clazz.getQueuedCompletionStatus = staticmethod(getQueuedCompletionStatus)
    clazz.postQueuedCompletionStatus = staticmethod(postQueuedCompletionStatus)
    clazz.getErrorMessage = staticmethod(getErrorMessage)

