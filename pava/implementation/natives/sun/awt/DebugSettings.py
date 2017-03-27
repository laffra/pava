def add_native_methods(clazz):
    def setCTracingOn(a0):
        raise NotImplementedError()

    def setCTracingOn(a0, a1):
        raise NotImplementedError()

    def setCTracingOn(a0, a1, a2):
        raise NotImplementedError()

    clazz.setCTracingOn = setCTracingOn
    clazz.setCTracingOn = setCTracingOn
    clazz.setCTracingOn = setCTracingOn

