def add_native_methods(clazz):
    def cmmLoadProfile(a0, a1):
        raise NotImplementedError()

    def cmmFreeProfile(a0):
        raise NotImplementedError()

    def cmmGetProfileSize(a0, a1):
        raise NotImplementedError()

    def cmmGetProfileData(a0, a1):
        raise NotImplementedError()

    def cmmGetTagSize(a0, a1, a2):
        raise NotImplementedError()

    def cmmGetTagData(a0, a1, a2):
        raise NotImplementedError()

    def cmmSetTagData(a0, a1, a2):
        raise NotImplementedError()

    def cmmGetTransform(a0, a1, a2, a3):
        raise NotImplementedError()

    def cmmCombineTransforms(a0, a1):
        raise NotImplementedError()

    def cmmFreeTransform(a0):
        raise NotImplementedError()

    def cmmGetNumComponents(a0, a1):
        raise NotImplementedError()

    def cmmColorConvert(a0, a1, a2):
        raise NotImplementedError()

    def cmmInit():
        raise NotImplementedError()

    def cmmTerminate():
        raise NotImplementedError()

    clazz.cmmLoadProfile = staticmethod(cmmLoadProfile)
    clazz.cmmFreeProfile = staticmethod(cmmFreeProfile)
    clazz.cmmGetProfileSize = staticmethod(cmmGetProfileSize)
    clazz.cmmGetProfileData = staticmethod(cmmGetProfileData)
    clazz.cmmGetTagSize = staticmethod(cmmGetTagSize)
    clazz.cmmGetTagData = staticmethod(cmmGetTagData)
    clazz.cmmSetTagData = staticmethod(cmmSetTagData)
    clazz.cmmGetTransform = staticmethod(cmmGetTransform)
    clazz.cmmCombineTransforms = staticmethod(cmmCombineTransforms)
    clazz.cmmFreeTransform = staticmethod(cmmFreeTransform)
    clazz.cmmGetNumComponents = staticmethod(cmmGetNumComponents)
    clazz.cmmColorConvert = staticmethod(cmmColorConvert)
    clazz.cmmInit = staticmethod(cmmInit)
    clazz.cmmTerminate = staticmethod(cmmTerminate)

