def add_native_methods(clazz):
    def invokeExact__java_lang_Object_____(a0, a1):
        raise NotImplementedError()

    def invoke__java_lang_Object_____(a0, a1):
        raise NotImplementedError()

    def invokeBasic__java_lang_Object_____(a0, a1):
        raise NotImplementedError()

    def linkToVirtual__java_lang_Object_____(a0):
        raise NotImplementedError()

    def linkToStatic__java_lang_Object_____(a0):
        raise NotImplementedError()

    def linkToSpecial__java_lang_Object_____(a0):
        raise NotImplementedError()

    def linkToInterface__java_lang_Object_____(a0):
        raise NotImplementedError()

    clazz.invokeExact__java_lang_Object_____ = invokeExact__java_lang_Object_____
    clazz.invoke__java_lang_Object_____ = invoke__java_lang_Object_____
    clazz.invokeBasic__java_lang_Object_____ = invokeBasic__java_lang_Object_____
    clazz.linkToVirtual__java_lang_Object_____ = staticmethod(linkToVirtual__java_lang_Object_____)
    clazz.linkToStatic__java_lang_Object_____ = staticmethod(linkToStatic__java_lang_Object_____)
    clazz.linkToSpecial__java_lang_Object_____ = staticmethod(linkToSpecial__java_lang_Object_____)
    clazz.linkToInterface__java_lang_Object_____ = staticmethod(linkToInterface__java_lang_Object_____)

