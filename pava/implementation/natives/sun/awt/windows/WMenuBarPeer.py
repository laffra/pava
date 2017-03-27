def add_native_methods(clazz):
    def addMenu(a0):
        raise NotImplementedError()

    def delMenu(a0):
        raise NotImplementedError()

    def create(a0):
        raise NotImplementedError()

    clazz.addMenu = addMenu
    clazz.delMenu = delMenu
    clazz.create = create

