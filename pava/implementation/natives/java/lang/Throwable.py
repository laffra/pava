def add_native_methods(clazz):
    def getStackTraceDepth____(a0):
        raise NotImplementedError()

    def getStackTraceElement__int__(a0, a1):
        raise NotImplementedError()

    clazz.getStackTraceDepth____ = getStackTraceDepth____
    clazz.getStackTraceElement__int__ = getStackTraceElement__int__

