def add_native_methods(clazz):
    def getTypeAnnotationBytes0():
        raise NotImplementedError()

    clazz.getTypeAnnotationBytes0 = getTypeAnnotationBytes0

