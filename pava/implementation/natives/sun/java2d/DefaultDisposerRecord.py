def add_native_methods(clazz):
    def invokeNativeDispose(a0, a1):
        raise NotImplementedError()

    clazz.invokeNativeDispose = staticmethod(invokeNativeDispose)

