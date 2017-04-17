def add_native_methods(clazz):
    def getStillActive____(a0):
        raise NotImplementedError()

    def getExitCodeProcess__long__(a0, a1):
        raise NotImplementedError()

    def waitForInterruptibly__long__(a0, a1):
        raise NotImplementedError()

    def waitForTimeoutInterruptibly__long__long__(a0, a1, a2):
        raise NotImplementedError()

    def terminateProcess__long__(a0, a1):
        raise NotImplementedError()

    def isProcessAlive__long__(a0, a1):
        raise NotImplementedError()

    def create__java_lang_String__java_lang_String__java_lang_String__long____boolean__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def openForAtomicAppend__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def closeHandle__long__(a0, a1):
        raise NotImplementedError()

    clazz.getStillActive____ = staticmethod(getStillActive____)
    clazz.getExitCodeProcess__long__ = staticmethod(getExitCodeProcess__long__)
    clazz.waitForInterruptibly__long__ = staticmethod(waitForInterruptibly__long__)
    clazz.waitForTimeoutInterruptibly__long__long__ = staticmethod(waitForTimeoutInterruptibly__long__long__)
    clazz.terminateProcess__long__ = staticmethod(terminateProcess__long__)
    clazz.isProcessAlive__long__ = staticmethod(isProcessAlive__long__)
    clazz.create__java_lang_String__java_lang_String__java_lang_String__long____boolean__ = staticmethod(create__java_lang_String__java_lang_String__java_lang_String__long____boolean__)
    clazz.openForAtomicAppend__java_lang_String__ = staticmethod(openForAtomicAppend__java_lang_String__)
    clazz.closeHandle__long__ = staticmethod(closeHandle__long__)

