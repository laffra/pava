def add_native_methods(clazz):
    def createCursorIndirect(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def getCursorWidth():
        raise NotImplementedError()

    def getCursorHeight():
        raise NotImplementedError()

    clazz.createCursorIndirect = createCursorIndirect
    clazz.getCursorWidth = staticmethod(getCursorWidth)
    clazz.getCursorHeight = staticmethod(getCursorHeight)

