def add_native_methods(clazz):
    def halt0(a0):
        raise NotImplementedError()

    def runAllFinalizers():
        raise NotImplementedError()

    clazz.halt0 = staticmethod(halt0)
    clazz.runAllFinalizers = staticmethod(runAllFinalizers)

