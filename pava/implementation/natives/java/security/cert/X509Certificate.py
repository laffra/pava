def add_native_methods(clazz):
    def getSubjectAlternativeNames():
        raise NotImplementedError()

    def getIssuerAlternativeNames():
        raise NotImplementedError()

    clazz.getSubjectAlternativeNames = getSubjectAlternativeNames
    clazz.getIssuerAlternativeNames = getIssuerAlternativeNames

