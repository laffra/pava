def add_native_methods(clazz):
    def initialize():
        raise NotImplementedError()

    def registerNatives():
        raise NotImplementedError()

    def compileClass(a0):
        raise NotImplementedError()

    def compileClasses(a0):
        raise NotImplementedError()

    def command(a0):
        raise NotImplementedError()

    def enable():
        raise NotImplementedError()

    def disable():
        raise NotImplementedError()

    clazz.initialize = staticmethod(initialize)
    clazz.registerNatives = staticmethod(registerNatives)
    clazz.compileClass = staticmethod(compileClass)
    clazz.compileClasses = staticmethod(compileClasses)
    clazz.command = staticmethod(command)
    clazz.enable = staticmethod(enable)
    clazz.disable = staticmethod(disable)

