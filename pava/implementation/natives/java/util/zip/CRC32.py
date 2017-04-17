def add_native_methods(clazz):
    def update__int__int__(a0, a1, a2):
        raise NotImplementedError()

    def updateBytes__int__byte____int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def updateByteBuffer__int__long__int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz.update__int__int__ = staticmethod(update__int__int__)
    clazz.updateBytes__int__byte____int__int__ = staticmethod(updateBytes__int__byte____int__int__)
    clazz.updateByteBuffer__int__long__int__int__ = staticmethod(updateByteBuffer__int__long__int__int__)

