def add_native_methods(clazz):
    def acquireDefaultNativeCreds(a0):
        raise NotImplementedError()

    clazz.acquireDefaultNativeCreds = staticmethod(acquireDefaultNativeCreds)

