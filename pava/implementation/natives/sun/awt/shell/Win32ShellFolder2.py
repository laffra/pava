def add_native_methods(clazz):
    def getNextPIDLEntry__long__(a0):
        raise NotImplementedError()

    def copyFirstPIDLEntry__long__(a0):
        raise NotImplementedError()

    def releasePIDL__long__(a0):
        raise NotImplementedError()

    def getStandardViewButton0__int__(a0):
        raise NotImplementedError()

    clazz.getNextPIDLEntry__long__ = staticmethod(getNextPIDLEntry__long__)
    clazz.copyFirstPIDLEntry__long__ = staticmethod(copyFirstPIDLEntry__long__)
    clazz.releasePIDL__long__ = staticmethod(releasePIDL__long__)
    clazz.getStandardViewButton0__int__ = staticmethod(getStandardViewButton0__int__)

