def add_native_methods(clazz):
    def getElem(a0, a1, a2):
        raise NotImplementedError()

    def setElem(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.getElem = getElem
    clazz.setElem = setElem

