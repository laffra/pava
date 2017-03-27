def add_native_methods(clazz):
    def copyFromShortArray(a0, a1, a2, a3):
        raise NotImplementedError()

    def copyToShortArray(a0, a1, a2, a3):
        raise NotImplementedError()

    def copyFromIntArray(a0, a1, a2, a3):
        raise NotImplementedError()

    def copyToIntArray(a0, a1, a2, a3):
        raise NotImplementedError()

    def copyFromLongArray(a0, a1, a2, a3):
        raise NotImplementedError()

    def copyToLongArray(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.copyFromShortArray = staticmethod(copyFromShortArray)
    clazz.copyToShortArray = staticmethod(copyToShortArray)
    clazz.copyFromIntArray = staticmethod(copyFromIntArray)
    clazz.copyToIntArray = staticmethod(copyToIntArray)
    clazz.copyFromLongArray = staticmethod(copyFromLongArray)
    clazz.copyToLongArray = staticmethod(copyToLongArray)

