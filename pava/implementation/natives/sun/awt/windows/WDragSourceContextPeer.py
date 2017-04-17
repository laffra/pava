def add_native_methods(clazz):
    def createDragSource__java_awt_Component__java_awt_datatransfer_Transferable__java_awt_event_InputEvent__int__long____java_util_Map__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def doDragDrop__long__java_awt_Cursor__int____int__int__int__int__(a0, a1, a2, a3, a4, a5, a6, a7):
        raise NotImplementedError()

    def setNativeCursor__long__java_awt_Cursor__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.createDragSource__java_awt_Component__java_awt_datatransfer_Transferable__java_awt_event_InputEvent__int__long____java_util_Map__ = createDragSource__java_awt_Component__java_awt_datatransfer_Transferable__java_awt_event_InputEvent__int__long____java_util_Map__
    clazz.doDragDrop__long__java_awt_Cursor__int____int__int__int__int__ = doDragDrop__long__java_awt_Cursor__int____int__int__int__int__
    clazz.setNativeCursor__long__java_awt_Cursor__int__ = setNativeCursor__long__java_awt_Cursor__int__

