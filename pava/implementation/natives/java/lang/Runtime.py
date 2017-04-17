def add_native_methods(clazz):
    def availableProcessors____(a0):
        raise NotImplementedError()

    def freeMemory____(a0):
        raise NotImplementedError()

    def totalMemory____(a0):
        raise NotImplementedError()

    def maxMemory____(a0):
        raise NotImplementedError()

    def gc____(a0):
        raise NotImplementedError()

    def traceInstructions__boolean__(a0, a1):
        raise NotImplementedError()

    def traceMethodCalls__boolean__(a0, a1):
        raise NotImplementedError()

    clazz.availableProcessors____ = availableProcessors____
    clazz.freeMemory____ = freeMemory____
    clazz.totalMemory____ = totalMemory____
    clazz.maxMemory____ = maxMemory____
    clazz.gc____ = gc____
    clazz.traceInstructions__boolean__ = traceInstructions__boolean__
    clazz.traceMethodCalls__boolean__ = traceMethodCalls__boolean__

