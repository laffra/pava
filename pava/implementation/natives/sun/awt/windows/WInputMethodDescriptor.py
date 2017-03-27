def add_native_methods(clazz):
    def getNativeAvailableLocales():
        raise NotImplementedError()

    clazz.getNativeAvailableLocales = staticmethod(getNativeAvailableLocales)

