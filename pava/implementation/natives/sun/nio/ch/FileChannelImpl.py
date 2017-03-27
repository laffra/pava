def add_native_methods(clazz):
    def map0(a0, a1, a2):
        raise NotImplementedError()

    def unmap0(a0, a1):
        raise NotImplementedError()

    def transferTo0(a0, a1, a2, a3):
        raise NotImplementedError()

    def position0(a0, a1):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.map0 = map0
    clazz.unmap0 = staticmethod(unmap0)
    clazz.transferTo0 = transferTo0
    clazz.position0 = position0
    clazz.initIDs = staticmethod(initIDs)

