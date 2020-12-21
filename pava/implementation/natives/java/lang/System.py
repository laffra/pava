from __future__ import print_function

def add_native_methods(clazz):
    def currentTimeMillis____():
        raise NotImplementedError()

    def nanoTime____():
        raise NotImplementedError()

    def arraycopy__java_lang_Object__int__java_lang_Object__int__int__(a0, a1, a2, a3, a4):
        a2[a3:a3+a4] = a0[a1:a1+a4]

    def identityHashCode__java_lang_Object__(a0):
        raise NotImplementedError()

    def mapLibraryName__java_lang_String__(a0):
        raise NotImplementedError()

    clazz.currentTimeMillis____ = staticmethod(currentTimeMillis____)
    clazz.nanoTime____ = staticmethod(nanoTime____)
    clazz.arraycopy__java_lang_Object__int__java_lang_Object__int__int__ = staticmethod(arraycopy__java_lang_Object__int__java_lang_Object__int__int__)
    clazz.identityHashCode__java_lang_Object__ = staticmethod(identityHashCode__java_lang_Object__)
    clazz.mapLibraryName__java_lang_String__ = staticmethod(mapLibraryName__java_lang_String__)


    # Custom initialization code

    class PythonPrintStream(object):
        def println__boolean__(self, s):
            print(s)
        def println__char__(self, s):
            print(s)
        def println__int__(self, s):
            print(s)
        def println__java_lang_String__(self, s):
            print(s)
    clazz.out = PythonPrintStream()