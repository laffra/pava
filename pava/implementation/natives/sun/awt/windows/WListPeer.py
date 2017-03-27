def add_native_methods(clazz):
    def addItems(a0, a1, a2):
        raise NotImplementedError()

    def delItems(a0, a1):
        raise NotImplementedError()

    def select(a0):
        raise NotImplementedError()

    def deselect(a0):
        raise NotImplementedError()

    def makeVisible(a0):
        raise NotImplementedError()

    def setMultipleSelections(a0):
        raise NotImplementedError()

    def getMaxWidth():
        raise NotImplementedError()

    def create(a0):
        raise NotImplementedError()

    def updateMaxItemWidth():
        raise NotImplementedError()

    def isSelected(a0):
        raise NotImplementedError()

    clazz.addItems = addItems
    clazz.delItems = delItems
    clazz.select = select
    clazz.deselect = deselect
    clazz.makeVisible = makeVisible
    clazz.setMultipleSelections = setMultipleSelections
    clazz.getMaxWidth = getMaxWidth
    clazz.create = create
    clazz.updateMaxItemWidth = updateMaxItemWidth
    clazz.isSelected = isSelected

