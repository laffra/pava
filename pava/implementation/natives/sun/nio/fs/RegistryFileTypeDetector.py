def add_native_methods(clazz):
    def queryStringValue(a0, a1):
        raise NotImplementedError()

    clazz.queryStringValue = staticmethod(queryStringValue)

