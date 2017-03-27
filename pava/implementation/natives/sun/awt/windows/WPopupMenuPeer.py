def add_native_methods(clazz):
    def createMenu(a0):
        raise NotImplementedError()

    def _show(a0):
        raise NotImplementedError()

    clazz.createMenu = createMenu
    clazz._show = _show

