def add_native_methods(clazz):
    def setWakeupSocket0__int__(a0, a1):
        raise NotImplementedError()

    def resetWakeupSocket0__int__(a0, a1):
        raise NotImplementedError()

    def discardUrgentData__int__(a0, a1):
        raise NotImplementedError()

    clazz.setWakeupSocket0__int__ = setWakeupSocket0__int__
    clazz.resetWakeupSocket0__int__ = resetWakeupSocket0__int__
    clazz.discardUrgentData__int__ = discardUrgentData__int__

