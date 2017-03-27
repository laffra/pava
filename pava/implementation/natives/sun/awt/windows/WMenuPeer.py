def add_native_methods(clazz):
    def addSeparator():
        raise NotImplementedError()

    def delItem(a0):
        raise NotImplementedError()

    def createMenu(a0):
        raise NotImplementedError()

    def createSubMenu(a0):
        raise NotImplementedError()

    clazz.addSeparator = addSeparator
    clazz.delItem = delItem
    clazz.createMenu = createMenu
    clazz.createSubMenu = createSubMenu

