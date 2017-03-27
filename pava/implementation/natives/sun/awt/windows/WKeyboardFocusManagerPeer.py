def add_native_methods(clazz):
    def setNativeFocusOwner(a0):
        raise NotImplementedError()

    def getNativeFocusOwner():
        raise NotImplementedError()

    def getNativeFocusedWindow():
        raise NotImplementedError()

    clazz.setNativeFocusOwner = staticmethod(setNativeFocusOwner)
    clazz.getNativeFocusOwner = staticmethod(getNativeFocusOwner)
    clazz.getNativeFocusedWindow = staticmethod(getNativeFocusedWindow)

