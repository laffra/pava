def add_native_methods(clazz):
    def setThreadResourceContext0__long__int__(a0, a1):
        raise NotImplementedError()

    def getThreadResourceContext0__long__(a0):
        raise NotImplementedError()

    clazz.setThreadResourceContext0__long__int__ = staticmethod(setThreadResourceContext0__long__int__)
    clazz.getThreadResourceContext0__long__ = staticmethod(getThreadResourceContext0__long__)

