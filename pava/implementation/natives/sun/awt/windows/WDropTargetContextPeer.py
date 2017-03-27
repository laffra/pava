def add_native_methods(clazz):
    def getData(a0, a1):
        raise NotImplementedError()

    def dropDone(a0, a1, a2):
        raise NotImplementedError()

    clazz.getData = getData
    clazz.dropDone = dropDone

