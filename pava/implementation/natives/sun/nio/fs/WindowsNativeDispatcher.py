def add_native_methods(clazz):
    def CreateEvent(a0, a1):
        raise NotImplementedError()

    def CreateFile0(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def CloseHandle(a0):
        raise NotImplementedError()

    def DeleteFile0(a0):
        raise NotImplementedError()

    def CreateDirectory0(a0, a1):
        raise NotImplementedError()

    def RemoveDirectory0(a0):
        raise NotImplementedError()

    def DeviceIoControlSetSparse(a0):
        raise NotImplementedError()

    def DeviceIoControlGetReparsePoint(a0, a1, a2):
        raise NotImplementedError()

    def FindFirstFile0(a0, a1):
        raise NotImplementedError()

    def FindFirstFile1(a0, a1):
        raise NotImplementedError()

    def FindNextFile(a0, a1):
        raise NotImplementedError()

    def FindFirstStream0(a0, a1):
        raise NotImplementedError()

    def FindNextStream(a0):
        raise NotImplementedError()

    def FindClose(a0):
        raise NotImplementedError()

    def GetFileInformationByHandle(a0, a1):
        raise NotImplementedError()

    def CopyFileEx0(a0, a1, a2, a3):
        raise NotImplementedError()

    def MoveFileEx0(a0, a1, a2):
        raise NotImplementedError()

    def GetFileAttributes0(a0):
        raise NotImplementedError()

    def SetFileAttributes0(a0, a1):
        raise NotImplementedError()

    def GetFileAttributesEx0(a0, a1):
        raise NotImplementedError()

    def SetFileTime(a0, a1, a2, a3):
        raise NotImplementedError()

    def SetEndOfFile(a0):
        raise NotImplementedError()

    def GetLogicalDrives():
        raise NotImplementedError()

    def GetVolumeInformation0(a0, a1):
        raise NotImplementedError()

    def GetDriveType0(a0):
        raise NotImplementedError()

    def GetDiskFreeSpaceEx0(a0, a1):
        raise NotImplementedError()

    def GetVolumePathName0(a0):
        raise NotImplementedError()

    def InitializeSecurityDescriptor(a0):
        raise NotImplementedError()

    def InitializeAcl(a0, a1):
        raise NotImplementedError()

    def GetFileSecurity0(a0, a1, a2, a3):
        raise NotImplementedError()

    def SetFileSecurity0(a0, a1, a2):
        raise NotImplementedError()

    def GetSecurityDescriptorOwner(a0):
        raise NotImplementedError()

    def SetSecurityDescriptorOwner(a0, a1):
        raise NotImplementedError()

    def GetSecurityDescriptorDacl(a0):
        raise NotImplementedError()

    def SetSecurityDescriptorDacl(a0, a1):
        raise NotImplementedError()

    def GetAclInformation0(a0, a1):
        raise NotImplementedError()

    def GetAce(a0, a1):
        raise NotImplementedError()

    def AddAccessAllowedAceEx(a0, a1, a2, a3):
        raise NotImplementedError()

    def AddAccessDeniedAceEx(a0, a1, a2, a3):
        raise NotImplementedError()

    def LookupAccountSid0(a0, a1):
        raise NotImplementedError()

    def LookupAccountName0(a0, a1, a2):
        raise NotImplementedError()

    def GetLengthSid(a0):
        raise NotImplementedError()

    def ConvertSidToStringSid(a0):
        raise NotImplementedError()

    def ConvertStringSidToSid0(a0):
        raise NotImplementedError()

    def GetCurrentProcess():
        raise NotImplementedError()

    def GetCurrentThread():
        raise NotImplementedError()

    def OpenProcessToken(a0, a1):
        raise NotImplementedError()

    def OpenThreadToken(a0, a1, a2):
        raise NotImplementedError()

    def DuplicateTokenEx(a0, a1):
        raise NotImplementedError()

    def SetThreadToken(a0, a1):
        raise NotImplementedError()

    def GetTokenInformation(a0, a1, a2, a3):
        raise NotImplementedError()

    def AdjustTokenPrivileges(a0, a1, a2):
        raise NotImplementedError()

    def AccessCheck(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def LookupPrivilegeValue0(a0):
        raise NotImplementedError()

    def CreateSymbolicLink0(a0, a1, a2):
        raise NotImplementedError()

    def CreateHardLink0(a0, a1):
        raise NotImplementedError()

    def GetFullPathName0(a0):
        raise NotImplementedError()

    def GetFinalPathNameByHandle(a0):
        raise NotImplementedError()

    def FormatMessage(a0):
        raise NotImplementedError()

    def LocalFree(a0):
        raise NotImplementedError()

    def CreateIoCompletionPort(a0, a1, a2):
        raise NotImplementedError()

    def GetQueuedCompletionStatus0(a0, a1):
        raise NotImplementedError()

    def PostQueuedCompletionStatus(a0, a1):
        raise NotImplementedError()

    def ReadDirectoryChangesW(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def CancelIo(a0):
        raise NotImplementedError()

    def GetOverlappedResult(a0, a1):
        raise NotImplementedError()

    def BackupRead0(a0, a1, a2, a3, a4, a5):
        raise NotImplementedError()

    def BackupSeek(a0, a1, a2):
        raise NotImplementedError()

    def initIDs():
        raise NotImplementedError()

    clazz.CreateEvent = staticmethod(CreateEvent)
    clazz.CreateFile0 = staticmethod(CreateFile0)
    clazz.CloseHandle = staticmethod(CloseHandle)
    clazz.DeleteFile0 = staticmethod(DeleteFile0)
    clazz.CreateDirectory0 = staticmethod(CreateDirectory0)
    clazz.RemoveDirectory0 = staticmethod(RemoveDirectory0)
    clazz.DeviceIoControlSetSparse = staticmethod(DeviceIoControlSetSparse)
    clazz.DeviceIoControlGetReparsePoint = staticmethod(DeviceIoControlGetReparsePoint)
    clazz.FindFirstFile0 = staticmethod(FindFirstFile0)
    clazz.FindFirstFile1 = staticmethod(FindFirstFile1)
    clazz.FindNextFile = staticmethod(FindNextFile)
    clazz.FindFirstStream0 = staticmethod(FindFirstStream0)
    clazz.FindNextStream = staticmethod(FindNextStream)
    clazz.FindClose = staticmethod(FindClose)
    clazz.GetFileInformationByHandle = staticmethod(GetFileInformationByHandle)
    clazz.CopyFileEx0 = staticmethod(CopyFileEx0)
    clazz.MoveFileEx0 = staticmethod(MoveFileEx0)
    clazz.GetFileAttributes0 = staticmethod(GetFileAttributes0)
    clazz.SetFileAttributes0 = staticmethod(SetFileAttributes0)
    clazz.GetFileAttributesEx0 = staticmethod(GetFileAttributesEx0)
    clazz.SetFileTime = staticmethod(SetFileTime)
    clazz.SetEndOfFile = staticmethod(SetEndOfFile)
    clazz.GetLogicalDrives = staticmethod(GetLogicalDrives)
    clazz.GetVolumeInformation0 = staticmethod(GetVolumeInformation0)
    clazz.GetDriveType0 = staticmethod(GetDriveType0)
    clazz.GetDiskFreeSpaceEx0 = staticmethod(GetDiskFreeSpaceEx0)
    clazz.GetVolumePathName0 = staticmethod(GetVolumePathName0)
    clazz.InitializeSecurityDescriptor = staticmethod(InitializeSecurityDescriptor)
    clazz.InitializeAcl = staticmethod(InitializeAcl)
    clazz.GetFileSecurity0 = staticmethod(GetFileSecurity0)
    clazz.SetFileSecurity0 = staticmethod(SetFileSecurity0)
    clazz.GetSecurityDescriptorOwner = staticmethod(GetSecurityDescriptorOwner)
    clazz.SetSecurityDescriptorOwner = staticmethod(SetSecurityDescriptorOwner)
    clazz.GetSecurityDescriptorDacl = staticmethod(GetSecurityDescriptorDacl)
    clazz.SetSecurityDescriptorDacl = staticmethod(SetSecurityDescriptorDacl)
    clazz.GetAclInformation0 = staticmethod(GetAclInformation0)
    clazz.GetAce = staticmethod(GetAce)
    clazz.AddAccessAllowedAceEx = staticmethod(AddAccessAllowedAceEx)
    clazz.AddAccessDeniedAceEx = staticmethod(AddAccessDeniedAceEx)
    clazz.LookupAccountSid0 = staticmethod(LookupAccountSid0)
    clazz.LookupAccountName0 = staticmethod(LookupAccountName0)
    clazz.GetLengthSid = staticmethod(GetLengthSid)
    clazz.ConvertSidToStringSid = staticmethod(ConvertSidToStringSid)
    clazz.ConvertStringSidToSid0 = staticmethod(ConvertStringSidToSid0)
    clazz.GetCurrentProcess = staticmethod(GetCurrentProcess)
    clazz.GetCurrentThread = staticmethod(GetCurrentThread)
    clazz.OpenProcessToken = staticmethod(OpenProcessToken)
    clazz.OpenThreadToken = staticmethod(OpenThreadToken)
    clazz.DuplicateTokenEx = staticmethod(DuplicateTokenEx)
    clazz.SetThreadToken = staticmethod(SetThreadToken)
    clazz.GetTokenInformation = staticmethod(GetTokenInformation)
    clazz.AdjustTokenPrivileges = staticmethod(AdjustTokenPrivileges)
    clazz.AccessCheck = staticmethod(AccessCheck)
    clazz.LookupPrivilegeValue0 = staticmethod(LookupPrivilegeValue0)
    clazz.CreateSymbolicLink0 = staticmethod(CreateSymbolicLink0)
    clazz.CreateHardLink0 = staticmethod(CreateHardLink0)
    clazz.GetFullPathName0 = staticmethod(GetFullPathName0)
    clazz.GetFinalPathNameByHandle = staticmethod(GetFinalPathNameByHandle)
    clazz.FormatMessage = staticmethod(FormatMessage)
    clazz.LocalFree = staticmethod(LocalFree)
    clazz.CreateIoCompletionPort = staticmethod(CreateIoCompletionPort)
    clazz.GetQueuedCompletionStatus0 = staticmethod(GetQueuedCompletionStatus0)
    clazz.PostQueuedCompletionStatus = staticmethod(PostQueuedCompletionStatus)
    clazz.ReadDirectoryChangesW = staticmethod(ReadDirectoryChangesW)
    clazz.CancelIo = staticmethod(CancelIo)
    clazz.GetOverlappedResult = staticmethod(GetOverlappedResult)
    clazz.BackupRead0 = staticmethod(BackupRead0)
    clazz.BackupSeek = staticmethod(BackupSeek)
    clazz.initIDs = staticmethod(initIDs)

