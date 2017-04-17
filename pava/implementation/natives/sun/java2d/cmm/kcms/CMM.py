def add_native_methods(clazz):
    def cmmLoadProfile__byte____long____(a0, a1):
        raise NotImplementedError()

    def cmmFreeProfile__long__(a0):
        raise NotImplementedError()

    def cmmGetProfileSize__long__int____(a0, a1):
        raise NotImplementedError()

    def cmmGetProfileData__long__byte____(a0, a1):
        raise NotImplementedError()

    def cmmGetTagSize__long__int__int____(a0, a1, a2):
        raise NotImplementedError()

    def cmmGetTagData__long__int__byte____(a0, a1, a2):
        raise NotImplementedError()

    def cmmSetTagData__long__int__byte____(a0, a1, a2):
        raise NotImplementedError()

    def cmmGetTransform__java_awt_color_ICC_Profile__int__int__sun_java2d_cmm_kcms_ICC_Transform__(a0, a1, a2, a3):
        raise NotImplementedError()

    def cmmCombineTransforms__sun_java2d_cmm_kcms_ICC_Transform____sun_java2d_cmm_kcms_ICC_Transform__(a0, a1):
        raise NotImplementedError()

    def cmmFreeTransform__long__(a0):
        raise NotImplementedError()

    def cmmGetNumComponents__long__int____(a0, a1):
        raise NotImplementedError()

    def cmmColorConvert__long__sun_java2d_cmm_kcms_CMMImageLayout__sun_java2d_cmm_kcms_CMMImageLayout__(a0, a1, a2):
        raise NotImplementedError()

    def cmmInit____():
        raise NotImplementedError()

    def cmmTerminate____():
        raise NotImplementedError()

    clazz.cmmLoadProfile__byte____long____ = staticmethod(cmmLoadProfile__byte____long____)
    clazz.cmmFreeProfile__long__ = staticmethod(cmmFreeProfile__long__)
    clazz.cmmGetProfileSize__long__int____ = staticmethod(cmmGetProfileSize__long__int____)
    clazz.cmmGetProfileData__long__byte____ = staticmethod(cmmGetProfileData__long__byte____)
    clazz.cmmGetTagSize__long__int__int____ = staticmethod(cmmGetTagSize__long__int__int____)
    clazz.cmmGetTagData__long__int__byte____ = staticmethod(cmmGetTagData__long__int__byte____)
    clazz.cmmSetTagData__long__int__byte____ = staticmethod(cmmSetTagData__long__int__byte____)
    clazz.cmmGetTransform__java_awt_color_ICC_Profile__int__int__sun_java2d_cmm_kcms_ICC_Transform__ = staticmethod(cmmGetTransform__java_awt_color_ICC_Profile__int__int__sun_java2d_cmm_kcms_ICC_Transform__)
    clazz.cmmCombineTransforms__sun_java2d_cmm_kcms_ICC_Transform____sun_java2d_cmm_kcms_ICC_Transform__ = staticmethod(cmmCombineTransforms__sun_java2d_cmm_kcms_ICC_Transform____sun_java2d_cmm_kcms_ICC_Transform__)
    clazz.cmmFreeTransform__long__ = staticmethod(cmmFreeTransform__long__)
    clazz.cmmGetNumComponents__long__int____ = staticmethod(cmmGetNumComponents__long__int____)
    clazz.cmmColorConvert__long__sun_java2d_cmm_kcms_CMMImageLayout__sun_java2d_cmm_kcms_CMMImageLayout__ = staticmethod(cmmColorConvert__long__sun_java2d_cmm_kcms_CMMImageLayout__sun_java2d_cmm_kcms_CMMImageLayout__)
    clazz.cmmInit____ = staticmethod(cmmInit____)
    clazz.cmmTerminate____ = staticmethod(cmmTerminate____)

