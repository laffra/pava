def add_native_methods(clazz):
    def getMetaInfEntryNames():
        raise NotImplementedError()

    clazz.getMetaInfEntryNames = getMetaInfEntryNames

