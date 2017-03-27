def add_native_methods(clazz):
    def getParameters0():
        raise NotImplementedError()

    def getTypeAnnotationBytes0():
        raise NotImplementedError()

    clazz.getParameters0 = getParameters0
    clazz.getTypeAnnotationBytes0 = getTypeAnnotationBytes0

