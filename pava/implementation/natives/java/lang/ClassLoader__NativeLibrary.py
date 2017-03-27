def add_native_methods(clazz):
    def load(a0, a1):
        raise NotImplementedError()

    def find(a0):
        raise NotImplementedError()

    def unload(a0, a1):
        raise NotImplementedError()

    clazz.load = load
    clazz.find = find
    clazz.unload = unload

