def add_native_methods(clazz):
    def setWakeupSocket0(a0):
        raise NotImplementedError()

    def resetWakeupSocket0(a0):
        raise NotImplementedError()

    def discardUrgentData(a0):
        raise NotImplementedError()

    clazz.setWakeupSocket0 = setWakeupSocket0
    clazz.resetWakeupSocket0 = resetWakeupSocket0
    clazz.discardUrgentData = discardUrgentData

