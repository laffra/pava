def add_native_methods(clazz):
    def _show():
        raise NotImplementedError()

    clazz._show = _show

