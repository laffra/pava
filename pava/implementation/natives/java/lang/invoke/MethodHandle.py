def add_native_methods(clazz):
    def invokeExact(a0):
        raise NotImplementedError()

    def invoke(a0):
        raise NotImplementedError()

    def invokeBasic(a0):
        raise NotImplementedError()

    def linkToVirtual(a0):
        raise NotImplementedError()

    def linkToStatic(a0):
        raise NotImplementedError()

    def linkToSpecial(a0):
        raise NotImplementedError()

    def linkToInterface(a0):
        raise NotImplementedError()

    clazz.invokeExact = invokeExact
    clazz.invoke = invoke
    clazz.invokeBasic = invokeBasic
    clazz.linkToVirtual = staticmethod(linkToVirtual)
    clazz.linkToStatic = staticmethod(linkToStatic)
    clazz.linkToSpecial = staticmethod(linkToSpecial)
    clazz.linkToInterface = staticmethod(linkToInterface)

