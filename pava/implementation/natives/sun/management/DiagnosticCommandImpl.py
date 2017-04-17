def add_native_methods(clazz):
    def setNotificationEnabled__boolean__(a0, a1):
        raise NotImplementedError()

    def getDiagnosticCommands____(a0):
        raise NotImplementedError()

    def getDiagnosticCommandInfo__java_lang_String____(a0, a1):
        raise NotImplementedError()

    def executeDiagnosticCommand__java_lang_String__(a0, a1):
        raise NotImplementedError()

    clazz.setNotificationEnabled__boolean__ = setNotificationEnabled__boolean__
    clazz.getDiagnosticCommands____ = getDiagnosticCommands____
    clazz.getDiagnosticCommandInfo__java_lang_String____ = getDiagnosticCommandInfo__java_lang_String____
    clazz.executeDiagnosticCommand__java_lang_String__ = executeDiagnosticCommand__java_lang_String__

