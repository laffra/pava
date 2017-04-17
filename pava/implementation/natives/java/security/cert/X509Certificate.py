def add_native_methods(clazz):
    def getSubjectAlternativeNames____(a0):
        raise NotImplementedError()

    def getIssuerAlternativeNames____(a0):
        raise NotImplementedError()

    clazz.getSubjectAlternativeNames____ = getSubjectAlternativeNames____
    clazz.getIssuerAlternativeNames____ = getIssuerAlternativeNames____

