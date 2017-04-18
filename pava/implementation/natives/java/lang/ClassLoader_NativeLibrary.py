def add_native_methods(clazz):
    def load__java_lang_String__boolean__(a0, a1, a2):
        raise NotImplementedError()

    def find__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def unload__java_lang_String__boolean__(a0, a1, a2):
        raise NotImplementedError()

    clazz.load__java_lang_String__boolean__ = load__java_lang_String__boolean__
    clazz.find__java_lang_String__ = find__java_lang_String__
    clazz.unload__java_lang_String__boolean__ = unload__java_lang_String__boolean__

