def add_native_methods(clazz):
    def registerNatives():
        raise NotImplementedError()

    def getClass():
        raise NotImplementedError()

    def hashCode():
        raise NotImplementedError()

    def clone():
        raise NotImplementedError()

    def notify():
        raise NotImplementedError()

    def notifyAll():
        raise NotImplementedError()

    def wait(a0):
        raise NotImplementedError()

    clazz.registerNatives = staticmethod(registerNatives)
    clazz.getClass = getClass
    clazz.hashCode = hashCode
    clazz.clone = clone
    clazz.notify = notify
    clazz.notifyAll = notifyAll
    clazz.wait = wait

