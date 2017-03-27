def add_native_methods(clazz):
    def Available(a0):
        raise NotImplementedError()

    def Read(a0):
        raise NotImplementedError()

    def ReadBytes(a0, a1, a2, a3):
        raise NotImplementedError()

    def Close(a0):
        raise NotImplementedError()

    clazz.Available = Available
    clazz.Read = Read
    clazz.ReadBytes = ReadBytes
    clazz.Close = Close

