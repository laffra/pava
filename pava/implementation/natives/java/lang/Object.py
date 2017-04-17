def add_native_methods(clazz):
    def getClass____(a0):
        raise NotImplementedError()

    def hashCode____(a0):
        raise NotImplementedError()

    def clone____(a0):
        raise NotImplementedError()

    def notify____(a0):
        raise NotImplementedError()

    def notifyAll____(a0):
        raise NotImplementedError()

    def wait__long__(a0, a1):
        raise NotImplementedError()

    clazz.getClass____ = getClass____
    clazz.hashCode____ = hashCode____
    clazz.clone____ = clone____
    clazz.notify____ = notify____
    clazz.notifyAll____ = notifyAll____
    clazz.wait__long__ = wait__long__

    # Custom methods

    def no___java_init______(self):
        print '='*120
        print 'java.lang.Object.init'
        print '='*120
        import traceback
        print traceback.format_stack()
