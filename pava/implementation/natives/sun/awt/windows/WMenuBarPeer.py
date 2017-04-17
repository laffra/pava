def add_native_methods(clazz):
    def addMenu__java_awt_Menu__(a0, a1):
        raise NotImplementedError()

    def delMenu__int__(a0, a1):
        raise NotImplementedError()

    clazz.addMenu__java_awt_Menu__ = addMenu__java_awt_Menu__
    clazz.delMenu__int__ = delMenu__int__

