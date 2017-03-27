def add_native_methods(clazz):
    def _update(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def _isVisible(a0):
        raise NotImplementedError()

    def _getBounds(a0):
        raise NotImplementedError()

    def _getInstance():
        raise NotImplementedError()

    def _close(a0):
        raise NotImplementedError()

    def _getImageFileName(a0):
        raise NotImplementedError()

    def _getImageJarName(a0):
        raise NotImplementedError()

    def _setImageData(a0, a1):
        raise NotImplementedError()

    def _getScaleFactor(a0):
        raise NotImplementedError()

    clazz._update = staticmethod(_update)
    clazz._isVisible = staticmethod(_isVisible)
    clazz._getBounds = staticmethod(_getBounds)
    clazz._getInstance = staticmethod(_getInstance)
    clazz._close = staticmethod(_close)
    clazz._getImageFileName = staticmethod(_getImageFileName)
    clazz._getImageJarName = staticmethod(_getImageJarName)
    clazz._setImageData = staticmethod(_setImageData)
    clazz._getScaleFactor = staticmethod(_getScaleFactor)

