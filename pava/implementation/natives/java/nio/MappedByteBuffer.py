def add_native_methods(clazz):
    def isLoaded0(a0, a1, a2):
        raise NotImplementedError()

    def load0(a0, a1):
        raise NotImplementedError()

    def force0(a0, a1, a2):
        raise NotImplementedError()

    clazz.isLoaded0 = isLoaded0
    clazz.load0 = load0
    clazz.force0 = force0

