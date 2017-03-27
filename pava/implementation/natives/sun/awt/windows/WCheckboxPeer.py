def add_native_methods(clazz):
    def setState(a0):
        raise NotImplementedError()

    def setCheckboxGroup(a0):
        raise NotImplementedError()

    def setLabel(a0):
        raise NotImplementedError()

    def getCheckMarkSize():
        raise NotImplementedError()

    def create(a0):
        raise NotImplementedError()

    clazz.setState = setState
    clazz.setCheckboxGroup = setCheckboxGroup
    clazz.setLabel = setLabel
    clazz.getCheckMarkSize = staticmethod(getCheckMarkSize)
    clazz.create = create

