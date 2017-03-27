def add_native_methods(clazz):
    def setEchoChar(a0):
        raise NotImplementedError()

    def create(a0):
        raise NotImplementedError()

    clazz.setEchoChar = setEchoChar
    clazz.create = create

