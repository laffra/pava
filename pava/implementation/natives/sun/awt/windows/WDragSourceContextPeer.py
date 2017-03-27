def add_native_methods(clazz):
    def createDragSource(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def doDragDrop(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def setNativeCursor(a0, a1, a2):
        raise NotImplementedError()

    clazz.createDragSource = createDragSource
    clazz.doDragDrop = doDragDrop
    clazz.setNativeCursor = setNativeCursor

