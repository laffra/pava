def add_native_methods(clazz):
    def getTagNative__long__int__(a0, a1):
        raise NotImplementedError()

    def getProfileID__java_awt_color_ICC_Profile__(a0):
        raise NotImplementedError()

    def colorConvert__sun_java2d_cmm_lcms_LCMSTransform__sun_java2d_cmm_lcms_LCMSImageLayout__sun_java2d_cmm_lcms_LCMSImageLayout__(a0, a1, a2):
        raise NotImplementedError()

    def freeTransform__long__(a0):
        raise NotImplementedError()

    def initLCMS__java_lang_Class__java_lang_Class__java_lang_Class__(a0, a1, a2):
        raise NotImplementedError()

    clazz.getTagNative__long__int__ = staticmethod(getTagNative__long__int__)
    clazz.getProfileID__java_awt_color_ICC_Profile__ = staticmethod(getProfileID__java_awt_color_ICC_Profile__)
    clazz.colorConvert__sun_java2d_cmm_lcms_LCMSTransform__sun_java2d_cmm_lcms_LCMSImageLayout__sun_java2d_cmm_lcms_LCMSImageLayout__ = staticmethod(colorConvert__sun_java2d_cmm_lcms_LCMSTransform__sun_java2d_cmm_lcms_LCMSImageLayout__sun_java2d_cmm_lcms_LCMSImageLayout__)
    clazz.freeTransform__long__ = staticmethod(freeTransform__long__)
    clazz.initLCMS__java_lang_Class__java_lang_Class__java_lang_Class__ = staticmethod(initLCMS__java_lang_Class__java_lang_Class__java_lang_Class__)

