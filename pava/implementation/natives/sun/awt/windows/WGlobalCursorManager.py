def add_native_methods(clazz):
    def nativeUpdateCursor__java_awt_Component__(a0):
        raise NotImplementedError()

    def setCursor__java_awt_Component__java_awt_Cursor__boolean__(a0, a1, a2, a3):
        raise NotImplementedError()

    def getCursorPos__java_awt_Point__(a0, a1):
        raise NotImplementedError()

    def findHeavyweightUnderCursor__boolean__(a0, a1):
        raise NotImplementedError()

    clazz.nativeUpdateCursor__java_awt_Component__ = staticmethod(nativeUpdateCursor__java_awt_Component__)
    clazz.setCursor__java_awt_Component__java_awt_Cursor__boolean__ = setCursor__java_awt_Component__java_awt_Cursor__boolean__
    clazz.getCursorPos__java_awt_Point__ = getCursorPos__java_awt_Point__
    clazz.findHeavyweightUnderCursor__boolean__ = findHeavyweightUnderCursor__boolean__

