def add_native_methods(clazz):
    def ShellExecute(a0, a1):
        raise NotImplementedError()

    clazz.ShellExecute = staticmethod(ShellExecute)

