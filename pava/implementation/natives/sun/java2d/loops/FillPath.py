def add_native_methods(clazz):
    def FillPath(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz.FillPath = FillPath

