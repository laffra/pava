def add_native_methods(clazz):
    def setNotificationEnabled(a0):
        raise NotImplementedError()

    def getDiagnosticCommands():
        raise NotImplementedError()

    def getDiagnosticCommandInfo(a0):
        raise NotImplementedError()

    def executeDiagnosticCommand(a0):
        raise NotImplementedError()

    clazz.setNotificationEnabled = setNotificationEnabled
    clazz.getDiagnosticCommands = getDiagnosticCommands
    clazz.getDiagnosticCommandInfo = getDiagnosticCommandInfo
    clazz.executeDiagnosticCommand = executeDiagnosticCommand

