def add_native_methods(clazz):
    def getIssuerAlternativeNameExtension____(a0):
        raise NotImplementedError()

    def getSubjectAlternativeNameExtension____(a0):
        raise NotImplementedError()

    def getSubjectAlternativeNames____(a0):
        raise NotImplementedError()

    def getSubjectAlternativeNames__java_security_cert_X509Certificate__(a0):
        raise NotImplementedError()

    def getIssuerAlternativeNames____(a0):
        raise NotImplementedError()

    def getIssuerAlternativeNames__java_security_cert_X509Certificate__(a0):
        raise NotImplementedError()

    clazz.getIssuerAlternativeNameExtension____ = getIssuerAlternativeNameExtension____
    clazz.getSubjectAlternativeNameExtension____ = getSubjectAlternativeNameExtension____
    clazz.getSubjectAlternativeNames____ = getSubjectAlternativeNames____
    clazz.getSubjectAlternativeNames__java_security_cert_X509Certificate__ = staticmethod(getSubjectAlternativeNames__java_security_cert_X509Certificate__)
    clazz.getIssuerAlternativeNames____ = getIssuerAlternativeNames____
    clazz.getIssuerAlternativeNames__java_security_cert_X509Certificate__ = staticmethod(getIssuerAlternativeNames__java_security_cert_X509Certificate__)

