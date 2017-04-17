def add_native_methods(clazz):
    def Available__long__(a0, a1):
        raise NotImplementedError()

    def Read__long__(a0, a1):
        raise NotImplementedError()

    def ReadBytes__long__byte____int__int__(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    clazz.Available__long__ = Available__long__
    clazz.Read__long__ = Read__long__
    clazz.ReadBytes__long__byte____int__int__ = ReadBytes__long__byte____int__int__

