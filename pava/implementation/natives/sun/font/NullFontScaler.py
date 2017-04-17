def add_native_methods(clazz):
    def getNullScalerContext____():
        raise NotImplementedError()

    clazz.getNullScalerContext____ = staticmethod(getNullScalerContext____)

