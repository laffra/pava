def add_native_methods(clazz):
    def _dispose():
        raise NotImplementedError()

    def create():
        raise NotImplementedError()

    def mouseMoveImpl(a0, a1):
        raise NotImplementedError()

    def mousePress(a0):
        raise NotImplementedError()

    def mouseRelease(a0):
        raise NotImplementedError()

    def mouseWheel(a0):
        raise NotImplementedError()

    def keyPress(a0):
        raise NotImplementedError()

    def keyRelease(a0):
        raise NotImplementedError()

    def getRGBPixels(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz._dispose = _dispose
    clazz.create = create
    clazz.mouseMoveImpl = mouseMoveImpl
    clazz.mousePress = mousePress
    clazz.mouseRelease = mouseRelease
    clazz.mouseWheel = mouseWheel
    clazz.keyPress = keyPress
    clazz.keyRelease = keyRelease
    clazz.getRGBPixels = getRGBPixels

