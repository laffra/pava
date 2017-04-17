def add_native_methods(clazz):
    def getJvmSpecialVersion____():
        raise NotImplementedError()

    def getJdkSpecialVersion____():
        raise NotImplementedError()

    clazz.getJvmSpecialVersion____ = staticmethod(getJvmSpecialVersion____)
    clazz.getJdkSpecialVersion____ = staticmethod(getJdkSpecialVersion____)

