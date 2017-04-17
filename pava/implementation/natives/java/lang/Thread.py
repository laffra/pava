def add_native_methods(clazz):
    def currentThread____():
        raise NotImplementedError()

    def yield____():
        raise NotImplementedError()

    def sleep__long__(a0):
        raise NotImplementedError()

    def isAlive____(a0):
        raise NotImplementedError()

    def countStackFrames____(a0):
        raise NotImplementedError()

    def holdsLock__java_lang_Object__(a0):
        raise NotImplementedError()

    clazz.currentThread____ = staticmethod(currentThread____)
    clazz.yield____ = staticmethod(yield____)
    clazz.sleep__long__ = staticmethod(sleep__long__)
    clazz.isAlive____ = isAlive____
    clazz.countStackFrames____ = countStackFrames____
    clazz.holdsLock__java_lang_Object__ = staticmethod(holdsLock__java_lang_Object__)

