def add_native_methods(clazz):
    def initialize():
        raise NotImplementedError()

    def getDefaultLocale(a0):
        raise NotImplementedError()

    def getDateTimePattern(a0, a1, a2):
        raise NotImplementedError()

    def getCalendarID(a0):
        raise NotImplementedError()

    def getAmPmStrings(a0, a1):
        raise NotImplementedError()

    def getEras(a0, a1):
        raise NotImplementedError()

    def getMonths(a0, a1):
        raise NotImplementedError()

    def getShortMonths(a0, a1):
        raise NotImplementedError()

    def getWeekdays(a0, a1):
        raise NotImplementedError()

    def getShortWeekdays(a0, a1):
        raise NotImplementedError()

    def getNumberPattern(a0, a1):
        raise NotImplementedError()

    def isNativeDigit(a0):
        raise NotImplementedError()

    def getCurrencySymbol(a0, a1):
        raise NotImplementedError()

    def getDecimalSeparator(a0, a1):
        raise NotImplementedError()

    def getGroupingSeparator(a0, a1):
        raise NotImplementedError()

    def getInfinity(a0, a1):
        raise NotImplementedError()

    def getInternationalCurrencySymbol(a0, a1):
        raise NotImplementedError()

    def getMinusSign(a0, a1):
        raise NotImplementedError()

    def getMonetaryDecimalSeparator(a0, a1):
        raise NotImplementedError()

    def getNaN(a0, a1):
        raise NotImplementedError()

    def getPercent(a0, a1):
        raise NotImplementedError()

    def getPerMill(a0, a1):
        raise NotImplementedError()

    def getZeroDigit(a0, a1):
        raise NotImplementedError()

    def getCalendarDataValue(a0, a1):
        raise NotImplementedError()

    def getDisplayString(a0, a1, a2):
        raise NotImplementedError()

    clazz.initialize = staticmethod(initialize)
    clazz.getDefaultLocale = staticmethod(getDefaultLocale)
    clazz.getDateTimePattern = staticmethod(getDateTimePattern)
    clazz.getCalendarID = staticmethod(getCalendarID)
    clazz.getAmPmStrings = staticmethod(getAmPmStrings)
    clazz.getEras = staticmethod(getEras)
    clazz.getMonths = staticmethod(getMonths)
    clazz.getShortMonths = staticmethod(getShortMonths)
    clazz.getWeekdays = staticmethod(getWeekdays)
    clazz.getShortWeekdays = staticmethod(getShortWeekdays)
    clazz.getNumberPattern = staticmethod(getNumberPattern)
    clazz.isNativeDigit = staticmethod(isNativeDigit)
    clazz.getCurrencySymbol = staticmethod(getCurrencySymbol)
    clazz.getDecimalSeparator = staticmethod(getDecimalSeparator)
    clazz.getGroupingSeparator = staticmethod(getGroupingSeparator)
    clazz.getInfinity = staticmethod(getInfinity)
    clazz.getInternationalCurrencySymbol = staticmethod(getInternationalCurrencySymbol)
    clazz.getMinusSign = staticmethod(getMinusSign)
    clazz.getMonetaryDecimalSeparator = staticmethod(getMonetaryDecimalSeparator)
    clazz.getNaN = staticmethod(getNaN)
    clazz.getPercent = staticmethod(getPercent)
    clazz.getPerMill = staticmethod(getPerMill)
    clazz.getZeroDigit = staticmethod(getZeroDigit)
    clazz.getCalendarDataValue = staticmethod(getCalendarDataValue)
    clazz.getDisplayString = staticmethod(getDisplayString)

