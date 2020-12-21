from __future__ import print_function

def add_native_methods(clazz):
    def intern____(a0):
        raise NotImplementedError()

    clazz.intern____ = intern____

    def __init__(self, value):
        print('CREATE STRING', value, type(value))
        super(self.__class__, self).__init__(value)
        self.value = value
    clazz.__init__ = __init__
