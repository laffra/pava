def add_native_methods(clazz):
    def fillPointWithCoords(a0):
        raise NotImplementedError()

    def isWindowUnderMouse(a0):
        raise NotImplementedError()

    clazz.fillPointWithCoords = fillPointWithCoords
    clazz.isWindowUnderMouse = isWindowUnderMouse

