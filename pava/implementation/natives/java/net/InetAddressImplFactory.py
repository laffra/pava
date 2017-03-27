def add_native_methods(clazz):
    def isIPv6Supported():
        raise NotImplementedError()

    clazz.isIPv6Supported = staticmethod(isIPv6Supported)

