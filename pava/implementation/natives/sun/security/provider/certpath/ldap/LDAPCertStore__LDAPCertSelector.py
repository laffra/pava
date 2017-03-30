def add_native_methods(clazz):
    def getSubjectAlternativeNames():
        raise NotImplementedError()

    clazz.getSubjectAlternativeNames = getSubjectAlternativeNames

