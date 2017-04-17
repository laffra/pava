def add_native_methods(clazz):
    def initIDs____(a0):
        raise NotImplementedError()

    def createIoCompletionPort__long__long__int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def close0__long__(a0, a1):
        raise NotImplementedError()

    def getQueuedCompletionStatus__long__sun_nio_ch_Iocp_CompletionStatus__(a0, a1, a2):
        raise NotImplementedError()

    def postQueuedCompletionStatus__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def getErrorMessage__int__(a0, a1):
        raise NotImplementedError()

    clazz.initIDs____ = staticmethod(initIDs____)
    clazz.createIoCompletionPort__long__long__int__int__ = staticmethod(createIoCompletionPort__long__long__int__int__)
    clazz.close0__long__ = staticmethod(close0__long__)
    clazz.getQueuedCompletionStatus__long__sun_nio_ch_Iocp_CompletionStatus__ = staticmethod(getQueuedCompletionStatus__long__sun_nio_ch_Iocp_CompletionStatus__)
    clazz.postQueuedCompletionStatus__long__int__ = staticmethod(postQueuedCompletionStatus__long__int__)
    clazz.getErrorMessage__int__ = staticmethod(getErrorMessage__int__)

