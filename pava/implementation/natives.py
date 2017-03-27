# Declarations for all native methods


import com

def nativeObjectInit(a0, a1):
    raise NotImplementedError("nativeObjectInit")
com.sun.demo.jvmti.hprof.Tracker.nativeObjectInit = staticmethod(nativeObjectInit)

def nativeNewArray(a0, a1):
    raise NotImplementedError("nativeNewArray")
com.sun.demo.jvmti.hprof.Tracker.nativeNewArray = staticmethod(nativeNewArray)

def nativeCallSite(a0, a1, a2):
    raise NotImplementedError("nativeCallSite")
com.sun.demo.jvmti.hprof.Tracker.nativeCallSite = staticmethod(nativeCallSite)

def nativeReturnSite(a0, a1, a2):
    raise NotImplementedError("nativeReturnSite")
com.sun.demo.jvmti.hprof.Tracker.nativeReturnSite = staticmethod(nativeReturnSite)

def initReaderIDs(a0, a1, a2):
    raise NotImplementedError("initReaderIDs")
com.sun.imageio.plugins.jpeg.JPEGImageReader.initReaderIDs = staticmethod(initReaderIDs)

def initJPEGImageReader():
    raise NotImplementedError("initJPEGImageReader")
com.sun.imageio.plugins.jpeg.JPEGImageReader.initJPEGImageReader = initJPEGImageReader

def setSource(a0):
    raise NotImplementedError("setSource")
com.sun.imageio.plugins.jpeg.JPEGImageReader.setSource = setSource

def readImageHeader(a0, a1, a2):
    raise NotImplementedError("readImageHeader")
com.sun.imageio.plugins.jpeg.JPEGImageReader.readImageHeader = readImageHeader

def setOutColorSpace(a0, a1):
    raise NotImplementedError("setOutColorSpace")
com.sun.imageio.plugins.jpeg.JPEGImageReader.setOutColorSpace = setOutColorSpace

def readImage(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16):
    raise NotImplementedError("readImage")
com.sun.imageio.plugins.jpeg.JPEGImageReader.readImage = readImage

def abortRead(a0):
    raise NotImplementedError("abortRead")
com.sun.imageio.plugins.jpeg.JPEGImageReader.abortRead = abortRead

def resetLibraryState(a0):
    raise NotImplementedError("resetLibraryState")
com.sun.imageio.plugins.jpeg.JPEGImageReader.resetLibraryState = resetLibraryState

def resetReader(a0):
    raise NotImplementedError("resetReader")
com.sun.imageio.plugins.jpeg.JPEGImageReader.resetReader = resetReader

def disposeReader(a0):
    raise NotImplementedError("disposeReader")
com.sun.imageio.plugins.jpeg.JPEGImageReader.disposeReader = staticmethod(disposeReader)

def initWriterIDs(a0, a1):
    raise NotImplementedError("initWriterIDs")
com.sun.imageio.plugins.jpeg.JPEGImageWriter.initWriterIDs = staticmethod(initWriterIDs)

def initJPEGImageWriter():
    raise NotImplementedError("initJPEGImageWriter")
com.sun.imageio.plugins.jpeg.JPEGImageWriter.initJPEGImageWriter = initJPEGImageWriter

def setDest(a0):
    raise NotImplementedError("setDest")
com.sun.imageio.plugins.jpeg.JPEGImageWriter.setDest = setDest

def writeImage(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25):
    raise NotImplementedError("writeImage")
com.sun.imageio.plugins.jpeg.JPEGImageWriter.writeImage = writeImage

def writeTables(a0, a1, a2, a3):
    raise NotImplementedError("writeTables")
com.sun.imageio.plugins.jpeg.JPEGImageWriter.writeTables = writeTables

def abortWrite(a0):
    raise NotImplementedError("abortWrite")
com.sun.imageio.plugins.jpeg.JPEGImageWriter.abortWrite = abortWrite

def resetWriter(a0):
    raise NotImplementedError("resetWriter")
com.sun.imageio.plugins.jpeg.JPEGImageWriter.resetWriter = resetWriter

def disposeWriter(a0):
    raise NotImplementedError("disposeWriter")
com.sun.imageio.plugins.jpeg.JPEGImageWriter.disposeWriter = staticmethod(disposeWriter)

def initIDs():
    raise NotImplementedError("initIDs")
com.sun.java.util.jar.pack.NativeUnpack.initIDs = staticmethod(initIDs)

def start(a0, a1):
    raise NotImplementedError("start")
com.sun.java.util.jar.pack.NativeUnpack.start = start

def getNextFile(a0):
    raise NotImplementedError("getNextFile")
com.sun.java.util.jar.pack.NativeUnpack.getNextFile = getNextFile

def getUnusedInput():
    raise NotImplementedError("getUnusedInput")
com.sun.java.util.jar.pack.NativeUnpack.getUnusedInput = getUnusedInput

def finish():
    raise NotImplementedError("finish")
com.sun.java.util.jar.pack.NativeUnpack.finish = finish

def setOption(a0, a1):
    raise NotImplementedError("setOption")
com.sun.java.util.jar.pack.NativeUnpack.setOption = setOption

def getOption(a0):
    raise NotImplementedError("getOption")
com.sun.java.util.jar.pack.NativeUnpack.getOption = getOption

def nGetFormats(a0, a1, a2, a3):
    raise NotImplementedError("nGetFormats")
com.sun.media.sound.DirectAudioDevice.nGetFormats = staticmethod(nGetFormats)

def nOpen(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    raise NotImplementedError("nOpen")
com.sun.media.sound.DirectAudioDevice.nOpen = staticmethod(nOpen)

def nStart(a0, a1):
    raise NotImplementedError("nStart")
com.sun.media.sound.DirectAudioDevice.nStart = staticmethod(nStart)

def nStop(a0, a1):
    raise NotImplementedError("nStop")
com.sun.media.sound.DirectAudioDevice.nStop = staticmethod(nStop)

def nClose(a0, a1):
    raise NotImplementedError("nClose")
com.sun.media.sound.DirectAudioDevice.nClose = staticmethod(nClose)

def nWrite(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("nWrite")
com.sun.media.sound.DirectAudioDevice.nWrite = staticmethod(nWrite)

def nRead(a0, a1, a2, a3, a4):
    raise NotImplementedError("nRead")
com.sun.media.sound.DirectAudioDevice.nRead = staticmethod(nRead)

def nGetBufferSize(a0, a1):
    raise NotImplementedError("nGetBufferSize")
com.sun.media.sound.DirectAudioDevice.nGetBufferSize = staticmethod(nGetBufferSize)

def nIsStillDraining(a0, a1):
    raise NotImplementedError("nIsStillDraining")
com.sun.media.sound.DirectAudioDevice.nIsStillDraining = staticmethod(nIsStillDraining)

def nFlush(a0, a1):
    raise NotImplementedError("nFlush")
com.sun.media.sound.DirectAudioDevice.nFlush = staticmethod(nFlush)

def nAvailable(a0, a1):
    raise NotImplementedError("nAvailable")
com.sun.media.sound.DirectAudioDevice.nAvailable = staticmethod(nAvailable)

def nGetBytePosition(a0, a1, a2):
    raise NotImplementedError("nGetBytePosition")
com.sun.media.sound.DirectAudioDevice.nGetBytePosition = staticmethod(nGetBytePosition)

def nSetBytePosition(a0, a1, a2):
    raise NotImplementedError("nSetBytePosition")
com.sun.media.sound.DirectAudioDevice.nSetBytePosition = staticmethod(nSetBytePosition)

def nRequiresServicing(a0, a1):
    raise NotImplementedError("nRequiresServicing")
com.sun.media.sound.DirectAudioDevice.nRequiresServicing = staticmethod(nRequiresServicing)

def nService(a0, a1):
    raise NotImplementedError("nService")
com.sun.media.sound.DirectAudioDevice.nService = staticmethod(nService)

def nGetNumDevices():
    raise NotImplementedError("nGetNumDevices")
com.sun.media.sound.DirectAudioDeviceProvider.nGetNumDevices = staticmethod(nGetNumDevices)

def nNewDirectAudioDeviceInfo(a0):
    raise NotImplementedError("nNewDirectAudioDeviceInfo")
com.sun.media.sound.DirectAudioDeviceProvider.nNewDirectAudioDeviceInfo = staticmethod(nNewDirectAudioDeviceInfo)

def nOpen(a0):
    raise NotImplementedError("nOpen")
com.sun.media.sound.MidiInDevice.nOpen = nOpen

def nClose(a0):
    raise NotImplementedError("nClose")
com.sun.media.sound.MidiInDevice.nClose = nClose

def nStart(a0):
    raise NotImplementedError("nStart")
com.sun.media.sound.MidiInDevice.nStart = nStart

def nStop(a0):
    raise NotImplementedError("nStop")
com.sun.media.sound.MidiInDevice.nStop = nStop

def nGetTimeStamp(a0):
    raise NotImplementedError("nGetTimeStamp")
com.sun.media.sound.MidiInDevice.nGetTimeStamp = nGetTimeStamp

def nGetMessages(a0):
    raise NotImplementedError("nGetMessages")
com.sun.media.sound.MidiInDevice.nGetMessages = nGetMessages

def nGetNumDevices():
    raise NotImplementedError("nGetNumDevices")
com.sun.media.sound.MidiInDeviceProvider.nGetNumDevices = staticmethod(nGetNumDevices)

def nGetName(a0):
    raise NotImplementedError("nGetName")
com.sun.media.sound.MidiInDeviceProvider.nGetName = staticmethod(nGetName)

def nGetVendor(a0):
    raise NotImplementedError("nGetVendor")
com.sun.media.sound.MidiInDeviceProvider.nGetVendor = staticmethod(nGetVendor)

def nGetDescription(a0):
    raise NotImplementedError("nGetDescription")
com.sun.media.sound.MidiInDeviceProvider.nGetDescription = staticmethod(nGetDescription)

def nGetVersion(a0):
    raise NotImplementedError("nGetVersion")
com.sun.media.sound.MidiInDeviceProvider.nGetVersion = staticmethod(nGetVersion)

def nOpen(a0):
    raise NotImplementedError("nOpen")
com.sun.media.sound.MidiOutDevice.nOpen = nOpen

def nClose(a0):
    raise NotImplementedError("nClose")
com.sun.media.sound.MidiOutDevice.nClose = nClose

def nSendShortMessage(a0, a1, a2):
    raise NotImplementedError("nSendShortMessage")
com.sun.media.sound.MidiOutDevice.nSendShortMessage = nSendShortMessage

def nSendLongMessage(a0, a1, a2, a3):
    raise NotImplementedError("nSendLongMessage")
com.sun.media.sound.MidiOutDevice.nSendLongMessage = nSendLongMessage

def nGetTimeStamp(a0):
    raise NotImplementedError("nGetTimeStamp")
com.sun.media.sound.MidiOutDevice.nGetTimeStamp = nGetTimeStamp

def nGetNumDevices():
    raise NotImplementedError("nGetNumDevices")
com.sun.media.sound.MidiOutDeviceProvider.nGetNumDevices = staticmethod(nGetNumDevices)

def nGetName(a0):
    raise NotImplementedError("nGetName")
com.sun.media.sound.MidiOutDeviceProvider.nGetName = staticmethod(nGetName)

def nGetVendor(a0):
    raise NotImplementedError("nGetVendor")
com.sun.media.sound.MidiOutDeviceProvider.nGetVendor = staticmethod(nGetVendor)

def nGetDescription(a0):
    raise NotImplementedError("nGetDescription")
com.sun.media.sound.MidiOutDeviceProvider.nGetDescription = staticmethod(nGetDescription)

def nGetVersion(a0):
    raise NotImplementedError("nGetVersion")
com.sun.media.sound.MidiOutDeviceProvider.nGetVersion = staticmethod(nGetVersion)

def nOpen(a0):
    raise NotImplementedError("nOpen")
com.sun.media.sound.PortMixer.nOpen = staticmethod(nOpen)

def nClose(a0):
    raise NotImplementedError("nClose")
com.sun.media.sound.PortMixer.nClose = staticmethod(nClose)

def nGetPortCount(a0):
    raise NotImplementedError("nGetPortCount")
com.sun.media.sound.PortMixer.nGetPortCount = staticmethod(nGetPortCount)

def nGetPortType(a0, a1):
    raise NotImplementedError("nGetPortType")
com.sun.media.sound.PortMixer.nGetPortType = staticmethod(nGetPortType)

def nGetPortName(a0, a1):
    raise NotImplementedError("nGetPortName")
com.sun.media.sound.PortMixer.nGetPortName = staticmethod(nGetPortName)

def nGetControls(a0, a1, a2):
    raise NotImplementedError("nGetControls")
com.sun.media.sound.PortMixer.nGetControls = staticmethod(nGetControls)

def nControlSetIntValue(a0, a1):
    raise NotImplementedError("nControlSetIntValue")
com.sun.media.sound.PortMixer.nControlSetIntValue = staticmethod(nControlSetIntValue)

def nControlGetIntValue(a0):
    raise NotImplementedError("nControlGetIntValue")
com.sun.media.sound.PortMixer.nControlGetIntValue = staticmethod(nControlGetIntValue)

def nControlSetFloatValue(a0, a1):
    raise NotImplementedError("nControlSetFloatValue")
com.sun.media.sound.PortMixer.nControlSetFloatValue = staticmethod(nControlSetFloatValue)

def nControlGetFloatValue(a0):
    raise NotImplementedError("nControlGetFloatValue")
com.sun.media.sound.PortMixer.nControlGetFloatValue = staticmethod(nControlGetFloatValue)

def nGetNumDevices():
    raise NotImplementedError("nGetNumDevices")
com.sun.media.sound.PortMixerProvider.nGetNumDevices = staticmethod(nGetNumDevices)

def nNewPortMixerInfo(a0):
    raise NotImplementedError("nNewPortMixerInfo")
com.sun.media.sound.PortMixerProvider.nNewPortMixerInfo = staticmethod(nNewPortMixerInfo)

def getCurrent(a0):
    raise NotImplementedError("getCurrent")
com.sun.security.auth.module.NTSystem.getCurrent = getCurrent

def getImpersonationToken0():
    raise NotImplementedError("getImpersonationToken0")
com.sun.security.auth.module.NTSystem.getImpersonationToken0 = getImpersonationToken0

import java

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Button.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Checkbox.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.CheckboxMenuItem.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Choice.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.FileDialog.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Menu.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.MenuItem.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.ScrollPane.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.ScrollPaneAdjustable.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Scrollbar.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.TextArea.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.TextField.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.image.Kernel.initIDs = staticmethod(initIDs)

def encoding():
    raise NotImplementedError("encoding")
java.io.Console.encoding = staticmethod(encoding)

def echo(a0):
    raise NotImplementedError("echo")
java.io.Console.echo = staticmethod(echo)

def istty():
    raise NotImplementedError("istty")
java.io.Console.istty = staticmethod(istty)

def getStillActive():
    raise NotImplementedError("getStillActive")
java.lang.ProcessImpl.getStillActive = staticmethod(getStillActive)

def getExitCodeProcess(a0):
    raise NotImplementedError("getExitCodeProcess")
java.lang.ProcessImpl.getExitCodeProcess = staticmethod(getExitCodeProcess)

def waitForInterruptibly(a0):
    raise NotImplementedError("waitForInterruptibly")
java.lang.ProcessImpl.waitForInterruptibly = staticmethod(waitForInterruptibly)

def waitForTimeoutInterruptibly(a0, a1):
    raise NotImplementedError("waitForTimeoutInterruptibly")
java.lang.ProcessImpl.waitForTimeoutInterruptibly = staticmethod(waitForTimeoutInterruptibly)

def terminateProcess(a0):
    raise NotImplementedError("terminateProcess")
java.lang.ProcessImpl.terminateProcess = staticmethod(terminateProcess)

def isProcessAlive(a0):
    raise NotImplementedError("isProcessAlive")
java.lang.ProcessImpl.isProcessAlive = staticmethod(isProcessAlive)

def create(a0, a1, a2, a3, a4):
    raise NotImplementedError("create")
java.lang.ProcessImpl.create = staticmethod(create)

def openForAtomicAppend(a0):
    raise NotImplementedError("openForAtomicAppend")
java.lang.ProcessImpl.openForAtomicAppend = staticmethod(openForAtomicAppend)

def closeHandle(a0):
    raise NotImplementedError("closeHandle")
java.lang.ProcessImpl.closeHandle = staticmethod(closeHandle)

def socketRead0(a0, a1, a2, a3, a4):
    raise NotImplementedError("socketRead0")
java.net.SocketInputStream.socketRead0 = socketRead0

def init():
    raise NotImplementedError("init")
java.net.SocketInputStream.init = staticmethod(init)

def socketWrite0(a0, a1, a2, a3):
    raise NotImplementedError("socketWrite0")
java.net.SocketOutputStream.socketWrite0 = socketWrite0

def init():
    raise NotImplementedError("init")
java.net.SocketOutputStream.init = staticmethod(init)

def initProto():
    raise NotImplementedError("initProto")
java.net.TwoStacksPlainSocketImpl.initProto = staticmethod(initProto)

def socketCreate(a0):
    raise NotImplementedError("socketCreate")
java.net.TwoStacksPlainSocketImpl.socketCreate = socketCreate

def socketConnect(a0, a1, a2):
    raise NotImplementedError("socketConnect")
java.net.TwoStacksPlainSocketImpl.socketConnect = socketConnect

def socketBind(a0, a1, a2):
    raise NotImplementedError("socketBind")
java.net.TwoStacksPlainSocketImpl.socketBind = socketBind

def socketListen(a0):
    raise NotImplementedError("socketListen")
java.net.TwoStacksPlainSocketImpl.socketListen = socketListen

def socketAccept(a0):
    raise NotImplementedError("socketAccept")
java.net.TwoStacksPlainSocketImpl.socketAccept = socketAccept

def socketAvailable():
    raise NotImplementedError("socketAvailable")
java.net.TwoStacksPlainSocketImpl.socketAvailable = socketAvailable

def socketClose0(a0):
    raise NotImplementedError("socketClose0")
java.net.TwoStacksPlainSocketImpl.socketClose0 = socketClose0

def socketShutdown(a0):
    raise NotImplementedError("socketShutdown")
java.net.TwoStacksPlainSocketImpl.socketShutdown = socketShutdown

def socketNativeSetOption(a0, a1, a2):
    raise NotImplementedError("socketNativeSetOption")
java.net.TwoStacksPlainSocketImpl.socketNativeSetOption = socketNativeSetOption

def socketGetOption(a0, a1):
    raise NotImplementedError("socketGetOption")
java.net.TwoStacksPlainSocketImpl.socketGetOption = socketGetOption

def socketSendUrgentData(a0):
    raise NotImplementedError("socketSendUrgentData")
java.net.TwoStacksPlainSocketImpl.socketSendUrgentData = socketSendUrgentData

def isSetUID():
    raise NotImplementedError("isSetUID")
java.util.logging.FileHandler.isSetUID = staticmethod(isSetUID)

def WindowsRegOpenKey(a0, a1, a2):
    raise NotImplementedError("WindowsRegOpenKey")
java.util.prefs.WindowsPreferences.WindowsRegOpenKey = staticmethod(WindowsRegOpenKey)

def WindowsRegCloseKey(a0):
    raise NotImplementedError("WindowsRegCloseKey")
java.util.prefs.WindowsPreferences.WindowsRegCloseKey = staticmethod(WindowsRegCloseKey)

def WindowsRegCreateKeyEx(a0, a1):
    raise NotImplementedError("WindowsRegCreateKeyEx")
java.util.prefs.WindowsPreferences.WindowsRegCreateKeyEx = staticmethod(WindowsRegCreateKeyEx)

def WindowsRegDeleteKey(a0, a1):
    raise NotImplementedError("WindowsRegDeleteKey")
java.util.prefs.WindowsPreferences.WindowsRegDeleteKey = staticmethod(WindowsRegDeleteKey)

def WindowsRegFlushKey(a0):
    raise NotImplementedError("WindowsRegFlushKey")
java.util.prefs.WindowsPreferences.WindowsRegFlushKey = staticmethod(WindowsRegFlushKey)

def WindowsRegQueryValueEx(a0, a1):
    raise NotImplementedError("WindowsRegQueryValueEx")
java.util.prefs.WindowsPreferences.WindowsRegQueryValueEx = staticmethod(WindowsRegQueryValueEx)

def WindowsRegSetValueEx(a0, a1, a2):
    raise NotImplementedError("WindowsRegSetValueEx")
java.util.prefs.WindowsPreferences.WindowsRegSetValueEx = staticmethod(WindowsRegSetValueEx)

def WindowsRegDeleteValue(a0, a1):
    raise NotImplementedError("WindowsRegDeleteValue")
java.util.prefs.WindowsPreferences.WindowsRegDeleteValue = staticmethod(WindowsRegDeleteValue)

def WindowsRegQueryInfoKey(a0):
    raise NotImplementedError("WindowsRegQueryInfoKey")
java.util.prefs.WindowsPreferences.WindowsRegQueryInfoKey = staticmethod(WindowsRegQueryInfoKey)

def WindowsRegEnumKeyEx(a0, a1, a2):
    raise NotImplementedError("WindowsRegEnumKeyEx")
java.util.prefs.WindowsPreferences.WindowsRegEnumKeyEx = staticmethod(WindowsRegEnumKeyEx)

def WindowsRegEnumValue(a0, a1, a2):
    raise NotImplementedError("WindowsRegEnumValue")
java.util.prefs.WindowsPreferences.WindowsRegEnumValue = staticmethod(WindowsRegEnumValue)

def update(a0, a1):
    raise NotImplementedError("update")
java.util.zip.Adler32.update = staticmethod(update)

def updateBytes(a0, a1, a2, a3):
    raise NotImplementedError("updateBytes")
java.util.zip.Adler32.updateBytes = staticmethod(updateBytes)

def updateByteBuffer(a0, a1, a2, a3):
    raise NotImplementedError("updateByteBuffer")
java.util.zip.Adler32.updateByteBuffer = staticmethod(updateByteBuffer)

def initIDs():
    raise NotImplementedError("initIDs")
java.util.zip.Deflater.initIDs = staticmethod(initIDs)

def init(a0, a1, a2):
    raise NotImplementedError("init")
java.util.zip.Deflater.init = staticmethod(init)

def setDictionary(a0, a1, a2, a3):
    raise NotImplementedError("setDictionary")
java.util.zip.Deflater.setDictionary = staticmethod(setDictionary)

def deflateBytes(a0, a1, a2, a3, a4):
    raise NotImplementedError("deflateBytes")
java.util.zip.Deflater.deflateBytes = deflateBytes

def getAdler(a0):
    raise NotImplementedError("getAdler")
java.util.zip.Deflater.getAdler = staticmethod(getAdler)

def reset(a0):
    raise NotImplementedError("reset")
java.util.zip.Deflater.reset = staticmethod(reset)

def end(a0):
    raise NotImplementedError("end")
java.util.zip.Deflater.end = staticmethod(end)

import jdk

def setVmMemoryPressure(a0):
    raise NotImplementedError("setVmMemoryPressure")
jdk.internal.cmm.SystemResourcePressureImpl.setVmMemoryPressure = setVmMemoryPressure

def getVmMemoryPressure():
    raise NotImplementedError("getVmMemoryPressure")
jdk.internal.cmm.SystemResourcePressureImpl.getVmMemoryPressure = getVmMemoryPressure

def retransformClasses0(a0):
    raise NotImplementedError("retransformClasses0")
jdk.internal.instrumentation.Tracer.retransformClasses0 = staticmethod(retransformClasses0)

def init():
    raise NotImplementedError("init")
jdk.internal.instrumentation.Tracer.init = staticmethod(init)

def featuresEnabled0():
    raise NotImplementedError("featuresEnabled0")
jdk.management.resource.internal.ResourceNatives.featuresEnabled0 = staticmethod(featuresEnabled0)

def sampleInterval0():
    raise NotImplementedError("sampleInterval0")
jdk.management.resource.internal.ResourceNatives.sampleInterval0 = staticmethod(sampleInterval0)

def getThreadStats0(a0, a1, a2):
    raise NotImplementedError("getThreadStats0")
jdk.management.resource.internal.ResourceNatives.getThreadStats0 = staticmethod(getThreadStats0)

def getCurrentThreadCPUTime0():
    raise NotImplementedError("getCurrentThreadCPUTime0")
jdk.management.resource.internal.ResourceNatives.getCurrentThreadCPUTime0 = staticmethod(getCurrentThreadCPUTime0)

def getCurrentThreadAllocatedHeap0():
    raise NotImplementedError("getCurrentThreadAllocatedHeap0")
jdk.management.resource.internal.ResourceNatives.getCurrentThreadAllocatedHeap0 = staticmethod(getCurrentThreadAllocatedHeap0)

def createResourceContext0(a0):
    raise NotImplementedError("createResourceContext0")
jdk.management.resource.internal.ResourceNatives.createResourceContext0 = staticmethod(createResourceContext0)

def destroyResourceContext0(a0, a1):
    raise NotImplementedError("destroyResourceContext0")
jdk.management.resource.internal.ResourceNatives.destroyResourceContext0 = staticmethod(destroyResourceContext0)

def setThreadResourceContext0(a0, a1):
    raise NotImplementedError("setThreadResourceContext0")
jdk.management.resource.internal.ResourceNatives.setThreadResourceContext0 = staticmethod(setThreadResourceContext0)

def getThreadResourceContext0(a0):
    raise NotImplementedError("getThreadResourceContext0")
jdk.management.resource.internal.ResourceNatives.getThreadResourceContext0 = staticmethod(getThreadResourceContext0)

def getContextsRetainedMemory0(a0, a1, a2):
    raise NotImplementedError("getContextsRetainedMemory0")
jdk.management.resource.internal.ResourceNatives.getContextsRetainedMemory0 = staticmethod(getContextsRetainedMemory0)

def setRetainedMemoryNotificationEnabled0(a0):
    raise NotImplementedError("setRetainedMemoryNotificationEnabled0")
jdk.management.resource.internal.ResourceNatives.setRetainedMemoryNotificationEnabled0 = staticmethod(setRetainedMemoryNotificationEnabled0)

def computeRetainedMemory0(a0, a1):
    raise NotImplementedError("computeRetainedMemory0")
jdk.management.resource.internal.ResourceNatives.computeRetainedMemory0 = staticmethod(computeRetainedMemory0)

import sun

def setCTracingOn(a0):
    raise NotImplementedError("setCTracingOn")
sun.awt.DebugSettings.setCTracingOn = setCTracingOn

def fillPointWithCoords(a0):
    raise NotImplementedError("fillPointWithCoords")
sun.awt.DefaultMouseInfoPeer.fillPointWithCoords = fillPointWithCoords

def isWindowUnderMouse(a0):
    raise NotImplementedError("isWindowUnderMouse")
sun.awt.DefaultMouseInfoPeer.isWindowUnderMouse = isWindowUnderMouse

def getElem(a0, a1, a2):
    raise NotImplementedError("getElem")
sun.awt.image.DataBufferNative.getElem = getElem

def setElem(a0, a1, a2, a3):
    raise NotImplementedError("setElem")
sun.awt.image.DataBufferNative.setElem = setElem

def init():
    raise NotImplementedError("init")
sun.awt.image.ImagingLib.init = staticmethod(init)

def transformBI(a0, a1, a2, a3):
    raise NotImplementedError("transformBI")
sun.awt.image.ImagingLib.transformBI = staticmethod(transformBI)

def transformRaster(a0, a1, a2, a3):
    raise NotImplementedError("transformRaster")
sun.awt.image.ImagingLib.transformRaster = staticmethod(transformRaster)

def convolveBI(a0, a1, a2, a3):
    raise NotImplementedError("convolveBI")
sun.awt.image.ImagingLib.convolveBI = staticmethod(convolveBI)

def convolveRaster(a0, a1, a2, a3):
    raise NotImplementedError("convolveRaster")
sun.awt.image.ImagingLib.convolveRaster = staticmethod(convolveRaster)

def lookupByteBI(a0, a1, a2):
    raise NotImplementedError("lookupByteBI")
sun.awt.image.ImagingLib.lookupByteBI = staticmethod(lookupByteBI)

def lookupByteRaster(a0, a1, a2):
    raise NotImplementedError("lookupByteRaster")
sun.awt.image.ImagingLib.lookupByteRaster = staticmethod(lookupByteRaster)

def initIDs(a0):
    raise NotImplementedError("initIDs")
sun.awt.image.JPEGImageDecoder.initIDs = staticmethod(initIDs)

def readImage(a0, a1):
    raise NotImplementedError("readImage")
sun.awt.image.JPEGImageDecoder.readImage = readImage

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.image.ShortComponentRaster.initIDs = staticmethod(initIDs)

def initDecoder(a0):
    raise NotImplementedError("initDecoder")
sun.awt.image.codec.JPEGImageDecoderImpl.initDecoder = initDecoder

def readJPEGStream(a0, a1, a2):
    raise NotImplementedError("readJPEGStream")
sun.awt.image.codec.JPEGImageDecoderImpl.readJPEGStream = readJPEGStream

def initEncoder(a0):
    raise NotImplementedError("initEncoder")
sun.awt.image.codec.JPEGImageEncoderImpl.initEncoder = initEncoder

def writeJPEGStream(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("writeJPEGStream")
sun.awt.image.codec.JPEGImageEncoderImpl.writeJPEGStream = writeJPEGStream

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.shell.Win32ShellFolder2.initIDs = staticmethod(initIDs)

def initDesktop():
    raise NotImplementedError("initDesktop")
sun.awt.shell.Win32ShellFolder2.initDesktop = initDesktop

def initSpecial(a0, a1):
    raise NotImplementedError("initSpecial")
sun.awt.shell.Win32ShellFolder2.initSpecial = initSpecial

def getNextPIDLEntry(a0):
    raise NotImplementedError("getNextPIDLEntry")
sun.awt.shell.Win32ShellFolder2.getNextPIDLEntry = staticmethod(getNextPIDLEntry)

def copyFirstPIDLEntry(a0):
    raise NotImplementedError("copyFirstPIDLEntry")
sun.awt.shell.Win32ShellFolder2.copyFirstPIDLEntry = staticmethod(copyFirstPIDLEntry)

def combinePIDLs(a0, a1):
    raise NotImplementedError("combinePIDLs")
sun.awt.shell.Win32ShellFolder2.combinePIDLs = staticmethod(combinePIDLs)

def releasePIDL(a0):
    raise NotImplementedError("releasePIDL")
sun.awt.shell.Win32ShellFolder2.releasePIDL = staticmethod(releasePIDL)

def releaseIShellFolder(a0):
    raise NotImplementedError("releaseIShellFolder")
sun.awt.shell.Win32ShellFolder2.releaseIShellFolder = staticmethod(releaseIShellFolder)

def compareIDs(a0, a1, a2):
    raise NotImplementedError("compareIDs")
sun.awt.shell.Win32ShellFolder2.compareIDs = staticmethod(compareIDs)

def getAttributes0(a0, a1, a2):
    raise NotImplementedError("getAttributes0")
sun.awt.shell.Win32ShellFolder2.getAttributes0 = staticmethod(getAttributes0)

def getFileSystemPath0(a0):
    raise NotImplementedError("getFileSystemPath0")
sun.awt.shell.Win32ShellFolder2.getFileSystemPath0 = staticmethod(getFileSystemPath0)

def getEnumObjects(a0, a1, a2):
    raise NotImplementedError("getEnumObjects")
sun.awt.shell.Win32ShellFolder2.getEnumObjects = getEnumObjects

def getNextChild(a0):
    raise NotImplementedError("getNextChild")
sun.awt.shell.Win32ShellFolder2.getNextChild = getNextChild

def releaseEnumObjects(a0):
    raise NotImplementedError("releaseEnumObjects")
sun.awt.shell.Win32ShellFolder2.releaseEnumObjects = releaseEnumObjects

def bindToObject(a0, a1):
    raise NotImplementedError("bindToObject")
sun.awt.shell.Win32ShellFolder2.bindToObject = staticmethod(bindToObject)

def getLinkLocation(a0, a1, a2):
    raise NotImplementedError("getLinkLocation")
sun.awt.shell.Win32ShellFolder2.getLinkLocation = staticmethod(getLinkLocation)

def parseDisplayName0(a0, a1):
    raise NotImplementedError("parseDisplayName0")
sun.awt.shell.Win32ShellFolder2.parseDisplayName0 = staticmethod(parseDisplayName0)

def getDisplayNameOf(a0, a1, a2):
    raise NotImplementedError("getDisplayNameOf")
sun.awt.shell.Win32ShellFolder2.getDisplayNameOf = staticmethod(getDisplayNameOf)

def getFolderType(a0):
    raise NotImplementedError("getFolderType")
sun.awt.shell.Win32ShellFolder2.getFolderType = staticmethod(getFolderType)

def getExecutableType(a0):
    raise NotImplementedError("getExecutableType")
sun.awt.shell.Win32ShellFolder2.getExecutableType = getExecutableType

def getIShellIcon(a0):
    raise NotImplementedError("getIShellIcon")
sun.awt.shell.Win32ShellFolder2.getIShellIcon = staticmethod(getIShellIcon)

def getIconIndex(a0, a1):
    raise NotImplementedError("getIconIndex")
sun.awt.shell.Win32ShellFolder2.getIconIndex = staticmethod(getIconIndex)

def getIcon(a0, a1):
    raise NotImplementedError("getIcon")
sun.awt.shell.Win32ShellFolder2.getIcon = staticmethod(getIcon)

def extractIcon(a0, a1, a2):
    raise NotImplementedError("extractIcon")
sun.awt.shell.Win32ShellFolder2.extractIcon = staticmethod(extractIcon)

def getSystemIcon(a0):
    raise NotImplementedError("getSystemIcon")
sun.awt.shell.Win32ShellFolder2.getSystemIcon = staticmethod(getSystemIcon)

def getIconResource(a0, a1, a2, a3, a4):
    raise NotImplementedError("getIconResource")
sun.awt.shell.Win32ShellFolder2.getIconResource = staticmethod(getIconResource)

def getIconBits(a0, a1):
    raise NotImplementedError("getIconBits")
sun.awt.shell.Win32ShellFolder2.getIconBits = staticmethod(getIconBits)

def disposeIcon(a0):
    raise NotImplementedError("disposeIcon")
sun.awt.shell.Win32ShellFolder2.disposeIcon = staticmethod(disposeIcon)

def getStandardViewButton0(a0):
    raise NotImplementedError("getStandardViewButton0")
sun.awt.shell.Win32ShellFolder2.getStandardViewButton0 = staticmethod(getStandardViewButton0)

def doGetColumnInfo(a0):
    raise NotImplementedError("doGetColumnInfo")
sun.awt.shell.Win32ShellFolder2.doGetColumnInfo = doGetColumnInfo

def doGetColumnValue(a0, a1, a2):
    raise NotImplementedError("doGetColumnValue")
sun.awt.shell.Win32ShellFolder2.doGetColumnValue = doGetColumnValue

def compareIDsByColumn(a0, a1, a2, a3):
    raise NotImplementedError("compareIDsByColumn")
sun.awt.shell.Win32ShellFolder2.compareIDsByColumn = staticmethod(compareIDsByColumn)

def initIDs(a0):
    raise NotImplementedError("initIDs")
sun.awt.windows.WBufferStrategy.initIDs = staticmethod(initIDs)

def getDrawBuffer(a0):
    raise NotImplementedError("getDrawBuffer")
sun.awt.windows.WBufferStrategy.getDrawBuffer = staticmethod(getDrawBuffer)

def setLabel(a0):
    raise NotImplementedError("setLabel")
sun.awt.windows.WButtonPeer.setLabel = setLabel

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WButtonPeer.create = create

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WButtonPeer.initIDs = staticmethod(initIDs)

def setState(a0):
    raise NotImplementedError("setState")
sun.awt.windows.WCheckboxMenuItemPeer.setState = setState

def setState(a0):
    raise NotImplementedError("setState")
sun.awt.windows.WCheckboxPeer.setState = setState

def setCheckboxGroup(a0):
    raise NotImplementedError("setCheckboxGroup")
sun.awt.windows.WCheckboxPeer.setCheckboxGroup = setCheckboxGroup

def setLabel(a0):
    raise NotImplementedError("setLabel")
sun.awt.windows.WCheckboxPeer.setLabel = setLabel

def getCheckMarkSize():
    raise NotImplementedError("getCheckMarkSize")
sun.awt.windows.WCheckboxPeer.getCheckMarkSize = staticmethod(getCheckMarkSize)

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WCheckboxPeer.create = create

def select(a0):
    raise NotImplementedError("select")
sun.awt.windows.WChoicePeer.select = select

def removeAll():
    raise NotImplementedError("removeAll")
sun.awt.windows.WChoicePeer.removeAll = removeAll

def remove(a0):
    raise NotImplementedError("remove")
sun.awt.windows.WChoicePeer.remove = remove

def addItems(a0, a1):
    raise NotImplementedError("addItems")
sun.awt.windows.WChoicePeer.addItems = addItems

def reshape(a0, a1, a2, a3):
    raise NotImplementedError("reshape")
sun.awt.windows.WChoicePeer.reshape = reshape

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WChoicePeer.create = create

def closeList():
    raise NotImplementedError("closeList")
sun.awt.windows.WChoicePeer.closeList = closeList

def openClipboard(a0):
    raise NotImplementedError("openClipboard")
sun.awt.windows.WClipboard.openClipboard = openClipboard

def closeClipboard():
    raise NotImplementedError("closeClipboard")
sun.awt.windows.WClipboard.closeClipboard = closeClipboard

def publishClipboardData(a0, a1):
    raise NotImplementedError("publishClipboardData")
sun.awt.windows.WClipboard.publishClipboardData = publishClipboardData

def init():
    raise NotImplementedError("init")
sun.awt.windows.WClipboard.init = staticmethod(init)

def getClipboardFormats():
    raise NotImplementedError("getClipboardFormats")
sun.awt.windows.WClipboard.getClipboardFormats = getClipboardFormats

def getClipboardData(a0):
    raise NotImplementedError("getClipboardData")
sun.awt.windows.WClipboard.getClipboardData = getClipboardData

def registerClipboardViewer():
    raise NotImplementedError("registerClipboardViewer")
sun.awt.windows.WClipboard.registerClipboardViewer = registerClipboardViewer

def createCursorIndirect(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("createCursorIndirect")
sun.awt.windows.WCustomCursor.createCursorIndirect = createCursorIndirect

def getCursorWidth():
    raise NotImplementedError("getCursorWidth")
sun.awt.windows.WCustomCursor.getCursorWidth = staticmethod(getCursorWidth)

def getCursorHeight():
    raise NotImplementedError("getCursorHeight")
sun.awt.windows.WCustomCursor.getCursorHeight = staticmethod(getCursorHeight)

def registerClipboardFormat(a0):
    raise NotImplementedError("registerClipboardFormat")
sun.awt.windows.WDataTransferer.registerClipboardFormat = staticmethod(registerClipboardFormat)

def getClipboardFormatName(a0):
    raise NotImplementedError("getClipboardFormatName")
sun.awt.windows.WDataTransferer.getClipboardFormatName = staticmethod(getClipboardFormatName)

def imageDataToPlatformImageBytes(a0, a1, a2, a3):
    raise NotImplementedError("imageDataToPlatformImageBytes")
sun.awt.windows.WDataTransferer.imageDataToPlatformImageBytes = imageDataToPlatformImageBytes

def platformImageBytesToImageData(a0, a1):
    raise NotImplementedError("platformImageBytesToImageData")
sun.awt.windows.WDataTransferer.platformImageBytesToImageData = platformImageBytesToImageData

def dragQueryFile(a0):
    raise NotImplementedError("dragQueryFile")
sun.awt.windows.WDataTransferer.dragQueryFile = dragQueryFile

def canConvert(a0):
    raise NotImplementedError("canConvert")
sun.awt.windows.WDefaultFontCharset.canConvert = canConvert

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WDefaultFontCharset.initIDs = staticmethod(initIDs)

def ShellExecute(a0, a1):
    raise NotImplementedError("ShellExecute")
sun.awt.windows.WDesktopPeer.ShellExecute = staticmethod(ShellExecute)

def createAwtDialog(a0):
    raise NotImplementedError("createAwtDialog")
sun.awt.windows.WDialogPeer.createAwtDialog = createAwtDialog

def showModal():
    raise NotImplementedError("showModal")
sun.awt.windows.WDialogPeer.showModal = showModal

def endModal():
    raise NotImplementedError("endModal")
sun.awt.windows.WDialogPeer.endModal = endModal

def pSetIMMOption(a0):
    raise NotImplementedError("pSetIMMOption")
sun.awt.windows.WDialogPeer.pSetIMMOption = pSetIMMOption

def createDragSource(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("createDragSource")
sun.awt.windows.WDragSourceContextPeer.createDragSource = createDragSource

def doDragDrop(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("doDragDrop")
sun.awt.windows.WDragSourceContextPeer.doDragDrop = doDragDrop

def setNativeCursor(a0, a1, a2):
    raise NotImplementedError("setNativeCursor")
sun.awt.windows.WDragSourceContextPeer.setNativeCursor = setNativeCursor

def getData(a0, a1):
    raise NotImplementedError("getData")
sun.awt.windows.WDropTargetContextPeer.getData = getData

def dropDone(a0, a1, a2):
    raise NotImplementedError("dropDone")
sun.awt.windows.WDropTargetContextPeer.dropDone = dropDone

def freeStgMedium(a0):
    raise NotImplementedError("freeStgMedium")
sun.awt.windows.WDropTargetContextPeerFileStream.freeStgMedium = freeStgMedium

def Available(a0):
    raise NotImplementedError("Available")
sun.awt.windows.WDropTargetContextPeerIStream.Available = Available

def Read(a0):
    raise NotImplementedError("Read")
sun.awt.windows.WDropTargetContextPeerIStream.Read = Read

def ReadBytes(a0, a1, a2, a3):
    raise NotImplementedError("ReadBytes")
sun.awt.windows.WDropTargetContextPeerIStream.ReadBytes = ReadBytes

def Close(a0):
    raise NotImplementedError("Close")
sun.awt.windows.WDropTargetContextPeerIStream.Close = Close

def isPrinterDC(a0):
    raise NotImplementedError("isPrinterDC")
sun.awt.windows.WEmbeddedFrame.isPrinterDC = isPrinterDC

def printBand(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    raise NotImplementedError("printBand")
sun.awt.windows.WEmbeddedFrame.printBand = printBand

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WEmbeddedFrame.initIDs = staticmethod(initIDs)

def notifyModalBlockedImpl(a0, a1, a2):
    raise NotImplementedError("notifyModalBlockedImpl")
sun.awt.windows.WEmbeddedFrame.notifyModalBlockedImpl = notifyModalBlockedImpl

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WEmbeddedFramePeer.create = create

def getBoundsPrivate():
    raise NotImplementedError("getBoundsPrivate")
sun.awt.windows.WEmbeddedFramePeer.getBoundsPrivate = getBoundsPrivate

def setFilterString(a0):
    raise NotImplementedError("setFilterString")
sun.awt.windows.WFileDialogPeer.setFilterString = staticmethod(setFilterString)

def _dispose():
    raise NotImplementedError("_dispose")
sun.awt.windows.WFileDialogPeer._dispose = _dispose

def _show():
    raise NotImplementedError("_show")
sun.awt.windows.WFileDialogPeer._show = _show

def _hide():
    raise NotImplementedError("_hide")
sun.awt.windows.WFileDialogPeer._hide = _hide

def toFront():
    raise NotImplementedError("toFront")
sun.awt.windows.WFileDialogPeer.toFront = toFront

def toBack():
    raise NotImplementedError("toBack")
sun.awt.windows.WFileDialogPeer.toBack = toBack

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WFileDialogPeer.initIDs = staticmethod(initIDs)

def stringWidth(a0):
    raise NotImplementedError("stringWidth")
sun.awt.windows.WFontMetrics.stringWidth = stringWidth

def charsWidth(a0, a1, a2):
    raise NotImplementedError("charsWidth")
sun.awt.windows.WFontMetrics.charsWidth = charsWidth

def bytesWidth(a0, a1, a2):
    raise NotImplementedError("bytesWidth")
sun.awt.windows.WFontMetrics.bytesWidth = bytesWidth

def init():
    raise NotImplementedError("init")
sun.awt.windows.WFontMetrics.init = init

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WFontMetrics.initIDs = staticmethod(initIDs)

def addItems(a0, a1, a2):
    raise NotImplementedError("addItems")
sun.awt.windows.WListPeer.addItems = addItems

def delItems(a0, a1):
    raise NotImplementedError("delItems")
sun.awt.windows.WListPeer.delItems = delItems

def select(a0):
    raise NotImplementedError("select")
sun.awt.windows.WListPeer.select = select

def deselect(a0):
    raise NotImplementedError("deselect")
sun.awt.windows.WListPeer.deselect = deselect

def makeVisible(a0):
    raise NotImplementedError("makeVisible")
sun.awt.windows.WListPeer.makeVisible = makeVisible

def setMultipleSelections(a0):
    raise NotImplementedError("setMultipleSelections")
sun.awt.windows.WListPeer.setMultipleSelections = setMultipleSelections

def getMaxWidth():
    raise NotImplementedError("getMaxWidth")
sun.awt.windows.WListPeer.getMaxWidth = getMaxWidth

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WListPeer.create = create

def updateMaxItemWidth():
    raise NotImplementedError("updateMaxItemWidth")
sun.awt.windows.WListPeer.updateMaxItemWidth = updateMaxItemWidth

def isSelected(a0):
    raise NotImplementedError("isSelected")
sun.awt.windows.WListPeer.isSelected = isSelected

def addMenu(a0):
    raise NotImplementedError("addMenu")
sun.awt.windows.WMenuBarPeer.addMenu = addMenu

def delMenu(a0):
    raise NotImplementedError("delMenu")
sun.awt.windows.WMenuBarPeer.delMenu = delMenu

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WMenuBarPeer.create = create

def _dispose():
    raise NotImplementedError("_dispose")
sun.awt.windows.WMenuItemPeer._dispose = _dispose

def _setLabel(a0):
    raise NotImplementedError("_setLabel")
sun.awt.windows.WMenuItemPeer._setLabel = _setLabel

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WMenuItemPeer.create = create

def enable(a0):
    raise NotImplementedError("enable")
sun.awt.windows.WMenuItemPeer.enable = enable

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WMenuItemPeer.initIDs = staticmethod(initIDs)

def _setFont(a0):
    raise NotImplementedError("_setFont")
sun.awt.windows.WMenuItemPeer._setFont = _setFont

def addSeparator():
    raise NotImplementedError("addSeparator")
sun.awt.windows.WMenuPeer.addSeparator = addSeparator

def delItem(a0):
    raise NotImplementedError("delItem")
sun.awt.windows.WMenuPeer.delItem = delItem

def createMenu(a0):
    raise NotImplementedError("createMenu")
sun.awt.windows.WMenuPeer.createMenu = createMenu

def createSubMenu(a0):
    raise NotImplementedError("createSubMenu")
sun.awt.windows.WMenuPeer.createSubMenu = createSubMenu

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WPageDialog.initIDs = staticmethod(initIDs)

def _show():
    raise NotImplementedError("_show")
sun.awt.windows.WPageDialogPeer._show = _show

def createMenu(a0):
    raise NotImplementedError("createMenu")
sun.awt.windows.WPopupMenuPeer.createMenu = createMenu

def _show(a0):
    raise NotImplementedError("_show")
sun.awt.windows.WPopupMenuPeer._show = _show

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WPrintDialog.initIDs = staticmethod(initIDs)

def _show():
    raise NotImplementedError("_show")
sun.awt.windows.WPrintDialogPeer._show = _show

def toFront():
    raise NotImplementedError("toFront")
sun.awt.windows.WPrintDialogPeer.toFront = toFront

def toBack():
    raise NotImplementedError("toBack")
sun.awt.windows.WPrintDialogPeer.toBack = toBack

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WPrintDialogPeer.initIDs = staticmethod(initIDs)

def setNativePrintService(a0):
    raise NotImplementedError("setNativePrintService")
sun.awt.windows.WPrinterJob.setNativePrintService = setNativePrintService

def getNativePrintService():
    raise NotImplementedError("getNativePrintService")
sun.awt.windows.WPrinterJob.getNativePrintService = getNativePrintService

def getDefaultPage(a0):
    raise NotImplementedError("getDefaultPage")
sun.awt.windows.WPrinterJob.getDefaultPage = getDefaultPage

def validatePaper(a0, a1):
    raise NotImplementedError("validatePaper")
sun.awt.windows.WPrinterJob.validatePaper = validatePaper

def setNativeCopies(a0):
    raise NotImplementedError("setNativeCopies")
sun.awt.windows.WPrinterJob.setNativeCopies = setNativeCopies

def jobSetup(a0, a1):
    raise NotImplementedError("jobSetup")
sun.awt.windows.WPrinterJob.jobSetup = jobSetup

def initPrinter():
    raise NotImplementedError("initPrinter")
sun.awt.windows.WPrinterJob.initPrinter = initPrinter

def _startDoc(a0, a1):
    raise NotImplementedError("_startDoc")
sun.awt.windows.WPrinterJob._startDoc = _startDoc

def endDoc():
    raise NotImplementedError("endDoc")
sun.awt.windows.WPrinterJob.endDoc = endDoc

def abortDoc():
    raise NotImplementedError("abortDoc")
sun.awt.windows.WPrinterJob.abortDoc = abortDoc

def deleteDC(a0, a1, a2):
    raise NotImplementedError("deleteDC")
sun.awt.windows.WPrinterJob.deleteDC = staticmethod(deleteDC)

def deviceStartPage(a0, a1, a2, a3):
    raise NotImplementedError("deviceStartPage")
sun.awt.windows.WPrinterJob.deviceStartPage = deviceStartPage

def deviceEndPage(a0, a1, a2):
    raise NotImplementedError("deviceEndPage")
sun.awt.windows.WPrinterJob.deviceEndPage = deviceEndPage

def printBand(a0, a1, a2, a3, a4):
    raise NotImplementedError("printBand")
sun.awt.windows.WPrinterJob.printBand = printBand

def beginPath(a0):
    raise NotImplementedError("beginPath")
sun.awt.windows.WPrinterJob.beginPath = beginPath

def endPath(a0):
    raise NotImplementedError("endPath")
sun.awt.windows.WPrinterJob.endPath = endPath

def closeFigure(a0):
    raise NotImplementedError("closeFigure")
sun.awt.windows.WPrinterJob.closeFigure = closeFigure

def fillPath(a0):
    raise NotImplementedError("fillPath")
sun.awt.windows.WPrinterJob.fillPath = fillPath

def moveTo(a0, a1, a2):
    raise NotImplementedError("moveTo")
sun.awt.windows.WPrinterJob.moveTo = moveTo

def lineTo(a0, a1, a2):
    raise NotImplementedError("lineTo")
sun.awt.windows.WPrinterJob.lineTo = lineTo

def polyBezierTo(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("polyBezierTo")
sun.awt.windows.WPrinterJob.polyBezierTo = polyBezierTo

def setPolyFillMode(a0, a1):
    raise NotImplementedError("setPolyFillMode")
sun.awt.windows.WPrinterJob.setPolyFillMode = setPolyFillMode

def selectSolidBrush(a0, a1, a2, a3):
    raise NotImplementedError("selectSolidBrush")
sun.awt.windows.WPrinterJob.selectSolidBrush = selectSolidBrush

def getPenX(a0):
    raise NotImplementedError("getPenX")
sun.awt.windows.WPrinterJob.getPenX = getPenX

def getPenY(a0):
    raise NotImplementedError("getPenY")
sun.awt.windows.WPrinterJob.getPenY = getPenY

def selectClipPath(a0):
    raise NotImplementedError("selectClipPath")
sun.awt.windows.WPrinterJob.selectClipPath = selectClipPath

def frameRect(a0, a1, a2, a3, a4):
    raise NotImplementedError("frameRect")
sun.awt.windows.WPrinterJob.frameRect = frameRect

def fillRect(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("fillRect")
sun.awt.windows.WPrinterJob.fillRect = fillRect

def selectPen(a0, a1, a2, a3, a4):
    raise NotImplementedError("selectPen")
sun.awt.windows.WPrinterJob.selectPen = selectPen

def selectStylePen(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("selectStylePen")
sun.awt.windows.WPrinterJob.selectStylePen = selectStylePen

def setFont(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("setFont")
sun.awt.windows.WPrinterJob.setFont = setFont

def setTextColor(a0, a1, a2, a3):
    raise NotImplementedError("setTextColor")
sun.awt.windows.WPrinterJob.setTextColor = setTextColor

def textOut(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("textOut")
sun.awt.windows.WPrinterJob.textOut = textOut

def getGDIAdvance(a0, a1):
    raise NotImplementedError("getGDIAdvance")
sun.awt.windows.WPrinterJob.getGDIAdvance = getGDIAdvance

def drawDIBImage(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):
    raise NotImplementedError("drawDIBImage")
sun.awt.windows.WPrinterJob.drawDIBImage = drawDIBImage

def showDocProperties(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):
    raise NotImplementedError("showDocProperties")
sun.awt.windows.WPrinterJob.showDocProperties = showDocProperties

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WPrinterJob.initIDs = staticmethod(initIDs)

def _dispose():
    raise NotImplementedError("_dispose")
sun.awt.windows.WRobotPeer._dispose = _dispose

def create():
    raise NotImplementedError("create")
sun.awt.windows.WRobotPeer.create = create

def mouseMoveImpl(a0, a1):
    raise NotImplementedError("mouseMoveImpl")
sun.awt.windows.WRobotPeer.mouseMoveImpl = mouseMoveImpl

def mousePress(a0):
    raise NotImplementedError("mousePress")
sun.awt.windows.WRobotPeer.mousePress = mousePress

def mouseRelease(a0):
    raise NotImplementedError("mouseRelease")
sun.awt.windows.WRobotPeer.mouseRelease = mouseRelease

def mouseWheel(a0):
    raise NotImplementedError("mouseWheel")
sun.awt.windows.WRobotPeer.mouseWheel = mouseWheel

def keyPress(a0):
    raise NotImplementedError("keyPress")
sun.awt.windows.WRobotPeer.keyPress = keyPress

def keyRelease(a0):
    raise NotImplementedError("keyRelease")
sun.awt.windows.WRobotPeer.keyRelease = keyRelease

def getRGBPixels(a0, a1, a2, a3, a4):
    raise NotImplementedError("getRGBPixels")
sun.awt.windows.WRobotPeer.getRGBPixels = getRGBPixels

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WScrollPanePeer.initIDs = staticmethod(initIDs)

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WScrollPanePeer.create = create

def getOffset(a0):
    raise NotImplementedError("getOffset")
sun.awt.windows.WScrollPanePeer.getOffset = getOffset

def setInsets():
    raise NotImplementedError("setInsets")
sun.awt.windows.WScrollPanePeer.setInsets = setInsets

def setScrollPosition(a0, a1):
    raise NotImplementedError("setScrollPosition")
sun.awt.windows.WScrollPanePeer.setScrollPosition = setScrollPosition

def _getHScrollbarHeight():
    raise NotImplementedError("_getHScrollbarHeight")
sun.awt.windows.WScrollPanePeer._getHScrollbarHeight = _getHScrollbarHeight

def _getVScrollbarWidth():
    raise NotImplementedError("_getVScrollbarWidth")
sun.awt.windows.WScrollPanePeer._getVScrollbarWidth = _getVScrollbarWidth

def setSpans(a0, a1, a2, a3):
    raise NotImplementedError("setSpans")
sun.awt.windows.WScrollPanePeer.setSpans = setSpans

def getScrollbarSize(a0):
    raise NotImplementedError("getScrollbarSize")
sun.awt.windows.WScrollbarPeer.getScrollbarSize = staticmethod(getScrollbarSize)

def setValues(a0, a1, a2, a3):
    raise NotImplementedError("setValues")
sun.awt.windows.WScrollbarPeer.setValues = setValues

def setLineIncrement(a0):
    raise NotImplementedError("setLineIncrement")
sun.awt.windows.WScrollbarPeer.setLineIncrement = setLineIncrement

def setPageIncrement(a0):
    raise NotImplementedError("setPageIncrement")
sun.awt.windows.WScrollbarPeer.setPageIncrement = setPageIncrement

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WScrollbarPeer.create = create

def replaceRange(a0, a1, a2):
    raise NotImplementedError("replaceRange")
sun.awt.windows.WTextAreaPeer.replaceRange = replaceRange

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WTextAreaPeer.create = create

def getText():
    raise NotImplementedError("getText")
sun.awt.windows.WTextComponentPeer.getText = getText

def setText(a0):
    raise NotImplementedError("setText")
sun.awt.windows.WTextComponentPeer.setText = setText

def getSelectionStart():
    raise NotImplementedError("getSelectionStart")
sun.awt.windows.WTextComponentPeer.getSelectionStart = getSelectionStart

def getSelectionEnd():
    raise NotImplementedError("getSelectionEnd")
sun.awt.windows.WTextComponentPeer.getSelectionEnd = getSelectionEnd

def select(a0, a1):
    raise NotImplementedError("select")
sun.awt.windows.WTextComponentPeer.select = select

def enableEditing(a0):
    raise NotImplementedError("enableEditing")
sun.awt.windows.WTextComponentPeer.enableEditing = enableEditing

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WTextComponentPeer.initIDs = staticmethod(initIDs)

def setEchoChar(a0):
    raise NotImplementedError("setEchoChar")
sun.awt.windows.WTextFieldPeer.setEchoChar = setEchoChar

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WTextFieldPeer.create = create

def startSecondaryEventLoop():
    raise NotImplementedError("startSecondaryEventLoop")
sun.awt.windows.WToolkitThreadBlockedHandler.startSecondaryEventLoop = startSecondaryEventLoop

def setToolTip(a0):
    raise NotImplementedError("setToolTip")
sun.awt.windows.WTrayIconPeer.setToolTip = setToolTip

def create():
    raise NotImplementedError("create")
sun.awt.windows.WTrayIconPeer.create = create

def _dispose():
    raise NotImplementedError("_dispose")
sun.awt.windows.WTrayIconPeer._dispose = _dispose

def updateNativeIcon(a0):
    raise NotImplementedError("updateNativeIcon")
sun.awt.windows.WTrayIconPeer.updateNativeIcon = updateNativeIcon

def setNativeIcon(a0, a1, a2, a3, a4):
    raise NotImplementedError("setNativeIcon")
sun.awt.windows.WTrayIconPeer.setNativeIcon = setNativeIcon

def _displayMessage(a0, a1, a2):
    raise NotImplementedError("_displayMessage")
sun.awt.windows.WTrayIconPeer._displayMessage = _displayMessage

def dispose():
    raise NotImplementedError("dispose")
sun.dc.pr.PathDasher.dispose = dispose

def setDash(a0, a1):
    raise NotImplementedError("setDash")
sun.dc.pr.PathDasher.setDash = setDash

def setDashT4(a0):
    raise NotImplementedError("setDashT4")
sun.dc.pr.PathDasher.setDashT4 = setDashT4

def setOutputT6(a0):
    raise NotImplementedError("setOutputT6")
sun.dc.pr.PathDasher.setOutputT6 = setOutputT6

def setOutputConsumer(a0):
    raise NotImplementedError("setOutputConsumer")
sun.dc.pr.PathDasher.setOutputConsumer = setOutputConsumer

def reset():
    raise NotImplementedError("reset")
sun.dc.pr.PathDasher.reset = reset

def beginPath():
    raise NotImplementedError("beginPath")
sun.dc.pr.PathDasher.beginPath = beginPath

def beginSubpath(a0, a1):
    raise NotImplementedError("beginSubpath")
sun.dc.pr.PathDasher.beginSubpath = beginSubpath

def appendLine(a0, a1):
    raise NotImplementedError("appendLine")
sun.dc.pr.PathDasher.appendLine = appendLine

def appendQuadratic(a0, a1, a2, a3):
    raise NotImplementedError("appendQuadratic")
sun.dc.pr.PathDasher.appendQuadratic = appendQuadratic

def appendCubic(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("appendCubic")
sun.dc.pr.PathDasher.appendCubic = appendCubic

def closedSubpath():
    raise NotImplementedError("closedSubpath")
sun.dc.pr.PathDasher.closedSubpath = closedSubpath

def endPath():
    raise NotImplementedError("endPath")
sun.dc.pr.PathDasher.endPath = endPath

def getCPathConsumer():
    raise NotImplementedError("getCPathConsumer")
sun.dc.pr.PathDasher.getCPathConsumer = getCPathConsumer

def cClassInitialize():
    raise NotImplementedError("cClassInitialize")
sun.dc.pr.PathDasher.cClassInitialize = staticmethod(cClassInitialize)

def cClassFinalize():
    raise NotImplementedError("cClassFinalize")
sun.dc.pr.PathDasher.cClassFinalize = staticmethod(cClassFinalize)

def cInitialize(a0):
    raise NotImplementedError("cInitialize")
sun.dc.pr.PathDasher.cInitialize = cInitialize

def dispose():
    raise NotImplementedError("dispose")
sun.dc.pr.PathFiller.dispose = dispose

def setFillMode(a0):
    raise NotImplementedError("setFillMode")
sun.dc.pr.PathFiller.setFillMode = setFillMode

def beginPath():
    raise NotImplementedError("beginPath")
sun.dc.pr.PathFiller.beginPath = beginPath

def beginSubpath(a0, a1):
    raise NotImplementedError("beginSubpath")
sun.dc.pr.PathFiller.beginSubpath = beginSubpath

def appendLine(a0, a1):
    raise NotImplementedError("appendLine")
sun.dc.pr.PathFiller.appendLine = appendLine

def appendQuadratic(a0, a1, a2, a3):
    raise NotImplementedError("appendQuadratic")
sun.dc.pr.PathFiller.appendQuadratic = appendQuadratic

def appendCubic(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("appendCubic")
sun.dc.pr.PathFiller.appendCubic = appendCubic

def closedSubpath():
    raise NotImplementedError("closedSubpath")
sun.dc.pr.PathFiller.closedSubpath = closedSubpath

def endPath():
    raise NotImplementedError("endPath")
sun.dc.pr.PathFiller.endPath = endPath

def getCPathConsumer():
    raise NotImplementedError("getCPathConsumer")
sun.dc.pr.PathFiller.getCPathConsumer = getCPathConsumer

def getAlphaBox(a0):
    raise NotImplementedError("getAlphaBox")
sun.dc.pr.PathFiller.getAlphaBox = getAlphaBox

def setOutputArea(a0, a1, a2, a3):
    raise NotImplementedError("setOutputArea")
sun.dc.pr.PathFiller.setOutputArea = setOutputArea

def getTileState():
    raise NotImplementedError("getTileState")
sun.dc.pr.PathFiller.getTileState = getTileState

def writeAlpha8(a0, a1, a2, a3):
    raise NotImplementedError("writeAlpha8")
sun.dc.pr.PathFiller.writeAlpha8 = writeAlpha8

def writeAlpha16(a0, a1, a2, a3):
    raise NotImplementedError("writeAlpha16")
sun.dc.pr.PathFiller.writeAlpha16 = writeAlpha16

def nextTile():
    raise NotImplementedError("nextTile")
sun.dc.pr.PathFiller.nextTile = nextTile

def reset():
    raise NotImplementedError("reset")
sun.dc.pr.PathFiller.reset = reset

def cClassInitialize():
    raise NotImplementedError("cClassInitialize")
sun.dc.pr.PathFiller.cClassInitialize = staticmethod(cClassInitialize)

def cClassFinalize():
    raise NotImplementedError("cClassFinalize")
sun.dc.pr.PathFiller.cClassFinalize = staticmethod(cClassFinalize)

def cInitialize():
    raise NotImplementedError("cInitialize")
sun.dc.pr.PathFiller.cInitialize = cInitialize

def dispose():
    raise NotImplementedError("dispose")
sun.dc.pr.PathStroker.dispose = dispose

def setPenDiameter(a0):
    raise NotImplementedError("setPenDiameter")
sun.dc.pr.PathStroker.setPenDiameter = setPenDiameter

def setPenT4(a0):
    raise NotImplementedError("setPenT4")
sun.dc.pr.PathStroker.setPenT4 = setPenT4

def setPenFitting(a0, a1):
    raise NotImplementedError("setPenFitting")
sun.dc.pr.PathStroker.setPenFitting = setPenFitting

def setCaps(a0):
    raise NotImplementedError("setCaps")
sun.dc.pr.PathStroker.setCaps = setCaps

def setCorners(a0, a1):
    raise NotImplementedError("setCorners")
sun.dc.pr.PathStroker.setCorners = setCorners

def setOutputT6(a0):
    raise NotImplementedError("setOutputT6")
sun.dc.pr.PathStroker.setOutputT6 = setOutputT6

def setOutputConsumer(a0):
    raise NotImplementedError("setOutputConsumer")
sun.dc.pr.PathStroker.setOutputConsumer = setOutputConsumer

def reset():
    raise NotImplementedError("reset")
sun.dc.pr.PathStroker.reset = reset

def beginPath():
    raise NotImplementedError("beginPath")
sun.dc.pr.PathStroker.beginPath = beginPath

def beginSubpath(a0, a1):
    raise NotImplementedError("beginSubpath")
sun.dc.pr.PathStroker.beginSubpath = beginSubpath

def appendLine(a0, a1):
    raise NotImplementedError("appendLine")
sun.dc.pr.PathStroker.appendLine = appendLine

def appendQuadratic(a0, a1, a2, a3):
    raise NotImplementedError("appendQuadratic")
sun.dc.pr.PathStroker.appendQuadratic = appendQuadratic

def appendCubic(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("appendCubic")
sun.dc.pr.PathStroker.appendCubic = appendCubic

def closedSubpath():
    raise NotImplementedError("closedSubpath")
sun.dc.pr.PathStroker.closedSubpath = closedSubpath

def endPath():
    raise NotImplementedError("endPath")
sun.dc.pr.PathStroker.endPath = endPath

def getCPathConsumer():
    raise NotImplementedError("getCPathConsumer")
sun.dc.pr.PathStroker.getCPathConsumer = getCPathConsumer

def cClassInitialize():
    raise NotImplementedError("cClassInitialize")
sun.dc.pr.PathStroker.cClassInitialize = staticmethod(cClassInitialize)

def cClassFinalize():
    raise NotImplementedError("cClassFinalize")
sun.dc.pr.PathStroker.cClassFinalize = staticmethod(cClassFinalize)

def cInitialize(a0):
    raise NotImplementedError("cInitialize")
sun.dc.pr.PathStroker.cInitialize = cInitialize

def cInitialize2D(a0):
    raise NotImplementedError("cInitialize2D")
sun.dc.pr.PathStroker.cInitialize2D = cInitialize2D

def initIDs(a0):
    raise NotImplementedError("initIDs")
sun.font.FreetypeFontScaler.initIDs = staticmethod(initIDs)

def initNativeScaler(a0, a1, a2, a3, a4):
    raise NotImplementedError("initNativeScaler")
sun.font.FreetypeFontScaler.initNativeScaler = initNativeScaler

def getFontMetricsNative(a0, a1, a2):
    raise NotImplementedError("getFontMetricsNative")
sun.font.FreetypeFontScaler.getFontMetricsNative = getFontMetricsNative

def getGlyphAdvanceNative(a0, a1, a2, a3):
    raise NotImplementedError("getGlyphAdvanceNative")
sun.font.FreetypeFontScaler.getGlyphAdvanceNative = getGlyphAdvanceNative

def getGlyphMetricsNative(a0, a1, a2, a3, a4):
    raise NotImplementedError("getGlyphMetricsNative")
sun.font.FreetypeFontScaler.getGlyphMetricsNative = getGlyphMetricsNative

def getGlyphImageNative(a0, a1, a2, a3):
    raise NotImplementedError("getGlyphImageNative")
sun.font.FreetypeFontScaler.getGlyphImageNative = getGlyphImageNative

def getGlyphOutlineBoundsNative(a0, a1, a2, a3):
    raise NotImplementedError("getGlyphOutlineBoundsNative")
sun.font.FreetypeFontScaler.getGlyphOutlineBoundsNative = getGlyphOutlineBoundsNative

def getGlyphOutlineNative(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("getGlyphOutlineNative")
sun.font.FreetypeFontScaler.getGlyphOutlineNative = getGlyphOutlineNative

def getGlyphVectorOutlineNative(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("getGlyphVectorOutlineNative")
sun.font.FreetypeFontScaler.getGlyphVectorOutlineNative = getGlyphVectorOutlineNative

def getGlyphPointNative(a0, a1, a2, a3, a4):
    raise NotImplementedError("getGlyphPointNative")
sun.font.FreetypeFontScaler.getGlyphPointNative = getGlyphPointNative

def getLayoutTableCacheNative(a0):
    raise NotImplementedError("getLayoutTableCacheNative")
sun.font.FreetypeFontScaler.getLayoutTableCacheNative = getLayoutTableCacheNative

def disposeNativeScaler(a0, a1):
    raise NotImplementedError("disposeNativeScaler")
sun.font.FreetypeFontScaler.disposeNativeScaler = disposeNativeScaler

def getGlyphCodeNative(a0, a1, a2):
    raise NotImplementedError("getGlyphCodeNative")
sun.font.FreetypeFontScaler.getGlyphCodeNative = getGlyphCodeNative

def getNumGlyphsNative(a0):
    raise NotImplementedError("getNumGlyphsNative")
sun.font.FreetypeFontScaler.getNumGlyphsNative = getNumGlyphsNative

def getMissingGlyphCodeNative(a0):
    raise NotImplementedError("getMissingGlyphCodeNative")
sun.font.FreetypeFontScaler.getMissingGlyphCodeNative = getMissingGlyphCodeNative

def getUnitsPerEMNative(a0):
    raise NotImplementedError("getUnitsPerEMNative")
sun.font.FreetypeFontScaler.getUnitsPerEMNative = getUnitsPerEMNative

def createScalerContextNative(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("createScalerContextNative")
sun.font.FreetypeFontScaler.createScalerContextNative = createScalerContextNative

def getNullScalerContext():
    raise NotImplementedError("getNullScalerContext")
sun.font.NullFontScaler.getNullScalerContext = staticmethod(getNullScalerContext)

def getGlyphImage(a0, a1):
    raise NotImplementedError("getGlyphImage")
sun.font.NullFontScaler.getGlyphImage = getGlyphImage

def initGVIDs():
    raise NotImplementedError("initGVIDs")
sun.font.SunLayoutEngine.initGVIDs = staticmethod(initGVIDs)

def nativeLayout(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16):
    raise NotImplementedError("nativeLayout")
sun.font.SunLayoutEngine.nativeLayout = staticmethod(nativeLayout)

def isModifiableClass0(a0, a1):
    raise NotImplementedError("isModifiableClass0")
sun.instrument.InstrumentationImpl.isModifiableClass0 = isModifiableClass0

def isRetransformClassesSupported0(a0):
    raise NotImplementedError("isRetransformClassesSupported0")
sun.instrument.InstrumentationImpl.isRetransformClassesSupported0 = isRetransformClassesSupported0

def setHasRetransformableTransformers(a0, a1):
    raise NotImplementedError("setHasRetransformableTransformers")
sun.instrument.InstrumentationImpl.setHasRetransformableTransformers = setHasRetransformableTransformers

def retransformClasses0(a0, a1):
    raise NotImplementedError("retransformClasses0")
sun.instrument.InstrumentationImpl.retransformClasses0 = retransformClasses0

def redefineClasses0(a0, a1):
    raise NotImplementedError("redefineClasses0")
sun.instrument.InstrumentationImpl.redefineClasses0 = redefineClasses0

def getAllLoadedClasses0(a0):
    raise NotImplementedError("getAllLoadedClasses0")
sun.instrument.InstrumentationImpl.getAllLoadedClasses0 = getAllLoadedClasses0

def getInitiatedClasses0(a0, a1):
    raise NotImplementedError("getInitiatedClasses0")
sun.instrument.InstrumentationImpl.getInitiatedClasses0 = getInitiatedClasses0

def getObjectSize0(a0, a1):
    raise NotImplementedError("getObjectSize0")
sun.instrument.InstrumentationImpl.getObjectSize0 = getObjectSize0

def appendToClassLoaderSearch0(a0, a1, a2):
    raise NotImplementedError("appendToClassLoaderSearch0")
sun.instrument.InstrumentationImpl.appendToClassLoaderSearch0 = appendToClassLoaderSearch0

def setNativeMethodPrefixes(a0, a1, a2):
    raise NotImplementedError("setNativeMethodPrefixes")
sun.instrument.InstrumentationImpl.setNativeMethodPrefixes = setNativeMethodPrefixes

def cmmLoadProfile(a0, a1):
    raise NotImplementedError("cmmLoadProfile")
sun.java2d.cmm.kcms.CMM.cmmLoadProfile = staticmethod(cmmLoadProfile)

def cmmFreeProfile(a0):
    raise NotImplementedError("cmmFreeProfile")
sun.java2d.cmm.kcms.CMM.cmmFreeProfile = staticmethod(cmmFreeProfile)

def cmmGetProfileSize(a0, a1):
    raise NotImplementedError("cmmGetProfileSize")
sun.java2d.cmm.kcms.CMM.cmmGetProfileSize = staticmethod(cmmGetProfileSize)

def cmmGetProfileData(a0, a1):
    raise NotImplementedError("cmmGetProfileData")
sun.java2d.cmm.kcms.CMM.cmmGetProfileData = staticmethod(cmmGetProfileData)

def cmmGetTagSize(a0, a1, a2):
    raise NotImplementedError("cmmGetTagSize")
sun.java2d.cmm.kcms.CMM.cmmGetTagSize = staticmethod(cmmGetTagSize)

def cmmGetTagData(a0, a1, a2):
    raise NotImplementedError("cmmGetTagData")
sun.java2d.cmm.kcms.CMM.cmmGetTagData = staticmethod(cmmGetTagData)

def cmmSetTagData(a0, a1, a2):
    raise NotImplementedError("cmmSetTagData")
sun.java2d.cmm.kcms.CMM.cmmSetTagData = staticmethod(cmmSetTagData)

def cmmGetTransform(a0, a1, a2, a3):
    raise NotImplementedError("cmmGetTransform")
sun.java2d.cmm.kcms.CMM.cmmGetTransform = staticmethod(cmmGetTransform)

def cmmCombineTransforms(a0, a1):
    raise NotImplementedError("cmmCombineTransforms")
sun.java2d.cmm.kcms.CMM.cmmCombineTransforms = staticmethod(cmmCombineTransforms)

def cmmFreeTransform(a0):
    raise NotImplementedError("cmmFreeTransform")
sun.java2d.cmm.kcms.CMM.cmmFreeTransform = staticmethod(cmmFreeTransform)

def cmmGetNumComponents(a0, a1):
    raise NotImplementedError("cmmGetNumComponents")
sun.java2d.cmm.kcms.CMM.cmmGetNumComponents = staticmethod(cmmGetNumComponents)

def cmmColorConvert(a0, a1, a2):
    raise NotImplementedError("cmmColorConvert")
sun.java2d.cmm.kcms.CMM.cmmColorConvert = staticmethod(cmmColorConvert)

def cmmInit():
    raise NotImplementedError("cmmInit")
sun.java2d.cmm.kcms.CMM.cmmInit = staticmethod(cmmInit)

def cmmTerminate():
    raise NotImplementedError("cmmTerminate")
sun.java2d.cmm.kcms.CMM.cmmTerminate = staticmethod(cmmTerminate)

def loadProfileNative(a0, a1):
    raise NotImplementedError("loadProfileNative")
sun.java2d.cmm.lcms.LCMS.loadProfileNative = loadProfileNative

def getProfileSizeNative(a0):
    raise NotImplementedError("getProfileSizeNative")
sun.java2d.cmm.lcms.LCMS.getProfileSizeNative = getProfileSizeNative

def getProfileDataNative(a0, a1):
    raise NotImplementedError("getProfileDataNative")
sun.java2d.cmm.lcms.LCMS.getProfileDataNative = getProfileDataNative

def getTagNative(a0, a1):
    raise NotImplementedError("getTagNative")
sun.java2d.cmm.lcms.LCMS.getTagNative = staticmethod(getTagNative)

def setTagDataNative(a0, a1, a2):
    raise NotImplementedError("setTagDataNative")
sun.java2d.cmm.lcms.LCMS.setTagDataNative = setTagDataNative

def getProfileID(a0):
    raise NotImplementedError("getProfileID")
sun.java2d.cmm.lcms.LCMS.getProfileID = staticmethod(getProfileID)

def createNativeTransform(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("createNativeTransform")
sun.java2d.cmm.lcms.LCMS.createNativeTransform = staticmethod(createNativeTransform)

def colorConvert(a0, a1, a2):
    raise NotImplementedError("colorConvert")
sun.java2d.cmm.lcms.LCMS.colorConvert = staticmethod(colorConvert)

def freeTransform(a0):
    raise NotImplementedError("freeTransform")
sun.java2d.cmm.lcms.LCMS.freeTransform = staticmethod(freeTransform)

def initLCMS(a0, a1, a2):
    raise NotImplementedError("initLCMS")
sun.java2d.cmm.lcms.LCMS.initLCMS = staticmethod(initLCMS)

def maskFill(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("maskFill")
sun.java2d.d3d.D3DMaskFill.maskFill = maskFill

def drawPoly(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("drawPoly")
sun.java2d.d3d.D3DRenderer.drawPoly = drawPoly

def drawGlyphList(a0, a1, a2, a3, a4, a5, a6, a7, a8):
    raise NotImplementedError("drawGlyphList")
sun.java2d.d3d.D3DTextRenderer.drawGlyphList = drawGlyphList

def Transform(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):
    raise NotImplementedError("Transform")
sun.java2d.loops.TransformBlit.Transform = Transform

def getOGLIdString():
    raise NotImplementedError("getOGLIdString")
sun.java2d.opengl.OGLContext.getOGLIdString = staticmethod(getOGLIdString)

def maskFill(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("maskFill")
sun.java2d.opengl.OGLMaskFill.maskFill = maskFill

def drawPoly(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("drawPoly")
sun.java2d.opengl.OGLRenderer.drawPoly = drawPoly

def initTexture(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("initTexture")
sun.java2d.opengl.OGLSurfaceData.initTexture = initTexture

def initFBObject(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("initFBObject")
sun.java2d.opengl.OGLSurfaceData.initFBObject = initFBObject

def initFlipBackbuffer(a0):
    raise NotImplementedError("initFlipBackbuffer")
sun.java2d.opengl.OGLSurfaceData.initFlipBackbuffer = initFlipBackbuffer

def getTextureTarget(a0):
    raise NotImplementedError("getTextureTarget")
sun.java2d.opengl.OGLSurfaceData.getTextureTarget = getTextureTarget

def getTextureID(a0):
    raise NotImplementedError("getTextureID")
sun.java2d.opengl.OGLSurfaceData.getTextureID = getTextureID

def drawGlyphList(a0, a1, a2, a3, a4, a5, a6, a7, a8):
    raise NotImplementedError("drawGlyphList")
sun.java2d.opengl.OGLTextRenderer.drawGlyphList = drawGlyphList

def initOps(a0, a1, a2):
    raise NotImplementedError("initOps")
sun.java2d.opengl.WGLSurfaceData.initOps = initOps

def initPbuffer(a0, a1, a2, a3, a4):
    raise NotImplementedError("initPbuffer")
sun.java2d.opengl.WGLSurfaceData.initPbuffer = initPbuffer

def updateWindowAccelImpl(a0, a1, a2, a3):
    raise NotImplementedError("updateWindowAccelImpl")
sun.java2d.opengl.WGLSurfaceData.updateWindowAccelImpl = staticmethod(updateWindowAccelImpl)

def enqueueTile(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14):
    raise NotImplementedError("enqueueTile")
sun.java2d.pipe.BufferedMaskBlit.enqueueTile = enqueueTile

def fillSpans(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("fillSpans")
sun.java2d.pipe.BufferedRenderPipe.fillSpans = fillSpans

def initIDs():
    raise NotImplementedError("initIDs")
sun.java2d.pipe.ShapeSpanIterator.initIDs = staticmethod(initIDs)

def appendPoly(a0, a1, a2, a3, a4):
    raise NotImplementedError("appendPoly")
sun.java2d.pipe.ShapeSpanIterator.appendPoly = appendPoly

def setNormalize(a0):
    raise NotImplementedError("setNormalize")
sun.java2d.pipe.ShapeSpanIterator.setNormalize = setNormalize

def setOutputAreaXYXY(a0, a1, a2, a3):
    raise NotImplementedError("setOutputAreaXYXY")
sun.java2d.pipe.ShapeSpanIterator.setOutputAreaXYXY = setOutputAreaXYXY

def setRule(a0):
    raise NotImplementedError("setRule")
sun.java2d.pipe.ShapeSpanIterator.setRule = setRule

def addSegment(a0, a1):
    raise NotImplementedError("addSegment")
sun.java2d.pipe.ShapeSpanIterator.addSegment = addSegment

def getPathBox(a0):
    raise NotImplementedError("getPathBox")
sun.java2d.pipe.ShapeSpanIterator.getPathBox = getPathBox

def intersectClipBox(a0, a1, a2, a3):
    raise NotImplementedError("intersectClipBox")
sun.java2d.pipe.ShapeSpanIterator.intersectClipBox = intersectClipBox

def nextSpan(a0):
    raise NotImplementedError("nextSpan")
sun.java2d.pipe.ShapeSpanIterator.nextSpan = nextSpan

def skipDownTo(a0):
    raise NotImplementedError("skipDownTo")
sun.java2d.pipe.ShapeSpanIterator.skipDownTo = skipDownTo

def getNativeIterator():
    raise NotImplementedError("getNativeIterator")
sun.java2d.pipe.ShapeSpanIterator.getNativeIterator = getNativeIterator

def dispose():
    raise NotImplementedError("dispose")
sun.java2d.pipe.ShapeSpanIterator.dispose = dispose

def moveTo(a0, a1):
    raise NotImplementedError("moveTo")
sun.java2d.pipe.ShapeSpanIterator.moveTo = moveTo

def lineTo(a0, a1):
    raise NotImplementedError("lineTo")
sun.java2d.pipe.ShapeSpanIterator.lineTo = lineTo

def quadTo(a0, a1, a2, a3):
    raise NotImplementedError("quadTo")
sun.java2d.pipe.ShapeSpanIterator.quadTo = quadTo

def curveTo(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("curveTo")
sun.java2d.pipe.ShapeSpanIterator.curveTo = curveTo

def closePath():
    raise NotImplementedError("closePath")
sun.java2d.pipe.ShapeSpanIterator.closePath = closePath

def pathDone():
    raise NotImplementedError("pathDone")
sun.java2d.pipe.ShapeSpanIterator.pathDone = pathDone

def getNativeConsumer():
    raise NotImplementedError("getNativeConsumer")
sun.java2d.pipe.ShapeSpanIterator.getNativeConsumer = getNativeConsumer

def setVerboseClass(a0):
    raise NotImplementedError("setVerboseClass")
sun.management.ClassLoadingImpl.setVerboseClass = staticmethod(setVerboseClass)

def setNotificationEnabled(a0):
    raise NotImplementedError("setNotificationEnabled")
sun.management.DiagnosticCommandImpl.setNotificationEnabled = setNotificationEnabled

def getDiagnosticCommands():
    raise NotImplementedError("getDiagnosticCommands")
sun.management.DiagnosticCommandImpl.getDiagnosticCommands = getDiagnosticCommands

def getDiagnosticCommandInfo(a0):
    raise NotImplementedError("getDiagnosticCommandInfo")
sun.management.DiagnosticCommandImpl.getDiagnosticCommandInfo = getDiagnosticCommandInfo

def executeDiagnosticCommand(a0):
    raise NotImplementedError("executeDiagnosticCommand")
sun.management.DiagnosticCommandImpl.executeDiagnosticCommand = executeDiagnosticCommand

def init0():
    raise NotImplementedError("init0")
sun.management.FileSystemImpl.init0 = staticmethod(init0)

def isSecuritySupported0(a0):
    raise NotImplementedError("isSecuritySupported0")
sun.management.FileSystemImpl.isSecuritySupported0 = staticmethod(isSecuritySupported0)

def isAccessUserOnly0(a0):
    raise NotImplementedError("isAccessUserOnly0")
sun.management.FileSystemImpl.isAccessUserOnly0 = staticmethod(isAccessUserOnly0)

def getAllFlagNames():
    raise NotImplementedError("getAllFlagNames")
sun.management.Flag.getAllFlagNames = staticmethod(getAllFlagNames)

def getFlags(a0, a1, a2):
    raise NotImplementedError("getFlags")
sun.management.Flag.getFlags = staticmethod(getFlags)

def getInternalFlagCount():
    raise NotImplementedError("getInternalFlagCount")
sun.management.Flag.getInternalFlagCount = staticmethod(getInternalFlagCount)

def setLongValue(a0, a1):
    raise NotImplementedError("setLongValue")
sun.management.Flag.setLongValue = staticmethod(setLongValue)

def setBooleanValue(a0, a1):
    raise NotImplementedError("setBooleanValue")
sun.management.Flag.setBooleanValue = staticmethod(setBooleanValue)

def setStringValue(a0, a1):
    raise NotImplementedError("setStringValue")
sun.management.Flag.setStringValue = staticmethod(setStringValue)

def initialize():
    raise NotImplementedError("initialize")
sun.management.Flag.initialize = staticmethod(initialize)

def getCollectionCount():
    raise NotImplementedError("getCollectionCount")
sun.management.GarbageCollectorImpl.getCollectionCount = getCollectionCount

def getCollectionTime():
    raise NotImplementedError("getCollectionTime")
sun.management.GarbageCollectorImpl.getCollectionTime = getCollectionTime

def setNotificationEnabled(a0, a1):
    raise NotImplementedError("setNotificationEnabled")
sun.management.GarbageCollectorImpl.setNotificationEnabled = setNotificationEnabled

def getNumGcExtAttributes(a0):
    raise NotImplementedError("getNumGcExtAttributes")
sun.management.GcInfoBuilder.getNumGcExtAttributes = getNumGcExtAttributes

def fillGcAttributeInfo(a0, a1, a2, a3, a4):
    raise NotImplementedError("fillGcAttributeInfo")
sun.management.GcInfoBuilder.fillGcAttributeInfo = fillGcAttributeInfo

def getLastGcInfo0(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("getLastGcInfo0")
sun.management.GcInfoBuilder.getLastGcInfo0 = getLastGcInfo0

def dumpHeap0(a0, a1):
    raise NotImplementedError("dumpHeap0")
sun.management.HotSpotDiagnostic.dumpHeap0 = dumpHeap0

def getInternalThreadCount():
    raise NotImplementedError("getInternalThreadCount")
sun.management.HotspotThread.getInternalThreadCount = getInternalThreadCount

def getInternalThreadTimes0(a0, a1):
    raise NotImplementedError("getInternalThreadTimes0")
sun.management.HotspotThread.getInternalThreadTimes0 = getInternalThreadTimes0

def getMemoryPools0():
    raise NotImplementedError("getMemoryPools0")
sun.management.MemoryImpl.getMemoryPools0 = staticmethod(getMemoryPools0)

def getMemoryManagers0():
    raise NotImplementedError("getMemoryManagers0")
sun.management.MemoryImpl.getMemoryManagers0 = staticmethod(getMemoryManagers0)

def getMemoryUsage0(a0):
    raise NotImplementedError("getMemoryUsage0")
sun.management.MemoryImpl.getMemoryUsage0 = getMemoryUsage0

def setVerboseGC(a0):
    raise NotImplementedError("setVerboseGC")
sun.management.MemoryImpl.setVerboseGC = setVerboseGC

def getMemoryPools0():
    raise NotImplementedError("getMemoryPools0")
sun.management.MemoryManagerImpl.getMemoryPools0 = getMemoryPools0

def getUsage0():
    raise NotImplementedError("getUsage0")
sun.management.MemoryPoolImpl.getUsage0 = getUsage0

def getPeakUsage0():
    raise NotImplementedError("getPeakUsage0")
sun.management.MemoryPoolImpl.getPeakUsage0 = getPeakUsage0

def getCollectionUsage0():
    raise NotImplementedError("getCollectionUsage0")
sun.management.MemoryPoolImpl.getCollectionUsage0 = getCollectionUsage0

def setUsageThreshold0(a0, a1):
    raise NotImplementedError("setUsageThreshold0")
sun.management.MemoryPoolImpl.setUsageThreshold0 = setUsageThreshold0

def setCollectionThreshold0(a0, a1):
    raise NotImplementedError("setCollectionThreshold0")
sun.management.MemoryPoolImpl.setCollectionThreshold0 = setCollectionThreshold0

def resetPeakUsage0():
    raise NotImplementedError("resetPeakUsage0")
sun.management.MemoryPoolImpl.resetPeakUsage0 = resetPeakUsage0

def getMemoryManagers0():
    raise NotImplementedError("getMemoryManagers0")
sun.management.MemoryPoolImpl.getMemoryManagers0 = getMemoryManagers0

def setPoolUsageSensor(a0):
    raise NotImplementedError("setPoolUsageSensor")
sun.management.MemoryPoolImpl.setPoolUsageSensor = setPoolUsageSensor

def setPoolCollectionSensor(a0):
    raise NotImplementedError("setPoolCollectionSensor")
sun.management.MemoryPoolImpl.setPoolCollectionSensor = setPoolCollectionSensor

def getCommittedVirtualMemorySize0():
    raise NotImplementedError("getCommittedVirtualMemorySize0")
sun.management.OperatingSystemImpl.getCommittedVirtualMemorySize0 = getCommittedVirtualMemorySize0

def getTotalSwapSpaceSize():
    raise NotImplementedError("getTotalSwapSpaceSize")
sun.management.OperatingSystemImpl.getTotalSwapSpaceSize = getTotalSwapSpaceSize

def getFreeSwapSpaceSize():
    raise NotImplementedError("getFreeSwapSpaceSize")
sun.management.OperatingSystemImpl.getFreeSwapSpaceSize = getFreeSwapSpaceSize

def getProcessCpuTime():
    raise NotImplementedError("getProcessCpuTime")
sun.management.OperatingSystemImpl.getProcessCpuTime = getProcessCpuTime

def getFreePhysicalMemorySize():
    raise NotImplementedError("getFreePhysicalMemorySize")
sun.management.OperatingSystemImpl.getFreePhysicalMemorySize = getFreePhysicalMemorySize

def getTotalPhysicalMemorySize():
    raise NotImplementedError("getTotalPhysicalMemorySize")
sun.management.OperatingSystemImpl.getTotalPhysicalMemorySize = getTotalPhysicalMemorySize

def getSystemCpuLoad():
    raise NotImplementedError("getSystemCpuLoad")
sun.management.OperatingSystemImpl.getSystemCpuLoad = getSystemCpuLoad

def getProcessCpuLoad():
    raise NotImplementedError("getProcessCpuLoad")
sun.management.OperatingSystemImpl.getProcessCpuLoad = getProcessCpuLoad

def initialize():
    raise NotImplementedError("initialize")
sun.management.OperatingSystemImpl.initialize = staticmethod(initialize)

def getThreads():
    raise NotImplementedError("getThreads")
sun.management.ThreadImpl.getThreads = staticmethod(getThreads)

def getThreadInfo1(a0, a1, a2):
    raise NotImplementedError("getThreadInfo1")
sun.management.ThreadImpl.getThreadInfo1 = staticmethod(getThreadInfo1)

def getThreadTotalCpuTime0(a0):
    raise NotImplementedError("getThreadTotalCpuTime0")
sun.management.ThreadImpl.getThreadTotalCpuTime0 = staticmethod(getThreadTotalCpuTime0)

def getThreadTotalCpuTime1(a0, a1):
    raise NotImplementedError("getThreadTotalCpuTime1")
sun.management.ThreadImpl.getThreadTotalCpuTime1 = staticmethod(getThreadTotalCpuTime1)

def getThreadUserCpuTime0(a0):
    raise NotImplementedError("getThreadUserCpuTime0")
sun.management.ThreadImpl.getThreadUserCpuTime0 = staticmethod(getThreadUserCpuTime0)

def getThreadUserCpuTime1(a0, a1):
    raise NotImplementedError("getThreadUserCpuTime1")
sun.management.ThreadImpl.getThreadUserCpuTime1 = staticmethod(getThreadUserCpuTime1)

def getThreadAllocatedMemory1(a0, a1):
    raise NotImplementedError("getThreadAllocatedMemory1")
sun.management.ThreadImpl.getThreadAllocatedMemory1 = staticmethod(getThreadAllocatedMemory1)

def setThreadCpuTimeEnabled0(a0):
    raise NotImplementedError("setThreadCpuTimeEnabled0")
sun.management.ThreadImpl.setThreadCpuTimeEnabled0 = staticmethod(setThreadCpuTimeEnabled0)

def setThreadAllocatedMemoryEnabled0(a0):
    raise NotImplementedError("setThreadAllocatedMemoryEnabled0")
sun.management.ThreadImpl.setThreadAllocatedMemoryEnabled0 = staticmethod(setThreadAllocatedMemoryEnabled0)

def setThreadContentionMonitoringEnabled0(a0):
    raise NotImplementedError("setThreadContentionMonitoringEnabled0")
sun.management.ThreadImpl.setThreadContentionMonitoringEnabled0 = staticmethod(setThreadContentionMonitoringEnabled0)

def findMonitorDeadlockedThreads0():
    raise NotImplementedError("findMonitorDeadlockedThreads0")
sun.management.ThreadImpl.findMonitorDeadlockedThreads0 = staticmethod(findMonitorDeadlockedThreads0)

def findDeadlockedThreads0():
    raise NotImplementedError("findDeadlockedThreads0")
sun.management.ThreadImpl.findDeadlockedThreads0 = staticmethod(findDeadlockedThreads0)

def resetPeakThreadCount0():
    raise NotImplementedError("resetPeakThreadCount0")
sun.management.ThreadImpl.resetPeakThreadCount0 = staticmethod(resetPeakThreadCount0)

def dumpThreads0(a0, a1, a2):
    raise NotImplementedError("dumpThreads0")
sun.management.ThreadImpl.dumpThreads0 = staticmethod(dumpThreads0)

def resetContentionTimes0(a0):
    raise NotImplementedError("resetContentionTimes0")
sun.management.ThreadImpl.resetContentionTimes0 = staticmethod(resetContentionTimes0)

def getVersion0():
    raise NotImplementedError("getVersion0")
sun.management.VMManagementImpl.getVersion0 = staticmethod(getVersion0)

def initOptionalSupportFields():
    raise NotImplementedError("initOptionalSupportFields")
sun.management.VMManagementImpl.initOptionalSupportFields = staticmethod(initOptionalSupportFields)

def isThreadContentionMonitoringEnabled():
    raise NotImplementedError("isThreadContentionMonitoringEnabled")
sun.management.VMManagementImpl.isThreadContentionMonitoringEnabled = isThreadContentionMonitoringEnabled

def isThreadCpuTimeEnabled():
    raise NotImplementedError("isThreadCpuTimeEnabled")
sun.management.VMManagementImpl.isThreadCpuTimeEnabled = isThreadCpuTimeEnabled

def isThreadAllocatedMemoryEnabled():
    raise NotImplementedError("isThreadAllocatedMemoryEnabled")
sun.management.VMManagementImpl.isThreadAllocatedMemoryEnabled = isThreadAllocatedMemoryEnabled

def getTotalClassCount():
    raise NotImplementedError("getTotalClassCount")
sun.management.VMManagementImpl.getTotalClassCount = getTotalClassCount

def getUnloadedClassCount():
    raise NotImplementedError("getUnloadedClassCount")
sun.management.VMManagementImpl.getUnloadedClassCount = getUnloadedClassCount

def getVerboseClass():
    raise NotImplementedError("getVerboseClass")
sun.management.VMManagementImpl.getVerboseClass = getVerboseClass

def getVerboseGC():
    raise NotImplementedError("getVerboseGC")
sun.management.VMManagementImpl.getVerboseGC = getVerboseGC

def getProcessId():
    raise NotImplementedError("getProcessId")
sun.management.VMManagementImpl.getProcessId = getProcessId

def getVmArguments0():
    raise NotImplementedError("getVmArguments0")
sun.management.VMManagementImpl.getVmArguments0 = getVmArguments0

def getStartupTime():
    raise NotImplementedError("getStartupTime")
sun.management.VMManagementImpl.getStartupTime = getStartupTime

def getUptime0():
    raise NotImplementedError("getUptime0")
sun.management.VMManagementImpl.getUptime0 = getUptime0

def getAvailableProcessors():
    raise NotImplementedError("getAvailableProcessors")
sun.management.VMManagementImpl.getAvailableProcessors = getAvailableProcessors

def getTotalCompileTime():
    raise NotImplementedError("getTotalCompileTime")
sun.management.VMManagementImpl.getTotalCompileTime = getTotalCompileTime

def getTotalThreadCount():
    raise NotImplementedError("getTotalThreadCount")
sun.management.VMManagementImpl.getTotalThreadCount = getTotalThreadCount

def getLiveThreadCount():
    raise NotImplementedError("getLiveThreadCount")
sun.management.VMManagementImpl.getLiveThreadCount = getLiveThreadCount

def getPeakThreadCount():
    raise NotImplementedError("getPeakThreadCount")
sun.management.VMManagementImpl.getPeakThreadCount = getPeakThreadCount

def getDaemonThreadCount():
    raise NotImplementedError("getDaemonThreadCount")
sun.management.VMManagementImpl.getDaemonThreadCount = getDaemonThreadCount

def getSafepointCount():
    raise NotImplementedError("getSafepointCount")
sun.management.VMManagementImpl.getSafepointCount = getSafepointCount

def getTotalSafepointTime():
    raise NotImplementedError("getTotalSafepointTime")
sun.management.VMManagementImpl.getTotalSafepointTime = getTotalSafepointTime

def getSafepointSyncTime():
    raise NotImplementedError("getSafepointSyncTime")
sun.management.VMManagementImpl.getSafepointSyncTime = getSafepointSyncTime

def getTotalApplicationNonStoppedTime():
    raise NotImplementedError("getTotalApplicationNonStoppedTime")
sun.management.VMManagementImpl.getTotalApplicationNonStoppedTime = getTotalApplicationNonStoppedTime

def getLoadedClassSize():
    raise NotImplementedError("getLoadedClassSize")
sun.management.VMManagementImpl.getLoadedClassSize = getLoadedClassSize

def getUnloadedClassSize():
    raise NotImplementedError("getUnloadedClassSize")
sun.management.VMManagementImpl.getUnloadedClassSize = getUnloadedClassSize

def getClassLoadingTime():
    raise NotImplementedError("getClassLoadingTime")
sun.management.VMManagementImpl.getClassLoadingTime = getClassLoadingTime

def getMethodDataSize():
    raise NotImplementedError("getMethodDataSize")
sun.management.VMManagementImpl.getMethodDataSize = getMethodDataSize

def getInitializedClassCount():
    raise NotImplementedError("getInitializedClassCount")
sun.management.VMManagementImpl.getInitializedClassCount = getInitializedClassCount

def getClassInitializationTime():
    raise NotImplementedError("getClassInitializationTime")
sun.management.VMManagementImpl.getClassInitializationTime = getClassInitializationTime

def getClassVerificationTime():
    raise NotImplementedError("getClassVerificationTime")
sun.management.VMManagementImpl.getClassVerificationTime = getClassVerificationTime

def maxObjectInspectionAge():
    raise NotImplementedError("maxObjectInspectionAge")
sun.misc.GC.maxObjectInspectionAge = staticmethod(maxObjectInspectionAge)

def toStderr(a0):
    raise NotImplementedError("toStderr")
sun.misc.MessageUtils.toStderr = staticmethod(toStderr)

def toStdout(a0):
    raise NotImplementedError("toStdout")
sun.misc.MessageUtils.toStdout = staticmethod(toStdout)

def initAgentProperties(a0):
    raise NotImplementedError("initAgentProperties")
sun.misc.VMSupport.initAgentProperties = staticmethod(initAgentProperties)

def getVMTemporaryDirectory():
    raise NotImplementedError("getVMTemporaryDirectory")
sun.misc.VMSupport.getVMTemporaryDirectory = staticmethod(getVMTemporaryDirectory)

def getLower0():
    raise NotImplementedError("getLower0")
sun.net.PortConfig.getLower0 = staticmethod(getLower0)

def getUpper0():
    raise NotImplementedError("getUpper0")
sun.net.PortConfig.getUpper0 = staticmethod(getUpper0)

def init0():
    raise NotImplementedError("init0")
sun.net.dns.ResolverConfigurationImpl.init0 = staticmethod(init0)

def loadDNSconfig0():
    raise NotImplementedError("loadDNSconfig0")
sun.net.dns.ResolverConfigurationImpl.loadDNSconfig0 = staticmethod(loadDNSconfig0)

def notifyAddrChange0():
    raise NotImplementedError("notifyAddrChange0")
sun.net.dns.ResolverConfigurationImpl.notifyAddrChange0 = staticmethod(notifyAddrChange0)

def create0():
    raise NotImplementedError("create0")
sun.net.sdp.SdpSupport.create0 = staticmethod(create0)

def convert0(a0):
    raise NotImplementedError("convert0")
sun.net.sdp.SdpSupport.convert0 = staticmethod(convert0)

def initFirst(a0):
    raise NotImplementedError("initFirst")
sun.net.www.protocol.http.ntlm.NTLMAuthSequence.initFirst = staticmethod(initFirst)

def getCredentialsHandle(a0, a1, a2):
    raise NotImplementedError("getCredentialsHandle")
sun.net.www.protocol.http.ntlm.NTLMAuthSequence.getCredentialsHandle = getCredentialsHandle

def getNextToken(a0, a1, a2):
    raise NotImplementedError("getNextToken")
sun.net.www.protocol.http.ntlm.NTLMAuthSequence.getNextToken = getNextToken

def initIDs():
    raise NotImplementedError("initIDs")
sun.nio.ch.DatagramChannelImpl.initIDs = staticmethod(initIDs)

def disconnect0(a0, a1):
    raise NotImplementedError("disconnect0")
sun.nio.ch.DatagramChannelImpl.disconnect0 = staticmethod(disconnect0)

def receive0(a0, a1, a2, a3):
    raise NotImplementedError("receive0")
sun.nio.ch.DatagramChannelImpl.receive0 = receive0

def send0(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("send0")
sun.nio.ch.DatagramChannelImpl.send0 = send0

def read0(a0, a1, a2):
    raise NotImplementedError("read0")
sun.nio.ch.DatagramDispatcher.read0 = staticmethod(read0)

def readv0(a0, a1, a2):
    raise NotImplementedError("readv0")
sun.nio.ch.DatagramDispatcher.readv0 = staticmethod(readv0)

def write0(a0, a1, a2):
    raise NotImplementedError("write0")
sun.nio.ch.DatagramDispatcher.write0 = staticmethod(write0)

def writev0(a0, a1, a2):
    raise NotImplementedError("writev0")
sun.nio.ch.DatagramDispatcher.writev0 = staticmethod(writev0)

def init(a0):
    raise NotImplementedError("init")
sun.nio.ch.FileKey.init = init

def initIDs():
    raise NotImplementedError("initIDs")
sun.nio.ch.FileKey.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
sun.nio.ch.Iocp.initIDs = staticmethod(initIDs)

def createIoCompletionPort(a0, a1, a2, a3):
    raise NotImplementedError("createIoCompletionPort")
sun.nio.ch.Iocp.createIoCompletionPort = staticmethod(createIoCompletionPort)

def close0(a0):
    raise NotImplementedError("close0")
sun.nio.ch.Iocp.close0 = staticmethod(close0)

def getQueuedCompletionStatus(a0, a1):
    raise NotImplementedError("getQueuedCompletionStatus")
sun.nio.ch.Iocp.getQueuedCompletionStatus = staticmethod(getQueuedCompletionStatus)

def postQueuedCompletionStatus(a0, a1):
    raise NotImplementedError("postQueuedCompletionStatus")
sun.nio.ch.Iocp.postQueuedCompletionStatus = staticmethod(postQueuedCompletionStatus)

def getErrorMessage(a0):
    raise NotImplementedError("getErrorMessage")
sun.nio.ch.Iocp.getErrorMessage = staticmethod(getErrorMessage)

def isIPv6Available0():
    raise NotImplementedError("isIPv6Available0")
sun.nio.ch.Net.isIPv6Available0 = staticmethod(isIPv6Available0)

def isExclusiveBindAvailable():
    raise NotImplementedError("isExclusiveBindAvailable")
sun.nio.ch.Net.isExclusiveBindAvailable = staticmethod(isExclusiveBindAvailable)

def canIPv6SocketJoinIPv4Group0():
    raise NotImplementedError("canIPv6SocketJoinIPv4Group0")
sun.nio.ch.Net.canIPv6SocketJoinIPv4Group0 = staticmethod(canIPv6SocketJoinIPv4Group0)

def canJoin6WithIPv4Group0():
    raise NotImplementedError("canJoin6WithIPv4Group0")
sun.nio.ch.Net.canJoin6WithIPv4Group0 = staticmethod(canJoin6WithIPv4Group0)

def socket0(a0, a1, a2, a3):
    raise NotImplementedError("socket0")
sun.nio.ch.Net.socket0 = staticmethod(socket0)

def bind0(a0, a1, a2, a3, a4):
    raise NotImplementedError("bind0")
sun.nio.ch.Net.bind0 = staticmethod(bind0)

def listen(a0, a1):
    raise NotImplementedError("listen")
sun.nio.ch.Net.listen = staticmethod(listen)

def connect0(a0, a1, a2, a3):
    raise NotImplementedError("connect0")
sun.nio.ch.Net.connect0 = staticmethod(connect0)

def shutdown(a0, a1):
    raise NotImplementedError("shutdown")
sun.nio.ch.Net.shutdown = staticmethod(shutdown)

def localPort(a0):
    raise NotImplementedError("localPort")
sun.nio.ch.Net.localPort = staticmethod(localPort)

def localInetAddress(a0):
    raise NotImplementedError("localInetAddress")
sun.nio.ch.Net.localInetAddress = staticmethod(localInetAddress)

def remotePort(a0):
    raise NotImplementedError("remotePort")
sun.nio.ch.Net.remotePort = staticmethod(remotePort)

def remoteInetAddress(a0):
    raise NotImplementedError("remoteInetAddress")
sun.nio.ch.Net.remoteInetAddress = staticmethod(remoteInetAddress)

def getIntOption0(a0, a1, a2, a3):
    raise NotImplementedError("getIntOption0")
sun.nio.ch.Net.getIntOption0 = staticmethod(getIntOption0)

def setIntOption0(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("setIntOption0")
sun.nio.ch.Net.setIntOption0 = staticmethod(setIntOption0)

def poll(a0, a1, a2):
    raise NotImplementedError("poll")
sun.nio.ch.Net.poll = staticmethod(poll)

def joinOrDrop4(a0, a1, a2, a3, a4):
    raise NotImplementedError("joinOrDrop4")
sun.nio.ch.Net.joinOrDrop4 = staticmethod(joinOrDrop4)

def blockOrUnblock4(a0, a1, a2, a3, a4):
    raise NotImplementedError("blockOrUnblock4")
sun.nio.ch.Net.blockOrUnblock4 = staticmethod(blockOrUnblock4)

def joinOrDrop6(a0, a1, a2, a3, a4):
    raise NotImplementedError("joinOrDrop6")
sun.nio.ch.Net.joinOrDrop6 = staticmethod(joinOrDrop6)

def blockOrUnblock6(a0, a1, a2, a3, a4):
    raise NotImplementedError("blockOrUnblock6")
sun.nio.ch.Net.blockOrUnblock6 = staticmethod(blockOrUnblock6)

def setInterface4(a0, a1):
    raise NotImplementedError("setInterface4")
sun.nio.ch.Net.setInterface4 = staticmethod(setInterface4)

def getInterface4(a0):
    raise NotImplementedError("getInterface4")
sun.nio.ch.Net.getInterface4 = staticmethod(getInterface4)

def setInterface6(a0, a1):
    raise NotImplementedError("setInterface6")
sun.nio.ch.Net.setInterface6 = staticmethod(setInterface6)

def getInterface6(a0):
    raise NotImplementedError("getInterface6")
sun.nio.ch.Net.getInterface6 = staticmethod(getInterface6)

def initIDs():
    raise NotImplementedError("initIDs")
sun.nio.ch.Net.initIDs = staticmethod(initIDs)

def pollinValue():
    raise NotImplementedError("pollinValue")
sun.nio.ch.Net.pollinValue = staticmethod(pollinValue)

def polloutValue():
    raise NotImplementedError("polloutValue")
sun.nio.ch.Net.polloutValue = staticmethod(polloutValue)

def pollerrValue():
    raise NotImplementedError("pollerrValue")
sun.nio.ch.Net.pollerrValue = staticmethod(pollerrValue)

def pollhupValue():
    raise NotImplementedError("pollhupValue")
sun.nio.ch.Net.pollhupValue = staticmethod(pollhupValue)

def pollnvalValue():
    raise NotImplementedError("pollnvalValue")
sun.nio.ch.Net.pollnvalValue = staticmethod(pollnvalValue)

def pollconnValue():
    raise NotImplementedError("pollconnValue")
sun.nio.ch.Net.pollconnValue = staticmethod(pollconnValue)

def accept0(a0, a1, a2):
    raise NotImplementedError("accept0")
sun.nio.ch.ServerSocketChannelImpl.accept0 = accept0

def initIDs():
    raise NotImplementedError("initIDs")
sun.nio.ch.ServerSocketChannelImpl.initIDs = staticmethod(initIDs)

def checkConnect(a0, a1, a2):
    raise NotImplementedError("checkConnect")
sun.nio.ch.SocketChannelImpl.checkConnect = staticmethod(checkConnect)

def sendOutOfBandData(a0, a1):
    raise NotImplementedError("sendOutOfBandData")
sun.nio.ch.SocketChannelImpl.sendOutOfBandData = staticmethod(sendOutOfBandData)

def read0(a0, a1, a2):
    raise NotImplementedError("read0")
sun.nio.ch.SocketDispatcher.read0 = staticmethod(read0)

def readv0(a0, a1, a2):
    raise NotImplementedError("readv0")
sun.nio.ch.SocketDispatcher.readv0 = staticmethod(readv0)

def write0(a0, a1, a2):
    raise NotImplementedError("write0")
sun.nio.ch.SocketDispatcher.write0 = staticmethod(write0)

def writev0(a0, a1, a2):
    raise NotImplementedError("writev0")
sun.nio.ch.SocketDispatcher.writev0 = staticmethod(writev0)

def preClose0(a0):
    raise NotImplementedError("preClose0")
sun.nio.ch.SocketDispatcher.preClose0 = staticmethod(preClose0)

def close0(a0):
    raise NotImplementedError("close0")
sun.nio.ch.SocketDispatcher.close0 = staticmethod(close0)

def readFile(a0, a1, a2, a3, a4):
    raise NotImplementedError("readFile")
sun.nio.ch.WindowsAsynchronousFileChannelImpl.readFile = staticmethod(readFile)

def writeFile(a0, a1, a2, a3, a4):
    raise NotImplementedError("writeFile")
sun.nio.ch.WindowsAsynchronousFileChannelImpl.writeFile = staticmethod(writeFile)

def lockFile(a0, a1, a2, a3, a4):
    raise NotImplementedError("lockFile")
sun.nio.ch.WindowsAsynchronousFileChannelImpl.lockFile = staticmethod(lockFile)

def close0(a0):
    raise NotImplementedError("close0")
sun.nio.ch.WindowsAsynchronousFileChannelImpl.close0 = staticmethod(close0)

def initIDs():
    raise NotImplementedError("initIDs")
sun.nio.ch.WindowsAsynchronousServerSocketChannelImpl.initIDs = staticmethod(initIDs)

def accept0(a0, a1, a2, a3):
    raise NotImplementedError("accept0")
sun.nio.ch.WindowsAsynchronousServerSocketChannelImpl.accept0 = staticmethod(accept0)

def updateAcceptContext(a0, a1):
    raise NotImplementedError("updateAcceptContext")
sun.nio.ch.WindowsAsynchronousServerSocketChannelImpl.updateAcceptContext = staticmethod(updateAcceptContext)

def closesocket0(a0):
    raise NotImplementedError("closesocket0")
sun.nio.ch.WindowsAsynchronousServerSocketChannelImpl.closesocket0 = staticmethod(closesocket0)

def initIDs():
    raise NotImplementedError("initIDs")
sun.nio.ch.WindowsAsynchronousSocketChannelImpl.initIDs = staticmethod(initIDs)

def connect0(a0, a1, a2, a3, a4):
    raise NotImplementedError("connect0")
sun.nio.ch.WindowsAsynchronousSocketChannelImpl.connect0 = staticmethod(connect0)

def updateConnectContext(a0):
    raise NotImplementedError("updateConnectContext")
sun.nio.ch.WindowsAsynchronousSocketChannelImpl.updateConnectContext = staticmethod(updateConnectContext)

def read0(a0, a1, a2, a3):
    raise NotImplementedError("read0")
sun.nio.ch.WindowsAsynchronousSocketChannelImpl.read0 = staticmethod(read0)

def write0(a0, a1, a2, a3):
    raise NotImplementedError("write0")
sun.nio.ch.WindowsAsynchronousSocketChannelImpl.write0 = staticmethod(write0)

def shutdown0(a0, a1):
    raise NotImplementedError("shutdown0")
sun.nio.ch.WindowsAsynchronousSocketChannelImpl.shutdown0 = staticmethod(shutdown0)

def closesocket0(a0):
    raise NotImplementedError("closesocket0")
sun.nio.ch.WindowsAsynchronousSocketChannelImpl.closesocket0 = staticmethod(closesocket0)

def poll0(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("poll0")
sun.nio.ch.WindowsSelectorImpl__SubSelector.poll0 = poll0

def setWakeupSocket0(a0):
    raise NotImplementedError("setWakeupSocket0")
sun.nio.ch.WindowsSelectorImpl.setWakeupSocket0 = setWakeupSocket0

def resetWakeupSocket0(a0):
    raise NotImplementedError("resetWakeupSocket0")
sun.nio.ch.WindowsSelectorImpl.resetWakeupSocket0 = resetWakeupSocket0

def discardUrgentData(a0):
    raise NotImplementedError("discardUrgentData")
sun.nio.ch.WindowsSelectorImpl.discardUrgentData = discardUrgentData

def queryStringValue(a0, a1):
    raise NotImplementedError("queryStringValue")
sun.nio.fs.RegistryFileTypeDetector.queryStringValue = staticmethod(queryStringValue)

def CreateEvent(a0, a1):
    raise NotImplementedError("CreateEvent")
sun.nio.fs.WindowsNativeDispatcher.CreateEvent = staticmethod(CreateEvent)

def CreateFile0(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("CreateFile0")
sun.nio.fs.WindowsNativeDispatcher.CreateFile0 = staticmethod(CreateFile0)

def CloseHandle(a0):
    raise NotImplementedError("CloseHandle")
sun.nio.fs.WindowsNativeDispatcher.CloseHandle = staticmethod(CloseHandle)

def DeleteFile0(a0):
    raise NotImplementedError("DeleteFile0")
sun.nio.fs.WindowsNativeDispatcher.DeleteFile0 = staticmethod(DeleteFile0)

def CreateDirectory0(a0, a1):
    raise NotImplementedError("CreateDirectory0")
sun.nio.fs.WindowsNativeDispatcher.CreateDirectory0 = staticmethod(CreateDirectory0)

def RemoveDirectory0(a0):
    raise NotImplementedError("RemoveDirectory0")
sun.nio.fs.WindowsNativeDispatcher.RemoveDirectory0 = staticmethod(RemoveDirectory0)

def DeviceIoControlSetSparse(a0):
    raise NotImplementedError("DeviceIoControlSetSparse")
sun.nio.fs.WindowsNativeDispatcher.DeviceIoControlSetSparse = staticmethod(DeviceIoControlSetSparse)

def DeviceIoControlGetReparsePoint(a0, a1, a2):
    raise NotImplementedError("DeviceIoControlGetReparsePoint")
sun.nio.fs.WindowsNativeDispatcher.DeviceIoControlGetReparsePoint = staticmethod(DeviceIoControlGetReparsePoint)

def FindFirstFile0(a0, a1):
    raise NotImplementedError("FindFirstFile0")
sun.nio.fs.WindowsNativeDispatcher.FindFirstFile0 = staticmethod(FindFirstFile0)

def FindFirstFile1(a0, a1):
    raise NotImplementedError("FindFirstFile1")
sun.nio.fs.WindowsNativeDispatcher.FindFirstFile1 = staticmethod(FindFirstFile1)

def FindNextFile(a0, a1):
    raise NotImplementedError("FindNextFile")
sun.nio.fs.WindowsNativeDispatcher.FindNextFile = staticmethod(FindNextFile)

def FindFirstStream0(a0, a1):
    raise NotImplementedError("FindFirstStream0")
sun.nio.fs.WindowsNativeDispatcher.FindFirstStream0 = staticmethod(FindFirstStream0)

def FindNextStream(a0):
    raise NotImplementedError("FindNextStream")
sun.nio.fs.WindowsNativeDispatcher.FindNextStream = staticmethod(FindNextStream)

def FindClose(a0):
    raise NotImplementedError("FindClose")
sun.nio.fs.WindowsNativeDispatcher.FindClose = staticmethod(FindClose)

def GetFileInformationByHandle(a0, a1):
    raise NotImplementedError("GetFileInformationByHandle")
sun.nio.fs.WindowsNativeDispatcher.GetFileInformationByHandle = staticmethod(GetFileInformationByHandle)

def CopyFileEx0(a0, a1, a2, a3):
    raise NotImplementedError("CopyFileEx0")
sun.nio.fs.WindowsNativeDispatcher.CopyFileEx0 = staticmethod(CopyFileEx0)

def MoveFileEx0(a0, a1, a2):
    raise NotImplementedError("MoveFileEx0")
sun.nio.fs.WindowsNativeDispatcher.MoveFileEx0 = staticmethod(MoveFileEx0)

def GetFileAttributes0(a0):
    raise NotImplementedError("GetFileAttributes0")
sun.nio.fs.WindowsNativeDispatcher.GetFileAttributes0 = staticmethod(GetFileAttributes0)

def SetFileAttributes0(a0, a1):
    raise NotImplementedError("SetFileAttributes0")
sun.nio.fs.WindowsNativeDispatcher.SetFileAttributes0 = staticmethod(SetFileAttributes0)

def GetFileAttributesEx0(a0, a1):
    raise NotImplementedError("GetFileAttributesEx0")
sun.nio.fs.WindowsNativeDispatcher.GetFileAttributesEx0 = staticmethod(GetFileAttributesEx0)

def SetFileTime(a0, a1, a2, a3):
    raise NotImplementedError("SetFileTime")
sun.nio.fs.WindowsNativeDispatcher.SetFileTime = staticmethod(SetFileTime)

def SetEndOfFile(a0):
    raise NotImplementedError("SetEndOfFile")
sun.nio.fs.WindowsNativeDispatcher.SetEndOfFile = staticmethod(SetEndOfFile)

def GetLogicalDrives():
    raise NotImplementedError("GetLogicalDrives")
sun.nio.fs.WindowsNativeDispatcher.GetLogicalDrives = staticmethod(GetLogicalDrives)

def GetVolumeInformation0(a0, a1):
    raise NotImplementedError("GetVolumeInformation0")
sun.nio.fs.WindowsNativeDispatcher.GetVolumeInformation0 = staticmethod(GetVolumeInformation0)

def GetDriveType0(a0):
    raise NotImplementedError("GetDriveType0")
sun.nio.fs.WindowsNativeDispatcher.GetDriveType0 = staticmethod(GetDriveType0)

def GetDiskFreeSpaceEx0(a0, a1):
    raise NotImplementedError("GetDiskFreeSpaceEx0")
sun.nio.fs.WindowsNativeDispatcher.GetDiskFreeSpaceEx0 = staticmethod(GetDiskFreeSpaceEx0)

def GetVolumePathName0(a0):
    raise NotImplementedError("GetVolumePathName0")
sun.nio.fs.WindowsNativeDispatcher.GetVolumePathName0 = staticmethod(GetVolumePathName0)

def InitializeSecurityDescriptor(a0):
    raise NotImplementedError("InitializeSecurityDescriptor")
sun.nio.fs.WindowsNativeDispatcher.InitializeSecurityDescriptor = staticmethod(InitializeSecurityDescriptor)

def InitializeAcl(a0, a1):
    raise NotImplementedError("InitializeAcl")
sun.nio.fs.WindowsNativeDispatcher.InitializeAcl = staticmethod(InitializeAcl)

def GetFileSecurity0(a0, a1, a2, a3):
    raise NotImplementedError("GetFileSecurity0")
sun.nio.fs.WindowsNativeDispatcher.GetFileSecurity0 = staticmethod(GetFileSecurity0)

def SetFileSecurity0(a0, a1, a2):
    raise NotImplementedError("SetFileSecurity0")
sun.nio.fs.WindowsNativeDispatcher.SetFileSecurity0 = staticmethod(SetFileSecurity0)

def GetSecurityDescriptorOwner(a0):
    raise NotImplementedError("GetSecurityDescriptorOwner")
sun.nio.fs.WindowsNativeDispatcher.GetSecurityDescriptorOwner = staticmethod(GetSecurityDescriptorOwner)

def SetSecurityDescriptorOwner(a0, a1):
    raise NotImplementedError("SetSecurityDescriptorOwner")
sun.nio.fs.WindowsNativeDispatcher.SetSecurityDescriptorOwner = staticmethod(SetSecurityDescriptorOwner)

def GetSecurityDescriptorDacl(a0):
    raise NotImplementedError("GetSecurityDescriptorDacl")
sun.nio.fs.WindowsNativeDispatcher.GetSecurityDescriptorDacl = staticmethod(GetSecurityDescriptorDacl)

def SetSecurityDescriptorDacl(a0, a1):
    raise NotImplementedError("SetSecurityDescriptorDacl")
sun.nio.fs.WindowsNativeDispatcher.SetSecurityDescriptorDacl = staticmethod(SetSecurityDescriptorDacl)

def GetAclInformation0(a0, a1):
    raise NotImplementedError("GetAclInformation0")
sun.nio.fs.WindowsNativeDispatcher.GetAclInformation0 = staticmethod(GetAclInformation0)

def GetAce(a0, a1):
    raise NotImplementedError("GetAce")
sun.nio.fs.WindowsNativeDispatcher.GetAce = staticmethod(GetAce)

def AddAccessAllowedAceEx(a0, a1, a2, a3):
    raise NotImplementedError("AddAccessAllowedAceEx")
sun.nio.fs.WindowsNativeDispatcher.AddAccessAllowedAceEx = staticmethod(AddAccessAllowedAceEx)

def AddAccessDeniedAceEx(a0, a1, a2, a3):
    raise NotImplementedError("AddAccessDeniedAceEx")
sun.nio.fs.WindowsNativeDispatcher.AddAccessDeniedAceEx = staticmethod(AddAccessDeniedAceEx)

def LookupAccountSid0(a0, a1):
    raise NotImplementedError("LookupAccountSid0")
sun.nio.fs.WindowsNativeDispatcher.LookupAccountSid0 = staticmethod(LookupAccountSid0)

def LookupAccountName0(a0, a1, a2):
    raise NotImplementedError("LookupAccountName0")
sun.nio.fs.WindowsNativeDispatcher.LookupAccountName0 = staticmethod(LookupAccountName0)

def GetLengthSid(a0):
    raise NotImplementedError("GetLengthSid")
sun.nio.fs.WindowsNativeDispatcher.GetLengthSid = staticmethod(GetLengthSid)

def ConvertSidToStringSid(a0):
    raise NotImplementedError("ConvertSidToStringSid")
sun.nio.fs.WindowsNativeDispatcher.ConvertSidToStringSid = staticmethod(ConvertSidToStringSid)

def ConvertStringSidToSid0(a0):
    raise NotImplementedError("ConvertStringSidToSid0")
sun.nio.fs.WindowsNativeDispatcher.ConvertStringSidToSid0 = staticmethod(ConvertStringSidToSid0)

def GetCurrentProcess():
    raise NotImplementedError("GetCurrentProcess")
sun.nio.fs.WindowsNativeDispatcher.GetCurrentProcess = staticmethod(GetCurrentProcess)

def GetCurrentThread():
    raise NotImplementedError("GetCurrentThread")
sun.nio.fs.WindowsNativeDispatcher.GetCurrentThread = staticmethod(GetCurrentThread)

def OpenProcessToken(a0, a1):
    raise NotImplementedError("OpenProcessToken")
sun.nio.fs.WindowsNativeDispatcher.OpenProcessToken = staticmethod(OpenProcessToken)

def OpenThreadToken(a0, a1, a2):
    raise NotImplementedError("OpenThreadToken")
sun.nio.fs.WindowsNativeDispatcher.OpenThreadToken = staticmethod(OpenThreadToken)

def DuplicateTokenEx(a0, a1):
    raise NotImplementedError("DuplicateTokenEx")
sun.nio.fs.WindowsNativeDispatcher.DuplicateTokenEx = staticmethod(DuplicateTokenEx)

def SetThreadToken(a0, a1):
    raise NotImplementedError("SetThreadToken")
sun.nio.fs.WindowsNativeDispatcher.SetThreadToken = staticmethod(SetThreadToken)

def GetTokenInformation(a0, a1, a2, a3):
    raise NotImplementedError("GetTokenInformation")
sun.nio.fs.WindowsNativeDispatcher.GetTokenInformation = staticmethod(GetTokenInformation)

def AdjustTokenPrivileges(a0, a1, a2):
    raise NotImplementedError("AdjustTokenPrivileges")
sun.nio.fs.WindowsNativeDispatcher.AdjustTokenPrivileges = staticmethod(AdjustTokenPrivileges)

def AccessCheck(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("AccessCheck")
sun.nio.fs.WindowsNativeDispatcher.AccessCheck = staticmethod(AccessCheck)

def LookupPrivilegeValue0(a0):
    raise NotImplementedError("LookupPrivilegeValue0")
sun.nio.fs.WindowsNativeDispatcher.LookupPrivilegeValue0 = staticmethod(LookupPrivilegeValue0)

def CreateSymbolicLink0(a0, a1, a2):
    raise NotImplementedError("CreateSymbolicLink0")
sun.nio.fs.WindowsNativeDispatcher.CreateSymbolicLink0 = staticmethod(CreateSymbolicLink0)

def CreateHardLink0(a0, a1):
    raise NotImplementedError("CreateHardLink0")
sun.nio.fs.WindowsNativeDispatcher.CreateHardLink0 = staticmethod(CreateHardLink0)

def GetFullPathName0(a0):
    raise NotImplementedError("GetFullPathName0")
sun.nio.fs.WindowsNativeDispatcher.GetFullPathName0 = staticmethod(GetFullPathName0)

def GetFinalPathNameByHandle(a0):
    raise NotImplementedError("GetFinalPathNameByHandle")
sun.nio.fs.WindowsNativeDispatcher.GetFinalPathNameByHandle = staticmethod(GetFinalPathNameByHandle)

def FormatMessage(a0):
    raise NotImplementedError("FormatMessage")
sun.nio.fs.WindowsNativeDispatcher.FormatMessage = staticmethod(FormatMessage)

def LocalFree(a0):
    raise NotImplementedError("LocalFree")
sun.nio.fs.WindowsNativeDispatcher.LocalFree = staticmethod(LocalFree)

def CreateIoCompletionPort(a0, a1, a2):
    raise NotImplementedError("CreateIoCompletionPort")
sun.nio.fs.WindowsNativeDispatcher.CreateIoCompletionPort = staticmethod(CreateIoCompletionPort)

def GetQueuedCompletionStatus0(a0, a1):
    raise NotImplementedError("GetQueuedCompletionStatus0")
sun.nio.fs.WindowsNativeDispatcher.GetQueuedCompletionStatus0 = staticmethod(GetQueuedCompletionStatus0)

def PostQueuedCompletionStatus(a0, a1):
    raise NotImplementedError("PostQueuedCompletionStatus")
sun.nio.fs.WindowsNativeDispatcher.PostQueuedCompletionStatus = staticmethod(PostQueuedCompletionStatus)

def ReadDirectoryChangesW(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("ReadDirectoryChangesW")
sun.nio.fs.WindowsNativeDispatcher.ReadDirectoryChangesW = staticmethod(ReadDirectoryChangesW)

def CancelIo(a0):
    raise NotImplementedError("CancelIo")
sun.nio.fs.WindowsNativeDispatcher.CancelIo = staticmethod(CancelIo)

def GetOverlappedResult(a0, a1):
    raise NotImplementedError("GetOverlappedResult")
sun.nio.fs.WindowsNativeDispatcher.GetOverlappedResult = staticmethod(GetOverlappedResult)

def BackupRead0(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("BackupRead0")
sun.nio.fs.WindowsNativeDispatcher.BackupRead0 = staticmethod(BackupRead0)

def BackupSeek(a0, a1, a2):
    raise NotImplementedError("BackupSeek")
sun.nio.fs.WindowsNativeDispatcher.BackupSeek = staticmethod(BackupSeek)

def initIDs():
    raise NotImplementedError("initIDs")
sun.nio.fs.WindowsNativeDispatcher.initIDs = staticmethod(initIDs)

def startPrintRawData(a0, a1):
    raise NotImplementedError("startPrintRawData")
sun.__print__.Win32PrintJob.startPrintRawData = startPrintRawData

def printRawData(a0, a1):
    raise NotImplementedError("printRawData")
sun.__print__.Win32PrintJob.printRawData = printRawData

def endPrintRawData():
    raise NotImplementedError("endPrintRawData")
sun.__print__.Win32PrintJob.endPrintRawData = endPrintRawData

def getAllMediaIDs(a0, a1):
    raise NotImplementedError("getAllMediaIDs")
sun.__print__.Win32PrintService.getAllMediaIDs = getAllMediaIDs

def getAllMediaSizes(a0, a1):
    raise NotImplementedError("getAllMediaSizes")
sun.__print__.Win32PrintService.getAllMediaSizes = getAllMediaSizes

def getAllMediaTrays(a0, a1):
    raise NotImplementedError("getAllMediaTrays")
sun.__print__.Win32PrintService.getAllMediaTrays = getAllMediaTrays

def getMediaPrintableArea(a0, a1):
    raise NotImplementedError("getMediaPrintableArea")
sun.__print__.Win32PrintService.getMediaPrintableArea = getMediaPrintableArea

def getAllMediaNames(a0, a1):
    raise NotImplementedError("getAllMediaNames")
sun.__print__.Win32PrintService.getAllMediaNames = getAllMediaNames

def getAllMediaTrayNames(a0, a1):
    raise NotImplementedError("getAllMediaTrayNames")
sun.__print__.Win32PrintService.getAllMediaTrayNames = getAllMediaTrayNames

def getCopiesSupported(a0, a1):
    raise NotImplementedError("getCopiesSupported")
sun.__print__.Win32PrintService.getCopiesSupported = getCopiesSupported

def getAllResolutions(a0, a1):
    raise NotImplementedError("getAllResolutions")
sun.__print__.Win32PrintService.getAllResolutions = getAllResolutions

def getCapabilities(a0, a1):
    raise NotImplementedError("getCapabilities")
sun.__print__.Win32PrintService.getCapabilities = getCapabilities

def getDefaultSettings(a0, a1):
    raise NotImplementedError("getDefaultSettings")
sun.__print__.Win32PrintService.getDefaultSettings = getDefaultSettings

def getJobStatus(a0, a1):
    raise NotImplementedError("getJobStatus")
sun.__print__.Win32PrintService.getJobStatus = getJobStatus

def getPrinterPort(a0):
    raise NotImplementedError("getPrinterPort")
sun.__print__.Win32PrintService.getPrinterPort = getPrinterPort

def getDefaultPrinterName():
    raise NotImplementedError("getDefaultPrinterName")
sun.__print__.Win32PrintServiceLookup.getDefaultPrinterName = getDefaultPrinterName

def getAllPrinterNames():
    raise NotImplementedError("getAllPrinterNames")
sun.__print__.Win32PrintServiceLookup.getAllPrinterNames = getAllPrinterNames

def notifyFirstPrinterChange(a0):
    raise NotImplementedError("notifyFirstPrinterChange")
sun.__print__.Win32PrintServiceLookup.notifyFirstPrinterChange = notifyFirstPrinterChange

def notifyClosePrinterChange(a0):
    raise NotImplementedError("notifyClosePrinterChange")
sun.__print__.Win32PrintServiceLookup.notifyClosePrinterChange = notifyClosePrinterChange

def notifyPrinterChange(a0):
    raise NotImplementedError("notifyPrinterChange")
sun.__print__.Win32PrintServiceLookup.notifyPrinterChange = notifyPrinterChange

def init(a0, a1):
    raise NotImplementedError("init")
sun.security.jgss.wrapper.GSSLibStub.init = staticmethod(init)

def getMechPtr(a0):
    raise NotImplementedError("getMechPtr")
sun.security.jgss.wrapper.GSSLibStub.getMechPtr = staticmethod(getMechPtr)

def indicateMechs():
    raise NotImplementedError("indicateMechs")
sun.security.jgss.wrapper.GSSLibStub.indicateMechs = staticmethod(indicateMechs)

def inquireNamesForMech():
    raise NotImplementedError("inquireNamesForMech")
sun.security.jgss.wrapper.GSSLibStub.inquireNamesForMech = inquireNamesForMech

def releaseName(a0):
    raise NotImplementedError("releaseName")
sun.security.jgss.wrapper.GSSLibStub.releaseName = releaseName

def importName(a0, a1):
    raise NotImplementedError("importName")
sun.security.jgss.wrapper.GSSLibStub.importName = importName

def compareName(a0, a1):
    raise NotImplementedError("compareName")
sun.security.jgss.wrapper.GSSLibStub.compareName = compareName

def canonicalizeName(a0):
    raise NotImplementedError("canonicalizeName")
sun.security.jgss.wrapper.GSSLibStub.canonicalizeName = canonicalizeName

def exportName(a0):
    raise NotImplementedError("exportName")
sun.security.jgss.wrapper.GSSLibStub.exportName = exportName

def displayName(a0):
    raise NotImplementedError("displayName")
sun.security.jgss.wrapper.GSSLibStub.displayName = displayName

def acquireCred(a0, a1, a2):
    raise NotImplementedError("acquireCred")
sun.security.jgss.wrapper.GSSLibStub.acquireCred = acquireCred

def releaseCred(a0):
    raise NotImplementedError("releaseCred")
sun.security.jgss.wrapper.GSSLibStub.releaseCred = releaseCred

def getCredName(a0):
    raise NotImplementedError("getCredName")
sun.security.jgss.wrapper.GSSLibStub.getCredName = getCredName

def getCredTime(a0):
    raise NotImplementedError("getCredTime")
sun.security.jgss.wrapper.GSSLibStub.getCredTime = getCredTime

def getCredUsage(a0):
    raise NotImplementedError("getCredUsage")
sun.security.jgss.wrapper.GSSLibStub.getCredUsage = getCredUsage

def importContext(a0):
    raise NotImplementedError("importContext")
sun.security.jgss.wrapper.GSSLibStub.importContext = importContext

def initContext(a0, a1, a2, a3, a4):
    raise NotImplementedError("initContext")
sun.security.jgss.wrapper.GSSLibStub.initContext = initContext

def acceptContext(a0, a1, a2, a3):
    raise NotImplementedError("acceptContext")
sun.security.jgss.wrapper.GSSLibStub.acceptContext = acceptContext

def inquireContext(a0):
    raise NotImplementedError("inquireContext")
sun.security.jgss.wrapper.GSSLibStub.inquireContext = inquireContext

def getContextMech(a0):
    raise NotImplementedError("getContextMech")
sun.security.jgss.wrapper.GSSLibStub.getContextMech = getContextMech

def getContextName(a0, a1):
    raise NotImplementedError("getContextName")
sun.security.jgss.wrapper.GSSLibStub.getContextName = getContextName

def getContextTime(a0):
    raise NotImplementedError("getContextTime")
sun.security.jgss.wrapper.GSSLibStub.getContextTime = getContextTime

def deleteContext(a0):
    raise NotImplementedError("deleteContext")
sun.security.jgss.wrapper.GSSLibStub.deleteContext = deleteContext

def wrapSizeLimit(a0, a1, a2, a3):
    raise NotImplementedError("wrapSizeLimit")
sun.security.jgss.wrapper.GSSLibStub.wrapSizeLimit = wrapSizeLimit

def exportContext(a0):
    raise NotImplementedError("exportContext")
sun.security.jgss.wrapper.GSSLibStub.exportContext = exportContext

def getMic(a0, a1, a2):
    raise NotImplementedError("getMic")
sun.security.jgss.wrapper.GSSLibStub.getMic = getMic

def verifyMic(a0, a1, a2, a3):
    raise NotImplementedError("verifyMic")
sun.security.jgss.wrapper.GSSLibStub.verifyMic = verifyMic

def wrap(a0, a1, a2):
    raise NotImplementedError("wrap")
sun.security.jgss.wrapper.GSSLibStub.wrap = wrap

def unwrap(a0, a1, a2):
    raise NotImplementedError("unwrap")
sun.security.jgss.wrapper.GSSLibStub.unwrap = unwrap

def getWindowsDirectory(a0):
    raise NotImplementedError("getWindowsDirectory")
sun.security.krb5.Config.getWindowsDirectory = staticmethod(getWindowsDirectory)

def acquireDefaultNativeCreds(a0):
    raise NotImplementedError("acquireDefaultNativeCreds")
sun.security.krb5.Credentials.acquireDefaultNativeCreds = staticmethod(acquireDefaultNativeCreds)

def installNotificationCallback():
    raise NotImplementedError("installNotificationCallback")
sun.security.krb5.SCDynamicStoreConfig.installNotificationCallback = staticmethod(installNotificationCallback)

def getKerberosConfig():
    raise NotImplementedError("getKerberosConfig")
sun.security.krb5.SCDynamicStoreConfig.getKerberosConfig = staticmethod(getKerberosConfig)

def nativeGenerateSeed(a0):
    raise NotImplementedError("nativeGenerateSeed")
sun.security.provider.NativeSeedGenerator.nativeGenerateSeed = staticmethod(nativeGenerateSeed)

def SCardEstablishContext(a0):
    raise NotImplementedError("SCardEstablishContext")
sun.security.smartcardio.PCSC.SCardEstablishContext = staticmethod(SCardEstablishContext)

def SCardListReaders(a0):
    raise NotImplementedError("SCardListReaders")
sun.security.smartcardio.PCSC.SCardListReaders = staticmethod(SCardListReaders)

def SCardConnect(a0, a1, a2, a3):
    raise NotImplementedError("SCardConnect")
sun.security.smartcardio.PCSC.SCardConnect = staticmethod(SCardConnect)

def SCardTransmit(a0, a1, a2, a3, a4):
    raise NotImplementedError("SCardTransmit")
sun.security.smartcardio.PCSC.SCardTransmit = staticmethod(SCardTransmit)

def SCardStatus(a0, a1):
    raise NotImplementedError("SCardStatus")
sun.security.smartcardio.PCSC.SCardStatus = staticmethod(SCardStatus)

def SCardDisconnect(a0, a1):
    raise NotImplementedError("SCardDisconnect")
sun.security.smartcardio.PCSC.SCardDisconnect = staticmethod(SCardDisconnect)

def SCardGetStatusChange(a0, a1, a2, a3):
    raise NotImplementedError("SCardGetStatusChange")
sun.security.smartcardio.PCSC.SCardGetStatusChange = staticmethod(SCardGetStatusChange)

def SCardBeginTransaction(a0):
    raise NotImplementedError("SCardBeginTransaction")
sun.security.smartcardio.PCSC.SCardBeginTransaction = staticmethod(SCardBeginTransaction)

def SCardEndTransaction(a0, a1):
    raise NotImplementedError("SCardEndTransaction")
sun.security.smartcardio.PCSC.SCardEndTransaction = staticmethod(SCardEndTransaction)

def SCardControl(a0, a1, a2):
    raise NotImplementedError("SCardControl")
sun.security.smartcardio.PCSC.SCardControl = staticmethod(SCardControl)

def activate0(a0, a1):
    raise NotImplementedError("activate0")
sun.tracing.dtrace.JVM.activate0 = staticmethod(activate0)

def dispose0(a0):
    raise NotImplementedError("dispose0")
sun.tracing.dtrace.JVM.dispose0 = staticmethod(dispose0)

def isEnabled0(a0):
    raise NotImplementedError("isEnabled0")
sun.tracing.dtrace.JVM.isEnabled0 = staticmethod(isEnabled0)

def isSupported0():
    raise NotImplementedError("isSupported0")
sun.tracing.dtrace.JVM.isSupported0 = staticmethod(isSupported0)

def defineClass0(a0, a1, a2, a3, a4):
    raise NotImplementedError("defineClass0")
sun.tracing.dtrace.JVM.defineClass0 = staticmethod(defineClass0)

def initialize():
    raise NotImplementedError("initialize")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.initialize = staticmethod(initialize)

def getDefaultLocale(a0):
    raise NotImplementedError("getDefaultLocale")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getDefaultLocale = staticmethod(getDefaultLocale)

def getDateTimePattern(a0, a1, a2):
    raise NotImplementedError("getDateTimePattern")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getDateTimePattern = staticmethod(getDateTimePattern)

def getCalendarID(a0):
    raise NotImplementedError("getCalendarID")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getCalendarID = staticmethod(getCalendarID)

def getAmPmStrings(a0, a1):
    raise NotImplementedError("getAmPmStrings")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getAmPmStrings = staticmethod(getAmPmStrings)

def getEras(a0, a1):
    raise NotImplementedError("getEras")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getEras = staticmethod(getEras)

def getMonths(a0, a1):
    raise NotImplementedError("getMonths")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getMonths = staticmethod(getMonths)

def getShortMonths(a0, a1):
    raise NotImplementedError("getShortMonths")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getShortMonths = staticmethod(getShortMonths)

def getWeekdays(a0, a1):
    raise NotImplementedError("getWeekdays")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getWeekdays = staticmethod(getWeekdays)

def getShortWeekdays(a0, a1):
    raise NotImplementedError("getShortWeekdays")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getShortWeekdays = staticmethod(getShortWeekdays)

def getNumberPattern(a0, a1):
    raise NotImplementedError("getNumberPattern")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getNumberPattern = staticmethod(getNumberPattern)

def isNativeDigit(a0):
    raise NotImplementedError("isNativeDigit")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.isNativeDigit = staticmethod(isNativeDigit)

def getCurrencySymbol(a0, a1):
    raise NotImplementedError("getCurrencySymbol")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getCurrencySymbol = staticmethod(getCurrencySymbol)

def getDecimalSeparator(a0, a1):
    raise NotImplementedError("getDecimalSeparator")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getDecimalSeparator = staticmethod(getDecimalSeparator)

def getGroupingSeparator(a0, a1):
    raise NotImplementedError("getGroupingSeparator")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getGroupingSeparator = staticmethod(getGroupingSeparator)

def getInfinity(a0, a1):
    raise NotImplementedError("getInfinity")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getInfinity = staticmethod(getInfinity)

def getInternationalCurrencySymbol(a0, a1):
    raise NotImplementedError("getInternationalCurrencySymbol")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getInternationalCurrencySymbol = staticmethod(getInternationalCurrencySymbol)

def getMinusSign(a0, a1):
    raise NotImplementedError("getMinusSign")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getMinusSign = staticmethod(getMinusSign)

def getMonetaryDecimalSeparator(a0, a1):
    raise NotImplementedError("getMonetaryDecimalSeparator")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getMonetaryDecimalSeparator = staticmethod(getMonetaryDecimalSeparator)

def getNaN(a0, a1):
    raise NotImplementedError("getNaN")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getNaN = staticmethod(getNaN)

def getPercent(a0, a1):
    raise NotImplementedError("getPercent")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getPercent = staticmethod(getPercent)

def getPerMill(a0, a1):
    raise NotImplementedError("getPerMill")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getPerMill = staticmethod(getPerMill)

def getZeroDigit(a0, a1):
    raise NotImplementedError("getZeroDigit")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getZeroDigit = staticmethod(getZeroDigit)

def getCalendarDataValue(a0, a1):
    raise NotImplementedError("getCalendarDataValue")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getCalendarDataValue = staticmethod(getCalendarDataValue)

def getDisplayString(a0, a1, a2):
    raise NotImplementedError("getDisplayString")
sun.util.locale.provider.HostLocaleProviderAdapterImpl.getDisplayString = staticmethod(getDisplayString)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.MenuBar.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Event.initIDs = staticmethod(initIDs)

def lazyPaint():
    raise NotImplementedError("lazyPaint")
sun.awt.windows.WLabelPeer.lazyPaint = lazyPaint

def setText(a0):
    raise NotImplementedError("setText")
sun.awt.windows.WLabelPeer.setText = setText

def setAlignment(a0):
    raise NotImplementedError("setAlignment")
sun.awt.windows.WLabelPeer.setAlignment = setAlignment

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WLabelPeer.create = create

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Label.initIDs = staticmethod(initIDs)

def sin(a0):
    raise NotImplementedError("sin")
java.lang.StrictMath.sin = staticmethod(sin)

def cos(a0):
    raise NotImplementedError("cos")
java.lang.StrictMath.cos = staticmethod(cos)

def tan(a0):
    raise NotImplementedError("tan")
java.lang.StrictMath.tan = staticmethod(tan)

def asin(a0):
    raise NotImplementedError("asin")
java.lang.StrictMath.asin = staticmethod(asin)

def acos(a0):
    raise NotImplementedError("acos")
java.lang.StrictMath.acos = staticmethod(acos)

def atan(a0):
    raise NotImplementedError("atan")
java.lang.StrictMath.atan = staticmethod(atan)

def exp(a0):
    raise NotImplementedError("exp")
java.lang.StrictMath.exp = staticmethod(exp)

def log(a0):
    raise NotImplementedError("log")
java.lang.StrictMath.log = staticmethod(log)

def log10(a0):
    raise NotImplementedError("log10")
java.lang.StrictMath.log10 = staticmethod(log10)

def sqrt(a0):
    raise NotImplementedError("sqrt")
java.lang.StrictMath.sqrt = staticmethod(sqrt)

def cbrt(a0):
    raise NotImplementedError("cbrt")
java.lang.StrictMath.cbrt = staticmethod(cbrt)

def IEEEremainder(a0, a1):
    raise NotImplementedError("IEEEremainder")
java.lang.StrictMath.IEEEremainder = staticmethod(IEEEremainder)

def atan2(a0, a1):
    raise NotImplementedError("atan2")
java.lang.StrictMath.atan2 = staticmethod(atan2)

def pow(a0, a1):
    raise NotImplementedError("pow")
java.lang.StrictMath.pow = staticmethod(pow)

def sinh(a0):
    raise NotImplementedError("sinh")
java.lang.StrictMath.sinh = staticmethod(sinh)

def cosh(a0):
    raise NotImplementedError("cosh")
java.lang.StrictMath.cosh = staticmethod(cosh)

def tanh(a0):
    raise NotImplementedError("tanh")
java.lang.StrictMath.tanh = staticmethod(tanh)

def hypot(a0, a1):
    raise NotImplementedError("hypot")
java.lang.StrictMath.hypot = staticmethod(hypot)

def expm1(a0):
    raise NotImplementedError("expm1")
java.lang.StrictMath.expm1 = staticmethod(expm1)

def log1p(a0):
    raise NotImplementedError("log1p")
java.lang.StrictMath.log1p = staticmethod(log1p)

def defineClass0(a0, a1, a2, a3, a4):
    raise NotImplementedError("defineClass0")
java.lang.reflect.Proxy.defineClass0 = staticmethod(defineClass0)

def floatsToBytes(a0, a1, a2, a3, a4):
    raise NotImplementedError("floatsToBytes")
java.io.ObjectOutputStream.floatsToBytes = staticmethod(floatsToBytes)

def doublesToBytes(a0, a1, a2, a3, a4):
    raise NotImplementedError("doublesToBytes")
java.io.ObjectOutputStream.doublesToBytes = staticmethod(doublesToBytes)

def initNative():
    raise NotImplementedError("initNative")
java.io.ObjectStreamClass.initNative = staticmethod(initNative)

def hasStaticInitializer(a0):
    raise NotImplementedError("hasStaticInitializer")
java.io.ObjectStreamClass.hasStaticInitializer = staticmethod(hasStaticInitializer)

def getAll():
    raise NotImplementedError("getAll")
java.net.NetworkInterface.getAll = staticmethod(getAll)

def getByName0(a0):
    raise NotImplementedError("getByName0")
java.net.NetworkInterface.getByName0 = staticmethod(getByName0)

def getByIndex0(a0):
    raise NotImplementedError("getByIndex0")
java.net.NetworkInterface.getByIndex0 = staticmethod(getByIndex0)

def getByInetAddress0(a0):
    raise NotImplementedError("getByInetAddress0")
java.net.NetworkInterface.getByInetAddress0 = staticmethod(getByInetAddress0)

def isUp0(a0, a1):
    raise NotImplementedError("isUp0")
java.net.NetworkInterface.isUp0 = staticmethod(isUp0)

def isLoopback0(a0, a1):
    raise NotImplementedError("isLoopback0")
java.net.NetworkInterface.isLoopback0 = staticmethod(isLoopback0)

def supportsMulticast0(a0, a1):
    raise NotImplementedError("supportsMulticast0")
java.net.NetworkInterface.supportsMulticast0 = staticmethod(supportsMulticast0)

def isP2P0(a0, a1):
    raise NotImplementedError("isP2P0")
java.net.NetworkInterface.isP2P0 = staticmethod(isP2P0)

def getMacAddr0(a0, a1, a2):
    raise NotImplementedError("getMacAddr0")
java.net.NetworkInterface.getMacAddr0 = staticmethod(getMacAddr0)

def getMTU0(a0, a1):
    raise NotImplementedError("getMTU0")
java.net.NetworkInterface.getMTU0 = staticmethod(getMTU0)

def init():
    raise NotImplementedError("init")
java.net.NetworkInterface.init = staticmethod(init)

def bind0(a0, a1, a2):
    raise NotImplementedError("bind0")
java.net.TwoStacksPlainDatagramSocketImpl.bind0 = bind0

def send(a0):
    raise NotImplementedError("send")
java.net.TwoStacksPlainDatagramSocketImpl.send = send

def peek(a0):
    raise NotImplementedError("peek")
java.net.TwoStacksPlainDatagramSocketImpl.peek = peek

def peekData(a0):
    raise NotImplementedError("peekData")
java.net.TwoStacksPlainDatagramSocketImpl.peekData = peekData

def receive0(a0):
    raise NotImplementedError("receive0")
java.net.TwoStacksPlainDatagramSocketImpl.receive0 = receive0

def setTimeToLive(a0):
    raise NotImplementedError("setTimeToLive")
java.net.TwoStacksPlainDatagramSocketImpl.setTimeToLive = setTimeToLive

def getTimeToLive():
    raise NotImplementedError("getTimeToLive")
java.net.TwoStacksPlainDatagramSocketImpl.getTimeToLive = getTimeToLive

def setTTL(a0):
    raise NotImplementedError("setTTL")
java.net.TwoStacksPlainDatagramSocketImpl.setTTL = setTTL

def getTTL():
    raise NotImplementedError("getTTL")
java.net.TwoStacksPlainDatagramSocketImpl.getTTL = getTTL

def join(a0, a1):
    raise NotImplementedError("join")
java.net.TwoStacksPlainDatagramSocketImpl.join = join

def leave(a0, a1):
    raise NotImplementedError("leave")
java.net.TwoStacksPlainDatagramSocketImpl.leave = leave

def datagramSocketCreate():
    raise NotImplementedError("datagramSocketCreate")
java.net.TwoStacksPlainDatagramSocketImpl.datagramSocketCreate = datagramSocketCreate

def datagramSocketClose():
    raise NotImplementedError("datagramSocketClose")
java.net.TwoStacksPlainDatagramSocketImpl.datagramSocketClose = datagramSocketClose

def socketNativeSetOption(a0, a1):
    raise NotImplementedError("socketNativeSetOption")
java.net.TwoStacksPlainDatagramSocketImpl.socketNativeSetOption = socketNativeSetOption

def socketGetOption(a0):
    raise NotImplementedError("socketGetOption")
java.net.TwoStacksPlainDatagramSocketImpl.socketGetOption = socketGetOption

def connect0(a0, a1):
    raise NotImplementedError("connect0")
java.net.TwoStacksPlainDatagramSocketImpl.connect0 = connect0

def socketLocalAddress(a0):
    raise NotImplementedError("socketLocalAddress")
java.net.TwoStacksPlainDatagramSocketImpl.socketLocalAddress = socketLocalAddress

def disconnect0(a0):
    raise NotImplementedError("disconnect0")
java.net.TwoStacksPlainDatagramSocketImpl.disconnect0 = disconnect0

def dataAvailable():
    raise NotImplementedError("dataAvailable")
java.net.TwoStacksPlainDatagramSocketImpl.dataAvailable = dataAvailable

def init():
    raise NotImplementedError("init")
java.net.TwoStacksPlainDatagramSocketImpl.init = staticmethod(init)

def initIDs():
    raise NotImplementedError("initIDs")
java.net.DualStackPlainDatagramSocketImpl.initIDs = staticmethod(initIDs)

def socketCreate(a0):
    raise NotImplementedError("socketCreate")
java.net.DualStackPlainDatagramSocketImpl.socketCreate = staticmethod(socketCreate)

def socketBind(a0, a1, a2, a3):
    raise NotImplementedError("socketBind")
java.net.DualStackPlainDatagramSocketImpl.socketBind = staticmethod(socketBind)

def socketConnect(a0, a1, a2):
    raise NotImplementedError("socketConnect")
java.net.DualStackPlainDatagramSocketImpl.socketConnect = staticmethod(socketConnect)

def socketDisconnect(a0):
    raise NotImplementedError("socketDisconnect")
java.net.DualStackPlainDatagramSocketImpl.socketDisconnect = staticmethod(socketDisconnect)

def socketClose(a0):
    raise NotImplementedError("socketClose")
java.net.DualStackPlainDatagramSocketImpl.socketClose = staticmethod(socketClose)

def socketLocalPort(a0):
    raise NotImplementedError("socketLocalPort")
java.net.DualStackPlainDatagramSocketImpl.socketLocalPort = staticmethod(socketLocalPort)

def socketLocalAddress(a0):
    raise NotImplementedError("socketLocalAddress")
java.net.DualStackPlainDatagramSocketImpl.socketLocalAddress = staticmethod(socketLocalAddress)

def socketReceiveOrPeekData(a0, a1, a2, a3, a4):
    raise NotImplementedError("socketReceiveOrPeekData")
java.net.DualStackPlainDatagramSocketImpl.socketReceiveOrPeekData = staticmethod(socketReceiveOrPeekData)

def socketSend(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("socketSend")
java.net.DualStackPlainDatagramSocketImpl.socketSend = staticmethod(socketSend)

def socketSetIntOption(a0, a1, a2):
    raise NotImplementedError("socketSetIntOption")
java.net.DualStackPlainDatagramSocketImpl.socketSetIntOption = staticmethod(socketSetIntOption)

def socketGetIntOption(a0, a1):
    raise NotImplementedError("socketGetIntOption")
java.net.DualStackPlainDatagramSocketImpl.socketGetIntOption = staticmethod(socketGetIntOption)

def dataAvailable():
    raise NotImplementedError("dataAvailable")
java.net.DualStackPlainDatagramSocketImpl.dataAvailable = dataAvailable

def getLocalHostName():
    raise NotImplementedError("getLocalHostName")
java.net.Inet4AddressImpl.getLocalHostName = getLocalHostName

def lookupAllHostAddr(a0):
    raise NotImplementedError("lookupAllHostAddr")
java.net.Inet4AddressImpl.lookupAllHostAddr = lookupAllHostAddr

def getHostByAddr(a0):
    raise NotImplementedError("getHostByAddr")
java.net.Inet4AddressImpl.getHostByAddr = getHostByAddr

def isReachable0(a0, a1, a2, a3):
    raise NotImplementedError("isReachable0")
java.net.Inet4AddressImpl.isReachable0 = isReachable0

def init():
    raise NotImplementedError("init")
java.net.DatagramPacket.init = staticmethod(init)

def createNativeContext():
    raise NotImplementedError("createNativeContext")
sun.awt.windows.WInputMethod.createNativeContext = createNativeContext

def destroyNativeContext(a0):
    raise NotImplementedError("destroyNativeContext")
sun.awt.windows.WInputMethod.destroyNativeContext = destroyNativeContext

def enableNativeIME(a0, a1, a2):
    raise NotImplementedError("enableNativeIME")
sun.awt.windows.WInputMethod.enableNativeIME = enableNativeIME

def disableNativeIME(a0):
    raise NotImplementedError("disableNativeIME")
sun.awt.windows.WInputMethod.disableNativeIME = disableNativeIME

def handleNativeIMEEvent(a0, a1):
    raise NotImplementedError("handleNativeIMEEvent")
sun.awt.windows.WInputMethod.handleNativeIMEEvent = handleNativeIMEEvent

def endCompositionNative(a0, a1):
    raise NotImplementedError("endCompositionNative")
sun.awt.windows.WInputMethod.endCompositionNative = endCompositionNative

def setConversionStatus(a0, a1):
    raise NotImplementedError("setConversionStatus")
sun.awt.windows.WInputMethod.setConversionStatus = setConversionStatus

def getConversionStatus(a0):
    raise NotImplementedError("getConversionStatus")
sun.awt.windows.WInputMethod.getConversionStatus = getConversionStatus

def setOpenStatus(a0, a1):
    raise NotImplementedError("setOpenStatus")
sun.awt.windows.WInputMethod.setOpenStatus = setOpenStatus

def getOpenStatus(a0):
    raise NotImplementedError("getOpenStatus")
sun.awt.windows.WInputMethod.getOpenStatus = getOpenStatus

def setStatusWindowVisible(a0, a1):
    raise NotImplementedError("setStatusWindowVisible")
sun.awt.windows.WInputMethod.setStatusWindowVisible = setStatusWindowVisible

def getNativeIMMDescription():
    raise NotImplementedError("getNativeIMMDescription")
sun.awt.windows.WInputMethod.getNativeIMMDescription = getNativeIMMDescription

def getNativeLocale():
    raise NotImplementedError("getNativeLocale")
sun.awt.windows.WInputMethod.getNativeLocale = staticmethod(getNativeLocale)

def setNativeLocale(a0, a1):
    raise NotImplementedError("setNativeLocale")
sun.awt.windows.WInputMethod.setNativeLocale = staticmethod(setNativeLocale)

def openCandidateWindow(a0, a1, a2):
    raise NotImplementedError("openCandidateWindow")
sun.awt.windows.WInputMethod.openCandidateWindow = openCandidateWindow

def VMSupportsCS8():
    raise NotImplementedError("VMSupportsCS8")
java.util.concurrent.atomic.AtomicLong.VMSupportsCS8 = staticmethod(VMSupportsCS8)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.image.BytePackedRaster.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.image.ByteComponentRaster.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.image.ComponentSampleModel.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.image.GifImageDecoder.initIDs = staticmethod(initIDs)

def parseImage(a0, a1, a2, a3, a4, a5, a6, a7, a8):
    raise NotImplementedError("parseImage")
sun.awt.image.GifImageDecoder.parseImage = parseImage

def update(a0, a1):
    raise NotImplementedError("update")
java.util.zip.CRC32.update = staticmethod(update)

def updateBytes(a0, a1, a2, a3):
    raise NotImplementedError("updateBytes")
java.util.zip.CRC32.updateBytes = staticmethod(updateBytes)

def updateByteBuffer(a0, a1, a2, a3):
    raise NotImplementedError("updateByteBuffer")
java.util.zip.CRC32.updateByteBuffer = staticmethod(updateByteBuffer)

def getSystemTimeZoneID(a0):
    raise NotImplementedError("getSystemTimeZoneID")
java.util.TimeZone.getSystemTimeZoneID = staticmethod(getSystemTimeZoneID)

def getSystemGMTOffsetID():
    raise NotImplementedError("getSystemGMTOffsetID")
java.util.TimeZone.getSystemGMTOffsetID = staticmethod(getSystemGMTOffsetID)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.image.ImageRepresentation.initIDs = staticmethod(initIDs)

def setICMpixels(a0, a1, a2, a3, a4, a5, a6, a7, a8):
    raise NotImplementedError("setICMpixels")
sun.awt.image.ImageRepresentation.setICMpixels = setICMpixels

def setDiffICM(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12):
    raise NotImplementedError("setDiffICM")
sun.awt.image.ImageRepresentation.setDiffICM = setDiffICM

def init():
    raise NotImplementedError("init")
java.net.Inet6Address.init = staticmethod(init)

def init():
    raise NotImplementedError("init")
sun.net.spi.DefaultProxySelector.init = staticmethod(init)

def getSystemProxy(a0, a1):
    raise NotImplementedError("getSystemProxy")
sun.net.spi.DefaultProxySelector.getSystemProxy = getSystemProxy

def init():
    raise NotImplementedError("init")
java.net.Inet4Address.init = staticmethod(init)

def getLocalHostName():
    raise NotImplementedError("getLocalHostName")
java.net.Inet6AddressImpl.getLocalHostName = getLocalHostName

def lookupAllHostAddr(a0):
    raise NotImplementedError("lookupAllHostAddr")
java.net.Inet6AddressImpl.lookupAllHostAddr = lookupAllHostAddr

def getHostByAddr(a0):
    raise NotImplementedError("getHostByAddr")
java.net.Inet6AddressImpl.getHostByAddr = getHostByAddr

def isReachable0(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("isReachable0")
java.net.Inet6AddressImpl.isReachable0 = isReachable0

def isIPv6Supported():
    raise NotImplementedError("isIPv6Supported")
java.net.InetAddressImplFactory.isIPv6Supported = staticmethod(isIPv6Supported)

def initIDs():
    raise NotImplementedError("initIDs")
java.net.DualStackPlainSocketImpl.initIDs = staticmethod(initIDs)

def socket0(a0, a1):
    raise NotImplementedError("socket0")
java.net.DualStackPlainSocketImpl.socket0 = staticmethod(socket0)

def bind0(a0, a1, a2, a3):
    raise NotImplementedError("bind0")
java.net.DualStackPlainSocketImpl.bind0 = staticmethod(bind0)

def connect0(a0, a1, a2):
    raise NotImplementedError("connect0")
java.net.DualStackPlainSocketImpl.connect0 = staticmethod(connect0)

def waitForConnect(a0, a1):
    raise NotImplementedError("waitForConnect")
java.net.DualStackPlainSocketImpl.waitForConnect = staticmethod(waitForConnect)

def localPort0(a0):
    raise NotImplementedError("localPort0")
java.net.DualStackPlainSocketImpl.localPort0 = staticmethod(localPort0)

def localAddress(a0, a1):
    raise NotImplementedError("localAddress")
java.net.DualStackPlainSocketImpl.localAddress = staticmethod(localAddress)

def listen0(a0, a1):
    raise NotImplementedError("listen0")
java.net.DualStackPlainSocketImpl.listen0 = staticmethod(listen0)

def accept0(a0, a1):
    raise NotImplementedError("accept0")
java.net.DualStackPlainSocketImpl.accept0 = staticmethod(accept0)

def waitForNewConnection(a0, a1):
    raise NotImplementedError("waitForNewConnection")
java.net.DualStackPlainSocketImpl.waitForNewConnection = staticmethod(waitForNewConnection)

def available0(a0):
    raise NotImplementedError("available0")
java.net.DualStackPlainSocketImpl.available0 = staticmethod(available0)

def close0(a0):
    raise NotImplementedError("close0")
java.net.DualStackPlainSocketImpl.close0 = staticmethod(close0)

def shutdown0(a0, a1):
    raise NotImplementedError("shutdown0")
java.net.DualStackPlainSocketImpl.shutdown0 = staticmethod(shutdown0)

def setIntOption(a0, a1, a2):
    raise NotImplementedError("setIntOption")
java.net.DualStackPlainSocketImpl.setIntOption = staticmethod(setIntOption)

def getIntOption(a0, a1):
    raise NotImplementedError("getIntOption")
java.net.DualStackPlainSocketImpl.getIntOption = staticmethod(getIntOption)

def sendOOB(a0, a1):
    raise NotImplementedError("sendOOB")
java.net.DualStackPlainSocketImpl.sendOOB = staticmethod(sendOOB)

def configureBlocking(a0, a1):
    raise NotImplementedError("configureBlocking")
java.net.DualStackPlainSocketImpl.configureBlocking = staticmethod(configureBlocking)

def init():
    raise NotImplementedError("init")
java.net.InetAddress.init = staticmethod(init)

def getSystemPackage0(a0):
    raise NotImplementedError("getSystemPackage0")
java.lang.Package.getSystemPackage0 = staticmethod(getSystemPackage0)

def getSystemPackages0():
    raise NotImplementedError("getSystemPackages0")
java.lang.Package.getSystemPackages0 = staticmethod(getSystemPackages0)

def initIDs(a0):
    raise NotImplementedError("initIDs")
sun.font.T2KFontScaler.initIDs = staticmethod(initIDs)

def initNativeScaler(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("initNativeScaler")
sun.font.T2KFontScaler.initNativeScaler = initNativeScaler

def getFontMetricsNative(a0, a1, a2):
    raise NotImplementedError("getFontMetricsNative")
sun.font.T2KFontScaler.getFontMetricsNative = getFontMetricsNative

def getGlyphAdvanceNative(a0, a1, a2, a3):
    raise NotImplementedError("getGlyphAdvanceNative")
sun.font.T2KFontScaler.getGlyphAdvanceNative = getGlyphAdvanceNative

def getGlyphMetricsNative(a0, a1, a2, a3, a4):
    raise NotImplementedError("getGlyphMetricsNative")
sun.font.T2KFontScaler.getGlyphMetricsNative = getGlyphMetricsNative

def getGlyphImageNative(a0, a1, a2, a3):
    raise NotImplementedError("getGlyphImageNative")
sun.font.T2KFontScaler.getGlyphImageNative = getGlyphImageNative

def getGlyphOutlineBoundsNative(a0, a1, a2, a3):
    raise NotImplementedError("getGlyphOutlineBoundsNative")
sun.font.T2KFontScaler.getGlyphOutlineBoundsNative = getGlyphOutlineBoundsNative

def getGlyphOutlineNative(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("getGlyphOutlineNative")
sun.font.T2KFontScaler.getGlyphOutlineNative = getGlyphOutlineNative

def getGlyphVectorOutlineNative(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("getGlyphVectorOutlineNative")
sun.font.T2KFontScaler.getGlyphVectorOutlineNative = getGlyphVectorOutlineNative

def getGlyphCodeNative(a0, a1):
    raise NotImplementedError("getGlyphCodeNative")
sun.font.T2KFontScaler.getGlyphCodeNative = getGlyphCodeNative

def getLayoutTableCacheNative(a0):
    raise NotImplementedError("getLayoutTableCacheNative")
sun.font.T2KFontScaler.getLayoutTableCacheNative = getLayoutTableCacheNative

def disposeNativeScaler(a0, a1):
    raise NotImplementedError("disposeNativeScaler")
sun.font.T2KFontScaler.disposeNativeScaler = disposeNativeScaler

def getNumGlyphsNative(a0):
    raise NotImplementedError("getNumGlyphsNative")
sun.font.T2KFontScaler.getNumGlyphsNative = getNumGlyphsNative

def getMissingGlyphCodeNative(a0):
    raise NotImplementedError("getMissingGlyphCodeNative")
sun.font.T2KFontScaler.getMissingGlyphCodeNative = getMissingGlyphCodeNative

def getUnitsPerEMNative(a0):
    raise NotImplementedError("getUnitsPerEMNative")
sun.font.T2KFontScaler.getUnitsPerEMNative = getUnitsPerEMNative

def createScalerContextNative(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("createScalerContextNative")
sun.font.T2KFontScaler.createScalerContextNative = createScalerContextNative

def getGlyphPointNative(a0, a1, a2, a3, a4):
    raise NotImplementedError("getGlyphPointNative")
sun.font.T2KFontScaler.getGlyphPointNative = getGlyphPointNative

def initNative():
    raise NotImplementedError("initNative")
sun.font.FileFontStrike.initNative = staticmethod(initNative)

def _getGlyphImageFromWindows(a0, a1, a2, a3, a4):
    raise NotImplementedError("_getGlyphImageFromWindows")
sun.font.FileFontStrike._getGlyphImageFromWindows = _getGlyphImageFromWindows

def read0(a0, a1, a2):
    raise NotImplementedError("read0")
sun.nio.ch.FileDispatcherImpl.read0 = staticmethod(read0)

def pread0(a0, a1, a2, a3):
    raise NotImplementedError("pread0")
sun.nio.ch.FileDispatcherImpl.pread0 = staticmethod(pread0)

def readv0(a0, a1, a2):
    raise NotImplementedError("readv0")
sun.nio.ch.FileDispatcherImpl.readv0 = staticmethod(readv0)

def write0(a0, a1, a2, a3):
    raise NotImplementedError("write0")
sun.nio.ch.FileDispatcherImpl.write0 = staticmethod(write0)

def pwrite0(a0, a1, a2, a3):
    raise NotImplementedError("pwrite0")
sun.nio.ch.FileDispatcherImpl.pwrite0 = staticmethod(pwrite0)

def writev0(a0, a1, a2, a3):
    raise NotImplementedError("writev0")
sun.nio.ch.FileDispatcherImpl.writev0 = staticmethod(writev0)

def force0(a0, a1):
    raise NotImplementedError("force0")
sun.nio.ch.FileDispatcherImpl.force0 = staticmethod(force0)

def truncate0(a0, a1):
    raise NotImplementedError("truncate0")
sun.nio.ch.FileDispatcherImpl.truncate0 = staticmethod(truncate0)

def size0(a0):
    raise NotImplementedError("size0")
sun.nio.ch.FileDispatcherImpl.size0 = staticmethod(size0)

def lock0(a0, a1, a2, a3, a4):
    raise NotImplementedError("lock0")
sun.nio.ch.FileDispatcherImpl.lock0 = staticmethod(lock0)

def release0(a0, a1, a2):
    raise NotImplementedError("release0")
sun.nio.ch.FileDispatcherImpl.release0 = staticmethod(release0)

def close0(a0):
    raise NotImplementedError("close0")
sun.nio.ch.FileDispatcherImpl.close0 = staticmethod(close0)

def closeByHandle(a0):
    raise NotImplementedError("closeByHandle")
sun.nio.ch.FileDispatcherImpl.closeByHandle = staticmethod(closeByHandle)

def duplicateHandle(a0):
    raise NotImplementedError("duplicateHandle")
sun.nio.ch.FileDispatcherImpl.duplicateHandle = staticmethod(duplicateHandle)

def randomBytes(a0):
    raise NotImplementedError("randomBytes")
sun.nio.ch.IOUtil.randomBytes = staticmethod(randomBytes)

def makePipe(a0):
    raise NotImplementedError("makePipe")
sun.nio.ch.IOUtil.makePipe = staticmethod(makePipe)

def drain(a0):
    raise NotImplementedError("drain")
sun.nio.ch.IOUtil.drain = staticmethod(drain)

def configureBlocking(a0, a1):
    raise NotImplementedError("configureBlocking")
sun.nio.ch.IOUtil.configureBlocking = staticmethod(configureBlocking)

def fdVal(a0):
    raise NotImplementedError("fdVal")
sun.nio.ch.IOUtil.fdVal = staticmethod(fdVal)

def setfdVal(a0, a1):
    raise NotImplementedError("setfdVal")
sun.nio.ch.IOUtil.setfdVal = staticmethod(setfdVal)

def fdLimit():
    raise NotImplementedError("fdLimit")
sun.nio.ch.IOUtil.fdLimit = staticmethod(fdLimit)

def iovMax():
    raise NotImplementedError("iovMax")
sun.nio.ch.IOUtil.iovMax = staticmethod(iovMax)

def initIDs():
    raise NotImplementedError("initIDs")
sun.nio.ch.IOUtil.initIDs = staticmethod(initIDs)

def map0(a0, a1, a2):
    raise NotImplementedError("map0")
sun.nio.ch.FileChannelImpl.map0 = map0

def unmap0(a0, a1):
    raise NotImplementedError("unmap0")
sun.nio.ch.FileChannelImpl.unmap0 = staticmethod(unmap0)

def transferTo0(a0, a1, a2, a3):
    raise NotImplementedError("transferTo0")
sun.nio.ch.FileChannelImpl.transferTo0 = transferTo0

def position0(a0, a1):
    raise NotImplementedError("position0")
sun.nio.ch.FileChannelImpl.position0 = position0

def initIDs():
    raise NotImplementedError("initIDs")
sun.nio.ch.FileChannelImpl.initIDs = staticmethod(initIDs)

def open0(a0, a1):
    raise NotImplementedError("open0")
java.io.RandomAccessFile.open0 = open0

def read0():
    raise NotImplementedError("read0")
java.io.RandomAccessFile.read0 = read0

def readBytes(a0, a1, a2):
    raise NotImplementedError("readBytes")
java.io.RandomAccessFile.readBytes = readBytes

def write0(a0):
    raise NotImplementedError("write0")
java.io.RandomAccessFile.write0 = write0

def writeBytes(a0, a1, a2):
    raise NotImplementedError("writeBytes")
java.io.RandomAccessFile.writeBytes = writeBytes

def getFilePointer():
    raise NotImplementedError("getFilePointer")
java.io.RandomAccessFile.getFilePointer = getFilePointer

def seek0(a0):
    raise NotImplementedError("seek0")
java.io.RandomAccessFile.seek0 = seek0

def length():
    raise NotImplementedError("length")
java.io.RandomAccessFile.length = length

def setLength(a0):
    raise NotImplementedError("setLength")
java.io.RandomAccessFile.setLength = setLength

def initIDs():
    raise NotImplementedError("initIDs")
java.io.RandomAccessFile.initIDs = staticmethod(initIDs)

def close0():
    raise NotImplementedError("close0")
java.io.RandomAccessFile.close0 = close0

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.FontMetrics.initIDs = staticmethod(initIDs)

def initIDs(a0, a1):
    raise NotImplementedError("initIDs")
sun.awt.image.BufImgSurfaceData.initIDs = staticmethod(initIDs)

def initRaster(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("initRaster")
sun.awt.image.BufImgSurfaceData.initRaster = initRaster

def freeNativeICMData(a0):
    raise NotImplementedError("freeNativeICMData")
sun.awt.image.BufImgSurfaceData.freeNativeICMData = staticmethod(freeNativeICMData)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.image.BufferedImage.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.image.IntegerComponentRaster.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.image.SampleModel.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.image.SinglePixelPackedSampleModel.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.image.Raster.initIDs = staticmethod(initIDs)

def getDefaultPixFmt(a0):
    raise NotImplementedError("getDefaultPixFmt")
sun.java2d.opengl.WGLGraphicsConfig.getDefaultPixFmt = staticmethod(getDefaultPixFmt)

def initWGL():
    raise NotImplementedError("initWGL")
sun.java2d.opengl.WGLGraphicsConfig.initWGL = staticmethod(initWGL)

def getWGLConfigInfo(a0, a1):
    raise NotImplementedError("getWGLConfigInfo")
sun.java2d.opengl.WGLGraphicsConfig.getWGLConfigInfo = staticmethod(getWGLConfigInfo)

def getOGLCapabilities(a0):
    raise NotImplementedError("getOGLCapabilities")
sun.java2d.opengl.WGLGraphicsConfig.getOGLCapabilities = staticmethod(getOGLCapabilities)

def initTexture(a0, a1, a2):
    raise NotImplementedError("initTexture")
sun.java2d.d3d.D3DSurfaceData.initTexture = initTexture

def initFlipBackbuffer(a0, a1, a2, a3, a4):
    raise NotImplementedError("initFlipBackbuffer")
sun.java2d.d3d.D3DSurfaceData.initFlipBackbuffer = initFlipBackbuffer

def initRTSurface(a0, a1):
    raise NotImplementedError("initRTSurface")
sun.java2d.d3d.D3DSurfaceData.initRTSurface = initRTSurface

def initOps(a0, a1, a2):
    raise NotImplementedError("initOps")
sun.java2d.d3d.D3DSurfaceData.initOps = initOps

def dbGetPixelNative(a0, a1, a2):
    raise NotImplementedError("dbGetPixelNative")
sun.java2d.d3d.D3DSurfaceData.dbGetPixelNative = staticmethod(dbGetPixelNative)

def dbSetPixelNative(a0, a1, a2, a3):
    raise NotImplementedError("dbSetPixelNative")
sun.java2d.d3d.D3DSurfaceData.dbSetPixelNative = staticmethod(dbSetPixelNative)

def getNativeResourceNative(a0, a1):
    raise NotImplementedError("getNativeResourceNative")
sun.java2d.d3d.D3DSurfaceData.getNativeResourceNative = staticmethod(getNativeResourceNative)

def updateWindowAccelImpl(a0, a1, a2, a3):
    raise NotImplementedError("updateWindowAccelImpl")
sun.java2d.d3d.D3DSurfaceData.updateWindowAccelImpl = staticmethod(updateWindowAccelImpl)

def setCursor(a0, a1, a2):
    raise NotImplementedError("setCursor")
sun.awt.windows.WGlobalCursorManager.setCursor = setCursor

def getCursorPos(a0):
    raise NotImplementedError("getCursorPos")
sun.awt.windows.WGlobalCursorManager.getCursorPos = getCursorPos

def findHeavyweightUnderCursor(a0):
    raise NotImplementedError("findHeavyweightUnderCursor")
sun.awt.windows.WGlobalCursorManager.findHeavyweightUnderCursor = findHeavyweightUnderCursor

def getLocationOnScreen(a0):
    raise NotImplementedError("getLocationOnScreen")
sun.awt.windows.WGlobalCursorManager.getLocationOnScreen = getLocationOnScreen

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Dialog.initIDs = staticmethod(initIDs)

def _update(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("_update")
java.awt.SplashScreen._update = staticmethod(_update)

def _isVisible(a0):
    raise NotImplementedError("_isVisible")
java.awt.SplashScreen._isVisible = staticmethod(_isVisible)

def _getBounds(a0):
    raise NotImplementedError("_getBounds")
java.awt.SplashScreen._getBounds = staticmethod(_getBounds)

def _getInstance():
    raise NotImplementedError("_getInstance")
java.awt.SplashScreen._getInstance = staticmethod(_getInstance)

def _close(a0):
    raise NotImplementedError("_close")
java.awt.SplashScreen._close = staticmethod(_close)

def _getImageFileName(a0):
    raise NotImplementedError("_getImageFileName")
java.awt.SplashScreen._getImageFileName = staticmethod(_getImageFileName)

def _getImageJarName(a0):
    raise NotImplementedError("_getImageJarName")
java.awt.SplashScreen._getImageJarName = staticmethod(_getImageJarName)

def _setImageData(a0, a1):
    raise NotImplementedError("_setImageData")
java.awt.SplashScreen._setImageData = staticmethod(_setImageData)

def _getScaleFactor(a0):
    raise NotImplementedError("_getScaleFactor")
java.awt.SplashScreen._getScaleFactor = staticmethod(_getScaleFactor)

def getNativeAvailableLocales():
    raise NotImplementedError("getNativeAvailableLocales")
sun.awt.windows.WInputMethodDescriptor.getNativeAvailableLocales = staticmethod(getNativeAvailableLocales)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.FontDescriptor.initIDs = staticmethod(initIDs)

def getEUDCFontFile():
    raise NotImplementedError("getEUDCFontFile")
sun.awt.Win32FontManager.getEUDCFontFile = staticmethod(getEUDCFontFile)

def populateFontFileNameMap0(a0, a1, a2, a3):
    raise NotImplementedError("populateFontFileNameMap0")
sun.awt.Win32FontManager.populateFontFileNameMap0 = staticmethod(populateFontFileNameMap0)

def getFontPath(a0):
    raise NotImplementedError("getFontPath")
sun.awt.Win32FontManager.getFontPath = getFontPath

def registerFontWithPlatform(a0):
    raise NotImplementedError("registerFontWithPlatform")
sun.awt.Win32FontManager.registerFontWithPlatform = staticmethod(registerFontWithPlatform)

def deRegisterFontWithPlatform(a0):
    raise NotImplementedError("deRegisterFontWithPlatform")
sun.awt.Win32FontManager.deRegisterFontWithPlatform = staticmethod(deRegisterFontWithPlatform)

def getGlyphCacheDescription(a0):
    raise NotImplementedError("getGlyphCacheDescription")
sun.font.StrikeCache.getGlyphCacheDescription = staticmethod(getGlyphCacheDescription)

def freeIntPointer(a0):
    raise NotImplementedError("freeIntPointer")
sun.font.StrikeCache.freeIntPointer = staticmethod(freeIntPointer)

def freeLongPointer(a0):
    raise NotImplementedError("freeLongPointer")
sun.font.StrikeCache.freeLongPointer = staticmethod(freeLongPointer)

def freeIntMemory(a0, a1):
    raise NotImplementedError("freeIntMemory")
sun.font.StrikeCache.freeIntMemory = staticmethod(freeIntMemory)

def freeLongMemory(a0, a1):
    raise NotImplementedError("freeLongMemory")
sun.font.StrikeCache.freeLongMemory = staticmethod(freeLongMemory)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.PlatformFont.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WFontPeer.initIDs = staticmethod(initIDs)

def getDefaultColor(a0):
    raise NotImplementedError("getDefaultColor")
sun.awt.windows.WColor.getDefaultColor = staticmethod(getDefaultColor)

def invokeNativeDispose(a0, a1):
    raise NotImplementedError("invokeNativeDispose")
sun.java2d.DefaultDisposerRecord.invokeNativeDispose = staticmethod(invokeNativeDispose)

def doDrawLine(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("doDrawLine")
sun.java2d.windows.GDIRenderer.doDrawLine = doDrawLine

def doDrawRect(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("doDrawRect")
sun.java2d.windows.GDIRenderer.doDrawRect = doDrawRect

def doDrawRoundRect(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    raise NotImplementedError("doDrawRoundRect")
sun.java2d.windows.GDIRenderer.doDrawRoundRect = doDrawRoundRect

def doDrawOval(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("doDrawOval")
sun.java2d.windows.GDIRenderer.doDrawOval = doDrawOval

def doDrawArc(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    raise NotImplementedError("doDrawArc")
sun.java2d.windows.GDIRenderer.doDrawArc = doDrawArc

def doDrawPoly(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    raise NotImplementedError("doDrawPoly")
sun.java2d.windows.GDIRenderer.doDrawPoly = doDrawPoly

def doFillRect(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("doFillRect")
sun.java2d.windows.GDIRenderer.doFillRect = doFillRect

def doFillRoundRect(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    raise NotImplementedError("doFillRoundRect")
sun.java2d.windows.GDIRenderer.doFillRoundRect = doFillRoundRect

def doFillOval(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("doFillOval")
sun.java2d.windows.GDIRenderer.doFillOval = doFillOval

def doFillArc(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    raise NotImplementedError("doFillArc")
sun.java2d.windows.GDIRenderer.doFillArc = doFillArc

def doFillPoly(a0, a1, a2, a3, a4, a5, a6, a7, a8):
    raise NotImplementedError("doFillPoly")
sun.java2d.windows.GDIRenderer.doFillPoly = doFillPoly

def doShape(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("doShape")
sun.java2d.windows.GDIRenderer.doShape = doShape

def devCopyArea(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("devCopyArea")
sun.java2d.windows.GDIRenderer.devCopyArea = devCopyArea

def Transform(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17):
    raise NotImplementedError("Transform")
sun.java2d.loops.TransformHelper.Transform = Transform

def DrawGlyphListLCD(a0, a1, a2):
    raise NotImplementedError("DrawGlyphListLCD")
sun.java2d.loops.DrawGlyphListLCD.DrawGlyphListLCD = DrawGlyphListLCD

def DrawGlyphListAA(a0, a1, a2):
    raise NotImplementedError("DrawGlyphListAA")
sun.java2d.loops.DrawGlyphListAA.DrawGlyphListAA = DrawGlyphListAA

def DrawGlyphList(a0, a1, a2):
    raise NotImplementedError("DrawGlyphList")
sun.java2d.loops.DrawGlyphList.DrawGlyphList = DrawGlyphList

def MaskFill(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    raise NotImplementedError("MaskFill")
sun.java2d.loops.MaskFill.MaskFill = MaskFill

def FillAAPgram(a0, a1, a2, a3, a4, a5, a6, a7, a8):
    raise NotImplementedError("FillAAPgram")
sun.java2d.loops.MaskFill.FillAAPgram = FillAAPgram

def DrawAAPgram(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    raise NotImplementedError("DrawAAPgram")
sun.java2d.loops.MaskFill.DrawAAPgram = DrawAAPgram

def MaskBlit(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12):
    raise NotImplementedError("MaskBlit")
sun.java2d.loops.MaskBlit.MaskBlit = MaskBlit

def FillPath(a0, a1, a2, a3, a4):
    raise NotImplementedError("FillPath")
sun.java2d.loops.FillPath.FillPath = FillPath

def DrawPath(a0, a1, a2, a3, a4):
    raise NotImplementedError("DrawPath")
sun.java2d.loops.DrawPath.DrawPath = DrawPath

def DrawPolygons(a0, a1, a2, a3, a4, a5, a6, a7, a8):
    raise NotImplementedError("DrawPolygons")
sun.java2d.loops.DrawPolygons.DrawPolygons = DrawPolygons

def DrawRect(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("DrawRect")
sun.java2d.loops.DrawRect.DrawRect = DrawRect

def DrawLine(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("DrawLine")
sun.java2d.loops.DrawLine.DrawLine = DrawLine

def DrawParallelogram(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    raise NotImplementedError("DrawParallelogram")
sun.java2d.loops.DrawParallelogram.DrawParallelogram = DrawParallelogram

def FillParallelogram(a0, a1, a2, a3, a4, a5, a6, a7):
    raise NotImplementedError("FillParallelogram")
sun.java2d.loops.FillParallelogram.FillParallelogram = FillParallelogram

def FillSpans(a0, a1, a2, a3, a4):
    raise NotImplementedError("FillSpans")
sun.java2d.loops.FillSpans.FillSpans = FillSpans

def FillRect(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("FillRect")
sun.java2d.loops.FillRect.FillRect = FillRect

def Scale(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):
    raise NotImplementedError("Scale")
sun.java2d.loops.ScaledBlit.Scale = Scale

def BlitBg(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    raise NotImplementedError("BlitBg")
sun.java2d.loops.BlitBg.BlitBg = BlitBg

def initIDs(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    raise NotImplementedError("initIDs")
sun.java2d.loops.GraphicsPrimitiveMgr.initIDs = staticmethod(initIDs)

def registerNativeLoops():
    raise NotImplementedError("registerNativeLoops")
sun.java2d.loops.GraphicsPrimitiveMgr.registerNativeLoops = staticmethod(registerNativeLoops)

def Blit(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    raise NotImplementedError("Blit")
sun.java2d.loops.Blit.Blit = Blit

def nativeBlit(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12):
    raise NotImplementedError("nativeBlit")
sun.java2d.windows.GDIBlitLoops.nativeBlit = nativeBlit

def initIDs(a0):
    raise NotImplementedError("initIDs")
sun.java2d.windows.GDIWindowSurfaceData.initIDs = staticmethod(initIDs)

def initOps(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("initOps")
sun.java2d.windows.GDIWindowSurfaceData.initOps = initOps

def invalidateSD():
    raise NotImplementedError("invalidateSD")
sun.java2d.windows.GDIWindowSurfaceData.invalidateSD = invalidateSD

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.TrayIcon.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.MenuComponent.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.event.MouseEvent.initIDs = staticmethod(initIDs)

def create(a0):
    raise NotImplementedError("create")
sun.awt.windows.WCanvasPeer.create = create

def setNativeBackgroundErase(a0, a1):
    raise NotImplementedError("setNativeBackgroundErase")
sun.awt.windows.WCanvasPeer.setNativeBackgroundErase = setNativeBackgroundErase

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WPanelPeer.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WWindowPeer.initIDs = staticmethod(initIDs)

def _toFront():
    raise NotImplementedError("_toFront")
sun.awt.windows.WWindowPeer._toFront = _toFront

def toBack():
    raise NotImplementedError("toBack")
sun.awt.windows.WWindowPeer.toBack = toBack

def setAlwaysOnTopNative(a0):
    raise NotImplementedError("setAlwaysOnTopNative")
sun.awt.windows.WWindowPeer.setAlwaysOnTopNative = setAlwaysOnTopNative

def setFocusableWindow(a0):
    raise NotImplementedError("setFocusableWindow")
sun.awt.windows.WWindowPeer.setFocusableWindow = setFocusableWindow

def _setTitle(a0):
    raise NotImplementedError("_setTitle")
sun.awt.windows.WWindowPeer._setTitle = _setTitle

def _setResizable(a0):
    raise NotImplementedError("_setResizable")
sun.awt.windows.WWindowPeer._setResizable = _setResizable

def createAwtWindow(a0):
    raise NotImplementedError("createAwtWindow")
sun.awt.windows.WWindowPeer.createAwtWindow = createAwtWindow

def updateInsets(a0):
    raise NotImplementedError("updateInsets")
sun.awt.windows.WWindowPeer.updateInsets = updateInsets

def getSysMinWidth():
    raise NotImplementedError("getSysMinWidth")
sun.awt.windows.WWindowPeer.getSysMinWidth = staticmethod(getSysMinWidth)

def getSysMinHeight():
    raise NotImplementedError("getSysMinHeight")
sun.awt.windows.WWindowPeer.getSysMinHeight = staticmethod(getSysMinHeight)

def getSysIconWidth():
    raise NotImplementedError("getSysIconWidth")
sun.awt.windows.WWindowPeer.getSysIconWidth = staticmethod(getSysIconWidth)

def getSysIconHeight():
    raise NotImplementedError("getSysIconHeight")
sun.awt.windows.WWindowPeer.getSysIconHeight = staticmethod(getSysIconHeight)

def getSysSmIconWidth():
    raise NotImplementedError("getSysSmIconWidth")
sun.awt.windows.WWindowPeer.getSysSmIconWidth = staticmethod(getSysSmIconWidth)

def getSysSmIconHeight():
    raise NotImplementedError("getSysSmIconHeight")
sun.awt.windows.WWindowPeer.getSysSmIconHeight = staticmethod(getSysSmIconHeight)

def setIconImagesData(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("setIconImagesData")
sun.awt.windows.WWindowPeer.setIconImagesData = setIconImagesData

def reshapeFrame(a0, a1, a2, a3):
    raise NotImplementedError("reshapeFrame")
sun.awt.windows.WWindowPeer.reshapeFrame = reshapeFrame

def requestWindowFocus(a0):
    raise NotImplementedError("requestWindowFocus")
sun.awt.windows.WWindowPeer.requestWindowFocus = requestWindowFocus

def setMinSize(a0, a1):
    raise NotImplementedError("setMinSize")
sun.awt.windows.WWindowPeer.setMinSize = setMinSize

def modalDisable(a0, a1):
    raise NotImplementedError("modalDisable")
sun.awt.windows.WWindowPeer.modalDisable = modalDisable

def modalEnable(a0):
    raise NotImplementedError("modalEnable")
sun.awt.windows.WWindowPeer.modalEnable = modalEnable

def getScreenImOn():
    raise NotImplementedError("getScreenImOn")
sun.awt.windows.WWindowPeer.getScreenImOn = getScreenImOn

def setFullScreenExclusiveModeState(a0):
    raise NotImplementedError("setFullScreenExclusiveModeState")
sun.awt.windows.WWindowPeer.setFullScreenExclusiveModeState = setFullScreenExclusiveModeState

def nativeGrab():
    raise NotImplementedError("nativeGrab")
sun.awt.windows.WWindowPeer.nativeGrab = nativeGrab

def nativeUngrab():
    raise NotImplementedError("nativeUngrab")
sun.awt.windows.WWindowPeer.nativeUngrab = nativeUngrab

def repositionSecurityWarning():
    raise NotImplementedError("repositionSecurityWarning")
sun.awt.windows.WWindowPeer.repositionSecurityWarning = repositionSecurityWarning

def setOpacity(a0):
    raise NotImplementedError("setOpacity")
sun.awt.windows.WWindowPeer.setOpacity = setOpacity

def setOpaqueImpl(a0):
    raise NotImplementedError("setOpaqueImpl")
sun.awt.windows.WWindowPeer.setOpaqueImpl = setOpaqueImpl

def updateWindowImpl(a0, a1, a2):
    raise NotImplementedError("updateWindowImpl")
sun.awt.windows.WWindowPeer.updateWindowImpl = updateWindowImpl

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WFramePeer.initIDs = staticmethod(initIDs)

def setState(a0):
    raise NotImplementedError("setState")
sun.awt.windows.WFramePeer.setState = setState

def getState():
    raise NotImplementedError("getState")
sun.awt.windows.WFramePeer.getState = getState

def setMaximizedBounds(a0, a1, a2, a3):
    raise NotImplementedError("setMaximizedBounds")
sun.awt.windows.WFramePeer.setMaximizedBounds = setMaximizedBounds

def clearMaximizedBounds():
    raise NotImplementedError("clearMaximizedBounds")
sun.awt.windows.WFramePeer.clearMaximizedBounds = clearMaximizedBounds

def setMenuBar0(a0):
    raise NotImplementedError("setMenuBar0")
sun.awt.windows.WFramePeer.setMenuBar0 = setMenuBar0

def createAwtFrame(a0):
    raise NotImplementedError("createAwtFrame")
sun.awt.windows.WFramePeer.createAwtFrame = createAwtFrame

def getSysMenuHeight():
    raise NotImplementedError("getSysMenuHeight")
sun.awt.windows.WFramePeer.getSysMenuHeight = staticmethod(getSysMenuHeight)

def pSetIMMOption(a0):
    raise NotImplementedError("pSetIMMOption")
sun.awt.windows.WFramePeer.pSetIMMOption = pSetIMMOption

def synthesizeWmActivate(a0):
    raise NotImplementedError("synthesizeWmActivate")
sun.awt.windows.WFramePeer.synthesizeWmActivate = synthesizeWmActivate

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.event.KeyEvent.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.Win32GraphicsConfig.initIDs = staticmethod(initIDs)

def getBounds(a0):
    raise NotImplementedError("getBounds")
sun.awt.Win32GraphicsConfig.getBounds = getBounds

def flushBuffer(a0, a1, a2):
    raise NotImplementedError("flushBuffer")
sun.java2d.d3d.D3DRenderQueue.flushBuffer = flushBuffer

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.Win32GraphicsDevice.initIDs = staticmethod(initIDs)

def initDevice(a0):
    raise NotImplementedError("initDevice")
sun.awt.Win32GraphicsDevice.initDevice = initDevice

def getMaxConfigsImpl(a0):
    raise NotImplementedError("getMaxConfigsImpl")
sun.awt.Win32GraphicsDevice.getMaxConfigsImpl = getMaxConfigsImpl

def isPixFmtSupported(a0, a1):
    raise NotImplementedError("isPixFmtSupported")
sun.awt.Win32GraphicsDevice.isPixFmtSupported = isPixFmtSupported

def getDefaultPixIDImpl(a0):
    raise NotImplementedError("getDefaultPixIDImpl")
sun.awt.Win32GraphicsDevice.getDefaultPixIDImpl = getDefaultPixIDImpl

def enterFullScreenExclusive(a0, a1):
    raise NotImplementedError("enterFullScreenExclusive")
sun.awt.Win32GraphicsDevice.enterFullScreenExclusive = enterFullScreenExclusive

def exitFullScreenExclusive(a0, a1):
    raise NotImplementedError("exitFullScreenExclusive")
sun.awt.Win32GraphicsDevice.exitFullScreenExclusive = exitFullScreenExclusive

def getCurrentDisplayMode(a0):
    raise NotImplementedError("getCurrentDisplayMode")
sun.awt.Win32GraphicsDevice.getCurrentDisplayMode = getCurrentDisplayMode

def configDisplayMode(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("configDisplayMode")
sun.awt.Win32GraphicsDevice.configDisplayMode = configDisplayMode

def enumDisplayModes(a0, a1):
    raise NotImplementedError("enumDisplayModes")
sun.awt.Win32GraphicsDevice.enumDisplayModes = enumDisplayModes

def makeColorModel(a0, a1):
    raise NotImplementedError("makeColorModel")
sun.awt.Win32GraphicsDevice.makeColorModel = makeColorModel

def initD3D():
    raise NotImplementedError("initD3D")
sun.java2d.d3d.D3DGraphicsDevice.initD3D = staticmethod(initD3D)

def getDeviceCapsNative(a0):
    raise NotImplementedError("getDeviceCapsNative")
sun.java2d.d3d.D3DGraphicsDevice.getDeviceCapsNative = staticmethod(getDeviceCapsNative)

def getDeviceIdNative(a0):
    raise NotImplementedError("getDeviceIdNative")
sun.java2d.d3d.D3DGraphicsDevice.getDeviceIdNative = staticmethod(getDeviceIdNative)

def enterFullScreenExclusiveNative(a0, a1):
    raise NotImplementedError("enterFullScreenExclusiveNative")
sun.java2d.d3d.D3DGraphicsDevice.enterFullScreenExclusiveNative = staticmethod(enterFullScreenExclusiveNative)

def exitFullScreenExclusiveNative(a0):
    raise NotImplementedError("exitFullScreenExclusiveNative")
sun.java2d.d3d.D3DGraphicsDevice.exitFullScreenExclusiveNative = staticmethod(exitFullScreenExclusiveNative)

def getCurrentDisplayModeNative(a0):
    raise NotImplementedError("getCurrentDisplayModeNative")
sun.java2d.d3d.D3DGraphicsDevice.getCurrentDisplayModeNative = staticmethod(getCurrentDisplayModeNative)

def configDisplayModeNative(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("configDisplayModeNative")
sun.java2d.d3d.D3DGraphicsDevice.configDisplayModeNative = staticmethod(configDisplayModeNative)

def enumDisplayModesNative(a0, a1):
    raise NotImplementedError("enumDisplayModesNative")
sun.java2d.d3d.D3DGraphicsDevice.enumDisplayModesNative = staticmethod(enumDisplayModesNative)

def getAvailableAcceleratedMemoryNative(a0):
    raise NotImplementedError("getAvailableAcceleratedMemoryNative")
sun.java2d.d3d.D3DGraphicsDevice.getAvailableAcceleratedMemoryNative = staticmethod(getAvailableAcceleratedMemoryNative)

def isD3DAvailableOnDeviceNative(a0):
    raise NotImplementedError("isD3DAvailableOnDeviceNative")
sun.java2d.d3d.D3DGraphicsDevice.isD3DAvailableOnDeviceNative = staticmethod(isD3DAvailableOnDeviceNative)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Cursor.initIDs = staticmethod(initIDs)

def finalizeImpl(a0):
    raise NotImplementedError("finalizeImpl")
java.awt.Cursor.finalizeImpl = staticmethod(finalizeImpl)

def setNativeFocusOwner(a0):
    raise NotImplementedError("setNativeFocusOwner")
sun.awt.windows.WKeyboardFocusManagerPeer.setNativeFocusOwner = staticmethod(setNativeFocusOwner)

def getNativeFocusOwner():
    raise NotImplementedError("getNativeFocusOwner")
sun.awt.windows.WKeyboardFocusManagerPeer.getNativeFocusOwner = staticmethod(getNativeFocusOwner)

def getNativeFocusedWindow():
    raise NotImplementedError("getNativeFocusedWindow")
sun.awt.windows.WKeyboardFocusManagerPeer.getNativeFocusedWindow = staticmethod(getNativeFocusedWindow)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.KeyboardFocusManager.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Color.initIDs = staticmethod(initIDs)

def isThemed():
    raise NotImplementedError("isThemed")
sun.awt.windows.ThemeReader.isThemed = staticmethod(isThemed)

def paintBackground(a0, a1, a2, a3, a4, a5, a6, a7, a8):
    raise NotImplementedError("paintBackground")
sun.awt.windows.ThemeReader.paintBackground = staticmethod(paintBackground)

def getThemeMargins(a0, a1, a2, a3):
    raise NotImplementedError("getThemeMargins")
sun.awt.windows.ThemeReader.getThemeMargins = staticmethod(getThemeMargins)

def isThemePartDefined(a0, a1, a2):
    raise NotImplementedError("isThemePartDefined")
sun.awt.windows.ThemeReader.isThemePartDefined = staticmethod(isThemePartDefined)

def getColor(a0, a1, a2, a3):
    raise NotImplementedError("getColor")
sun.awt.windows.ThemeReader.getColor = staticmethod(getColor)

def getInt(a0, a1, a2, a3):
    raise NotImplementedError("getInt")
sun.awt.windows.ThemeReader.getInt = staticmethod(getInt)

def getEnum(a0, a1, a2, a3):
    raise NotImplementedError("getEnum")
sun.awt.windows.ThemeReader.getEnum = staticmethod(getEnum)

def getBoolean(a0, a1, a2, a3):
    raise NotImplementedError("getBoolean")
sun.awt.windows.ThemeReader.getBoolean = staticmethod(getBoolean)

def getSysBoolean(a0, a1):
    raise NotImplementedError("getSysBoolean")
sun.awt.windows.ThemeReader.getSysBoolean = staticmethod(getSysBoolean)

def getPoint(a0, a1, a2, a3):
    raise NotImplementedError("getPoint")
sun.awt.windows.ThemeReader.getPoint = staticmethod(getPoint)

def getPosition(a0, a1, a2, a3):
    raise NotImplementedError("getPosition")
sun.awt.windows.ThemeReader.getPosition = staticmethod(getPosition)

def getPartSize(a0, a1, a2):
    raise NotImplementedError("getPartSize")
sun.awt.windows.ThemeReader.getPartSize = staticmethod(getPartSize)

def openTheme(a0):
    raise NotImplementedError("openTheme")
sun.awt.windows.ThemeReader.openTheme = staticmethod(openTheme)

def closeTheme(a0):
    raise NotImplementedError("closeTheme")
sun.awt.windows.ThemeReader.closeTheme = staticmethod(closeTheme)

def setWindowTheme(a0):
    raise NotImplementedError("setWindowTheme")
sun.awt.windows.ThemeReader.setWindowTheme = staticmethod(setWindowTheme)

def getThemeTransitionDuration(a0, a1, a2, a3, a4):
    raise NotImplementedError("getThemeTransitionDuration")
sun.awt.windows.ThemeReader.getThemeTransitionDuration = staticmethod(getThemeTransitionDuration)

def isGetThemeTransitionDurationDefined():
    raise NotImplementedError("isGetThemeTransitionDurationDefined")
sun.awt.windows.ThemeReader.isGetThemeTransitionDurationDefined = staticmethod(isGetThemeTransitionDurationDefined)

def getThemeBackgroundContentMargins(a0, a1, a2, a3, a4):
    raise NotImplementedError("getThemeBackgroundContentMargins")
sun.awt.windows.ThemeReader.getThemeBackgroundContentMargins = staticmethod(getThemeBackgroundContentMargins)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WDesktopProperties.initIDs = staticmethod(initIDs)

def init():
    raise NotImplementedError("init")
sun.awt.windows.WDesktopProperties.init = init

def getWindowsParameters():
    raise NotImplementedError("getWindowsParameters")
sun.awt.windows.WDesktopProperties.getWindowsParameters = getWindowsParameters

def playWindowsSound(a0):
    raise NotImplementedError("playWindowsSound")
sun.awt.windows.WDesktopProperties.playWindowsSound = playWindowsSound

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Rectangle.initIDs = staticmethod(initIDs)

def halt0(a0):
    raise NotImplementedError("halt0")
java.lang.Shutdown.halt0 = staticmethod(halt0)

def runAllFinalizers():
    raise NotImplementedError("runAllFinalizers")
java.lang.Shutdown.runAllFinalizers = staticmethod(runAllFinalizers)

def initNativeFlags():
    raise NotImplementedError("initNativeFlags")
sun.java2d.windows.WindowsFlags.initNativeFlags = staticmethod(initNativeFlags)

def initIDs():
    raise NotImplementedError("initIDs")
sun.java2d.pipe.Region.initIDs = staticmethod(initIDs)

def initIDs(a0, a1):
    raise NotImplementedError("initIDs")
sun.java2d.pipe.SpanClipRenderer.initIDs = staticmethod(initIDs)

def fillTile(a0, a1, a2, a3, a4):
    raise NotImplementedError("fillTile")
sun.java2d.pipe.SpanClipRenderer.fillTile = fillTile

def eraseTile(a0, a1, a2, a3, a4):
    raise NotImplementedError("eraseTile")
sun.java2d.pipe.SpanClipRenderer.eraseTile = eraseTile

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.image.IndexColorModel.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.image.ColorModel.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
sun.java2d.SurfaceData.initIDs = staticmethod(initIDs)

def isOpaqueGray(a0):
    raise NotImplementedError("isOpaqueGray")
sun.java2d.SurfaceData.isOpaqueGray = staticmethod(isOpaqueGray)

def initDisplay():
    raise NotImplementedError("initDisplay")
sun.awt.Win32GraphicsEnvironment.initDisplay = staticmethod(initDisplay)

def getNumScreens():
    raise NotImplementedError("getNumScreens")
sun.awt.Win32GraphicsEnvironment.getNumScreens = getNumScreens

def getDefaultScreen():
    raise NotImplementedError("getDefaultScreen")
sun.awt.Win32GraphicsEnvironment.getDefaultScreen = getDefaultScreen

def getXResolution():
    raise NotImplementedError("getXResolution")
sun.awt.Win32GraphicsEnvironment.getXResolution = getXResolution

def getYResolution():
    raise NotImplementedError("getYResolution")
sun.awt.Win32GraphicsEnvironment.getYResolution = getYResolution

def isVistaOS():
    raise NotImplementedError("isVistaOS")
sun.awt.Win32GraphicsEnvironment.isVistaOS = staticmethod(isVistaOS)

def closeSplashScreen():
    raise NotImplementedError("closeSplashScreen")
sun.awt.SunToolkit.closeSplashScreen = staticmethod(closeSplashScreen)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Dimension.initIDs = staticmethod(initIDs)

def invoke0(a0, a1, a2):
    raise NotImplementedError("invoke0")
sun.reflect.NativeMethodAccessorImpl.invoke0 = staticmethod(invoke0)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Font.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
sun.awt.windows.WObjectPeer.initIDs = staticmethod(initIDs)

def isObscured():
    raise NotImplementedError("isObscured")
sun.awt.windows.WComponentPeer.isObscured = isObscured

def pShow():
    raise NotImplementedError("pShow")
sun.awt.windows.WComponentPeer.pShow = pShow

def hide():
    raise NotImplementedError("hide")
sun.awt.windows.WComponentPeer.hide = hide

def enable():
    raise NotImplementedError("enable")
sun.awt.windows.WComponentPeer.enable = enable

def disable():
    raise NotImplementedError("disable")
sun.awt.windows.WComponentPeer.disable = disable

def getLocationOnScreen():
    raise NotImplementedError("getLocationOnScreen")
sun.awt.windows.WComponentPeer.getLocationOnScreen = getLocationOnScreen

def reshapeNoCheck(a0, a1, a2, a3):
    raise NotImplementedError("reshapeNoCheck")
sun.awt.windows.WComponentPeer.reshapeNoCheck = reshapeNoCheck

def updateWindow():
    raise NotImplementedError("updateWindow")
sun.awt.windows.WComponentPeer.updateWindow = updateWindow

def createPrintedPixels(a0, a1, a2, a3, a4):
    raise NotImplementedError("createPrintedPixels")
sun.awt.windows.WComponentPeer.createPrintedPixels = createPrintedPixels

def reshape(a0, a1, a2, a3):
    raise NotImplementedError("reshape")
sun.awt.windows.WComponentPeer.reshape = reshape

def nativeHandleEvent(a0):
    raise NotImplementedError("nativeHandleEvent")
sun.awt.windows.WComponentPeer.nativeHandleEvent = nativeHandleEvent

def setFocus(a0):
    raise NotImplementedError("setFocus")
sun.awt.windows.WComponentPeer.setFocus = setFocus

def _dispose():
    raise NotImplementedError("_dispose")
sun.awt.windows.WComponentPeer._dispose = _dispose

def _setForeground(a0):
    raise NotImplementedError("_setForeground")
sun.awt.windows.WComponentPeer._setForeground = _setForeground

def _setBackground(a0):
    raise NotImplementedError("_setBackground")
sun.awt.windows.WComponentPeer._setBackground = _setBackground

def _setFont(a0):
    raise NotImplementedError("_setFont")
sun.awt.windows.WComponentPeer._setFont = _setFont

def start():
    raise NotImplementedError("start")
sun.awt.windows.WComponentPeer.start = start

def beginValidate():
    raise NotImplementedError("beginValidate")
sun.awt.windows.WComponentPeer.beginValidate = beginValidate

def endValidate():
    raise NotImplementedError("endValidate")
sun.awt.windows.WComponentPeer.endValidate = endValidate

def addNativeDropTarget():
    raise NotImplementedError("addNativeDropTarget")
sun.awt.windows.WComponentPeer.addNativeDropTarget = addNativeDropTarget

def removeNativeDropTarget():
    raise NotImplementedError("removeNativeDropTarget")
sun.awt.windows.WComponentPeer.removeNativeDropTarget = removeNativeDropTarget

def nativeHandlesWheelScrolling():
    raise NotImplementedError("nativeHandlesWheelScrolling")
sun.awt.windows.WComponentPeer.nativeHandlesWheelScrolling = nativeHandlesWheelScrolling

def pSetParent(a0):
    raise NotImplementedError("pSetParent")
sun.awt.windows.WComponentPeer.pSetParent = pSetParent

def setRectangularShape(a0, a1, a2, a3, a4):
    raise NotImplementedError("setRectangularShape")
sun.awt.windows.WComponentPeer.setRectangularShape = setRectangularShape

def setZOrder(a0):
    raise NotImplementedError("setZOrder")
sun.awt.windows.WComponentPeer.setZOrder = setZOrder

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.AWTEvent.initIDs = staticmethod(initIDs)

def nativeSetSource(a0):
    raise NotImplementedError("nativeSetSource")
java.awt.AWTEvent.nativeSetSource = nativeSetSource

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.event.InputEvent.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Insets.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Toolkit.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Window.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Frame.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Component.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.awt.Container.initIDs = staticmethod(initIDs)

def initIDs():
    raise NotImplementedError("initIDs")
java.util.zip.Inflater.initIDs = staticmethod(initIDs)

def init(a0):
    raise NotImplementedError("init")
java.util.zip.Inflater.init = staticmethod(init)

def setDictionary(a0, a1, a2, a3):
    raise NotImplementedError("setDictionary")
java.util.zip.Inflater.setDictionary = staticmethod(setDictionary)

def inflateBytes(a0, a1, a2, a3):
    raise NotImplementedError("inflateBytes")
java.util.zip.Inflater.inflateBytes = inflateBytes

def getAdler(a0):
    raise NotImplementedError("getAdler")
java.util.zip.Inflater.getAdler = staticmethod(getAdler)

def reset(a0):
    raise NotImplementedError("reset")
java.util.zip.Inflater.reset = staticmethod(reset)

def end(a0):
    raise NotImplementedError("end")
java.util.zip.Inflater.end = staticmethod(end)

def isLoaded0(a0, a1, a2):
    raise NotImplementedError("isLoaded0")
java.nio.MappedByteBuffer.isLoaded0 = isLoaded0

def load0(a0, a1):
    raise NotImplementedError("load0")
java.nio.MappedByteBuffer.load0 = load0

def force0(a0, a1, a2):
    raise NotImplementedError("force0")
java.nio.MappedByteBuffer.force0 = force0

def attach(a0, a1, a2):
    raise NotImplementedError("attach")
sun.misc.Perf.attach = attach

def detach(a0):
    raise NotImplementedError("detach")
sun.misc.Perf.detach = detach

def createLong(a0, a1, a2, a3):
    raise NotImplementedError("createLong")
sun.misc.Perf.createLong = createLong

def createByteArray(a0, a1, a2, a3, a4):
    raise NotImplementedError("createByteArray")
sun.misc.Perf.createByteArray = createByteArray

def highResCounter():
    raise NotImplementedError("highResCounter")
sun.misc.Perf.highResCounter = highResCounter

def highResFrequency():
    raise NotImplementedError("highResFrequency")
sun.misc.Perf.highResFrequency = highResFrequency

def registerNatives():
    raise NotImplementedError("registerNatives")
sun.misc.Perf.registerNatives = staticmethod(registerNatives)

def getMetaInfEntryNames():
    raise NotImplementedError("getMetaInfEntryNames")
java.util.jar.JarFile.getMetaInfEntryNames = getMetaInfEntryNames

def initIDs():
    raise NotImplementedError("initIDs")
java.util.zip.ZipFile.initIDs = staticmethod(initIDs)

def getEntry(a0, a1, a2):
    raise NotImplementedError("getEntry")
java.util.zip.ZipFile.getEntry = staticmethod(getEntry)

def freeEntry(a0, a1):
    raise NotImplementedError("freeEntry")
java.util.zip.ZipFile.freeEntry = staticmethod(freeEntry)

def getNextEntry(a0, a1):
    raise NotImplementedError("getNextEntry")
java.util.zip.ZipFile.getNextEntry = staticmethod(getNextEntry)

def close(a0):
    raise NotImplementedError("close")
java.util.zip.ZipFile.close = staticmethod(close)

def open(a0, a1, a2, a3):
    raise NotImplementedError("open")
java.util.zip.ZipFile.open = staticmethod(open)

def getTotal(a0):
    raise NotImplementedError("getTotal")
java.util.zip.ZipFile.getTotal = staticmethod(getTotal)

def startsWithLOC(a0):
    raise NotImplementedError("startsWithLOC")
java.util.zip.ZipFile.startsWithLOC = staticmethod(startsWithLOC)

def read(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("read")
java.util.zip.ZipFile.read = staticmethod(read)

def getEntryTime(a0):
    raise NotImplementedError("getEntryTime")
java.util.zip.ZipFile.getEntryTime = staticmethod(getEntryTime)

def getEntryCrc(a0):
    raise NotImplementedError("getEntryCrc")
java.util.zip.ZipFile.getEntryCrc = staticmethod(getEntryCrc)

def getEntryCSize(a0):
    raise NotImplementedError("getEntryCSize")
java.util.zip.ZipFile.getEntryCSize = staticmethod(getEntryCSize)

def getEntrySize(a0):
    raise NotImplementedError("getEntrySize")
java.util.zip.ZipFile.getEntrySize = staticmethod(getEntrySize)

def getEntryMethod(a0):
    raise NotImplementedError("getEntryMethod")
java.util.zip.ZipFile.getEntryMethod = staticmethod(getEntryMethod)

def getEntryFlag(a0):
    raise NotImplementedError("getEntryFlag")
java.util.zip.ZipFile.getEntryFlag = staticmethod(getEntryFlag)

def getCommentBytes(a0):
    raise NotImplementedError("getCommentBytes")
java.util.zip.ZipFile.getCommentBytes = staticmethod(getCommentBytes)

def getEntryBytes(a0, a1):
    raise NotImplementedError("getEntryBytes")
java.util.zip.ZipFile.getEntryBytes = staticmethod(getEntryBytes)

def getZipMessage(a0):
    raise NotImplementedError("getZipMessage")
java.util.zip.ZipFile.getZipMessage = staticmethod(getZipMessage)

def environmentBlock():
    raise NotImplementedError("environmentBlock")
java.lang.ProcessEnvironment.environmentBlock = staticmethod(environmentBlock)

def getLookupCacheURLs(a0):
    raise NotImplementedError("getLookupCacheURLs")
sun.misc.URLClassPath.getLookupCacheURLs = staticmethod(getLookupCacheURLs)

def getLookupCacheForClassLoader(a0, a1):
    raise NotImplementedError("getLookupCacheForClassLoader")
sun.misc.URLClassPath.getLookupCacheForClassLoader = staticmethod(getLookupCacheForClassLoader)

def knownToNotExist0(a0, a1):
    raise NotImplementedError("knownToNotExist0")
sun.misc.URLClassPath.knownToNotExist0 = staticmethod(knownToNotExist0)

def getLength(a0):
    raise NotImplementedError("getLength")
java.lang.reflect.Array.getLength = staticmethod(getLength)

def get(a0, a1):
    raise NotImplementedError("get")
java.lang.reflect.Array.get = staticmethod(get)

def getBoolean(a0, a1):
    raise NotImplementedError("getBoolean")
java.lang.reflect.Array.getBoolean = staticmethod(getBoolean)

def getByte(a0, a1):
    raise NotImplementedError("getByte")
java.lang.reflect.Array.getByte = staticmethod(getByte)

def getChar(a0, a1):
    raise NotImplementedError("getChar")
java.lang.reflect.Array.getChar = staticmethod(getChar)

def getShort(a0, a1):
    raise NotImplementedError("getShort")
java.lang.reflect.Array.getShort = staticmethod(getShort)

def getInt(a0, a1):
    raise NotImplementedError("getInt")
java.lang.reflect.Array.getInt = staticmethod(getInt)

def getLong(a0, a1):
    raise NotImplementedError("getLong")
java.lang.reflect.Array.getLong = staticmethod(getLong)

def getFloat(a0, a1):
    raise NotImplementedError("getFloat")
java.lang.reflect.Array.getFloat = staticmethod(getFloat)

def getDouble(a0, a1):
    raise NotImplementedError("getDouble")
java.lang.reflect.Array.getDouble = staticmethod(getDouble)

def __set__(a0, a1, a2):
    raise NotImplementedError("__set__")
java.lang.reflect.Array.__set__ = staticmethod(__set__)

def setBoolean(a0, a1, a2):
    raise NotImplementedError("setBoolean")
java.lang.reflect.Array.setBoolean = staticmethod(setBoolean)

def setByte(a0, a1, a2):
    raise NotImplementedError("setByte")
java.lang.reflect.Array.setByte = staticmethod(setByte)

def setChar(a0, a1, a2):
    raise NotImplementedError("setChar")
java.lang.reflect.Array.setChar = staticmethod(setChar)

def setShort(a0, a1, a2):
    raise NotImplementedError("setShort")
java.lang.reflect.Array.setShort = staticmethod(setShort)

def setInt(a0, a1, a2):
    raise NotImplementedError("setInt")
java.lang.reflect.Array.setInt = staticmethod(setInt)

def setLong(a0, a1, a2):
    raise NotImplementedError("setLong")
java.lang.reflect.Array.setLong = staticmethod(setLong)

def setFloat(a0, a1, a2):
    raise NotImplementedError("setFloat")
java.lang.reflect.Array.setFloat = staticmethod(setFloat)

def setDouble(a0, a1, a2):
    raise NotImplementedError("setDouble")
java.lang.reflect.Array.setDouble = staticmethod(setDouble)

def newArray(a0, a1):
    raise NotImplementedError("newArray")
java.lang.reflect.Array.newArray = staticmethod(newArray)

def multiNewArray(a0, a1):
    raise NotImplementedError("multiNewArray")
java.lang.reflect.Array.multiNewArray = staticmethod(multiNewArray)

def initialize():
    raise NotImplementedError("initialize")
java.lang.Compiler.initialize = staticmethod(initialize)

def registerNatives():
    raise NotImplementedError("registerNatives")
java.lang.Compiler.registerNatives = staticmethod(registerNatives)

def compileClass(a0):
    raise NotImplementedError("compileClass")
java.lang.Compiler.compileClass = staticmethod(compileClass)

def compileClasses(a0):
    raise NotImplementedError("compileClasses")
java.lang.Compiler.compileClasses = staticmethod(compileClasses)

def command(a0):
    raise NotImplementedError("command")
java.lang.Compiler.command = staticmethod(command)

def enable():
    raise NotImplementedError("enable")
java.lang.Compiler.enable = staticmethod(enable)

def disable():
    raise NotImplementedError("disable")
java.lang.Compiler.disable = staticmethod(disable)

def setErrorMode(a0):
    raise NotImplementedError("setErrorMode")
sun.io.Win32ErrorMode.setErrorMode = staticmethod(setErrorMode)

def handle0(a0, a1):
    raise NotImplementedError("handle0")
sun.misc.NativeSignalHandler.handle0 = staticmethod(handle0)

def findSignal(a0):
    raise NotImplementedError("findSignal")
sun.misc.Signal.findSignal = staticmethod(findSignal)

def handle0(a0, a1):
    raise NotImplementedError("handle0")
sun.misc.Signal.handle0 = staticmethod(handle0)

def raise0(a0):
    raise NotImplementedError("raise0")
sun.misc.Signal.raise0 = staticmethod(raise0)

def load(a0, a1):
    raise NotImplementedError("load")
java.lang.ClassLoader__NativeLibrary.load = load

def find(a0):
    raise NotImplementedError("find")
java.lang.ClassLoader__NativeLibrary.find = find

def unload(a0, a1):
    raise NotImplementedError("unload")
java.lang.ClassLoader__NativeLibrary.unload = unload

def getDriveDirectory(a0):
    raise NotImplementedError("getDriveDirectory")
java.io.WinNTFileSystem.getDriveDirectory = getDriveDirectory

def canonicalize0(a0):
    raise NotImplementedError("canonicalize0")
java.io.WinNTFileSystem.canonicalize0 = canonicalize0

def canonicalizeWithPrefix0(a0, a1):
    raise NotImplementedError("canonicalizeWithPrefix0")
java.io.WinNTFileSystem.canonicalizeWithPrefix0 = canonicalizeWithPrefix0

def getBooleanAttributes(a0):
    raise NotImplementedError("getBooleanAttributes")
java.io.WinNTFileSystem.getBooleanAttributes = getBooleanAttributes

def checkAccess(a0, a1):
    raise NotImplementedError("checkAccess")
java.io.WinNTFileSystem.checkAccess = checkAccess

def getLastModifiedTime(a0):
    raise NotImplementedError("getLastModifiedTime")
java.io.WinNTFileSystem.getLastModifiedTime = getLastModifiedTime

def getLength(a0):
    raise NotImplementedError("getLength")
java.io.WinNTFileSystem.getLength = getLength

def setPermission(a0, a1, a2, a3):
    raise NotImplementedError("setPermission")
java.io.WinNTFileSystem.setPermission = setPermission

def createFileExclusively(a0):
    raise NotImplementedError("createFileExclusively")
java.io.WinNTFileSystem.createFileExclusively = createFileExclusively

def list(a0):
    raise NotImplementedError("list")
java.io.WinNTFileSystem.list = list

def createDirectory(a0):
    raise NotImplementedError("createDirectory")
java.io.WinNTFileSystem.createDirectory = createDirectory

def setLastModifiedTime(a0, a1):
    raise NotImplementedError("setLastModifiedTime")
java.io.WinNTFileSystem.setLastModifiedTime = setLastModifiedTime

def setReadOnly(a0):
    raise NotImplementedError("setReadOnly")
java.io.WinNTFileSystem.setReadOnly = setReadOnly

def delete0(a0):
    raise NotImplementedError("delete0")
java.io.WinNTFileSystem.delete0 = delete0

def rename0(a0, a1):
    raise NotImplementedError("rename0")
java.io.WinNTFileSystem.rename0 = rename0

def listRoots0():
    raise NotImplementedError("listRoots0")
java.io.WinNTFileSystem.listRoots0 = staticmethod(listRoots0)

def getSpace0(a0, a1):
    raise NotImplementedError("getSpace0")
java.io.WinNTFileSystem.getSpace0 = getSpace0

def initIDs():
    raise NotImplementedError("initIDs")
java.io.WinNTFileSystem.initIDs = staticmethod(initIDs)

def copyFromShortArray(a0, a1, a2, a3):
    raise NotImplementedError("copyFromShortArray")
java.nio.Bits.copyFromShortArray = staticmethod(copyFromShortArray)

def copyToShortArray(a0, a1, a2, a3):
    raise NotImplementedError("copyToShortArray")
java.nio.Bits.copyToShortArray = staticmethod(copyToShortArray)

def copyFromIntArray(a0, a1, a2, a3):
    raise NotImplementedError("copyFromIntArray")
java.nio.Bits.copyFromIntArray = staticmethod(copyFromIntArray)

def copyToIntArray(a0, a1, a2, a3):
    raise NotImplementedError("copyToIntArray")
java.nio.Bits.copyToIntArray = staticmethod(copyToIntArray)

def copyFromLongArray(a0, a1, a2, a3):
    raise NotImplementedError("copyFromLongArray")
java.nio.Bits.copyFromLongArray = staticmethod(copyFromLongArray)

def copyToLongArray(a0, a1, a2, a3):
    raise NotImplementedError("copyToLongArray")
java.nio.Bits.copyToLongArray = staticmethod(copyToLongArray)

def newInstance0(a0, a1):
    raise NotImplementedError("newInstance0")
sun.reflect.NativeConstructorAccessorImpl.newInstance0 = staticmethod(newInstance0)

def open0(a0, a1):
    raise NotImplementedError("open0")
java.io.FileOutputStream.open0 = open0

def write(a0, a1):
    raise NotImplementedError("write")
java.io.FileOutputStream.write = write

def writeBytes(a0, a1, a2, a3):
    raise NotImplementedError("writeBytes")
java.io.FileOutputStream.writeBytes = writeBytes

def close0():
    raise NotImplementedError("close0")
java.io.FileOutputStream.close0 = close0

def initIDs():
    raise NotImplementedError("initIDs")
java.io.FileOutputStream.initIDs = staticmethod(initIDs)

def getCallerClass():
    raise NotImplementedError("getCallerClass")
sun.reflect.Reflection.getCallerClass = staticmethod(getCallerClass)

def getClassAccessFlags(a0):
    raise NotImplementedError("getClassAccessFlags")
sun.reflect.Reflection.getClassAccessFlags = staticmethod(getClassAccessFlags)

def sync():
    raise NotImplementedError("sync")
java.io.FileDescriptor.sync = sync

def initIDs():
    raise NotImplementedError("initIDs")
java.io.FileDescriptor.initIDs = staticmethod(initIDs)

def __set__(a0):
    raise NotImplementedError("__set__")
java.io.FileDescriptor.__set__ = staticmethod(__set__)

def open0(a0):
    raise NotImplementedError("open0")
java.io.FileInputStream.open0 = open0

def read0():
    raise NotImplementedError("read0")
java.io.FileInputStream.read0 = read0

def readBytes(a0, a1, a2):
    raise NotImplementedError("readBytes")
java.io.FileInputStream.readBytes = readBytes

def skip(a0):
    raise NotImplementedError("skip")
java.io.FileInputStream.skip = skip

def available():
    raise NotImplementedError("available")
java.io.FileInputStream.available = available

def initIDs():
    raise NotImplementedError("initIDs")
java.io.FileInputStream.initIDs = staticmethod(initIDs)

def close0():
    raise NotImplementedError("close0")
java.io.FileInputStream.close0 = close0

def getJvmSpecialVersion():
    raise NotImplementedError("getJvmSpecialVersion")
sun.misc.Version.getJvmSpecialVersion = staticmethod(getJvmSpecialVersion)

def getJdkSpecialVersion():
    raise NotImplementedError("getJdkSpecialVersion")
sun.misc.Version.getJdkSpecialVersion = staticmethod(getJdkSpecialVersion)

def getJvmVersionInfo():
    raise NotImplementedError("getJvmVersionInfo")
sun.misc.Version.getJvmVersionInfo = staticmethod(getJvmVersionInfo)

def getJdkVersionInfo():
    raise NotImplementedError("getJdkVersionInfo")
sun.misc.Version.getJdkVersionInfo = staticmethod(getJdkVersionInfo)

def availableProcessors():
    raise NotImplementedError("availableProcessors")
java.lang.Runtime.availableProcessors = availableProcessors

def freeMemory():
    raise NotImplementedError("freeMemory")
java.lang.Runtime.freeMemory = freeMemory

def totalMemory():
    raise NotImplementedError("totalMemory")
java.lang.Runtime.totalMemory = totalMemory

def maxMemory():
    raise NotImplementedError("maxMemory")
java.lang.Runtime.maxMemory = maxMemory

def gc():
    raise NotImplementedError("gc")
java.lang.Runtime.gc = gc

def runFinalization0():
    raise NotImplementedError("runFinalization0")
java.lang.Runtime.runFinalization0 = staticmethod(runFinalization0)

def traceInstructions(a0):
    raise NotImplementedError("traceInstructions")
java.lang.Runtime.traceInstructions = traceInstructions

def traceMethodCalls(a0):
    raise NotImplementedError("traceMethodCalls")
java.lang.Runtime.traceMethodCalls = traceMethodCalls

def latestUserDefinedLoader():
    raise NotImplementedError("latestUserDefinedLoader")
sun.misc.VM.latestUserDefinedLoader = staticmethod(latestUserDefinedLoader)

def initialize():
    raise NotImplementedError("initialize")
sun.misc.VM.initialize = staticmethod(initialize)

def doPrivileged(a0):
    raise NotImplementedError("doPrivileged")
java.security.AccessController.doPrivileged = staticmethod(doPrivileged)

def getStackAccessControlContext():
    raise NotImplementedError("getStackAccessControlContext")
java.security.AccessController.getStackAccessControlContext = staticmethod(getStackAccessControlContext)

def getInheritedAccessControlContext():
    raise NotImplementedError("getInheritedAccessControlContext")
java.security.AccessController.getInheritedAccessControlContext = staticmethod(getInheritedAccessControlContext)

def doubleToRawLongBits(a0):
    raise NotImplementedError("doubleToRawLongBits")
java.lang.Double.doubleToRawLongBits = staticmethod(doubleToRawLongBits)

def longBitsToDouble(a0):
    raise NotImplementedError("longBitsToDouble")
java.lang.Double.longBitsToDouble = staticmethod(longBitsToDouble)

def floatToRawIntBits(a0):
    raise NotImplementedError("floatToRawIntBits")
java.lang.Float.floatToRawIntBits = staticmethod(floatToRawIntBits)

def intBitsToFloat(a0):
    raise NotImplementedError("intBitsToFloat")
java.lang.Float.intBitsToFloat = staticmethod(intBitsToFloat)

def registerNatives():
    raise NotImplementedError("registerNatives")
sun.misc.Unsafe.registerNatives = staticmethod(registerNatives)

def getInt(a0, a1):
    raise NotImplementedError("getInt")
sun.misc.Unsafe.getInt = getInt

def putInt(a0, a1, a2):
    raise NotImplementedError("putInt")
sun.misc.Unsafe.putInt = putInt

def getObject(a0, a1):
    raise NotImplementedError("getObject")
sun.misc.Unsafe.getObject = getObject

def putObject(a0, a1, a2):
    raise NotImplementedError("putObject")
sun.misc.Unsafe.putObject = putObject

def getBoolean(a0, a1):
    raise NotImplementedError("getBoolean")
sun.misc.Unsafe.getBoolean = getBoolean

def putBoolean(a0, a1, a2):
    raise NotImplementedError("putBoolean")
sun.misc.Unsafe.putBoolean = putBoolean

def getByte(a0, a1):
    raise NotImplementedError("getByte")
sun.misc.Unsafe.getByte = getByte

def putByte(a0, a1, a2):
    raise NotImplementedError("putByte")
sun.misc.Unsafe.putByte = putByte

def getShort(a0, a1):
    raise NotImplementedError("getShort")
sun.misc.Unsafe.getShort = getShort

def putShort(a0, a1, a2):
    raise NotImplementedError("putShort")
sun.misc.Unsafe.putShort = putShort

def getChar(a0, a1):
    raise NotImplementedError("getChar")
sun.misc.Unsafe.getChar = getChar

def putChar(a0, a1, a2):
    raise NotImplementedError("putChar")
sun.misc.Unsafe.putChar = putChar

def getLong(a0, a1):
    raise NotImplementedError("getLong")
sun.misc.Unsafe.getLong = getLong

def putLong(a0, a1, a2):
    raise NotImplementedError("putLong")
sun.misc.Unsafe.putLong = putLong

def getFloat(a0, a1):
    raise NotImplementedError("getFloat")
sun.misc.Unsafe.getFloat = getFloat

def putFloat(a0, a1, a2):
    raise NotImplementedError("putFloat")
sun.misc.Unsafe.putFloat = putFloat

def getDouble(a0, a1):
    raise NotImplementedError("getDouble")
sun.misc.Unsafe.getDouble = getDouble

def putDouble(a0, a1, a2):
    raise NotImplementedError("putDouble")
sun.misc.Unsafe.putDouble = putDouble

def getAddress(a0):
    raise NotImplementedError("getAddress")
sun.misc.Unsafe.getAddress = getAddress

def putAddress(a0, a1):
    raise NotImplementedError("putAddress")
sun.misc.Unsafe.putAddress = putAddress

def allocateMemory(a0):
    raise NotImplementedError("allocateMemory")
sun.misc.Unsafe.allocateMemory = allocateMemory

def reallocateMemory(a0, a1):
    raise NotImplementedError("reallocateMemory")
sun.misc.Unsafe.reallocateMemory = reallocateMemory

def setMemory(a0, a1, a2, a3):
    raise NotImplementedError("setMemory")
sun.misc.Unsafe.setMemory = setMemory

def copyMemory(a0, a1, a2, a3, a4):
    raise NotImplementedError("copyMemory")
sun.misc.Unsafe.copyMemory = copyMemory

def freeMemory(a0):
    raise NotImplementedError("freeMemory")
sun.misc.Unsafe.freeMemory = freeMemory

def staticFieldOffset(a0):
    raise NotImplementedError("staticFieldOffset")
sun.misc.Unsafe.staticFieldOffset = staticFieldOffset

def objectFieldOffset(a0):
    raise NotImplementedError("objectFieldOffset")
sun.misc.Unsafe.objectFieldOffset = objectFieldOffset

def staticFieldBase(a0):
    raise NotImplementedError("staticFieldBase")
sun.misc.Unsafe.staticFieldBase = staticFieldBase

def shouldBeInitialized(a0):
    raise NotImplementedError("shouldBeInitialized")
sun.misc.Unsafe.shouldBeInitialized = shouldBeInitialized

def ensureClassInitialized(a0):
    raise NotImplementedError("ensureClassInitialized")
sun.misc.Unsafe.ensureClassInitialized = ensureClassInitialized

def arrayBaseOffset(a0):
    raise NotImplementedError("arrayBaseOffset")
sun.misc.Unsafe.arrayBaseOffset = arrayBaseOffset

def arrayIndexScale(a0):
    raise NotImplementedError("arrayIndexScale")
sun.misc.Unsafe.arrayIndexScale = arrayIndexScale

def addressSize():
    raise NotImplementedError("addressSize")
sun.misc.Unsafe.addressSize = addressSize

def pageSize():
    raise NotImplementedError("pageSize")
sun.misc.Unsafe.pageSize = pageSize

def defineClass(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("defineClass")
sun.misc.Unsafe.defineClass = defineClass

def defineAnonymousClass(a0, a1, a2):
    raise NotImplementedError("defineAnonymousClass")
sun.misc.Unsafe.defineAnonymousClass = defineAnonymousClass

def allocateInstance(a0):
    raise NotImplementedError("allocateInstance")
sun.misc.Unsafe.allocateInstance = allocateInstance

def monitorEnter(a0):
    raise NotImplementedError("monitorEnter")
sun.misc.Unsafe.monitorEnter = monitorEnter

def monitorExit(a0):
    raise NotImplementedError("monitorExit")
sun.misc.Unsafe.monitorExit = monitorExit

def tryMonitorEnter(a0):
    raise NotImplementedError("tryMonitorEnter")
sun.misc.Unsafe.tryMonitorEnter = tryMonitorEnter

def throwException(a0):
    raise NotImplementedError("throwException")
sun.misc.Unsafe.throwException = throwException

def compareAndSwapObject(a0, a1, a2, a3):
    raise NotImplementedError("compareAndSwapObject")
sun.misc.Unsafe.compareAndSwapObject = compareAndSwapObject

def compareAndSwapInt(a0, a1, a2, a3):
    raise NotImplementedError("compareAndSwapInt")
sun.misc.Unsafe.compareAndSwapInt = compareAndSwapInt

def compareAndSwapLong(a0, a1, a2, a3):
    raise NotImplementedError("compareAndSwapLong")
sun.misc.Unsafe.compareAndSwapLong = compareAndSwapLong

def getObjectVolatile(a0, a1):
    raise NotImplementedError("getObjectVolatile")
sun.misc.Unsafe.getObjectVolatile = getObjectVolatile

def putObjectVolatile(a0, a1, a2):
    raise NotImplementedError("putObjectVolatile")
sun.misc.Unsafe.putObjectVolatile = putObjectVolatile

def getIntVolatile(a0, a1):
    raise NotImplementedError("getIntVolatile")
sun.misc.Unsafe.getIntVolatile = getIntVolatile

def putIntVolatile(a0, a1, a2):
    raise NotImplementedError("putIntVolatile")
sun.misc.Unsafe.putIntVolatile = putIntVolatile

def getBooleanVolatile(a0, a1):
    raise NotImplementedError("getBooleanVolatile")
sun.misc.Unsafe.getBooleanVolatile = getBooleanVolatile

def putBooleanVolatile(a0, a1, a2):
    raise NotImplementedError("putBooleanVolatile")
sun.misc.Unsafe.putBooleanVolatile = putBooleanVolatile

def getByteVolatile(a0, a1):
    raise NotImplementedError("getByteVolatile")
sun.misc.Unsafe.getByteVolatile = getByteVolatile

def putByteVolatile(a0, a1, a2):
    raise NotImplementedError("putByteVolatile")
sun.misc.Unsafe.putByteVolatile = putByteVolatile

def getShortVolatile(a0, a1):
    raise NotImplementedError("getShortVolatile")
sun.misc.Unsafe.getShortVolatile = getShortVolatile

def putShortVolatile(a0, a1, a2):
    raise NotImplementedError("putShortVolatile")
sun.misc.Unsafe.putShortVolatile = putShortVolatile

def getCharVolatile(a0, a1):
    raise NotImplementedError("getCharVolatile")
sun.misc.Unsafe.getCharVolatile = getCharVolatile

def putCharVolatile(a0, a1, a2):
    raise NotImplementedError("putCharVolatile")
sun.misc.Unsafe.putCharVolatile = putCharVolatile

def getLongVolatile(a0, a1):
    raise NotImplementedError("getLongVolatile")
sun.misc.Unsafe.getLongVolatile = getLongVolatile

def putLongVolatile(a0, a1, a2):
    raise NotImplementedError("putLongVolatile")
sun.misc.Unsafe.putLongVolatile = putLongVolatile

def getFloatVolatile(a0, a1):
    raise NotImplementedError("getFloatVolatile")
sun.misc.Unsafe.getFloatVolatile = getFloatVolatile

def putFloatVolatile(a0, a1, a2):
    raise NotImplementedError("putFloatVolatile")
sun.misc.Unsafe.putFloatVolatile = putFloatVolatile

def getDoubleVolatile(a0, a1):
    raise NotImplementedError("getDoubleVolatile")
sun.misc.Unsafe.getDoubleVolatile = getDoubleVolatile

def putDoubleVolatile(a0, a1, a2):
    raise NotImplementedError("putDoubleVolatile")
sun.misc.Unsafe.putDoubleVolatile = putDoubleVolatile

def putOrderedObject(a0, a1, a2):
    raise NotImplementedError("putOrderedObject")
sun.misc.Unsafe.putOrderedObject = putOrderedObject

def putOrderedInt(a0, a1, a2):
    raise NotImplementedError("putOrderedInt")
sun.misc.Unsafe.putOrderedInt = putOrderedInt

def putOrderedLong(a0, a1, a2):
    raise NotImplementedError("putOrderedLong")
sun.misc.Unsafe.putOrderedLong = putOrderedLong

def unpark(a0):
    raise NotImplementedError("unpark")
sun.misc.Unsafe.unpark = unpark

def park(a0, a1):
    raise NotImplementedError("park")
sun.misc.Unsafe.park = park

def getLoadAverage(a0, a1):
    raise NotImplementedError("getLoadAverage")
sun.misc.Unsafe.getLoadAverage = getLoadAverage

def loadFence():
    raise NotImplementedError("loadFence")
sun.misc.Unsafe.loadFence = loadFence

def storeFence():
    raise NotImplementedError("storeFence")
sun.misc.Unsafe.storeFence = storeFence

def fullFence():
    raise NotImplementedError("fullFence")
sun.misc.Unsafe.fullFence = fullFence

def init(a0, a1):
    raise NotImplementedError("init")
java.lang.invoke.MethodHandleNatives.init = staticmethod(init)

def expand(a0):
    raise NotImplementedError("expand")
java.lang.invoke.MethodHandleNatives.expand = staticmethod(expand)

def resolve(a0, a1):
    raise NotImplementedError("resolve")
java.lang.invoke.MethodHandleNatives.resolve = staticmethod(resolve)

def getMembers(a0, a1, a2, a3, a4, a5, a6):
    raise NotImplementedError("getMembers")
java.lang.invoke.MethodHandleNatives.getMembers = staticmethod(getMembers)

def objectFieldOffset(a0):
    raise NotImplementedError("objectFieldOffset")
java.lang.invoke.MethodHandleNatives.objectFieldOffset = staticmethod(objectFieldOffset)

def staticFieldOffset(a0):
    raise NotImplementedError("staticFieldOffset")
java.lang.invoke.MethodHandleNatives.staticFieldOffset = staticmethod(staticFieldOffset)

def staticFieldBase(a0):
    raise NotImplementedError("staticFieldBase")
java.lang.invoke.MethodHandleNatives.staticFieldBase = staticmethod(staticFieldBase)

def getMemberVMInfo(a0):
    raise NotImplementedError("getMemberVMInfo")
java.lang.invoke.MethodHandleNatives.getMemberVMInfo = staticmethod(getMemberVMInfo)

def getConstant(a0):
    raise NotImplementedError("getConstant")
java.lang.invoke.MethodHandleNatives.getConstant = staticmethod(getConstant)

def setCallSiteTargetNormal(a0, a1):
    raise NotImplementedError("setCallSiteTargetNormal")
java.lang.invoke.MethodHandleNatives.setCallSiteTargetNormal = staticmethod(setCallSiteTargetNormal)

def setCallSiteTargetVolatile(a0, a1):
    raise NotImplementedError("setCallSiteTargetVolatile")
java.lang.invoke.MethodHandleNatives.setCallSiteTargetVolatile = staticmethod(setCallSiteTargetVolatile)

def registerNatives():
    raise NotImplementedError("registerNatives")
java.lang.invoke.MethodHandleNatives.registerNatives = staticmethod(registerNatives)

def getNamedCon(a0, a1):
    raise NotImplementedError("getNamedCon")
java.lang.invoke.MethodHandleNatives.getNamedCon = staticmethod(getNamedCon)

def invokeExact(a0):
    raise NotImplementedError("invokeExact")
java.lang.invoke.MethodHandle.invokeExact = invokeExact

def invoke(a0):
    raise NotImplementedError("invoke")
java.lang.invoke.MethodHandle.invoke = invoke

def invokeBasic(a0):
    raise NotImplementedError("invokeBasic")
java.lang.invoke.MethodHandle.invokeBasic = invokeBasic

def linkToVirtual(a0):
    raise NotImplementedError("linkToVirtual")
java.lang.invoke.MethodHandle.linkToVirtual = staticmethod(linkToVirtual)

def linkToStatic(a0):
    raise NotImplementedError("linkToStatic")
java.lang.invoke.MethodHandle.linkToStatic = staticmethod(linkToStatic)

def linkToSpecial(a0):
    raise NotImplementedError("linkToSpecial")
java.lang.invoke.MethodHandle.linkToSpecial = staticmethod(linkToSpecial)

def linkToInterface(a0):
    raise NotImplementedError("linkToInterface")
java.lang.invoke.MethodHandle.linkToInterface = staticmethod(linkToInterface)

def getSize0(a0):
    raise NotImplementedError("getSize0")
sun.reflect.ConstantPool.getSize0 = getSize0

def getClassAt0(a0, a1):
    raise NotImplementedError("getClassAt0")
sun.reflect.ConstantPool.getClassAt0 = getClassAt0

def getClassAtIfLoaded0(a0, a1):
    raise NotImplementedError("getClassAtIfLoaded0")
sun.reflect.ConstantPool.getClassAtIfLoaded0 = getClassAtIfLoaded0

def getMethodAt0(a0, a1):
    raise NotImplementedError("getMethodAt0")
sun.reflect.ConstantPool.getMethodAt0 = getMethodAt0

def getMethodAtIfLoaded0(a0, a1):
    raise NotImplementedError("getMethodAtIfLoaded0")
sun.reflect.ConstantPool.getMethodAtIfLoaded0 = getMethodAtIfLoaded0

def getFieldAt0(a0, a1):
    raise NotImplementedError("getFieldAt0")
sun.reflect.ConstantPool.getFieldAt0 = getFieldAt0

def getFieldAtIfLoaded0(a0, a1):
    raise NotImplementedError("getFieldAtIfLoaded0")
sun.reflect.ConstantPool.getFieldAtIfLoaded0 = getFieldAtIfLoaded0

def getMemberRefInfoAt0(a0, a1):
    raise NotImplementedError("getMemberRefInfoAt0")
sun.reflect.ConstantPool.getMemberRefInfoAt0 = getMemberRefInfoAt0

def getIntAt0(a0, a1):
    raise NotImplementedError("getIntAt0")
sun.reflect.ConstantPool.getIntAt0 = getIntAt0

def getLongAt0(a0, a1):
    raise NotImplementedError("getLongAt0")
sun.reflect.ConstantPool.getLongAt0 = getLongAt0

def getFloatAt0(a0, a1):
    raise NotImplementedError("getFloatAt0")
sun.reflect.ConstantPool.getFloatAt0 = getFloatAt0

def getDoubleAt0(a0, a1):
    raise NotImplementedError("getDoubleAt0")
sun.reflect.ConstantPool.getDoubleAt0 = getDoubleAt0

def getStringAt0(a0, a1):
    raise NotImplementedError("getStringAt0")
sun.reflect.ConstantPool.getStringAt0 = getStringAt0

def getUTF8At0(a0, a1):
    raise NotImplementedError("getUTF8At0")
sun.reflect.ConstantPool.getUTF8At0 = getUTF8At0

def getParameters0():
    raise NotImplementedError("getParameters0")
java.lang.reflect.Executable.getParameters0 = getParameters0

def getTypeAnnotationBytes0():
    raise NotImplementedError("getTypeAnnotationBytes0")
java.lang.reflect.Executable.getTypeAnnotationBytes0 = getTypeAnnotationBytes0

def getTypeAnnotationBytes0():
    raise NotImplementedError("getTypeAnnotationBytes0")
java.lang.reflect.Field.getTypeAnnotationBytes0 = getTypeAnnotationBytes0

def registerNatives():
    raise NotImplementedError("registerNatives")
java.lang.Thread.registerNatives = staticmethod(registerNatives)

def currentThread():
    raise NotImplementedError("currentThread")
java.lang.Thread.currentThread = staticmethod(currentThread)

def __yield__():
    raise NotImplementedError("__yield__")
java.lang.Thread.__yield__ = staticmethod(__yield__)

def sleep(a0):
    raise NotImplementedError("sleep")
java.lang.Thread.sleep = staticmethod(sleep)

def start0():
    raise NotImplementedError("start0")
java.lang.Thread.start0 = start0

def isInterrupted(a0):
    raise NotImplementedError("isInterrupted")
java.lang.Thread.isInterrupted = isInterrupted

def isAlive():
    raise NotImplementedError("isAlive")
java.lang.Thread.isAlive = isAlive

def countStackFrames():
    raise NotImplementedError("countStackFrames")
java.lang.Thread.countStackFrames = countStackFrames

def holdsLock(a0):
    raise NotImplementedError("holdsLock")
java.lang.Thread.holdsLock = staticmethod(holdsLock)

def dumpThreads(a0):
    raise NotImplementedError("dumpThreads")
java.lang.Thread.dumpThreads = staticmethod(dumpThreads)

def getThreads():
    raise NotImplementedError("getThreads")
java.lang.Thread.getThreads = staticmethod(getThreads)

def setPriority0(a0):
    raise NotImplementedError("setPriority0")
java.lang.Thread.setPriority0 = setPriority0

def stop0(a0):
    raise NotImplementedError("stop0")
java.lang.Thread.stop0 = stop0

def suspend0():
    raise NotImplementedError("suspend0")
java.lang.Thread.suspend0 = suspend0

def resume0():
    raise NotImplementedError("resume0")
java.lang.Thread.resume0 = resume0

def interrupt0():
    raise NotImplementedError("interrupt0")
java.lang.Thread.interrupt0 = interrupt0

def setNativeName(a0):
    raise NotImplementedError("setNativeName")
java.lang.Thread.setNativeName = setNativeName

def getClassContext():
    raise NotImplementedError("getClassContext")
java.lang.SecurityManager.getClassContext = getClassContext

def currentClassLoader0():
    raise NotImplementedError("currentClassLoader0")
java.lang.SecurityManager.currentClassLoader0 = currentClassLoader0

def classDepth(a0):
    raise NotImplementedError("classDepth")
java.lang.SecurityManager.classDepth = classDepth

def classLoaderDepth0():
    raise NotImplementedError("classLoaderDepth0")
java.lang.SecurityManager.classLoaderDepth0 = classLoaderDepth0

def currentLoadedClass0():
    raise NotImplementedError("currentLoadedClass0")
java.lang.SecurityManager.currentLoadedClass0 = currentLoadedClass0

def fillInStackTrace(a0):
    raise NotImplementedError("fillInStackTrace")
java.lang.Throwable.fillInStackTrace = fillInStackTrace

def getStackTraceDepth():
    raise NotImplementedError("getStackTraceDepth")
java.lang.Throwable.getStackTraceDepth = getStackTraceDepth

def getStackTraceElement(a0):
    raise NotImplementedError("getStackTraceElement")
java.lang.Throwable.getStackTraceElement = getStackTraceElement

def registerNatives():
    raise NotImplementedError("registerNatives")
java.lang.System.registerNatives = staticmethod(registerNatives)

def setIn0(a0):
    raise NotImplementedError("setIn0")
java.lang.System.setIn0 = staticmethod(setIn0)

def setOut0(printStream):
    java.lang.System.out = printStream
java.lang.System.setOut0 = staticmethod(setOut0)

def setErr0(a0):
    raise NotImplementedError("setErr0")
java.lang.System.setErr0 = staticmethod(setErr0)

def currentTimeMillis():
    raise NotImplementedError("currentTimeMillis")
java.lang.System.currentTimeMillis = staticmethod(currentTimeMillis)

def nanoTime():
    raise NotImplementedError("nanoTime")
java.lang.System.nanoTime = staticmethod(nanoTime)

def arraycopy(a0, a1, a2, a3, a4):
    raise NotImplementedError("arraycopy")
java.lang.System.arraycopy = staticmethod(arraycopy)

def identityHashCode(a0):
    raise NotImplementedError("identityHashCode")
java.lang.System.identityHashCode = staticmethod(identityHashCode)

def initProperties(a0):
    raise NotImplementedError("initProperties")
java.lang.System.initProperties = staticmethod(initProperties)

def mapLibraryName(a0):
    raise NotImplementedError("mapLibraryName")
java.lang.System.mapLibraryName = staticmethod(mapLibraryName)

def registerNatives():
    raise NotImplementedError("registerNatives")
java.lang.ClassLoader.registerNatives = staticmethod(registerNatives)

def defineClass0(a0, a1, a2, a3, a4):
    raise NotImplementedError("defineClass0")
java.lang.ClassLoader.defineClass0 = defineClass0

def defineClass1(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("defineClass1")
java.lang.ClassLoader.defineClass1 = defineClass1

def defineClass2(a0, a1, a2, a3, a4, a5):
    raise NotImplementedError("defineClass2")
java.lang.ClassLoader.defineClass2 = defineClass2

def resolveClass0(a0):
    raise NotImplementedError("resolveClass0")
java.lang.ClassLoader.resolveClass0 = resolveClass0

def findBootstrapClass(a0):
    raise NotImplementedError("findBootstrapClass")
java.lang.ClassLoader.findBootstrapClass = findBootstrapClass

def findLoadedClass0(a0):
    raise NotImplementedError("findLoadedClass0")
java.lang.ClassLoader.findLoadedClass0 = findLoadedClass0

def findBuiltinLib(a0):
    raise NotImplementedError("findBuiltinLib")
java.lang.ClassLoader.findBuiltinLib = staticmethod(findBuiltinLib)

def retrieveDirectives():
    raise NotImplementedError("retrieveDirectives")
java.lang.ClassLoader.retrieveDirectives = staticmethod(retrieveDirectives)

def registerNatives():
    raise NotImplementedError("registerNatives")
java.lang.Class.registerNatives = staticmethod(registerNatives)

def forName0(a0, a1, a2, a3):
    raise NotImplementedError("forName0")
java.lang.Class.forName0 = staticmethod(forName0)

def isInstance(a0):
    raise NotImplementedError("isInstance")
java.lang.Class.isInstance = isInstance

def isAssignableFrom(a0):
    raise NotImplementedError("isAssignableFrom")
java.lang.Class.isAssignableFrom = isAssignableFrom

def isInterface():
    raise NotImplementedError("isInterface")
java.lang.Class.isInterface = isInterface

def isArray():
    raise NotImplementedError("isArray")
java.lang.Class.isArray = isArray

def isPrimitive():
    raise NotImplementedError("isPrimitive")
java.lang.Class.isPrimitive = isPrimitive

def getName0():
    raise NotImplementedError("getName0")
java.lang.Class.getName0 = getName0

def getSuperclass():
    raise NotImplementedError("getSuperclass")
java.lang.Class.getSuperclass = getSuperclass

def getInterfaces0():
    raise NotImplementedError("getInterfaces0")
java.lang.Class.getInterfaces0 = getInterfaces0

def getComponentType():
    raise NotImplementedError("getComponentType")
java.lang.Class.getComponentType = getComponentType

def getModifiers():
    raise NotImplementedError("getModifiers")
java.lang.Class.getModifiers = getModifiers

def getSigners():
    raise NotImplementedError("getSigners")
java.lang.Class.getSigners = getSigners

def setSigners(a0):
    raise NotImplementedError("setSigners")
java.lang.Class.setSigners = setSigners

def getEnclosingMethod0():
    raise NotImplementedError("getEnclosingMethod0")
java.lang.Class.getEnclosingMethod0 = getEnclosingMethod0

def getDeclaringClass0():
    raise NotImplementedError("getDeclaringClass0")
java.lang.Class.getDeclaringClass0 = getDeclaringClass0

def getProtectionDomain0():
    raise NotImplementedError("getProtectionDomain0")
java.lang.Class.getProtectionDomain0 = getProtectionDomain0

def getPrimitiveClass(a0):
    raise NotImplementedError("getPrimitiveClass")
java.lang.Class.getPrimitiveClass = staticmethod(getPrimitiveClass)

def getGenericSignature0():
    raise NotImplementedError("getGenericSignature0")
java.lang.Class.getGenericSignature0 = getGenericSignature0

def getRawAnnotations():
    raise NotImplementedError("getRawAnnotations")
java.lang.Class.getRawAnnotations = getRawAnnotations

def getRawTypeAnnotations():
    raise NotImplementedError("getRawTypeAnnotations")
java.lang.Class.getRawTypeAnnotations = getRawTypeAnnotations

def getConstantPool():
    raise NotImplementedError("getConstantPool")
java.lang.Class.getConstantPool = getConstantPool

def getDeclaredFields0(a0):
    raise NotImplementedError("getDeclaredFields0")
java.lang.Class.getDeclaredFields0 = getDeclaredFields0

def getDeclaredMethods0(a0):
    raise NotImplementedError("getDeclaredMethods0")
java.lang.Class.getDeclaredMethods0 = getDeclaredMethods0

def getDeclaredConstructors0(a0):
    raise NotImplementedError("getDeclaredConstructors0")
java.lang.Class.getDeclaredConstructors0 = getDeclaredConstructors0

def getDeclaredClasses0():
    raise NotImplementedError("getDeclaredClasses0")
java.lang.Class.getDeclaredClasses0 = getDeclaredClasses0

def desiredAssertionStatus0(a0):
    raise NotImplementedError("desiredAssertionStatus0")
java.lang.Class.desiredAssertionStatus0 = staticmethod(desiredAssertionStatus0)

def intern():
    raise NotImplementedError("intern")
java.lang.String.intern = intern

def registerNatives():
    raise NotImplementedError("registerNatives")
java.lang.Object.registerNatives = staticmethod(registerNatives)

def getClass():
    raise NotImplementedError("getClass")
java.lang.Object.getClass = getClass

def hashCode():
    raise NotImplementedError("hashCode")
java.lang.Object.hashCode = hashCode

def clone():
    raise NotImplementedError("clone")
java.lang.Object.clone = clone

def notify():
    raise NotImplementedError("notify")
java.lang.Object.notify = notify

def notifyAll():
    raise NotImplementedError("notifyAll")
java.lang.Object.notifyAll = notifyAll

def wait(a0):
    raise NotImplementedError("wait")
java.lang.Object.wait = wait


# Custom initialization code


class PythonPrintStream(object):
    def println(self, s):
        print s
java.lang.System.setOut0(PythonPrintStream())

