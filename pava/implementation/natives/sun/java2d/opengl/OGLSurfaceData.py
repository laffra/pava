def add_native_methods(clazz):
    def initTexture__long__boolean__boolean__boolean__int__int__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def initFBObject__long__boolean__boolean__boolean__int__int__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def initFlipBackbuffer__long__(a0, a1):
        raise NotImplementedError()

    clazz.initTexture__long__boolean__boolean__boolean__int__int__ = initTexture__long__boolean__boolean__boolean__int__int__
    clazz.initFBObject__long__boolean__boolean__boolean__int__int__ = initFBObject__long__boolean__boolean__boolean__int__int__
    clazz.initFlipBackbuffer__long__ = initFlipBackbuffer__long__

