def add_native_methods(clazz):
    def readFile__long__long__int__long__long__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def writeFile__long__long__int__long__long__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def lockFile__long__long__long__boolean__long__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def close0__long__(a0, a1):
        raise NotImplementedError()

    clazz.readFile__long__long__int__long__long__ = staticmethod(readFile__long__long__int__long__long__)
    clazz.writeFile__long__long__int__long__long__ = staticmethod(writeFile__long__long__int__long__long__)
    clazz.lockFile__long__long__long__boolean__long__ = staticmethod(lockFile__long__long__long__boolean__long__)
    clazz.close0__long__ = staticmethod(close0__long__)

