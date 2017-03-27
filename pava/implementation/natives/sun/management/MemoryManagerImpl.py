def add_native_methods(clazz):
    def getMemoryPools0():
        raise NotImplementedError()

    clazz.getMemoryPools0 = getMemoryPools0

