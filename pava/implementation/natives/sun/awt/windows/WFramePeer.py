def add_native_methods(clazz):
    def initIDs():
        raise NotImplementedError()

    def setState(a0):
        raise NotImplementedError()

    def getState():
        raise NotImplementedError()

    def setMaximizedBounds(a0, a1, a2, a3):
        raise NotImplementedError()

    def clearMaximizedBounds():
        raise NotImplementedError()

    def setMenuBar0(a0):
        raise NotImplementedError()

    def createAwtFrame(a0):
        raise NotImplementedError()

    def getSysMenuHeight():
        raise NotImplementedError()

    def pSetIMMOption(a0):
        raise NotImplementedError()

    def synthesizeWmActivate(a0):
        raise NotImplementedError()

    clazz.initIDs = staticmethod(initIDs)
    clazz.setState = setState
    clazz.getState = getState
    clazz.setMaximizedBounds = setMaximizedBounds
    clazz.clearMaximizedBounds = clearMaximizedBounds
    clazz.setMenuBar0 = setMenuBar0
    clazz.createAwtFrame = createAwtFrame
    clazz.getSysMenuHeight = staticmethod(getSysMenuHeight)
    clazz.pSetIMMOption = pSetIMMOption
    clazz.synthesizeWmActivate = synthesizeWmActivate

