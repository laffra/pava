def add_native_methods(clazz):
    def init__java_lang_String__boolean__(a0, a1):
        raise NotImplementedError()

    def indicateMechs____():
        raise NotImplementedError()

    def inquireNamesForMech____(a0):
        raise NotImplementedError()

    def releaseName__long__(a0, a1):
        raise NotImplementedError()

    def importName__byte____org_ietf_jgss_Oid__(a0, a1, a2):
        raise NotImplementedError()

    def compareName__long__long__(a0, a1, a2):
        raise NotImplementedError()

    def canonicalizeName__long__(a0, a1):
        raise NotImplementedError()

    def exportName__long__(a0, a1):
        raise NotImplementedError()

    def displayName__long__(a0, a1):
        raise NotImplementedError()

    def acquireCred__long__int__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def releaseCred__long__(a0, a1):
        raise NotImplementedError()

    def getCredName__long__(a0, a1):
        raise NotImplementedError()

    def getCredTime__long__(a0, a1):
        raise NotImplementedError()

    def getCredUsage__long__(a0, a1):
        raise NotImplementedError()

    def importContext__byte____(a0, a1):
        raise NotImplementedError()

    def initContext__long__long__org_ietf_jgss_ChannelBinding__byte____sun_security_jgss_wrapper_NativeGSSContext__(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def acceptContext__long__org_ietf_jgss_ChannelBinding__byte____sun_security_jgss_wrapper_NativeGSSContext__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def inquireContext__long__(a0, a1):
        raise NotImplementedError()

    def getContextMech__long__(a0, a1):
        raise NotImplementedError()

    def getContextName__long__boolean__(a0, a1, a2):
        raise NotImplementedError()

    def getContextTime__long__(a0, a1):
        raise NotImplementedError()

    def deleteContext__long__(a0, a1):
        raise NotImplementedError()

    def wrapSizeLimit__long__int__int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def exportContext__long__(a0, a1):
        raise NotImplementedError()

    def getMic__long__int__byte____(a0, a1, a2, a3):
        raise NotImplementedError()

    def verifyMic__long__byte____byte____org_ietf_jgss_MessageProp__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def wrap__long__byte____org_ietf_jgss_MessageProp__(a0, a1, a2, a3):
        raise NotImplementedError()

    def unwrap__long__byte____org_ietf_jgss_MessageProp__(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.init__java_lang_String__boolean__ = staticmethod(init__java_lang_String__boolean__)
    clazz.indicateMechs____ = staticmethod(indicateMechs____)
    clazz.inquireNamesForMech____ = inquireNamesForMech____
    clazz.releaseName__long__ = releaseName__long__
    clazz.importName__byte____org_ietf_jgss_Oid__ = importName__byte____org_ietf_jgss_Oid__
    clazz.compareName__long__long__ = compareName__long__long__
    clazz.canonicalizeName__long__ = canonicalizeName__long__
    clazz.exportName__long__ = exportName__long__
    clazz.displayName__long__ = displayName__long__
    clazz.acquireCred__long__int__int__ = acquireCred__long__int__int__
    clazz.releaseCred__long__ = releaseCred__long__
    clazz.getCredName__long__ = getCredName__long__
    clazz.getCredTime__long__ = getCredTime__long__
    clazz.getCredUsage__long__ = getCredUsage__long__
    clazz.importContext__byte____ = importContext__byte____
    clazz.initContext__long__long__org_ietf_jgss_ChannelBinding__byte____sun_security_jgss_wrapper_NativeGSSContext__ = initContext__long__long__org_ietf_jgss_ChannelBinding__byte____sun_security_jgss_wrapper_NativeGSSContext__
    clazz.acceptContext__long__org_ietf_jgss_ChannelBinding__byte____sun_security_jgss_wrapper_NativeGSSContext__ = acceptContext__long__org_ietf_jgss_ChannelBinding__byte____sun_security_jgss_wrapper_NativeGSSContext__
    clazz.inquireContext__long__ = inquireContext__long__
    clazz.getContextMech__long__ = getContextMech__long__
    clazz.getContextName__long__boolean__ = getContextName__long__boolean__
    clazz.getContextTime__long__ = getContextTime__long__
    clazz.deleteContext__long__ = deleteContext__long__
    clazz.wrapSizeLimit__long__int__int__int__ = wrapSizeLimit__long__int__int__int__
    clazz.exportContext__long__ = exportContext__long__
    clazz.getMic__long__int__byte____ = getMic__long__int__byte____
    clazz.verifyMic__long__byte____byte____org_ietf_jgss_MessageProp__ = verifyMic__long__byte____byte____org_ietf_jgss_MessageProp__
    clazz.wrap__long__byte____org_ietf_jgss_MessageProp__ = wrap__long__byte____org_ietf_jgss_MessageProp__
    clazz.unwrap__long__byte____org_ietf_jgss_MessageProp__ = unwrap__long__byte____org_ietf_jgss_MessageProp__

