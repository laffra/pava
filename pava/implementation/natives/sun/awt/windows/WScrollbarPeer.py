def add_native_methods(clazz):
    def getScrollbarSize(a0):
        raise NotImplementedError()

    def setValues(a0, a1, a2, a3):
        raise NotImplementedError()

    def setLineIncrement(a0):
        raise NotImplementedError()

    def setPageIncrement(a0):
        raise NotImplementedError()

    def create(a0):
        raise NotImplementedError()

    clazz.getScrollbarSize = staticmethod(getScrollbarSize)
    clazz.setValues = setValues
    clazz.setLineIncrement = setLineIncrement
    clazz.setPageIncrement = setPageIncrement
    clazz.create = create

