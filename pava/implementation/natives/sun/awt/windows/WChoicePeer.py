def add_native_methods(clazz):
    def select(a0):
        raise NotImplementedError()

    def removeAll():
        raise NotImplementedError()

    def remove(a0):
        raise NotImplementedError()

    def addItems(a0, a1):
        raise NotImplementedError()

    def reshape(a0, a1, a2, a3):
        raise NotImplementedError()

    def create(a0):
        raise NotImplementedError()

    def closeList():
        raise NotImplementedError()

    clazz.select = select
    clazz.removeAll = removeAll
    clazz.remove = remove
    clazz.addItems = addItems
    clazz.reshape = reshape
    clazz.create = create
    clazz.closeList = closeList

