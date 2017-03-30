def add_native_methods(clazz):
    def nativeConnectDisabled():
        raise NotImplementedError()

    clazz.nativeConnectDisabled = nativeConnectDisabled

