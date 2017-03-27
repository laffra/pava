def add_native_methods(clazz):
    def getStillActive():
        raise NotImplementedError()

    def getExitCodeProcess(a0):
        raise NotImplementedError()

    def waitForInterruptibly(a0):
        raise NotImplementedError()

    def waitForTimeoutInterruptibly(a0, a1):
        raise NotImplementedError()

    def terminateProcess(a0):
        raise NotImplementedError()

    def isProcessAlive(a0):
        raise NotImplementedError()

    def create(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def openForAtomicAppend(a0):
        raise NotImplementedError()

    def closeHandle(a0):
        raise NotImplementedError()

    clazz.getStillActive = staticmethod(getStillActive)
    clazz.getExitCodeProcess = staticmethod(getExitCodeProcess)
    clazz.waitForInterruptibly = staticmethod(waitForInterruptibly)
    clazz.waitForTimeoutInterruptibly = staticmethod(waitForTimeoutInterruptibly)
    clazz.terminateProcess = staticmethod(terminateProcess)
    clazz.isProcessAlive = staticmethod(isProcessAlive)
    clazz.create = staticmethod(create)
    clazz.openForAtomicAppend = staticmethod(openForAtomicAppend)
    clazz.closeHandle = staticmethod(closeHandle)

