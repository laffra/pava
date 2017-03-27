def add_native_methods(clazz):
    def setNativePrintService(a0):
        raise NotImplementedError()

    def getNativePrintService():
        raise NotImplementedError()

    def getDefaultPage(a0):
        raise NotImplementedError()

    def validatePaper(a0, a1):
        raise NotImplementedError()

    def setNativeCopies(a0):
        raise NotImplementedError()

    def jobSetup(a0, a1):
        raise NotImplementedError()

    def initPrinter():
        raise NotImplementedError()

    def _startDoc(a0, a1):
        raise NotImplementedError()

    def endDoc():
        raise NotImplementedError()

    def abortDoc():
        raise NotImplementedError()

    def deleteDC(a0, a1, a2):
        raise NotImplementedError()

    def deviceStartPage(a0, a1, a2, a3):
        raise NotImplementedError()

    def deviceEndPage(a0, a1, a2):
        raise NotImplementedError()

    def printBand(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def beginPath(a0):
        raise NotImplementedError()

    def endPath(a0):
        raise NotImplementedError()

    def closeFigure(a0):
        raise NotImplementedError()

    def fillPath(a0):
        raise NotImplementedError()

    def moveTo(a0, a1, a2):
        raise NotImplementedError()

    def lineTo(a0, a1, a2):
        raise NotImplementedError()

    def polyBezierTo(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def setPolyFillMode(a0, a1):
        raise NotImplementedError()

    def selectSolidBrush(a0, a1, a2, a3):
        raise NotImplementedError()

    def getPenX(a0):
        raise NotImplementedError()

    def getPenY(a0):
        raise NotImplementedError()

    def selectClipPath(a0):
        raise NotImplementedError()

    def frameRect(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def fillRect(a0, a1, a2, a3, a4, a5, a6, a7):
        raise NotImplementedError()

    def selectPen(a0, a1, a2, a3, a4):
        raise NotImplementedError()

    def selectStylePen(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def setFont(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def setTextColor(a0, a1, a2, a3):
        raise NotImplementedError()

    def textOut(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def getGDIAdvance(a0, a1):
        raise NotImplementedError()

    def drawDIBImage(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):
        raise NotImplementedError()

    def showDocProperties(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.setNativePrintService = setNativePrintService
    clazz.getNativePrintService = getNativePrintService
    clazz.getDefaultPage = getDefaultPage
    clazz.validatePaper = validatePaper
    clazz.setNativeCopies = setNativeCopies
    clazz.jobSetup = jobSetup
    clazz.initPrinter = initPrinter
    clazz._startDoc = _startDoc
    clazz.endDoc = endDoc
    clazz.abortDoc = abortDoc
    clazz.deleteDC = staticmethod(deleteDC)
    clazz.deviceStartPage = deviceStartPage
    clazz.deviceEndPage = deviceEndPage
    clazz.printBand = printBand
    clazz.beginPath = beginPath
    clazz.endPath = endPath
    clazz.closeFigure = closeFigure
    clazz.fillPath = fillPath
    clazz.moveTo = moveTo
    clazz.lineTo = lineTo
    clazz.polyBezierTo = polyBezierTo
    clazz.setPolyFillMode = setPolyFillMode
    clazz.selectSolidBrush = selectSolidBrush
    clazz.getPenX = getPenX
    clazz.getPenY = getPenY
    clazz.selectClipPath = selectClipPath
    clazz.frameRect = frameRect
    clazz.fillRect = fillRect
    clazz.selectPen = selectPen
    clazz.selectStylePen = selectStylePen
    clazz.setFont = setFont
    clazz.setTextColor = setTextColor
    clazz.textOut = textOut
    clazz.getGDIAdvance = getGDIAdvance
    clazz.drawDIBImage = drawDIBImage
    clazz.showDocProperties = showDocProperties
    clazz.initIDs = staticmethod(initIDs)

