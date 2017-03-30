def add_native_methods(clazz):
    def getSubjectAlternativeNames(a0):
        raise NotImplementedError()

    clazz.getSubjectAlternativeNames = getSubjectAlternativeNames

