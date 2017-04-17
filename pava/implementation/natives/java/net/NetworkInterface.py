def add_native_methods(clazz):
    def getAll____(a0):
        raise NotImplementedError()

    def getByName0__java_lang_String__(a0, a1):
        raise NotImplementedError()

    def getByIndex0__int__(a0, a1):
        raise NotImplementedError()

    def getByInetAddress0__java_net_InetAddress__(a0, a1):
        raise NotImplementedError()

    def isUp0__java_lang_String__int__(a0, a1, a2):
        raise NotImplementedError()

    def isLoopback0__java_lang_String__int__(a0, a1, a2):
        raise NotImplementedError()

    def supportsMulticast0__java_lang_String__int__(a0, a1, a2):
        raise NotImplementedError()

    def isP2P0__java_lang_String__int__(a0, a1, a2):
        raise NotImplementedError()

    def getMacAddr0__byte____java_lang_String__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def getMTU0__java_lang_String__int__(a0, a1, a2):
        raise NotImplementedError()

    def init____(a0):
        raise NotImplementedError()

    clazz.getAll____ = staticmethod(getAll____)
    clazz.getByName0__java_lang_String__ = staticmethod(getByName0__java_lang_String__)
    clazz.getByIndex0__int__ = staticmethod(getByIndex0__int__)
    clazz.getByInetAddress0__java_net_InetAddress__ = staticmethod(getByInetAddress0__java_net_InetAddress__)
    clazz.isUp0__java_lang_String__int__ = staticmethod(isUp0__java_lang_String__int__)
    clazz.isLoopback0__java_lang_String__int__ = staticmethod(isLoopback0__java_lang_String__int__)
    clazz.supportsMulticast0__java_lang_String__int__ = staticmethod(supportsMulticast0__java_lang_String__int__)
    clazz.isP2P0__java_lang_String__int__ = staticmethod(isP2P0__java_lang_String__int__)
    clazz.getMacAddr0__byte____java_lang_String__int__ = staticmethod(getMacAddr0__byte____java_lang_String__int__)
    clazz.getMTU0__java_lang_String__int__ = staticmethod(getMTU0__java_lang_String__int__)
    clazz.init____ = staticmethod(init____)

