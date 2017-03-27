def add_native_methods(clazz):
    def featuresEnabled0():
        raise NotImplementedError()

    def sampleInterval0():
        raise NotImplementedError()

    def getThreadStats0(a0, a1, a2):
        raise NotImplementedError()

    def getCurrentThreadCPUTime0():
        raise NotImplementedError()

    def getCurrentThreadAllocatedHeap0():
        raise NotImplementedError()

    def createResourceContext0(a0):
        raise NotImplementedError()

    def destroyResourceContext0(a0, a1):
        raise NotImplementedError()

    def setThreadResourceContext0(a0, a1):
        raise NotImplementedError()

    def getThreadResourceContext0(a0):
        raise NotImplementedError()

    def getContextsRetainedMemory0(a0, a1, a2):
        raise NotImplementedError()

    def setRetainedMemoryNotificationEnabled0(a0):
        raise NotImplementedError()

    def computeRetainedMemory0(a0, a1):
        raise NotImplementedError()

    clazz.featuresEnabled0 = staticmethod(featuresEnabled0)
    clazz.sampleInterval0 = staticmethod(sampleInterval0)
    clazz.getThreadStats0 = staticmethod(getThreadStats0)
    clazz.getCurrentThreadCPUTime0 = staticmethod(getCurrentThreadCPUTime0)
    clazz.getCurrentThreadAllocatedHeap0 = staticmethod(getCurrentThreadAllocatedHeap0)
    clazz.createResourceContext0 = staticmethod(createResourceContext0)
    clazz.destroyResourceContext0 = staticmethod(destroyResourceContext0)
    clazz.setThreadResourceContext0 = staticmethod(setThreadResourceContext0)
    clazz.getThreadResourceContext0 = staticmethod(getThreadResourceContext0)
    clazz.getContextsRetainedMemory0 = staticmethod(getContextsRetainedMemory0)
    clazz.setRetainedMemoryNotificationEnabled0 = staticmethod(setRetainedMemoryNotificationEnabled0)
    clazz.computeRetainedMemory0 = staticmethod(computeRetainedMemory0)

