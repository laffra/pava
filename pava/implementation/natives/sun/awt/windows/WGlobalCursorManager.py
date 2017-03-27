def add_native_methods(clazz):
    def setCursor(a0, a1, a2):
        raise NotImplementedError()

    def getCursorPos(a0):
        raise NotImplementedError()

    def findHeavyweightUnderCursor(a0):
        raise NotImplementedError()

    def getLocationOnScreen(a0):
        raise NotImplementedError()

    clazz.setCursor = setCursor
    clazz.getCursorPos = getCursorPos
    clazz.findHeavyweightUnderCursor = findHeavyweightUnderCursor
    clazz.getLocationOnScreen = getLocationOnScreen

