def add_native_methods(clazz):
    def maxObjectInspectionAge():
        raise NotImplementedError()

    clazz.maxObjectInspectionAge = staticmethod(maxObjectInspectionAge)

