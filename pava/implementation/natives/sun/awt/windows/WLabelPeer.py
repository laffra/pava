def add_native_methods(clazz):
    def lazyPaint():
        raise NotImplementedError()

    def setText(a0):
        raise NotImplementedError()

    def setAlignment(a0):
        raise NotImplementedError()

    def create(a0):
        raise NotImplementedError()

    clazz.lazyPaint = lazyPaint
    clazz.setText = setText
    clazz.setAlignment = setAlignment
    clazz.create = create

