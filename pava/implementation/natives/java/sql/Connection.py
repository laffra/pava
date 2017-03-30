def add_native_methods(clazz):
    def nativeSQL(a0):
        raise NotImplementedError()

    clazz.nativeSQL = nativeSQL

