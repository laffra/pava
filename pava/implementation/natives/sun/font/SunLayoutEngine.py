def add_native_methods(clazz):
    def initGVIDs():
        raise NotImplementedError()

    def nativeLayout(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16):
        raise NotImplementedError()

    clazz.initGVIDs = staticmethod(initGVIDs)
    clazz.nativeLayout = staticmethod(nativeLayout)

