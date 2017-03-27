def add_native_methods(clazz):
    def registerNatives():
        raise NotImplementedError()

    def setIn0(a0):
        clazz.__in__ = a0

    def setOut0(a0):
        clazz.out = a0

    def setErr0(a0):
        clazz.err = a0

    def currentTimeMillis():
        raise NotImplementedError()

    def nanoTime():
        raise NotImplementedError()

    def arraycopy(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def identityHashCode(a0):
        raise NotImplementedError()

    def initProperties(a0):
        raise NotImplementedError()

    def mapLibraryName(a0):
        raise NotImplementedError()

    clazz.registerNatives = staticmethod(registerNatives)
    clazz.setIn0 = staticmethod(setIn0)
    clazz.setOut0 = staticmethod(setOut0)
    clazz.setErr0 = staticmethod(setErr0)
    clazz.currentTimeMillis = staticmethod(currentTimeMillis)
    clazz.nanoTime = staticmethod(nanoTime)
    clazz.arraycopy = staticmethod(arraycopy)
    clazz.identityHashCode = staticmethod(identityHashCode)
    clazz.initProperties = staticmethod(initProperties)
    clazz.mapLibraryName = staticmethod(mapLibraryName)

    # Custom initialization code

    class PythonPrintStream(object):
        def println(self, s):
            print s
    clazz.setOut0(PythonPrintStream())
