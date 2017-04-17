def add_native_methods(clazz):
    def create____(a0):
        raise NotImplementedError()

    def mouseMoveImpl__int__int__(a0, a1, a2):
        raise NotImplementedError()

    def mousePress__int__(a0, a1):
        raise NotImplementedError()

    def mouseRelease__int__(a0, a1):
        raise NotImplementedError()

    def mouseWheel__int__(a0, a1):
        raise NotImplementedError()

    def keyPress__int__(a0, a1):
        raise NotImplementedError()

    def keyRelease__int__(a0, a1):
        raise NotImplementedError()

    clazz.create____ = create____
    clazz.mouseMoveImpl__int__int__ = mouseMoveImpl__int__int__
    clazz.mousePress__int__ = mousePress__int__
    clazz.mouseRelease__int__ = mouseRelease__int__
    clazz.mouseWheel__int__ = mouseWheel__int__
    clazz.keyPress__int__ = keyPress__int__
    clazz.keyRelease__int__ = keyRelease__int__

