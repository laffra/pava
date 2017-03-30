def add_native_methods(clazz):
    def nativeAddDirtyRegion(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def nativeQueueSurfaceDataRunnable(a0, a1, a2):
        raise NotImplementedError()

    clazz.nativeAddDirtyRegion = nativeAddDirtyRegion
    clazz.nativeQueueSurfaceDataRunnable = nativeQueueSurfaceDataRunnable

