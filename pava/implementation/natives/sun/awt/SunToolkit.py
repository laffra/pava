def add_native_methods(clazz):
    def closeSplashScreen():
        raise NotImplementedError()

    clazz.closeSplashScreen = staticmethod(closeSplashScreen)

