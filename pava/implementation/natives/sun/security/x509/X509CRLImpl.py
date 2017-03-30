def add_native_methods(clazz):
    def getIssuerAltNameExtension():
        raise NotImplementedError()

    clazz.getIssuerAltNameExtension = getIssuerAltNameExtension

