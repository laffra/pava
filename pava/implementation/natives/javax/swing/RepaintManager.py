def add_native_methods(clazz):
    def nativeAddDirtyRegion__sun_awt_AppContext__java_awt_Container__int__int__int__int__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def nativeQueueSurfaceDataRunnable__sun_awt_AppContext__java_awt_Component__java_lang_Runnable__(a0, a1, a2, a3):
        raise NotImplementedError()

    clazz.nativeAddDirtyRegion__sun_awt_AppContext__java_awt_Container__int__int__int__int__ = nativeAddDirtyRegion__sun_awt_AppContext__java_awt_Container__int__int__int__int__
    clazz.nativeQueueSurfaceDataRunnable__sun_awt_AppContext__java_awt_Component__java_lang_Runnable__ = nativeQueueSurfaceDataRunnable__sun_awt_AppContext__java_awt_Component__java_lang_Runnable__

