def add_native_methods(clazz):
    def getWindowsDirectory(a0):
        raise NotImplementedError()

    clazz.getWindowsDirectory = staticmethod(getWindowsDirectory)

