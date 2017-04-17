def add_native_methods(clazz):
    def compileClass__java_lang_Class_____(a0):
        raise NotImplementedError()

    def compileClasses__java_lang_String__(a0):
        raise NotImplementedError()

    def command__java_lang_Object__(a0):
        raise NotImplementedError()

    def enable____():
        raise NotImplementedError()

    def disable____():
        raise NotImplementedError()

    clazz.compileClass__java_lang_Class_____ = staticmethod(compileClass__java_lang_Class_____)
    clazz.compileClasses__java_lang_String__ = staticmethod(compileClasses__java_lang_String__)
    clazz.command__java_lang_Object__ = staticmethod(command__java_lang_Object__)
    clazz.enable____ = staticmethod(enable____)
    clazz.disable____ = staticmethod(disable____)

