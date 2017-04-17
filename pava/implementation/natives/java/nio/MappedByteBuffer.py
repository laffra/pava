def add_native_methods(clazz):
    def isLoaded0__long__long__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def load0__long__long__(a0, a1, a2):
        raise NotImplementedError()

    clazz.isLoaded0__long__long__int__ = isLoaded0__long__long__int__
    clazz.load0__long__long__ = load0__long__long__

