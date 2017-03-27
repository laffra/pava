def add_native_methods(clazz):
    def fillInStackTrace(a0):
        raise NotImplementedError()

    def getStackTraceDepth():
        raise NotImplementedError()

    def getStackTraceElement(a0):
        raise NotImplementedError()

    clazz.fillInStackTrace = fillInStackTrace
    clazz.getStackTraceDepth = getStackTraceDepth
    clazz.getStackTraceElement = getStackTraceElement

