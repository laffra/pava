def add_native_methods(clazz):
    def activate0__java_lang_String__sun_tracing_dtrace_DTraceProvider____(a0, a1, a2):
        raise NotImplementedError()

    def dispose0__long__(a0, a1):
        raise NotImplementedError()

    def isEnabled0__java_lang_reflect_Method__(a0, a1):
        raise NotImplementedError()

    def isSupported0____(a0):
        raise NotImplementedError()

    def defineClass0__java_lang_ClassLoader__java_lang_String__byte____int__int__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    clazz.activate0__java_lang_String__sun_tracing_dtrace_DTraceProvider____ = staticmethod(activate0__java_lang_String__sun_tracing_dtrace_DTraceProvider____)
    clazz.dispose0__long__ = staticmethod(dispose0__long__)
    clazz.isEnabled0__java_lang_reflect_Method__ = staticmethod(isEnabled0__java_lang_reflect_Method__)
    clazz.isSupported0____ = staticmethod(isSupported0____)
    clazz.defineClass0__java_lang_ClassLoader__java_lang_String__byte____int__int__ = staticmethod(defineClass0__java_lang_ClassLoader__java_lang_String__byte____int__int__)

