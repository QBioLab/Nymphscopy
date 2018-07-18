import ctypes

def PIGCS(dll):
	
	# DLL initialization and comm functions
	# int	PI_FUNC_DECL	PI_InterfaceSetupDlg(const char* szRegKeyName);
	dll.PI_InterfaceSetupDlg.argtypes = [ctypes.c_char_p]
	dll.PI_InterfaceSetupDlg.restype = ctypes.c_int
	# int 	PI_FUNC_DECL	PI_ConnectRS232(int nPortNr, int iBaudRate);
	dll.PI_ConnectRS232.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_ConnectRS232.restype = ctypes.c_int
	# int PI_FUNC_DECL PI_TryConnectRS232(int port, int baudrate);
	dll.PI_TryConnectRS232.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_TryConnectRS232.restype = ctypes.c_int
	# int PI_FUNC_DECL PI_TryConnectUSB(const char* szDescription);
	dll.PI_TryConnectUSB.argtypes = [ctypes.c_char_p]
	dll.PI_TryConnectUSB.restype = ctypes.c_int
	# BOOL PI_FUNC_DECL PI_IsConnecting(int threadID, BOOL* bCOnnecting);
	dll.PI_IsConnecting.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_IsConnecting.restype = ctypes.c_bool
	# int PI_FUNC_DECL PI_GetControllerID(int threadID);
	dll.PI_GetControllerID.argtypes = [ctypes.c_int]
	dll.PI_GetControllerID.restype = ctypes.c_int
	# BOOL PI_FUNC_DECL PI_CancelConnect(int threadI);
	dll.PI_CancelConnect.argtypes = [ctypes.c_int]
	dll.PI_CancelConnect.restype = ctypes.c_bool
	# int 	PI_FUNC_DECL	PI_ConnectRS232ByDevName(const char* szDevName, int BaudRate); This syntax does not exist, while PI_ConnectRS232details could be found
	# dll.PI_ConnectRS232ByDevName.argtypes = [ctypes.c_char_p, ctypes.c_int]
	# dll.PI_ConnectRS232ByDevName.restype = ctypes.c_int
	# int 	PI_FUNC_DECL	PI_OpenRS232DaisyChain(int iPortNumber, int iBaudRate, int* pNumberOfConnectedDaisyChainDevices, char* szDeviceIDNs, int iBufferSize);
	dll.PI_OpenRS232DaisyChain.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
	dll.PI_OpenRS232DaisyChain.restype = ctypes.c_int
	# int 	PI_FUNC_DECL	PI_ConnectDaisyChainDevice(int iPortId, int iDeviceNumber);
	dll.PI_ConnectDaisyChainDevice.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_ConnectDaisyChainDevice.restype = ctypes.c_int
	# void 	PI_FUNC_DECL	PI_CloseDaisyChain(int iPortId);
	dll.PI_CloseDaisyChain.argtypes = [ctypes.c_int]
	dll.PI_CloseDaisyChain.restype = None
	# int	    PI_FUNC_DECL	PI_ConnectNIgpib(int nBoard, int nDevAddr);
	dll.PI_ConnectNIgpib.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_ConnectNIgpib.restype = ctypes.c_int
	# int	    PI_FUNC_DECL	PI_ConnectTCPIP(const char* szHostname, int port);
	dll.PI_ConnectTCPIP.argtypes = [ctypes.c_char_p, ctypes.c_int]
	dll.PI_ConnectTCPIP.restype = ctypes.c_int
	# int	    PI_FUNC_DECL	PI_EnableTCPIPScan(int iMask);
	dll.PI_EnableTCPIPScan.argtypes = [ctypes.c_int]
	dll.PI_EnableTCPIPScan.restype = ctypes.c_int
	# int	    PI_FUNC_DECL	PI_EnumerateTCPIPDevices(char* szBuffer, int iBufferSize, const char* szFilter);
	dll.PI_EnumerateTCPIPDevices.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p]
	dll.PI_EnumerateTCPIPDevices.restype = ctypes.c_int
	# int	    PI_FUNC_DECL	PI_ConnectTCPIPByDescription(const char* szDescription);
	dll.PI_ConnectTCPIPByDescription.argtypes = [ctypes.c_char_p]
	dll.PI_ConnectTCPIPByDescription.restype = ctypes.c_int
	# int 	PI_FUNC_DECL	PI_OpenTCPIPDaisyChain(const char* szHostname, int port, int* pNumberOfConnectedDaisyChainDevices, char* szDeviceIDNs, int iBufferSize);
	dll.PI_OpenTCPIPDaisyChain.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
	dll.PI_OpenTCPIPDaisyChain.restype = ctypes.c_int
	# int	    PI_FUNC_DECL	PI_EnumerateUSB(char* szBuffer, int iBufferSize, const char* szFilter);
	dll.PI_EnumerateUSB.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p]
	dll.PI_EnumerateUSB.restype = ctypes.c_int
	# int	    PI_FUNC_DECL	PI_ConnectUSB(const char* szDescription);
	dll.PI_ConnectUSB.argtypes = [ctypes.c_char_p]
	dll.PI_ConnectUSB.restype = ctypes.c_int
	# int	    PI_FUNC_DECL	PI_ConnectUSBWithBaudRate(const char* szDescription,int iBaudRate);
	dll.PI_ConnectUSBWithBaudRate.argtypes = [ctypes.c_char_p, ctypes.c_int]
	dll.PI_ConnectUSBWithBaudRate.restype = ctypes.c_int
	# int 	PI_FUNC_DECL	PI_OpenUSBDaisyChain(const char* szDescription, int* pNumberOfConnectedDaisyChainDevices, char* szDeviceIDNs, int iBufferSize);
	dll.PI_OpenUSBDaisyChain.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
	dll.PI_OpenUSBDaisyChain.restype = ctypes.c_int
	# BOOL	PI_FUNC_DECL	PI_IsConnected(int ID);
	dll.PI_IsConnected.argtypes = [ctypes.c_int]
	dll.PI_IsConnected.restype = ctypes.c_bool
	# void	PI_FUNC_DECL	PI_CloseConnection(int ID);
	dll.PI_CloseConnection.argtypes = [ctypes.c_int]
	dll.PI_CloseConnection.restype = None
	# int	    PI_FUNC_DECL	PI_GetError(int ID);
	dll.PI_GetError.argtypes = [ctypes.c_int]
	dll.PI_GetError.restype = ctypes.c_int
	# BOOL	PI_FUNC_DECL	PI_SetErrorCheck(int ID, BOOL bErrorCheck);
	dll.PI_SetErrorCheck.argtypes = [ctypes.c_int, ctypes.c_bool]
	dll.PI_SetErrorCheck.restype = ctypes.c_bool
	# BOOL	PI_FUNC_DECL	PI_TranslateError(int errNr, char* szBuffer, int iBufferSize);
	dll.PI_TranslateError.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_TranslateError.restype = ctypes.c_bool
	# int	    PI_FUNC_DECL	PI_SetTimeout(int ID, int timeoutInMS);
	dll.PI_SetTimeout.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_SetTimeout.restype = ctypes.c_int
	# int		PI_FUNC_DECL	PI_SetDaisyChainScanMaxDeviceID(int maxID);
	dll.PI_SetDaisyChainScanMaxDeviceID.argtypes = [ctypes.c_int]
	dll.PI_SetDaisyChainScanMaxDeviceID.restype = ctypes.c_int
	# BOOL	PI_FUNC_DECL	PI_EnableReconnect(int ID, BOOL bEnable);
	dll.PI_EnableReconnect.argtypes = [ctypes.c_int, ctypes.c_bool]
	dll.PI_EnableReconnect.restype = ctypes.c_bool
	# int     PI_FUNC_DECL    PI_SetNrTimeoutsBeforeClose(int ID, int nrTimeoutsBeforeClose);
	dll.PI_SetNrTimeoutsBeforeClose.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_SetNrTimeoutsBeforeClose.restype = ctypes.c_int
	# BOOL    PI_FUNC_DECL    PI_GetInterfaceDescription(int ID, char* szBuffer, int iBufferSize);
	dll.PI_GetInterfaceDescription.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_GetInterfaceDescription.restype = ctypes.c_bool
	
	# general
	# BOOL PI_FUNC_DECL PI_qERR(int ID, int* pnError);
	dll.PI_qERR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qERR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qIDN(int ID, char* szBuffer, int iBufferSize);
	dll.PI_qIDN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qIDN.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_INI(int ID, const char* szAxes);
	dll.PI_INI.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_INI.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHLP(int ID, char* szBuffer, int iBufferSize);
	dll.PI_qHLP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qHLP.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHPA(int ID, char* szBuffer, int iBufferSize);
	dll.PI_qHPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qHPA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHPV(int ID, char* szBuffer, int iBufferSize);
	dll.PI_qHPV.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qHPV.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qCSV(int ID, double* pdCommandSyntaxVersion);
	dll.PI_qCSV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qCSV.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qOVF(int ID, const char* szAxes, BOOL* piValueArray);
	dll.PI_qOVF.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qOVF.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_RBT(int ID);
	dll.PI_RBT.argtypes = [ctypes.c_int]
	dll.PI_RBT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_REP(int ID);
	dll.PI_REP.argtypes = [ctypes.c_int]
	dll.PI_REP.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_BDR(int ID, int iBaudRate);
	dll.PI_BDR.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_BDR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qBDR(int ID, int* iBaudRate);
	dll.PI_qBDR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qBDR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DBR(int ID, int iBaudRate);
	dll.PI_DBR.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_DBR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDBR(int ID, int* iBaudRate);
	dll.PI_qDBR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qDBR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qVER(int ID, char* szBuffer, int iBufferSize);
	dll.PI_qVER.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qVER.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSSN(int ID, char* szSerialNumber, int iBufferSize);
	dll.PI_qSSN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qSSN.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_CCT(int ID, int iCommandType);
	dll.PI_CCT.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_CCT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qCCT(int ID, int *iCommandType);
	dll.PI_qCCT.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_qCCT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTVI(int ID, char* szBuffer, int iBufferSize);
	dll.PI_qTVI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qTVI.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_IFC(int ID, const char* szParameters, const char* szValues);
	dll.PI_IFC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
	dll.PI_IFC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qIFC(int ID, const char* szParameters, char* szBuffer, int iBufferSize);
	dll.PI_qIFC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qIFC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_IFS(int ID, const char* szPassword, const char* szParameters, const char* szValues);
	dll.PI_IFS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
	dll.PI_IFS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qIFS(int ID, const char* szParameters, char* szBuffer, int iBufferSize);
	dll.PI_qIFS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qIFS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qECO(int ID, const char* szSendString, char* szValues, int iBufferSize);
	dll.PI_qECO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qECO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MOV(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_MOV.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_MOV.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qMOV(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qMOV.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qMOV.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MVR(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_MVR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_MVR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MVE(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_MVE.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_MVE.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_POS(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_POS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_POS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qPOS(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qPOS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qPOS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_IsMoving(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_IsMoving.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_IsMoving.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_HLT(int ID, const char* szAxes);
	dll.PI_HLT.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_HLT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_STP(int ID);
	dll.PI_STP.argtypes = [ctypes.c_int]
	dll.PI_STP.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_StopAll(int ID);
	dll.PI_StopAll.argtypes = [ctypes.c_int]
	dll.PI_StopAll.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qONT(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qONT.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qONT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_RTO(int ID, const char* szAxes);
	dll.PI_RTO.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_RTO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qRTO(int ID, const char* szAxes, int* piValueArray);
	dll.PI_qRTO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qRTO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_ATZ(int ID, const char* szAxes, const double* pdLowvoltageArray, const BOOL* pfUseDefaultArray);
	dll.PI_ATZ.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_bool)]
	dll.PI_ATZ.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qATZ(int ID, const char* szAxes, int* piAtzResultArray);
	dll.PI_qATZ.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qATZ.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_AOS(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_AOS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_AOS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qAOS(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qAOS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qAOS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_HasPosChanged(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_HasPosChanged.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_HasPosChanged.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_GetErrorStatus(int ID, BOOL* pbIsReferencedArray, BOOL* pbIsReferencing, BOOL* pbIsMovingArray, BOOL* pbIsMotionErrorArray);
	dll.PI_GetErrorStatus.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool)]
	dll.PI_GetErrorStatus.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SVA(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_SVA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_SVA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSVA(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qSVA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qSVA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SVR(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_SVR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_SVR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DFH(int ID, const char* szAxes);
	dll.PI_DFH.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_DFH.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDFH(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qDFH.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qDFH.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_GOH(int ID, const char* szAxes);
	dll.PI_GOH.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_GOH.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qCST(int ID, const char* szAxes, char* szNames, int iBufferSize);
	dll.PI_qCST.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qCST.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_CST(int ID, const char* szAxes, const char* szNames);
	dll.PI_CST.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
	dll.PI_CST.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qVST(int ID, char* szBuffer, int iBufferSize);
	dll.PI_qVST.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qVST.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qPUN(int ID, const char* szAxes, char* szUnit, int iBufferSize);
	dll.PI_qPUN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qPUN.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SVO(int ID, const char* szAxes, const BOOL* pbValueArray);
	dll.PI_SVO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_SVO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSVO(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qSVO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qSVO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SMO( int ID, const char*  szAxes, const int* piValueArray);
	dll.PI_SMO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
	dll.PI_SMO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSMO(int ID, const char* szAxes, int* piValueArray);
	dll.PI_qSMO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qSMO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DCO(int ID, const char* szAxes, const BOOL* pbValueArray);
	dll.PI_DCO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_DCO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDCO(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qDCO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qDCO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_BRA(int ID, const char* szAxes, const BOOL* pbValueArray);
	dll.PI_BRA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_BRA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qBRA(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qBRA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qBRA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_RON(int ID, const char* szAxes, const BOOL* pbValueArray);
	dll.PI_RON.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_RON.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qRON(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qRON.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qRON.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_VEL(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_VEL.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_VEL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qVEL(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qVEL.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qVEL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_JOG(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_JOG.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_JOG.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qJOG(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qJOG.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qJOG.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTCV(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qTCV.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qTCV.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_VLS(int ID, double dSystemVelocity);
	dll.PI_VLS.argtypes = [ctypes.c_int, ctypes.c_double]
	dll.PI_VLS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qVLS(int ID, double* pdSystemVelocity);
	dll.PI_qVLS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qVLS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_ACC(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_ACC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_ACC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qACC(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qACC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qACC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DEC(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_DEC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_DEC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDEC(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qDEC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qDEC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_VCO(int ID, const char* szAxes, const BOOL* pbValueArray);
	dll.PI_VCO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_VCO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qVCO(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qVCO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qVCO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SPA(int ID, const char* szAxes, const unsigned int* iParameterArray, const double* pdValueArray, const char* szStrings);
	dll.PI_SPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_double), ctypes.c_char_p]
	dll.PI_SPA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSPA(int ID, const char* szAxes, unsigned int* iParameterArray, double* pdValueArray, char* szStrings, int iMaxNameSize);
	dll.PI_qSPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_double), ctypes.c_char_p, ctypes.c_int]
	dll.PI_qSPA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SEP(int ID, const char* szPassword, const char* szAxes, const unsigned int* iParameterArray, const double* pdValueArray, const char* szStrings);
	dll.PI_SEP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_double), ctypes.c_char_p]
	dll.PI_SEP.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSEP(int ID, const char* szAxes, unsigned int* iParameterArray, double* pdValueArray, char* szStrings, int iMaxNameSize);
	dll.PI_qSEP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_double), ctypes.c_char_p, ctypes.c_int]
	dll.PI_qSEP.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WPA(int ID, const char* szPassword, const char* szAxes, const unsigned int* iParameterArray);
	dll.PI_WPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint)]
	dll.PI_WPA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DPA(int ID, const char* szPassword, const char* szAxes, const unsigned int* iParameterArray);
	dll.PI_DPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint)]
	dll.PI_DPA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_TIM(int ID, double dTimer);
	dll.PI_TIM.argtypes = [ctypes.c_int, ctypes.c_double]
	dll.PI_TIM.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTIM(int ID, double* pdTimer);
	dll.PI_qTIM.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qTIM.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_RPA(int ID, const char* szAxes, const unsigned int* iParameterArray);
	dll.PI_RPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint)]
	dll.PI_RPA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SPA_String(int ID, const char* szAxes, const unsigned int* iParameterArray, const char* szStrings);
	dll.PI_SPA_String.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p]
	dll.PI_SPA_String.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSPA_String(int ID, const char* szAxes, const unsigned int* iParameterArray, char* szStrings, int iMaxNameSize);
	dll.PI_qSPA_String.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p, ctypes.c_int]
	dll.PI_qSPA_String.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SEP_String(int ID, const char* szPassword, const char* szAxes, const unsigned int* iParameterArray, const char* szStrings);
	dll.PI_SEP_String.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p]
	dll.PI_SEP_String.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSEP_String(int ID, const char* szAxes, unsigned int* iParameterArray, char* szStrings, int iMaxNameSize);
	dll.PI_qSEP_String.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p, ctypes.c_int]
	dll.PI_qSEP_String.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SPA_int64(int ID, const char* szAxes, const unsigned int* iParameterArray, const __int64* piValueArray);
	dll.PI_SPA_int64.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_longlong)]
	dll.PI_SPA_int64.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSPA_int64(int ID, const char* szAxes, unsigned int* iParameterArray, __int64* piValueArray);
	dll.PI_qSPA_int64.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_longlong)]
	dll.PI_qSPA_int64.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SEP_int64(int ID, const char* szPassword, const char* szAxes, const unsigned int* iParameterArray, const __int64* piValueArray);
	dll.PI_SEP_int64.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_longlong)]
	dll.PI_SEP_int64.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSEP_int64(int ID, const char* szAxes, unsigned int* iParameterArray, __int64* piValueArray);
	dll.PI_qSEP_int64.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_longlong)]
	dll.PI_qSEP_int64.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_STE(int ID, const char* szAxes, const double* dOffsetArray);
	dll.PI_STE.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_STE.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSTE(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qSTE.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qSTE.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_IMP(int ID, const char*  szAxes, const double* pdImpulseSize);
	dll.PI_IMP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_IMP.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_IMP_PulseWidth(int ID, char cAxis, double dOffset, int iPulseWidth);
	dll.PI_IMP_PulseWidth.argtypes = [ctypes.c_int, ctypes.c_char, ctypes.c_double, ctypes.c_int]
	dll.PI_IMP_PulseWidth.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qIMP(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qIMP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qIMP.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SAI(int ID, const char* szOldAxes, const char* szNewAxes);
	dll.PI_SAI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
	dll.PI_SAI.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSAI(int ID, char* szAxes, int iBufferSize);
	dll.PI_qSAI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qSAI.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSAI_ALL(int ID, char* szAxes, int iBufferSize);
	dll.PI_qSAI_ALL.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qSAI_ALL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_CCL(int ID, int iComandLevel, const char* szPassWord);
	dll.PI_CCL.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
	dll.PI_CCL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qCCL(int ID, int* piComandLevel);
	dll.PI_qCCL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qCCL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_AVG(int ID, int iAverrageTime);
	dll.PI_AVG.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_AVG.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qAVG(int ID, int *iAverrageTime);
	dll.PI_qAVG.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_qAVG.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHAR(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qHAR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qHAR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qLIM(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qLIM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qLIM.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTRS(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qTRS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qTRS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_FNL(int ID, const char* szAxes);
	dll.PI_FNL.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_FNL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_FPL(int ID, const char* szAxes);
	dll.PI_FPL.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_FPL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_FRF(int ID, const char* szAxes);
	dll.PI_FRF.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_FRF.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_FED(int ID, const char* szAxes, const int* piEdgeArray, const int* piParamArray);
	dll.PI_FED.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
	dll.PI_FED.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qFRF(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qFRF.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qFRF.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DIO(int ID, const int* piChannelsArray, const BOOL* pbValueArray, int iArraySize);
	dll.PI_DIO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
	dll.PI_DIO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDIO(int ID, const int* piChannelsArray, BOOL* pbValueArray, int iArraySize);
	dll.PI_qDIO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
	dll.PI_qDIO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTIO(int ID, int* piInputNr, int* piOutputNr);
	dll.PI_qTIO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
	dll.PI_qTIO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_IsControllerReady(int ID, int* piControllerReady);
	dll.PI_IsControllerReady.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_IsControllerReady.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSRG(int ID, const char* szAxes, const int* iRegisterArray, int* iValArray);
	dll.PI_qSRG.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
	dll.PI_qSRG.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_ATC(int ID, const int* piChannels, const int* piValueArray, int iArraySize);
	dll.PI_ATC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_ATC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qATC(int ID, const int* piChannels, int* piValueArray, int iArraySize);
	dll.PI_qATC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qATC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qATS(int ID, const int* piChannels, const int* piOptions, int* piValueArray, int iArraySize);
	dll.PI_qATS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qATS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SPI(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_SPI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_SPI.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSPI(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qSPI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qSPI.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SCT(int ID, double dCycleTime);
	dll.PI_SCT.argtypes = [ctypes.c_int, ctypes.c_double]
	dll.PI_SCT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSCT(int ID, double* pdCycleTime);
	dll.PI_qSCT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qSCT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SST(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_SST.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_SST.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSST(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qSST.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qSST.restype = ctypes.c_bool
	
	# Macro commande
	# BOOL PI_FUNC_DECL PI_IsRunningMacro(int ID, BOOL* pbRunningMacro);
	dll.PI_IsRunningMacro.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_IsRunningMacro.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MAC_BEG(int ID, const char* szMacroName);
	dll.PI_MAC_BEG.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_MAC_BEG.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MAC_START(int ID, const char* szMacroName);
	dll.PI_MAC_START.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_MAC_START.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MAC_NSTART(int ID, const char* szMacroName, int nrRuns);
	dll.PI_MAC_NSTART.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_MAC_NSTART.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MAC_START_Args(int ID, const char* szMacroName, const char* szArgs);
	dll.PI_MAC_START_Args.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
	dll.PI_MAC_START_Args.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MAC_NSTART_Args(int ID, const char* szMacroName, int nrRuns, const char* szArgs);
	dll.PI_MAC_NSTART_Args.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p]
	dll.PI_MAC_NSTART_Args.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MAC_END(int ID);
	dll.PI_MAC_END.argtypes = [ctypes.c_int]
	dll.PI_MAC_END.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MAC_DEL(int ID, const char* szMacroName);
	dll.PI_MAC_DEL.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_MAC_DEL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MAC_DEF(int ID, const char* szMacroName);
	dll.PI_MAC_DEF.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_MAC_DEF.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MAC_qDEF(int ID, char* szBuffer, int iBufferSize);
	dll.PI_MAC_qDEF.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_MAC_qDEF.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MAC_qERR(int ID, char* szBuffer, int iBufferSize);
	dll.PI_MAC_qERR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_MAC_qERR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MAC_qFREE(int ID, int* iFreeSpace);
	dll.PI_MAC_qFREE.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_MAC_qFREE.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qMAC(int ID, const char* szMacroName, char* szBuffer, int iBufferSize);
	dll.PI_qMAC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qMAC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qRMC(int ID, char* szBuffer, int iBufferSize);
	dll.PI_qRMC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qRMC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DEL(int ID, int nMilliSeconds);
	dll.PI_DEL.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_DEL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WAC(int ID, const char* szCondition);
	dll.PI_WAC.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_WAC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MEX(int ID, const char* szCondition);
	dll.PI_MEX.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_MEX.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_VAR(int ID, const char* szVariable, const char* szValue);
	dll.PI_VAR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
	dll.PI_VAR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qVAR(int ID, const char* szVariables, char* szValues,  int iBufferSize);
	dll.PI_qVAR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qVAR.restype = ctypes.c_bool
	
	# String commands.
	# BOOL PI_FUNC_DECL PI_GcsCommandset(int ID, const char* szCommand);
	dll.PI_GcsCommandset.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_GcsCommandset.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_GcsGetAnswer(int ID, char* szAnswer, int iBufferSize);
	dll.PI_GcsGetAnswer.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_GcsGetAnswer.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_GcsGetAnswerSize(int ID, int* iAnswerSize);
	dll.PI_GcsGetAnswerSize.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_GcsGetAnswerSize.restype = ctypes.c_bool
	
	# limits
	# BOOL PI_FUNC_DECL PI_qTMN(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qTMN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qTMN.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTMX(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qTMX.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qTMX.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_NLM(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_NLM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_NLM.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qNLM(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qNLM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qNLM.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_PLM(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_PLM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_PLM.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qPLM(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qPLM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qPLM.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SSL(int ID, const char* szAxes, const BOOL* pbValueArray);
	dll.PI_SSL.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_SSL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSSL(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qSSL.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qSSL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qVMO(int ID, const char* szAxes, const double* pdValarray, BOOL* pbMovePossible);
	dll.PI_qVMO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qVMO.restype = ctypes.c_bool
	
	# Wave commands.
	# BOOL PI_FUNC_DECL PI_IsGeneratorRunning(int ID, const int* piWaveGeneratorIds, BOOL* pbValueArray, int iArraySize);
	dll.PI_IsGeneratorRunning.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
	dll.PI_IsGeneratorRunning.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTWG(int ID, int* piWaveGenerators);
	dll.PI_qTWG.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qTWG.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WAV_SIN_P(int ID, int iWaveTableId, int iOffsetOfFirstPointInWaveTable, int iNumberOfPoints, int iAddAppendWave, int iCenterPointOfWave, double dAmplitudeOfWave, double dOffsetOfWave, int iSegmentLength);
	dll.PI_WAV_SIN_P.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_int]
	dll.PI_WAV_SIN_P.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WAV_LIN(int ID, int iWaveTableId, int iOffsetOfFirstPointInWaveTable, int iNumberOfPoints, int iAddAppendWave, int iNumberOfSpeedUpDownPointsInWave, double dAmplitudeOfWave, double dOffsetOfWave, int iSegmentLength);
	dll.PI_WAV_LIN.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_int]
	dll.PI_WAV_LIN.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WAV_NOISE(int ID, int iWaveTableId, int iAddAppendWave, double dAmplitudeOfWave, double dOffsetOfWave,int iSegmentLength);   
	dll.PI_WAV_NOISE.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_int]
	dll.PI_WAV_NOISE.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WAV_RAMP(int ID, int iWaveTableId, int iOffsetOfFirstPointInWaveTable, int iNumberOfPoints, int iAddAppendWave, int iCenterPointOfWave, int iNumberOfSpeedUpDownPointsInWave, double dAmplitudeOfWave, double dOffsetOfWave, int iSegmentLength);
	dll.PI_WAV_RAMP.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_int]
	dll.PI_WAV_RAMP.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WAV_PNT(int ID, int iWaveTableId, int iOffsetOfFirstPointInWaveTable, int iNumberOfPoints, int iAddAppendWave, const double* pdWavePoints);
	dll.PI_WAV_PNT.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
	dll.PI_WAV_PNT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qWAV(int ID, const int* piWaveTableIdsArray, const int* piParamereIdsArray, double* pdValueArray, int iArraySize);
	dll.PI_qWAV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qWAV.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WGO(int ID, const int* piWaveGeneratorIdsArray, const int* iStartModArray, int iArraySize);
	dll.PI_WGO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_WGO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qWGO(int ID, const int* piWaveGeneratorIdsArray, int* piValueArray, int iArraySize);
	dll.PI_qWGO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qWGO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WGC(int ID, const int* piWaveGeneratorIdsArray, const int* piNumberOfCyclesArray, int iArraySize);
	dll.PI_WGC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_WGC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qWGC(int ID, const int* piWaveGeneratorIdsArray, int* piValueArray, int iArraySize);
	dll.PI_qWGC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qWGC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qWGI(int ID, const int* piWaveGeneratorIdsArray, int* piValueArray, int iArraySize);
	dll.PI_qWGI.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qWGI.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qWGN(int ID, const int* piWaveGeneratorIdsArray, int* piValueArray, int iArraySize);
	dll.PI_qWGN.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qWGN.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WSL(int ID, const int* piWaveGeneratorIdsArray, const int* piWaveTableIdsArray, int iArraySize);
	dll.PI_WSL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_WSL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qWSL(int ID, const int* piWaveGeneratorIdsArray, int* piWaveTableIdsArray, int iArraySize);
	dll.PI_qWSL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qWSL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DTC(int ID, const int* piDdlTableIdsArray, int iArraySize);
	dll.PI_DTC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_DTC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDTL(int ID, const int* piDdlTableIdsArray, int* piValueArray, int iArraySize);
	dll.PI_qDTL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qDTL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WCL(int ID, const int* piWaveTableIdsArray, int iArraySize);
	dll.PI_WCL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_WCL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTLT(int ID, int* piNumberOfDdlTables);
	dll.PI_qTLT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qTLT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qGWD_SYNC(int ID, int iWaveTableId, int iOffsetOfFirstPointInWaveTable, int iNumberOfValues, double* pdValueArray);
	dll.PI_qGWD_SYNC.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qGWD_SYNC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qGWD(int ID, const int* iWaveTableIdsArray, int iNumberOfWaveTables, int iOffset, int nrValues, double** pdValarray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
	dll.PI_qGWD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
	dll.PI_qGWD.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WOS(int ID, const int* iWaveTableIdsArray, const double* pdValueArray, int iArraySize);
	dll.PI_WOS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_WOS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qWOS(int ID, const int* iWaveTableIdsArray, double* pdValueArray, int iArraySize);
	dll.PI_qWOS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qWOS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WTR(int ID, const int* piWaveGeneratorIdsArray, const int* piTableRateArray, const int* piInterpolationTypeArray, int iArraySize);
	dll.PI_WTR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_WTR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qWTR(int ID, const int* piWaveGeneratorIdsArray, int* piTableRateArray, int* piInterpolationTypeArray, int iArraySize);
	dll.PI_qWTR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qWTR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DDL(int ID, int iDdlTableId,  int iOffsetOfFirstPointInDdlTable,  int iNumberOfValues, const double* pdValueArray);
	dll.PI_DDL.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
	dll.PI_DDL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDDL_SYNC(int ID,  int iDdlTableId,  int iOffsetOfFirstPointInDdlTable,  int iNumberOfValues, double* pdValueArray);
	dll.PI_qDDL_SYNC.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qDDL_SYNC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDDL(int ID, const int* iDdlTableIdsArray, int iNumberOfDdlTables, int iOffset, int nrValues, double** pdValarray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
	dll.PI_qDDL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
	dll.PI_qDDL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DPO(int ID, const char* szAxes);
	dll.PI_DPO.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_DPO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qWMS(int ID, const int* piWaveTableIds, int* iWaveTableMaximumSize, int iArraySize);
	dll.PI_qWMS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qWMS.restype = ctypes.c_bool
	
	# Trigger commands.
	# BOOL PI_FUNC_DECL PI_TWC(int ID);
	dll.PI_TWC.argtypes = [ctypes.c_int]
	dll.PI_TWC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_TWS(int ID, const int* piTriggerChannelIdsArray, const int* piPointNumberArray, const int* piSwitchArray, int iArraySize);
	dll.PI_TWS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_TWS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTWS(int ID, const int* iTriggerChannelIdsArray, int iNumberOfTriggerChannels, int iOffset, int nrValues, double** pdValarray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
	dll.PI_qTWS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
	dll.PI_qTWS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_CTO(int ID, const int* piTriggerOutputIdsArray, const int* piTriggerParameterArray, const double* pdValueArray, int iArraySize);
	dll.PI_CTO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_CTO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_CTOString(int ID, const int* piTriggerOutputIdsArray, const int* piTriggerParameterArray, const char* szValueArray, int iArraySize);
	dll.PI_CTOString.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
	dll.PI_CTOString.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qCTO(int ID, const int* piTriggerOutputIdsArray, const int* piTriggerParameterArray, double* pdValueArray, int iArraySize);
	dll.PI_qCTO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qCTO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qCTOString(int ID, const int* piTriggerOutputIdsArray, const int* piTriggerParameterArray, char* szValueArray, int iArraySize, int maxBufLen);
	dll.PI_qCTOString.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
	dll.PI_qCTOString.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_TRO(int ID, const int* piTriggerChannelIds, const BOOL* pbTriggerChannelEnabel, int iArraySize);
	dll.PI_TRO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
	dll.PI_TRO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTRO(int ID, const int* piTriggerChannelIds, BOOL* pbTriggerChannelEnabel, int iArraySize);
	dll.PI_qTRO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
	dll.PI_qTRO.restype = ctypes.c_bool
	
	# Record tabel commands.
	# BOOL PI_FUNC_DECL PI_qHDR(int ID, char* szBuffer, int iBufferSize);
	dll.PI_qHDR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qHDR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTNR(int ID, int* piNumberOfRecordCannels);
	dll.PI_qTNR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qTNR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DRC(int ID, const int* piRecordTableIdsArray, const char* szRecordSourceIds, const int* piRecordOptionArray);
	dll.PI_DRC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
	dll.PI_DRC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDRC(int ID, const int* piRecordTableIdsArray, char* szRecordSourceIds, int* piRecordOptionArray, int iRecordSourceIdsBufferSize, int iRecordOptionArraySize);
	dll.PI_qDRC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
	dll.PI_qDRC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDRR_SYNC(int ID,  int iRecordTablelId,  int iOffsetOfFirstPointInRecordTable,  int iNumberOfValues, double* pdValueArray);
	dll.PI_qDRR_SYNC.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qDRR_SYNC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDRR(int ID, const int* piRecTableIdIdsArray,  int iNumberOfRecChannels,  int iOffsetOfFirstPointInRecordTable,  int iNumberOfValues, double** pdValueArray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
	dll.PI_qDRR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
	dll.PI_qDRR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_DRT(int ID, const int* piRecordChannelIdsArray, const int* piTriggerSourceArray, const char* szValues, int iArraySize);
	dll.PI_DRT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
	dll.PI_DRT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDRT(int ID, const int* piRecordChannelIdsArray, int* piTriggerSourceArray, char* szValues, int iArraySize, int iValueBufferLength);
	dll.PI_qDRT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
	dll.PI_qDRT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_RTR(int ID, int piReportTableRate);
	dll.PI_RTR.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_RTR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qRTR(int ID, int* piReportTableRate);
	dll.PI_qRTR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qRTR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_WGR(int ID);
	dll.PI_WGR.argtypes = [ctypes.c_int]
	dll.PI_WGR.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDRL(int ID, const int* piRecordChannelIdsArray, int* piNuberOfRecordedValuesArray, int iArraySize);
	dll.PI_qDRL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qDRL.restype = ctypes.c_bool
	
	# Piezo-Channel commands.
	# BOOL PI_FUNC_DECL PI_VMA(int ID, const int* piPiezoChannelsArray, const double* pdValueArray, int iArraySize);
	dll.PI_VMA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_VMA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qVMA(int ID, const int* piPiezoChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qVMA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qVMA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_VMI(int ID, const int* piPiezoChannelsArray, const double* pdValueArray, int iArraySize);
	dll.PI_VMI.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_VMI.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qVMI(int ID, const int* piPiezoChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qVMI.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qVMI.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_VOL(int ID, const int* piPiezoChannelsArray, const double* pdValueArray, int iArraySize);
	dll.PI_VOL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_VOL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qVOL(int ID, const int* piPiezoChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qVOL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qVOL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTPC(int ID, int* piNumberOfPiezoChannels);
	dll.PI_qTPC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qTPC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_ONL(int ID, const int* iPiezoCannels, const int* piValueArray, int iArraySize);
	dll.PI_ONL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_ONL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qONL(int ID, const int* iPiezoCannels, int* piValueArray, int iArraySize);
	dll.PI_qONL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qONL.restype = ctypes.c_bool
	
	# Sensor-Channel commands.
	# BOOL PI_FUNC_DECL PI_qTAD(int ID, const int* piSensorsChannelsArray, int* piValueArray, int iArraySize);
	dll.PI_qTAD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qTAD.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTNS(int ID, const int* piSensorsChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qTNS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qTNS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTSP(int ID, const int* piSensorsChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qTSP.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qTSP.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SCN(int ID, const int* piSensorsChannelsArray, const int* piValueArray, int iArraySize);
	dll.PI_SCN.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_SCN.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSCN(int ID, const int* piSensorsChannelsArray, int* piValueArray, int iArraySize);
	dll.PI_qSCN.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qSCN.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTSC(int ID, int* piNumberOfSensorChannels);
	dll.PI_qTSC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qTSC.restype = ctypes.c_bool
	
	# PIEZOWALK(R)-Channel commands.
	# BOOL PI_FUNC_DECL PI_APG(int ID, const int* piPIEZOWALKChannelsArray, int iArraySize);
	dll.PI_APG.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_APG.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qAPG(int ID, const int* piPIEZOWALKChannelsArray, int* piValueArray, int iArraySize);
	dll.PI_qAPG.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qAPG.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_OAC(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
	dll.PI_OAC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_OAC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qOAC(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qOAC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qOAC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_OAD(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
	dll.PI_OAD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_OAD.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qOAD(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qOAD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qOAD.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_ODC(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
	dll.PI_ODC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_ODC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qODC(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qODC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qODC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_OCD(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
	dll.PI_OCD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_OCD.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qOCD(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qOCD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qOCD.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_OSM(int ID, const int* piPIEZOWALKChannelsArray, const int* piValueArray, int iArraySize);
	dll.PI_OSM.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_OSM.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qOSM(int ID, const int* piPIEZOWALKChannelsArray, int* piValueArray, int iArraySize);
	dll.PI_qOSM.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qOSM.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_OSMf(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
	dll.PI_OSMf.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_OSMf.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qOSMf(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qOSMf.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qOSMf.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_OVL(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
	dll.PI_OVL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_OVL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qOVL(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qOVL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qOVL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qOSN(int ID, const int* piPIEZOWALKChannelsArray, int* piValueArray, int iArraySize);
	dll.PI_qOSN.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qOSN.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_SSA(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
	dll.PI_SSA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_SSA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSSA(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qSSA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qSSA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_RNP(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
	dll.PI_RNP.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_RNP.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_PGS(int ID, const int* piPIEZOWALKChannelsArray, int iArraySize);
	dll.PI_PGS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_PGS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTAC(int ID, int* pnNrChannels);
	dll.PI_qTAC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qTAC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qTAV(int ID, const int* piChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qTAV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qTAV.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_OMA(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_OMA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_OMA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qOMA(int ID, const char* szAxes, double* pdValueArray);
	dll.PI_qOMA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_qOMA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_OMR(int ID, const char* szAxes, const double* pdValueArray);
	dll.PI_OMR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
	dll.PI_OMR.restype = ctypes.c_bool
	
	# Joystick
	# BOOL PI_FUNC_DECL PI_qJAS(int ID, const int* iJoystickIDsArray, const int* iAxesIDsArray, double* pdValueArray, int iArraySize);
	dll.PI_qJAS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qJAS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_JAX(int ID,  int iJoystickID,  int iAxesID, const char* szAxesBuffer);
	dll.PI_JAX.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
	dll.PI_JAX.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qJAX(int ID, const int* iJoystickIDsArray, const int* iAxesIDsArray, int iArraySize, char* szAxesBuffer, int iBufferSize);
	dll.PI_qJAX.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qJAX.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qJBS(int ID, const int* iJoystickIDsArray, const int* iButtonIDsArray, BOOL* pbValueArray, int iArraySize);
	dll.PI_qJBS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
	dll.PI_qJBS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_JDT(int ID, const int* iJoystickIDsArray, const int* iAxisIDsArray,const int* piValueArray, int iArraySize);
	dll.PI_JDT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_JDT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_JLT(int ID, int iJoystickID, int iAxisID, int iStartAdress, const double* pdValueArray,int iArraySize);
	dll.PI_JLT.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_JLT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qJLT(int ID, const int* iJoystickIDsArray, const int* iAxisIDsArray,  int iNumberOfTables,  int iOffsetOfFirstPointInTable,  int iNumberOfValues, double** pdValueArray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
	dll.PI_qJLT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
	dll.PI_qJLT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_JON(int ID, const int* iJoystickIDsArray, const BOOL* pbValueArray, int iArraySize);
	dll.PI_JON.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
	dll.PI_JON.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qJON(int ID, const int* iJoystickIDsArray, BOOL* pbValueArray, int iArraySize);
	dll.PI_qJON.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
	dll.PI_qJON.restype = ctypes.c_bool
	
	# fast scan commands
	# BOOL PI_FUNC_DECL PI_AAP(int ID, const char* szAxis1, double dLength1, const char* szAxis2, double dLength2, double dAlignStep, int iNrRepeatedPositions, int iAnalogInput);
	dll.PI_AAP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
	dll.PI_AAP.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_FIO(int ID, const char* szAxis1, double dLength1, const char* szAxis2, double dLength2, double dThreshold, double dLinearStep, double dAngleScan, int iAnalogInput);
	dll.PI_FIO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
	dll.PI_FIO.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_FLM(int ID, const char* szAxis, double dLength, double dThreshold, int iAnalogInput, int iDirection);
	dll.PI_FLM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
	dll.PI_FLM.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_FLS(int ID, const char* szAxis, double dLength, double dThreshold, int iAnalogInput, int iDirection);
	dll.PI_FLS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
	dll.PI_FLS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_FSA(int ID, const char* szAxis1, double dLength1, const char* szAxis2, double dLength2, double dThreshold, double dDistance, double dAlignStep, int iAnalogInput);
	dll.PI_FSA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
	dll.PI_FSA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_FSC(int ID, const char* szAxis1, double dLength1, const char* szAxis2, double dLength2, double dThreshold, double dDistance, int iAnalogInput);
	dll.PI_FSC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
	dll.PI_FSC.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_FSM(int ID, const char* szAxis1, double dLength1, const char* szAxis2, double dLength2, double dThreshold, double dDistance, int iAnalogInput);
	dll.PI_FSM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
	dll.PI_FSM.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qFSS(int ID, int* piResult);
	dll.PI_qFSS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
	dll.PI_qFSS.restype = ctypes.c_bool
	
	# optical boards (hexapod)
	# BOOL PI_FUNC_DECL PI_SGA(int ID, const int* piAnalogChannelIds, const int* piGainValues, int iArraySize);
	dll.PI_SGA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_SGA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qSGA(int ID, const int* piAnalogChannelIds, int* piGainValues, int iArraySize);
	dll.PI_qSGA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qSGA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_NAV(int ID, const int* piAnalogChannelIds, const int* piNrReadingsValues, int iArraySize);
	dll.PI_NAV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_NAV.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qNAV(int ID, const int* piAnalogChannelIds, int* piNrReadingsValues, int iArraySize);
	dll.PI_qNAV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qNAV.restype = ctypes.c_bool
	# more hexapod specific
	# BOOL	PI_FUNC_DECL	PI_GetDynamicMoveBufferSize(int ID, int *iSize);
	dll.PI_GetDynamicMoveBufferSize.argtypes = [ctypes.c_int, ctypes.c_int]
	dll.PI_GetDynamicMoveBufferSize.restype = ctypes.c_bool
	
	# PIShift
	# BOOL PI_FUNC_DECL PI_qCOV(int ID, const int* piChannelsArray, double* pdValueArray, int iArraySize);
	dll.PI_qCOV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qCOV.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_MOD(int ID, const char* szItems, const unsigned int* iModeArray, const char* szValues);
	dll.PI_MOD.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p]
	dll.PI_MOD.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qMOD(int ID, const char* szItems, const unsigned int* iModeArray, char* szValues, int iMaxValuesSize);
	dll.PI_qMOD.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p, ctypes.c_int]
	dll.PI_qMOD.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qDIA(int ID, const unsigned int* iIDArray, char* szValues,  int iBufferSize, int iArraySize);
	dll.PI_qDIA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
	dll.PI_qDIA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHDI(int ID, char* szBuffer,  int iBufferSize);
	dll.PI_qHDI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qHDI.restype = ctypes.c_bool
	
	# HID
	# BOOL PI_FUNC_DECL PI_qHIS(int ID, char* szBuffer,  int iBufferSize);
	dll.PI_qHIS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qHIS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_HIS(int ID, const int* iDeviceIDsArray, const int* iItemIDsArray, const int* iPropertyIDArray, const char* szValues, int iArraySize);
	dll.PI_HIS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
	dll.PI_HIS.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHIE(int ID, const int* iDeviceIDsArray, const int* iAxesIDsArray, double* pdValueArray, int iArraySize);
	dll.PI_qHIE.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_qHIE.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHIB(int ID, const int* iDeviceIDsArray, const int* iButtonIDsArray, int* pbValueArray, int iArraySize);
	dll.PI_qHIB.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qHIB.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_HIL(int ID, const int* iDeviceIDsArray, const int* iLED_IDsArray, const int* pnValueArray, int iArraySize);
	dll.PI_HIL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_HIL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHIL(int ID, const int* iDeviceIDsArray, const int* iLED_IDsArray, int* pnValueArray, int iArraySize);
	dll.PI_qHIL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qHIL.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_HIN(int ID, const char* szAxes, const BOOL* pbValueArray);
	dll.PI_HIN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_HIN.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHIN(int ID, const char* szAxes, BOOL* pbValueArray);
	dll.PI_qHIN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
	dll.PI_qHIN.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_HIA(int ID, const char* szAxes, const int* iFunctionArray, const int* iDeviceIDsArray, const int* iAxesIDsArray);
	dll.PI_HIA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
	dll.PI_HIA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHIA(int ID, const char* szAxes, const int* iFunctionArray, int* iDeviceIDsArray, int* iAxesIDsArray);
	dll.PI_qHIA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
	dll.PI_qHIA.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_HDT(int ID, const int* iDeviceIDsArray, const int* iAxisIDsArray, const int* piValueArray, int iArraySize);
	dll.PI_HDT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_HDT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHDT(int ID, const int* iDeviceIDsArray, const int* iAxisIDsArray, int* piValueArray, int iArraySize);
	dll.PI_qHDT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
	dll.PI_qHDT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_HIT(int ID, const int* piTableIdsArray, const int* piPointNumberArray, const double* pdValueArray, int iArraySize);
	dll.PI_HIT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
	dll.PI_HIT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qHIT(int ID, const int* piTableIdsArray,  int iNumberOfTables,  int iOffsetOfFirstPointInTable,  int iNumberOfValues, double** pdValueArray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
	dll.PI_qHIT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
	dll.PI_qHIT.restype = ctypes.c_bool
	# BOOL PI_FUNC_DECL PI_qMAN(int ID, const char* szCommand, char* szBuffer,  int iBufferSize);
	dll.PI_qMAN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
	dll.PI_qMAN.restype = ctypes.c_bool
	
	# Spezial
	# BOOL	PI_FUNC_DECL	PI_GetSupportedParameters(int ID, int* piParameterIdArray, int* piCommandLevelArray, int* piMemoryLocationArray, int* piDataTypeArray, int* piNumberOfItems, const int iiBufferSize, char* szParameterName, const int iMaxParameterNameSize);
	dll.PI_GetSupportedParameters.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
	dll.PI_GetSupportedParameters.restype = ctypes.c_bool
	# BOOL	PI_FUNC_DECL	PI_GetSupportedControllers(char* szBuffer, int iBufferSize);
	dll.PI_GetSupportedControllers.argtypes = [ctypes.c_char_p, ctypes.c_int]
	dll.PI_GetSupportedControllers.restype = ctypes.c_bool
	# int		PI_FUNC_DECL	PI_GetAsyncBufferIndex(int ID);
	dll.PI_GetAsyncBufferIndex.argtypes = [ctypes.c_int]
	dll.PI_GetAsyncBufferIndex.restype = ctypes.c_int
	# BOOL	PI_FUNC_DECL	PI_GetAsyncBuffer(int ID, double** pdValueArray);
	dll.PI_GetAsyncBuffer.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double))]
	dll.PI_GetAsyncBuffer.restype = ctypes.c_bool
	# BOOL	PI_FUNC_DECL	PI_AddStage(int ID, const char* szAxes);
	dll.PI_AddStage.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_AddStage.restype = ctypes.c_bool
	# BOOL	PI_FUNC_DECL	PI_RemoveStage(int ID, const char* szStageName);
	dll.PI_RemoveStage.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.PI_RemoveStage.restype = ctypes.c_bool
	# BOOL	PI_FUNC_DECL	PI_OpenUserStagesEditDialog(int ID);
	dll.PI_OpenUserStagesEditDialog.argtypes = [ctypes.c_int]
	dll.PI_OpenUserStagesEditDialog.restype = ctypes.c_bool
	# BOOL	PI_FUNC_DECL	PI_OpenPiStagesEditDialog(int ID);
	dll.PI_OpenPiStagesEditDialog.argtypes = [ctypes.c_int]
	dll.PI_OpenPiStagesEditDialog.restype = ctypes.c_bool
	
	# for internal use
	# BOOL	PI_FUNC_DECL	PI_DisableSingleStagesDatFiles(int ID,BOOL bDisable);
	dll.PI_DisableSingleStagesDatFiles.argtypes = [ctypes.c_int, ctypes.c_bool]
	dll.PI_DisableSingleStagesDatFiles.restype = ctypes.c_bool
	# BOOL	PI_FUNC_DECL	PI_DisableUserStagesDatFiles(int ID,BOOL bDisable);
	dll.PI_DisableUserStagesDatFiles.argtypes = [ctypes.c_int, ctypes.c_bool]
	dll.PI_DisableUserStagesDatFiles.restype = ctypes.c_bool
	
	
	
