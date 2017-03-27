def add_native_methods(clazz):
    def dumpHeap0(a0, a1):
        raise NotImplementedError()

    clazz.dumpHeap0 = dumpHeap0

