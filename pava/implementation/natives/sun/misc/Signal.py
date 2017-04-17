def add_native_methods(clazz):
    def findSignal__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def handle0__int__long__(a0, a1, a2):
        raise NotImplementedError()

    def raise0__int__(a0, a1):
        raise NotImplementedError()

    clazz.findSignal__java_lang_String__ = staticmethod(findSignal__java_lang_String__)
    clazz.handle0__int__long__ = staticmethod(handle0__int__long__)
    clazz.raise0__int__ = staticmethod(raise0__int__)

