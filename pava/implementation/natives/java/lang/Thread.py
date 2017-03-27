def add_native_methods(clazz):
    def registerNatives():
        raise NotImplementedError()

    def currentThread():
        raise NotImplementedError()

    def __yield__():
        raise NotImplementedError()

    def sleep(a0):
        raise NotImplementedError()

    def start0():
        raise NotImplementedError()

    def isInterrupted(a0):
        raise NotImplementedError()

    def isAlive():
        raise NotImplementedError()

    def countStackFrames():
        raise NotImplementedError()

    def holdsLock(a0):
        raise NotImplementedError()

    def dumpThreads(a0):
        raise NotImplementedError()

    def getThreads():
        raise NotImplementedError()

    def setPriority0(a0):
        raise NotImplementedError()

    def stop0(a0):
        raise NotImplementedError()

    def suspend0():
        raise NotImplementedError()

    def resume0():
        raise NotImplementedError()

    def interrupt0():
        raise NotImplementedError()

    def setNativeName(a0):
        raise NotImplementedError()

    clazz.registerNatives = staticmethod(registerNatives)
    clazz.currentThread = staticmethod(currentThread)
    clazz.__yield__ = staticmethod(__yield__)
    clazz.sleep = staticmethod(sleep)
    clazz.start0 = start0
    clazz.isInterrupted = isInterrupted
    clazz.isAlive = isAlive
    clazz.countStackFrames = countStackFrames
    clazz.holdsLock = staticmethod(holdsLock)
    clazz.dumpThreads = staticmethod(dumpThreads)
    clazz.getThreads = staticmethod(getThreads)
    clazz.setPriority0 = setPriority0
    clazz.stop0 = stop0
    clazz.suspend0 = suspend0
    clazz.resume0 = resume0
    clazz.interrupt0 = interrupt0
    clazz.setNativeName = setNativeName

