def add_native_methods(clazz):
    def initAgentProperties(a0):
        raise NotImplementedError()

    def getVMTemporaryDirectory():
        raise NotImplementedError()

    clazz.initAgentProperties = staticmethod(initAgentProperties)
    clazz.getVMTemporaryDirectory = staticmethod(getVMTemporaryDirectory)

