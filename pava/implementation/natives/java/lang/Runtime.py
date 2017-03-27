def add_native_methods(clazz):
    def availableProcessors():
        raise NotImplementedError()

    def freeMemory():
        raise NotImplementedError()

    def totalMemory():
        raise NotImplementedError()

    def maxMemory():
        raise NotImplementedError()

    def gc():
        raise NotImplementedError()

    def runFinalization0():
        raise NotImplementedError()

    def traceInstructions(a0):
        raise NotImplementedError()

    def traceMethodCalls(a0):
        raise NotImplementedError()

    clazz.availableProcessors = availableProcessors
    clazz.freeMemory = freeMemory
    clazz.totalMemory = totalMemory
    clazz.maxMemory = maxMemory
    clazz.gc = gc
    clazz.runFinalization0 = staticmethod(runFinalization0)
    clazz.traceInstructions = traceInstructions
    clazz.traceMethodCalls = traceMethodCalls

