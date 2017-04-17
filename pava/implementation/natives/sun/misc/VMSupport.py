def add_native_methods(clazz):
    def getVMTemporaryDirectory____():
        raise NotImplementedError()

    clazz.getVMTemporaryDirectory____ = staticmethod(getVMTemporaryDirectory____)

