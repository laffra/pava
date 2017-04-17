def add_native_methods(clazz):
    def CreateEvent__boolean__boolean__(a0, a1):
        raise NotImplementedError()

    def CloseHandle__long__(a0):
        raise NotImplementedError()

    def DeviceIoControlSetSparse__long__(a0):
        raise NotImplementedError()

    def DeviceIoControlGetReparsePoint__long__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def FindNextFile__long__long__(a0, a1):
        raise NotImplementedError()

    def FindNextStream__long__(a0):
        raise NotImplementedError()

    def FindClose__long__(a0):
        raise NotImplementedError()

    def GetFileInformationByHandle__long__long__(a0, a1):
        raise NotImplementedError()

    def SetFileTime__long__long__long__long__(a0, a1, a2, a3):
        raise NotImplementedError()

    def SetEndOfFile__long__(a0):
        raise NotImplementedError()

    def GetLogicalDrives____():
        raise NotImplementedError()

    def InitializeSecurityDescriptor__long__(a0):
        raise NotImplementedError()

    def InitializeAcl__long__int__(a0, a1):
        raise NotImplementedError()

    def SetFileSecurity0__long__int__long__(a0, a1, a2):
        raise NotImplementedError()

    def GetSecurityDescriptorOwner__long__(a0):
        raise NotImplementedError()

    def SetSecurityDescriptorOwner__long__long__(a0, a1):
        raise NotImplementedError()

    def GetSecurityDescriptorDacl__long__(a0):
        raise NotImplementedError()

    def SetSecurityDescriptorDacl__long__long__(a0, a1):
        raise NotImplementedError()

    def GetAce__long__int__(a0, a1):
        raise NotImplementedError()

    def AddAccessAllowedAceEx__long__int__int__long__(a0, a1, a2, a3):
        raise NotImplementedError()

    def AddAccessDeniedAceEx__long__int__int__long__(a0, a1, a2, a3):
        raise NotImplementedError()

    def GetLengthSid__long__(a0):
        raise NotImplementedError()

    def ConvertSidToStringSid__long__(a0):
        raise NotImplementedError()

    def GetCurrentProcess____():
        raise NotImplementedError()

    def GetCurrentThread____():
        raise NotImplementedError()

    def OpenProcessToken__long__int__(a0, a1):
        raise NotImplementedError()

    def OpenThreadToken__long__int__boolean__(a0, a1, a2):
        raise NotImplementedError()

    def DuplicateTokenEx__long__int__(a0, a1):
        raise NotImplementedError()

    def SetThreadToken__long__long__(a0, a1):
        raise NotImplementedError()

    def GetTokenInformation__long__int__long__int__(a0, a1, a2, a3):
        raise NotImplementedError()

    def AdjustTokenPrivileges__long__long__int__(a0, a1, a2):
        raise NotImplementedError()

    def AccessCheck__long__long__int__int__int__int__int__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def GetFinalPathNameByHandle__long__(a0):
        raise NotImplementedError()

    def FormatMessage__int__(a0):
        raise NotImplementedError()

    def LocalFree__long__(a0):
        raise NotImplementedError()

    def CreateIoCompletionPort__long__long__long__(a0, a1, a2):
        raise NotImplementedError()

    def PostQueuedCompletionStatus__long__long__(a0, a1):
        raise NotImplementedError()

    def ReadDirectoryChangesW__long__long__int__boolean__int__long__long__(a0, a1, a2, a3, a4, a5, a6):
        raise NotImplementedError()

    def CancelIo__long__(a0):
        raise NotImplementedError()

    def GetOverlappedResult__long__long__(a0, a1):
        raise NotImplementedError()

    def BackupSeek__long__long__long__(a0, a1, a2):
        raise NotImplementedError()

    clazz.CreateEvent__boolean__boolean__ = staticmethod(CreateEvent__boolean__boolean__)
    clazz.CloseHandle__long__ = staticmethod(CloseHandle__long__)
    clazz.DeviceIoControlSetSparse__long__ = staticmethod(DeviceIoControlSetSparse__long__)
    clazz.DeviceIoControlGetReparsePoint__long__long__int__ = staticmethod(DeviceIoControlGetReparsePoint__long__long__int__)
    clazz.FindNextFile__long__long__ = staticmethod(FindNextFile__long__long__)
    clazz.FindNextStream__long__ = staticmethod(FindNextStream__long__)
    clazz.FindClose__long__ = staticmethod(FindClose__long__)
    clazz.GetFileInformationByHandle__long__long__ = staticmethod(GetFileInformationByHandle__long__long__)
    clazz.SetFileTime__long__long__long__long__ = staticmethod(SetFileTime__long__long__long__long__)
    clazz.SetEndOfFile__long__ = staticmethod(SetEndOfFile__long__)
    clazz.GetLogicalDrives____ = staticmethod(GetLogicalDrives____)
    clazz.InitializeSecurityDescriptor__long__ = staticmethod(InitializeSecurityDescriptor__long__)
    clazz.InitializeAcl__long__int__ = staticmethod(InitializeAcl__long__int__)
    clazz.SetFileSecurity0__long__int__long__ = staticmethod(SetFileSecurity0__long__int__long__)
    clazz.GetSecurityDescriptorOwner__long__ = staticmethod(GetSecurityDescriptorOwner__long__)
    clazz.SetSecurityDescriptorOwner__long__long__ = staticmethod(SetSecurityDescriptorOwner__long__long__)
    clazz.GetSecurityDescriptorDacl__long__ = staticmethod(GetSecurityDescriptorDacl__long__)
    clazz.SetSecurityDescriptorDacl__long__long__ = staticmethod(SetSecurityDescriptorDacl__long__long__)
    clazz.GetAce__long__int__ = staticmethod(GetAce__long__int__)
    clazz.AddAccessAllowedAceEx__long__int__int__long__ = staticmethod(AddAccessAllowedAceEx__long__int__int__long__)
    clazz.AddAccessDeniedAceEx__long__int__int__long__ = staticmethod(AddAccessDeniedAceEx__long__int__int__long__)
    clazz.GetLengthSid__long__ = staticmethod(GetLengthSid__long__)
    clazz.ConvertSidToStringSid__long__ = staticmethod(ConvertSidToStringSid__long__)
    clazz.GetCurrentProcess____ = staticmethod(GetCurrentProcess____)
    clazz.GetCurrentThread____ = staticmethod(GetCurrentThread____)
    clazz.OpenProcessToken__long__int__ = staticmethod(OpenProcessToken__long__int__)
    clazz.OpenThreadToken__long__int__boolean__ = staticmethod(OpenThreadToken__long__int__boolean__)
    clazz.DuplicateTokenEx__long__int__ = staticmethod(DuplicateTokenEx__long__int__)
    clazz.SetThreadToken__long__long__ = staticmethod(SetThreadToken__long__long__)
    clazz.GetTokenInformation__long__int__long__int__ = staticmethod(GetTokenInformation__long__int__long__int__)
    clazz.AdjustTokenPrivileges__long__long__int__ = staticmethod(AdjustTokenPrivileges__long__long__int__)
    clazz.AccessCheck__long__long__int__int__int__int__int__ = staticmethod(AccessCheck__long__long__int__int__int__int__int__)
    clazz.GetFinalPathNameByHandle__long__ = staticmethod(GetFinalPathNameByHandle__long__)
    clazz.FormatMessage__int__ = staticmethod(FormatMessage__int__)
    clazz.LocalFree__long__ = staticmethod(LocalFree__long__)
    clazz.CreateIoCompletionPort__long__long__long__ = staticmethod(CreateIoCompletionPort__long__long__long__)
    clazz.PostQueuedCompletionStatus__long__long__ = staticmethod(PostQueuedCompletionStatus__long__long__)
    clazz.ReadDirectoryChangesW__long__long__int__boolean__int__long__long__ = staticmethod(ReadDirectoryChangesW__long__long__int__boolean__int__long__long__)
    clazz.CancelIo__long__ = staticmethod(CancelIo__long__)
    clazz.GetOverlappedResult__long__long__ = staticmethod(GetOverlappedResult__long__long__)
    clazz.BackupSeek__long__long__long__ = staticmethod(BackupSeek__long__long__long__)

