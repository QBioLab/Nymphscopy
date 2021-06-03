# import re

# def MotionControlDLL():
	# file = open('MotionControlDLL.py', 'r')
	# file_write = open('MotionControlDLL_fixed.py', 'w')
	# index = 0
	# res = {'BOOL':'ctypes.c_bool', 'int':'ctypes.c_int', 'void': 'None'}
	# arg = {'char':'ctypes.c_char', 'char*':'ctypes.c_char_p', 'BOOL':'ctypes.c_bool', 'BOOL*':'ctypes.POINTER(ctypes.c_bool)', 'int':'ctypes.c_int', 'int*':'ctypes.POINTER(ctypes.c_int)', '__int64*':'ctypes.POINTER(ctypes.c_longlong)', 'unsigned_int*':'ctypes.POINTER(ctypes.c_uint)', 'double':'ctypes.c_double', 'double*':'ctypes.POINTER(ctypes.c_double)', 'double**':'ctypes.POINTER(ctypes.POINTER(ctypes.c_double))'}
	# for line in file:
		# index = index + 1
		# linearray = re.split("[\t\n, ();]+", line)
		# for _ in range(linearray.count('const')):
			# linearray.remove('const')
		# for _ in range(linearray.count('unsigned')):
			# linearray[ linearray.index('unsigned') + 1 ] = ''.join([ 'unsigned_', linearray[ linearray.index('unsigned') + 1 ] ])
			# linearray.remove('unsigned')
		# if len(linearray) < 3:
			# file_write.write(line)
			# continue
		# if linearray[2] == 'PI_FUNC_DECL':
			 # if linearray[1] in ('BOOL', 'int', 'void'):
				 # continue
				 # print(linearray[1])
			 # for i in range(4, len(linearray) - 1 , 2):
				 # if linearray[i] in ('char', 'char*', 'BOOL*', 'int', 'int*', '__int64*', 'unsigned_int*', 'BOOL', 'double', 'double*', 'double**'):
					 # continue
				 # print(linearray[i], '\t:', index)
			# text = ''.join([ '\t# ', line[1:] ])
			# file_write.write(text)
			# text = ''.join([ '\tdll.', linearray[3], '.argtypes = [' ])
			# for i in range(4, len(linearray) - 3 , 2):
				# text = ''.join([ text, arg[linearray[i]], ', ' ])
			# text = ''.join([ text, arg[linearray[len(linearray) - 3]], ']\n' ])
			# file_write.write(text)
			# text = ''.join([ '\tdll.', linearray[3], '.restype = ', res[linearray[1]], '\n' ])
			# file_write.write(text)
			# continue
		# file_write.write(line)
	# file.close()
	# file_write.close()

import ctypes
import os
import sys

PIGCS = ctypes.windll.LoadLibrary('Libraries\\PI_GCS2_DLL_x64.dll')

# DLL initialization and comm functions
# int	PI_FUNC_DECL	PI_InterfaceSetupDlg(const char* szRegKeyName);
PI_InterfaceSetupDlg = PIGCS.PI_InterfaceSetupDlg
PI_InterfaceSetupDlg.argtypes = [ctypes.c_char_p]
PI_InterfaceSetupDlg.restype = ctypes.c_int
# int 	PI_FUNC_DECL	PI_ConnectRS232(int nPortNr, int iBaudRate);
PI_ConnectRS232 = PIGCS.PI_ConnectRS232
PI_ConnectRS232.argtypes = [ctypes.c_int, ctypes.c_int]
PI_ConnectRS232.restype = ctypes.c_int
# int PI_FUNC_DECL PI_TryConnectRS232(int port, int baudrate);
PI_TryConnectRS232 = PIGCS.PI_TryConnectRS232
PI_TryConnectRS232.argtypes = [ctypes.c_int, ctypes.c_int]
PI_TryConnectRS232.restype = ctypes.c_int
# int PI_FUNC_DECL PI_TryConnectUSB(const char* szDescription);
PI_TryConnectUSB = PIGCS.PI_TryConnectUSB
PI_TryConnectUSB.argtypes = [ctypes.c_char_p]
PI_TryConnectUSB.restype = ctypes.c_int
# BOOL PI_FUNC_DECL PI_IsConnecting(int threadID, BOOL* bCOnnecting);
PI_IsConnecting = PIGCS.PI_IsConnecting
PI_IsConnecting.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]
PI_IsConnecting.restype = ctypes.c_bool
# int PI_FUNC_DECL PI_GetControllerID(int threadID);
PI_GetControllerID = PIGCS.PI_GetControllerID
PI_GetControllerID.argtypes = [ctypes.c_int]
PI_GetControllerID.restype = ctypes.c_int
# BOOL PI_FUNC_DECL PI_CancelConnect(int threadI);
PI_CancelConnect = PIGCS.PI_CancelConnect
PI_CancelConnect.argtypes = [ctypes.c_int]
PI_CancelConnect.restype = ctypes.c_bool
# int 	PI_FUNC_DECL	PI_ConnectRS232ByDevName(const char* szDevName, int BaudRate); This syntax does not exist, while PI_ConnectRS232details could be found
# dll.PI_ConnectRS232ByDevName.argtypes = [ctypes.c_char_p, ctypes.c_int]
# dll.PI_ConnectRS232ByDevName.restype = ctypes.c_int
# int 	PI_FUNC_DECL	PI_OpenRS232DaisyChain(int iPortNumber, int iBaudRate, int* pNumberOfConnectedDaisyChainDevices, char* szDeviceIDNs, int iBufferSize);
PI_OpenRS232DaisyChain = PIGCS.PI_OpenRS232DaisyChain
PI_OpenRS232DaisyChain.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
PI_OpenRS232DaisyChain.restype = ctypes.c_int
# int 	PI_FUNC_DECL	PI_ConnectDaisyChainDevice(int iPortId, int iDeviceNumber);
PI_ConnectDaisyChainDevice = PIGCS.PI_ConnectDaisyChainDevice
PI_ConnectDaisyChainDevice.argtypes = [ctypes.c_int, ctypes.c_int]
PI_ConnectDaisyChainDevice.restype = ctypes.c_int
# void 	PI_FUNC_DECL	PI_CloseDaisyChain(int iPortId);
PI_CloseDaisyChain = PIGCS.PI_CloseDaisyChain
PI_CloseDaisyChain.argtypes = [ctypes.c_int]
PI_CloseDaisyChain.restype = None
# int	    PI_FUNC_DECL	PI_ConnectNIgpib(int nBoard, int nDevAddr);
PI_ConnectNIgpib = PIGCS.PI_ConnectNIgpib
PI_ConnectNIgpib.argtypes = [ctypes.c_int, ctypes.c_int]
PI_ConnectNIgpib.restype = ctypes.c_int
# int	    PI_FUNC_DECL	PI_ConnectTCPIP(const char* szHostname, int port);
PI_ConnectTCPIP = PIGCS.PI_ConnectTCPIP
PI_ConnectTCPIP.argtypes = [ctypes.c_char_p, ctypes.c_int]
PI_ConnectTCPIP.restype = ctypes.c_int
# int	    PI_FUNC_DECL	PI_EnableTCPIPScan(int iMask);
PI_EnableTCPIPScan = PIGCS.PI_EnableTCPIPScan
PI_EnableTCPIPScan.argtypes = [ctypes.c_int]
PI_EnableTCPIPScan.restype = ctypes.c_int
# int	    PI_FUNC_DECL	PI_EnumerateTCPIPDevices(char* szBuffer, int iBufferSize, const char* szFilter);
PI_EnumerateTCPIPDevices = PIGCS.PI_EnumerateTCPIPDevices
PI_EnumerateTCPIPDevices.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p]
PI_EnumerateTCPIPDevices.restype = ctypes.c_int
# int	    PI_FUNC_DECL	PI_ConnectTCPIPByDescription(const char* szDescription);
PI_ConnectTCPIPByDescription = PIGCS.PI_ConnectTCPIPByDescription
PI_ConnectTCPIPByDescription.argtypes = [ctypes.c_char_p]
PI_ConnectTCPIPByDescription.restype = ctypes.c_int
# int 	PI_FUNC_DECL	PI_OpenTCPIPDaisyChain(const char* szHostname, int port, int* pNumberOfConnectedDaisyChainDevices, char* szDeviceIDNs, int iBufferSize);
PI_OpenTCPIPDaisyChain = PIGCS.PI_OpenTCPIPDaisyChain
PI_OpenTCPIPDaisyChain.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
PI_OpenTCPIPDaisyChain.restype = ctypes.c_int
# int	    PI_FUNC_DECL	PI_EnumerateUSB(char* szBuffer, int iBufferSize, const char* szFilter);
PI_EnumerateUSB = PIGCS.PI_EnumerateUSB
PI_EnumerateUSB.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p]
PI_EnumerateUSB.restype = ctypes.c_int
# int	    PI_FUNC_DECL	PI_ConnectUSB(const char* szDescription);
PI_ConnectUSB = PIGCS.PI_ConnectUSB
PI_ConnectUSB.argtypes = [ctypes.c_char_p]
PI_ConnectUSB.restype = ctypes.c_int
# int	    PI_FUNC_DECL	PI_ConnectUSBWithBaudRate(const char* szDescription,int iBaudRate);
PI_ConnectUSBWithBaudRate = PIGCS.PI_ConnectUSBWithBaudRate
PI_ConnectUSBWithBaudRate.argtypes = [ctypes.c_char_p, ctypes.c_int]
PI_ConnectUSBWithBaudRate.restype = ctypes.c_int
# int 	PI_FUNC_DECL	PI_OpenUSBDaisyChain(const char* szDescription, int* pNumberOfConnectedDaisyChainDevices, char* szDeviceIDNs, int iBufferSize);
PI_OpenUSBDaisyChain = PIGCS.PI_OpenUSBDaisyChain
PI_OpenUSBDaisyChain.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
PI_OpenUSBDaisyChain.restype = ctypes.c_int
# BOOL	PI_FUNC_DECL	PI_IsConnected(int ID);
PI_IsConnected = PIGCS.PI_IsConnected
PI_IsConnected.argtypes = [ctypes.c_int]
PI_IsConnected.restype = ctypes.c_bool
# void	PI_FUNC_DECL	PI_CloseConnection(int ID);
PI_CloseConnection = PIGCS.PI_CloseConnection
PI_CloseConnection.argtypes = [ctypes.c_int]
PI_CloseConnection.restype = None
# int	    PI_FUNC_DECL	PI_GetError(int ID);
PI_GetError = PIGCS.PI_GetError
PI_GetError.argtypes = [ctypes.c_int]
PI_GetError.restype = ctypes.c_int
# BOOL	PI_FUNC_DECL	PI_SetErrorCheck(int ID, BOOL bErrorCheck);
PI_SetErrorCheck = PIGCS.PI_SetErrorCheck
PI_SetErrorCheck.argtypes = [ctypes.c_int, ctypes.c_bool]
PI_SetErrorCheck.restype = ctypes.c_bool
# BOOL	PI_FUNC_DECL	PI_TranslateError(int errNr, char* szBuffer, int iBufferSize);
PI_TranslateError = PIGCS.PI_TranslateError
PI_TranslateError.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_TranslateError.restype = ctypes.c_bool
# int	    PI_FUNC_DECL	PI_SetTimeout(int ID, int timeoutInMS);
PI_SetTimeout = PIGCS.PI_SetTimeout
PI_SetTimeout.argtypes = [ctypes.c_int, ctypes.c_int]
PI_SetTimeout.restype = ctypes.c_int
# int		PI_FUNC_DECL	PI_SetDaisyChainScanMaxDeviceID(int maxID);
PI_SetDaisyChainScanMaxDeviceID = PIGCS.PI_SetDaisyChainScanMaxDeviceID
PI_SetDaisyChainScanMaxDeviceID.argtypes = [ctypes.c_int]
PI_SetDaisyChainScanMaxDeviceID.restype = ctypes.c_int
# BOOL	PI_FUNC_DECL	PI_EnableReconnect(int ID, BOOL bEnable);
PI_EnableReconnect = PIGCS.PI_EnableReconnect
PI_EnableReconnect.argtypes = [ctypes.c_int, ctypes.c_bool]
PI_EnableReconnect.restype = ctypes.c_bool
# int     PI_FUNC_DECL    PI_SetNrTimeoutsBeforeClose(int ID, int nrTimeoutsBeforeClose);
PI_SetNrTimeoutsBeforeClose = PIGCS.PI_SetNrTimeoutsBeforeClose
PI_SetNrTimeoutsBeforeClose.argtypes = [ctypes.c_int, ctypes.c_int]
PI_SetNrTimeoutsBeforeClose.restype = ctypes.c_int
# BOOL    PI_FUNC_DECL    PI_GetInterfaceDescription(int ID, char* szBuffer, int iBufferSize);
PI_GetInterfaceDescription = PIGCS.PI_GetInterfaceDescription
PI_GetInterfaceDescription.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_GetInterfaceDescription.restype = ctypes.c_bool

# general
# BOOL PI_FUNC_DECL PI_qERR(int ID, int* pnError);
PI_qERR = PIGCS.PI_qERR
PI_qERR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qERR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qIDN(int ID, char* szBuffer, int iBufferSize);
PI_qIDN = PIGCS.PI_qIDN
PI_qIDN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qIDN.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_INI(int ID, const char* szAxes);
PI_INI = PIGCS.PI_INI
PI_INI.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_INI.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHLP(int ID, char* szBuffer, int iBufferSize);
PI_qHLP = PIGCS.PI_qHLP
PI_qHLP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qHLP.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHPA(int ID, char* szBuffer, int iBufferSize);
PI_qHPA = PIGCS.PI_qHPA
PI_qHPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qHPA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHPV(int ID, char* szBuffer, int iBufferSize);
PI_qHPV = PIGCS.PI_qHPV
PI_qHPV.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qHPV.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qCSV(int ID, double* pdCommandSyntaxVersion);
PI_qCSV = PIGCS.PI_qCSV
PI_qCSV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
PI_qCSV.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qOVF(int ID, const char* szAxes, BOOL* piValueArray);
PI_qOVF = PIGCS.PI_qOVF
PI_qOVF.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qOVF.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_RBT(int ID);
PI_RBT = PIGCS.PI_RBT
PI_RBT.argtypes = [ctypes.c_int]
PI_RBT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_REP(int ID);
PI_REP = PIGCS.PI_REP
PI_REP.argtypes = [ctypes.c_int]
PI_REP.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_BDR(int ID, int iBaudRate);
PI_BDR = PIGCS.PI_BDR
PI_BDR.argtypes = [ctypes.c_int, ctypes.c_int]
PI_BDR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qBDR(int ID, int* iBaudRate);
PI_qBDR = PIGCS.PI_qBDR
PI_qBDR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qBDR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DBR(int ID, int iBaudRate);
PI_DBR = PIGCS.PI_DBR
PI_DBR.argtypes = [ctypes.c_int, ctypes.c_int]
PI_DBR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDBR(int ID, int* iBaudRate);
PI_qDBR = PIGCS.PI_qDBR
PI_qDBR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qDBR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qVER(int ID, char* szBuffer, int iBufferSize);
PI_qVER = PIGCS.PI_qVER
PI_qVER.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qVER.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSSN(int ID, char* szSerialNumber, int iBufferSize);
PI_qSSN = PIGCS.PI_qSSN
PI_qSSN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qSSN.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_CCT(int ID, int iCommandType);
PI_CCT = PIGCS.PI_CCT
PI_CCT.argtypes = [ctypes.c_int, ctypes.c_int]
PI_CCT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qCCT(int ID, int *iCommandType);
PI_qCCT = PIGCS.PI_qCCT
PI_qCCT.argtypes = [ctypes.c_int, ctypes.c_int]
PI_qCCT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTVI(int ID, char* szBuffer, int iBufferSize);
PI_qTVI = PIGCS.PI_qTVI
PI_qTVI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qTVI.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_IFC(int ID, const char* szParameters, const char* szValues);
PI_IFC = PIGCS.PI_IFC
PI_IFC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
PI_IFC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qIFC(int ID, const char* szParameters, char* szBuffer, int iBufferSize);
PI_qIFC = PIGCS.PI_qIFC
PI_qIFC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
PI_qIFC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_IFS(int ID, const char* szPassword, const char* szParameters, const char* szValues);
PI_IFS = PIGCS.PI_IFS
PI_IFS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
PI_IFS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qIFS(int ID, const char* szParameters, char* szBuffer, int iBufferSize);
PI_qIFS = PIGCS.PI_qIFS
PI_qIFS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
PI_qIFS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qECO(int ID, const char* szSendString, char* szValues, int iBufferSize);
PI_qECO = PIGCS.PI_qECO
PI_qECO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
PI_qECO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MOV(int ID, const char* szAxes, const double* pdValueArray);
PI_MOV = PIGCS.PI_MOV
PI_MOV.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_MOV.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qMOV(int ID, const char* szAxes, double* pdValueArray);
PI_qMOV = PIGCS.PI_qMOV
PI_qMOV.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qMOV.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MVR(int ID, const char* szAxes, const double* pdValueArray);
PI_MVR = PIGCS.PI_MVR
PI_MVR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_MVR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MVE(int ID, const char* szAxes, const double* pdValueArray);
PI_MVE = PIGCS.PI_MVE
PI_MVE.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_MVE.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_POS(int ID, const char* szAxes, const double* pdValueArray);
PI_POS = PIGCS.PI_POS
PI_POS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_POS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qPOS(int ID, const char* szAxes, double* pdValueArray);
PI_qPOS = PIGCS.PI_qPOS
PI_qPOS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qPOS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_IsMoving(int ID, const char* szAxes, BOOL* pbValueArray);
PI_IsMoving = PIGCS.PI_IsMoving
PI_IsMoving.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_IsMoving.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_HLT(int ID, const char* szAxes);
PI_HLT = PIGCS.PI_HLT
PI_HLT.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_HLT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_STP(int ID);
PI_STP = PIGCS.PI_STP
PI_STP.argtypes = [ctypes.c_int]
PI_STP.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_StopAll(int ID);
PI_StopAll = PIGCS.PI_StopAll
PI_StopAll.argtypes = [ctypes.c_int]
PI_StopAll.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qONT(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qONT = PIGCS.PI_qONT
PI_qONT.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qONT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_RTO(int ID, const char* szAxes);
PI_RTO = PIGCS.PI_RTO
PI_RTO.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_RTO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qRTO(int ID, const char* szAxes, int* piValueArray);
PI_qRTO = PIGCS.PI_qRTO
PI_qRTO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
PI_qRTO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_ATZ(int ID, const char* szAxes, const double* pdLowvoltageArray, const BOOL* pfUseDefaultArray);
PI_ATZ = PIGCS.PI_ATZ
PI_ATZ.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_bool)]
PI_ATZ.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qATZ(int ID, const char* szAxes, int* piAtzResultArray);
PI_qATZ = PIGCS.PI_qATZ
PI_qATZ.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
PI_qATZ.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_AOS(int ID, const char* szAxes, const double* pdValueArray);
PI_AOS = PIGCS.PI_AOS
PI_AOS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_AOS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qAOS(int ID, const char* szAxes, double* pdValueArray);
PI_qAOS = PIGCS.PI_qAOS
PI_qAOS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qAOS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_HasPosChanged(int ID, const char* szAxes, BOOL* pbValueArray);
PI_HasPosChanged = PIGCS.PI_HasPosChanged
PI_HasPosChanged.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_HasPosChanged.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_GetErrorStatus(int ID, BOOL* pbIsReferencedArray, BOOL* pbIsReferencing, BOOL* pbIsMovingArray, BOOL* pbIsMotionErrorArray);
PI_GetErrorStatus = PIGCS.PI_GetErrorStatus
PI_GetErrorStatus.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool)]
PI_GetErrorStatus.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SVA(int ID, const char* szAxes, const double* pdValueArray);
PI_SVA = PIGCS.PI_SVA
PI_SVA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_SVA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSVA(int ID, const char* szAxes, double* pdValueArray);
PI_qSVA = PIGCS.PI_qSVA
PI_qSVA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qSVA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SVR(int ID, const char* szAxes, const double* pdValueArray);
PI_SVR = PIGCS.PI_SVR
PI_SVR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_SVR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DFH(int ID, const char* szAxes);
PI_DFH = PIGCS.PI_DFH
PI_DFH.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_DFH.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDFH(int ID, const char* szAxes, double* pdValueArray);
PI_qDFH = PIGCS.PI_qDFH
PI_qDFH.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qDFH.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_GOH(int ID, const char* szAxes);
PI_GOH = PIGCS.PI_GOH
PI_GOH.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_GOH.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qCST(int ID, const char* szAxes, char* szNames, int iBufferSize);
PI_qCST = PIGCS.PI_qCST
PI_qCST.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
PI_qCST.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_CST(int ID, const char* szAxes, const char* szNames);
PI_CST = PIGCS.PI_CST
PI_CST.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
PI_CST.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qVST(int ID, char* szBuffer, int iBufferSize);
PI_qVST = PIGCS.PI_qVST
PI_qVST.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qVST.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qPUN(int ID, const char* szAxes, char* szUnit, int iBufferSize);
PI_qPUN = PIGCS.PI_qPUN
PI_qPUN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
PI_qPUN.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SVO(int ID, const char* szAxes, const BOOL* pbValueArray);
PI_SVO = PIGCS.PI_SVO
PI_SVO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_SVO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSVO(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qSVO = PIGCS.PI_qSVO
PI_qSVO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qSVO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SMO( int ID, const char*  szAxes, const int* piValueArray);
PI_SMO = PIGCS.PI_SMO
PI_SMO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
PI_SMO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSMO(int ID, const char* szAxes, int* piValueArray);
PI_qSMO = PIGCS.PI_qSMO
PI_qSMO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
PI_qSMO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DCO(int ID, const char* szAxes, const BOOL* pbValueArray);
PI_DCO = PIGCS.PI_DCO
PI_DCO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_DCO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDCO(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qDCO = PIGCS.PI_qDCO
PI_qDCO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qDCO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_BRA(int ID, const char* szAxes, const BOOL* pbValueArray);
PI_BRA = PIGCS.PI_BRA
PI_BRA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_BRA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qBRA(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qBRA = PIGCS.PI_qBRA
PI_qBRA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qBRA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_RON(int ID, const char* szAxes, const BOOL* pbValueArray);
PI_RON = PIGCS.PI_RON
PI_RON.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_RON.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qRON(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qRON = PIGCS.PI_qRON
PI_qRON.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qRON.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_VEL(int ID, const char* szAxes, const double* pdValueArray);
PI_VEL = PIGCS.PI_VEL
PI_VEL.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_VEL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qVEL(int ID, const char* szAxes, double* pdValueArray);
PI_qVEL = PIGCS.PI_qVEL
PI_qVEL.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qVEL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_JOG(int ID, const char* szAxes, const double* pdValueArray);
PI_JOG = PIGCS.PI_JOG
PI_JOG.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_JOG.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qJOG(int ID, const char* szAxes, double* pdValueArray);
PI_qJOG = PIGCS.PI_qJOG
PI_qJOG.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qJOG.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTCV(int ID, const char* szAxes, double* pdValueArray);
PI_qTCV = PIGCS.PI_qTCV
PI_qTCV.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qTCV.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_VLS(int ID, double dSystemVelocity);
PI_VLS = PIGCS.PI_VLS
PI_VLS.argtypes = [ctypes.c_int, ctypes.c_double]
PI_VLS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qVLS(int ID, double* pdSystemVelocity);
PI_qVLS = PIGCS.PI_qVLS
PI_qVLS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
PI_qVLS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_ACC(int ID, const char* szAxes, const double* pdValueArray);
PI_ACC = PIGCS.PI_ACC
PI_ACC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_ACC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qACC(int ID, const char* szAxes, double* pdValueArray);
PI_qACC = PIGCS.PI_qACC
PI_qACC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qACC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DEC(int ID, const char* szAxes, const double* pdValueArray);
PI_DEC = PIGCS.PI_DEC
PI_DEC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_DEC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDEC(int ID, const char* szAxes, double* pdValueArray);
PI_qDEC = PIGCS.PI_qDEC
PI_qDEC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qDEC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_VCO(int ID, const char* szAxes, const BOOL* pbValueArray);
PI_VCO = PIGCS.PI_VCO
PI_VCO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_VCO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qVCO(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qVCO = PIGCS.PI_qVCO
PI_qVCO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qVCO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SPA(int ID, const char* szAxes, const unsigned int* iParameterArray, const double* pdValueArray, const char* szStrings);
PI_SPA = PIGCS.PI_SPA
PI_SPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_double), ctypes.c_char_p]
PI_SPA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSPA(int ID, const char* szAxes, unsigned int* iParameterArray, double* pdValueArray, char* szStrings, int iMaxNameSize);
PI_qSPA = PIGCS.PI_qSPA
PI_qSPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_double), ctypes.c_char_p, ctypes.c_int]
PI_qSPA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SEP(int ID, const char* szPassword, const char* szAxes, const unsigned int* iParameterArray, const double* pdValueArray, const char* szStrings);
PI_SEP = PIGCS.PI_SEP
PI_SEP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_double), ctypes.c_char_p]
PI_SEP.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSEP(int ID, const char* szAxes, unsigned int* iParameterArray, double* pdValueArray, char* szStrings, int iMaxNameSize);
PI_qSEP = PIGCS.PI_qSEP
PI_qSEP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_double), ctypes.c_char_p, ctypes.c_int]
PI_qSEP.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WPA(int ID, const char* szPassword, const char* szAxes, const unsigned int* iParameterArray);
PI_WPA = PIGCS.PI_WPA
PI_WPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint)]
PI_WPA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DPA(int ID, const char* szPassword, const char* szAxes, const unsigned int* iParameterArray);
PI_DPA = PIGCS.PI_DPA
PI_DPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint)]
PI_DPA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_TIM(int ID, double dTimer);
PI_TIM = PIGCS.PI_TIM
PI_TIM.argtypes = [ctypes.c_int, ctypes.c_double]
PI_TIM.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTIM(int ID, double* pdTimer);
PI_qTIM = PIGCS.PI_qTIM
PI_qTIM.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
PI_qTIM.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_RPA(int ID, const char* szAxes, const unsigned int* iParameterArray);
PI_RPA = PIGCS.PI_RPA
PI_RPA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint)]
PI_RPA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SPA_String(int ID, const char* szAxes, const unsigned int* iParameterArray, const char* szStrings);
PI_SPA_String = PIGCS.PI_SPA_String
PI_SPA_String.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p]
PI_SPA_String.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSPA_String(int ID, const char* szAxes, const unsigned int* iParameterArray, char* szStrings, int iMaxNameSize);
PI_qSPA_String = PIGCS.PI_qSPA_String
PI_qSPA_String.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p, ctypes.c_int]
PI_qSPA_String.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SEP_String(int ID, const char* szPassword, const char* szAxes, const unsigned int* iParameterArray, const char* szStrings);
PI_SEP_String = PIGCS.PI_SEP_String
PI_SEP_String.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p]
PI_SEP_String.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSEP_String(int ID, const char* szAxes, unsigned int* iParameterArray, char* szStrings, int iMaxNameSize);
PI_qSEP_String = PIGCS.PI_qSEP_String
PI_qSEP_String.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p, ctypes.c_int]
PI_qSEP_String.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SPA_int64(int ID, const char* szAxes, const unsigned int* iParameterArray, const __int64* piValueArray);
PI_SPA_int64 = PIGCS.PI_SPA_int64
PI_SPA_int64.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_longlong)]
PI_SPA_int64.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSPA_int64(int ID, const char* szAxes, unsigned int* iParameterArray, __int64* piValueArray);
PI_qSPA_int64 = PIGCS.PI_qSPA_int64
PI_qSPA_int64.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_longlong)]
PI_qSPA_int64.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SEP_int64(int ID, const char* szPassword, const char* szAxes, const unsigned int* iParameterArray, const __int64* piValueArray);
PI_SEP_int64 = PIGCS.PI_SEP_int64
PI_SEP_int64.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_longlong)]
PI_SEP_int64.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSEP_int64(int ID, const char* szAxes, unsigned int* iParameterArray, __int64* piValueArray);
PI_qSEP_int64 = PIGCS.PI_qSEP_int64
PI_qSEP_int64.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_longlong)]
PI_qSEP_int64.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_STE(int ID, const char* szAxes, const double* dOffsetArray);
PI_STE = PIGCS.PI_STE
PI_STE.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_STE.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSTE(int ID, const char* szAxes, double* pdValueArray);
PI_qSTE = PIGCS.PI_qSTE
PI_qSTE.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qSTE.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_IMP(int ID, const char*  szAxes, const double* pdImpulseSize);
PI_IMP = PIGCS.PI_IMP
PI_IMP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_IMP.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_IMP_PulseWidth(int ID, char cAxis, double dOffset, int iPulseWidth);
PI_IMP_PulseWidth = PIGCS.PI_IMP_PulseWidth
PI_IMP_PulseWidth.argtypes = [ctypes.c_int, ctypes.c_char, ctypes.c_double, ctypes.c_int]
PI_IMP_PulseWidth.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qIMP(int ID, const char* szAxes, double* pdValueArray);
PI_qIMP = PIGCS.PI_qIMP
PI_qIMP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qIMP.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SAI(int ID, const char* szOldAxes, const char* szNewAxes);
PI_SAI = PIGCS.PI_SAI
PI_SAI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
PI_SAI.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSAI(int ID, char* szAxes, int iBufferSize);
PI_qSAI = PIGCS.PI_qSAI
PI_qSAI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qSAI.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSAI_ALL(int ID, char* szAxes, int iBufferSize);
PI_qSAI_ALL = PIGCS.PI_qSAI_ALL
PI_qSAI_ALL.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qSAI_ALL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_CCL(int ID, int iComandLevel, const char* szPassWord);
PI_CCL = PIGCS.PI_CCL
PI_CCL.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
PI_CCL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qCCL(int ID, int* piComandLevel);
PI_qCCL = PIGCS.PI_qCCL
PI_qCCL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qCCL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_AVG(int ID, int iAverrageTime);
PI_AVG = PIGCS.PI_AVG
PI_AVG.argtypes = [ctypes.c_int, ctypes.c_int]
PI_AVG.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qAVG(int ID, int *iAverrageTime);
PI_qAVG = PIGCS.PI_qAVG
PI_qAVG.argtypes = [ctypes.c_int, ctypes.c_int]
PI_qAVG.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHAR(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qHAR = PIGCS.PI_qHAR
PI_qHAR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qHAR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qLIM(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qLIM = PIGCS.PI_qLIM
PI_qLIM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qLIM.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTRS(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qTRS = PIGCS.PI_qTRS
PI_qTRS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qTRS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_FNL(int ID, const char* szAxes);
PI_FNL = PIGCS.PI_FNL
PI_FNL.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_FNL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_FPL(int ID, const char* szAxes);
PI_FPL = PIGCS.PI_FPL
PI_FPL.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_FPL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_FRF(int ID, const char* szAxes);
PI_FRF = PIGCS.PI_FRF
PI_FRF.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_FRF.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_FED(int ID, const char* szAxes, const int* piEdgeArray, const int* piParamArray);
PI_FED = PIGCS.PI_FED
PI_FED.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
PI_FED.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qFRF(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qFRF = PIGCS.PI_qFRF
PI_qFRF.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qFRF.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DIO(int ID, const int* piChannelsArray, const BOOL* pbValueArray, int iArraySize);
PI_DIO = PIGCS.PI_DIO
PI_DIO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
PI_DIO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDIO(int ID, const int* piChannelsArray, BOOL* pbValueArray, int iArraySize);
PI_qDIO = PIGCS.PI_qDIO
PI_qDIO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
PI_qDIO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTIO(int ID, int* piInputNr, int* piOutputNr);
PI_qTIO = PIGCS.PI_qTIO
PI_qTIO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
PI_qTIO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_IsControllerReady(int ID, int* piControllerReady);
PI_IsControllerReady = PIGCS.PI_IsControllerReady
PI_IsControllerReady.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_IsControllerReady.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSRG(int ID, const char* szAxes, const int* iRegisterArray, int* iValArray);
PI_qSRG = PIGCS.PI_qSRG
PI_qSRG.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
PI_qSRG.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_ATC(int ID, const int* piChannels, const int* piValueArray, int iArraySize);
PI_ATC = PIGCS.PI_ATC
PI_ATC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_ATC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qATC(int ID, const int* piChannels, int* piValueArray, int iArraySize);
PI_qATC = PIGCS.PI_qATC
PI_qATC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qATC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qATS(int ID, const int* piChannels, const int* piOptions, int* piValueArray, int iArraySize);
PI_qATS = PIGCS.PI_qATS
PI_qATS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qATS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SPI(int ID, const char* szAxes, const double* pdValueArray);
PI_SPI = PIGCS.PI_SPI
PI_SPI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_SPI.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSPI(int ID, const char* szAxes, double* pdValueArray);
PI_qSPI = PIGCS.PI_qSPI
PI_qSPI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qSPI.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SCT(int ID, double dCycleTime);
PI_SCT = PIGCS.PI_SCT
PI_SCT.argtypes = [ctypes.c_int, ctypes.c_double]
PI_SCT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSCT(int ID, double* pdCycleTime);
PI_qSCT = PIGCS.PI_qSCT
PI_qSCT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
PI_qSCT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SST(int ID, const char* szAxes, const double* pdValueArray);
PI_SST = PIGCS.PI_SST
PI_SST.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_SST.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSST(int ID, const char* szAxes, double* pdValueArray);
PI_qSST = PIGCS.PI_qSST
PI_qSST.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qSST.restype = ctypes.c_bool

# Macro commande
# BOOL PI_FUNC_DECL PI_IsRunningMacro(int ID, BOOL* pbRunningMacro);
PI_IsRunningMacro = PIGCS.PI_IsRunningMacro
PI_IsRunningMacro.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]
PI_IsRunningMacro.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MAC_BEG(int ID, const char* szMacroName);
PI_MAC_BEG = PIGCS.PI_MAC_BEG
PI_MAC_BEG.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_MAC_BEG.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MAC_START(int ID, const char* szMacroName);
PI_MAC_START = PIGCS.PI_MAC_START
PI_MAC_START.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_MAC_START.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MAC_NSTART(int ID, const char* szMacroName, int nrRuns);
PI_MAC_NSTART = PIGCS.PI_MAC_NSTART
PI_MAC_NSTART.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_MAC_NSTART.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MAC_START_Args(int ID, const char* szMacroName, const char* szArgs);
PI_MAC_START_Args = PIGCS.PI_MAC_START_Args
PI_MAC_START_Args.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
PI_MAC_START_Args.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MAC_NSTART_Args(int ID, const char* szMacroName, int nrRuns, const char* szArgs);
PI_MAC_NSTART_Args = PIGCS.PI_MAC_NSTART_Args
PI_MAC_NSTART_Args.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p]
PI_MAC_NSTART_Args.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MAC_END(int ID);
PI_MAC_END = PIGCS.PI_MAC_END
PI_MAC_END.argtypes = [ctypes.c_int]
PI_MAC_END.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MAC_DEL(int ID, const char* szMacroName);
PI_MAC_DEL = PIGCS.PI_MAC_DEL
PI_MAC_DEL.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_MAC_DEL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MAC_DEF(int ID, const char* szMacroName);
PI_MAC_DEF = PIGCS.PI_MAC_DEF
PI_MAC_DEF.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_MAC_DEF.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MAC_qDEF(int ID, char* szBuffer, int iBufferSize);
PI_MAC_qDEF = PIGCS.PI_MAC_qDEF
PI_MAC_qDEF.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_MAC_qDEF.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MAC_qERR(int ID, char* szBuffer, int iBufferSize);
PI_MAC_qERR = PIGCS.PI_MAC_qERR
PI_MAC_qERR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_MAC_qERR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MAC_qFREE(int ID, int* iFreeSpace);
PI_MAC_qFREE = PIGCS.PI_MAC_qFREE
PI_MAC_qFREE.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_MAC_qFREE.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qMAC(int ID, const char* szMacroName, char* szBuffer, int iBufferSize);
PI_qMAC = PIGCS.PI_qMAC
PI_qMAC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
PI_qMAC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qRMC(int ID, char* szBuffer, int iBufferSize);
PI_qRMC = PIGCS.PI_qRMC
PI_qRMC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qRMC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DEL(int ID, int nMilliSeconds);
PI_DEL = PIGCS.PI_DEL
PI_DEL.argtypes = [ctypes.c_int, ctypes.c_int]
PI_DEL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WAC(int ID, const char* szCondition);
PI_WAC = PIGCS.PI_WAC
PI_WAC.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_WAC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MEX(int ID, const char* szCondition);
PI_MEX = PIGCS.PI_MEX
PI_MEX.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_MEX.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_VAR(int ID, const char* szVariable, const char* szValue);
PI_VAR = PIGCS.PI_VAR
PI_VAR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
PI_VAR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qVAR(int ID, const char* szVariables, char* szValues,  int iBufferSize);
PI_qVAR = PIGCS.PI_qVAR
PI_qVAR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
PI_qVAR.restype = ctypes.c_bool

# String commands.
# BOOL PI_FUNC_DECL PI_GcsCommandset(int ID, const char* szCommand);
PI_GcsCommandset = PIGCS.PI_GcsCommandset
PI_GcsCommandset.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_GcsCommandset.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_GcsGetAnswer(int ID, char* szAnswer, int iBufferSize);
PI_GcsGetAnswer = PIGCS.PI_GcsGetAnswer
PI_GcsGetAnswer.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_GcsGetAnswer.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_GcsGetAnswerSize(int ID, int* iAnswerSize);
PI_GcsGetAnswerSize = PIGCS.PI_GcsGetAnswerSize
PI_GcsGetAnswerSize.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_GcsGetAnswerSize.restype = ctypes.c_bool

# limits
# BOOL PI_FUNC_DECL PI_qTMN(int ID, const char* szAxes, double* pdValueArray);
PI_qTMN = PIGCS.PI_qTMN
PI_qTMN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qTMN.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTMX(int ID, const char* szAxes, double* pdValueArray);
PI_qTMX = PIGCS.PI_qTMX
PI_qTMX.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qTMX.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_NLM(int ID, const char* szAxes, const double* pdValueArray);
PI_NLM = PIGCS.PI_NLM
PI_NLM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_NLM.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qNLM(int ID, const char* szAxes, double* pdValueArray);
PI_qNLM = PIGCS.PI_qNLM
PI_qNLM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qNLM.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_PLM(int ID, const char* szAxes, const double* pdValueArray);
PI_PLM = PIGCS.PI_PLM
PI_PLM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_PLM.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qPLM(int ID, const char* szAxes, double* pdValueArray);
PI_qPLM = PIGCS.PI_qPLM
PI_qPLM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qPLM.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SSL(int ID, const char* szAxes, const BOOL* pbValueArray);
PI_SSL = PIGCS.PI_SSL
PI_SSL.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_SSL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSSL(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qSSL = PIGCS.PI_qSSL
PI_qSSL.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qSSL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qVMO(int ID, const char* szAxes, const double* pdValarray, BOOL* pbMovePossible);
PI_qVMO = PIGCS.PI_qVMO
PI_qVMO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_bool)]
PI_qVMO.restype = ctypes.c_bool

# Wave commands.
# BOOL PI_FUNC_DECL PI_IsGeneratorRunning(int ID, const int* piWaveGeneratorIds, BOOL* pbValueArray, int iArraySize);
PI_IsGeneratorRunning = PIGCS.PI_IsGeneratorRunning
PI_IsGeneratorRunning.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
PI_IsGeneratorRunning.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTWG(int ID, int* piWaveGenerators);
PI_qTWG = PIGCS.PI_qTWG
PI_qTWG.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qTWG.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WAV_SIN_P(int ID, int iWaveTableId, int iOffsetOfFirstPointInWaveTable, int iNumberOfPoints, int iAddAppendWave, int iCenterPointOfWave, double dAmplitudeOfWave, double dOffsetOfWave, int iSegmentLength);
PI_WAV_SIN_P = PIGCS.PI_WAV_SIN_P
PI_WAV_SIN_P.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_int]
PI_WAV_SIN_P.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WAV_LIN(int ID, int iWaveTableId, int iOffsetOfFirstPointInWaveTable, int iNumberOfPoints, int iAddAppendWave, int iNumberOfSpeedUpDownPointsInWave, double dAmplitudeOfWave, double dOffsetOfWave, int iSegmentLength);
PI_WAV_LIN = PIGCS.PI_WAV_LIN
PI_WAV_LIN.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_int]
PI_WAV_LIN.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WAV_NOISE(int ID, int iWaveTableId, int iAddAppendWave, double dAmplitudeOfWave, double dOffsetOfWave,int iSegmentLength);   
PI_WAV_NOISE = PIGCS.PI_WAV_NOISE
PI_WAV_NOISE.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_int]
PI_WAV_NOISE.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WAV_RAMP(int ID, int iWaveTableId, int iOffsetOfFirstPointInWaveTable, int iNumberOfPoints, int iAddAppendWave, int iCenterPointOfWave, int iNumberOfSpeedUpDownPointsInWave, double dAmplitudeOfWave, double dOffsetOfWave, int iSegmentLength);
PI_WAV_RAMP = PIGCS.PI_WAV_RAMP
PI_WAV_RAMP.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_int]
PI_WAV_RAMP.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WAV_PNT(int ID, int iWaveTableId, int iOffsetOfFirstPointInWaveTable, int iNumberOfPoints, int iAddAppendWave, const double* pdWavePoints);
PI_WAV_PNT = PIGCS.PI_WAV_PNT
PI_WAV_PNT.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
PI_WAV_PNT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qWAV(int ID, const int* piWaveTableIdsArray, const int* piParamereIdsArray, double* pdValueArray, int iArraySize);
PI_qWAV = PIGCS.PI_qWAV
PI_qWAV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qWAV.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WGO(int ID, const int* piWaveGeneratorIdsArray, const int* iStartModArray, int iArraySize);
PI_WGO = PIGCS.PI_WGO
PI_WGO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_WGO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qWGO(int ID, const int* piWaveGeneratorIdsArray, int* piValueArray, int iArraySize);
PI_qWGO = PIGCS.PI_qWGO
PI_qWGO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qWGO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WGC(int ID, const int* piWaveGeneratorIdsArray, const int* piNumberOfCyclesArray, int iArraySize);
PI_WGC = PIGCS.PI_WGC
PI_WGC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_WGC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qWGC(int ID, const int* piWaveGeneratorIdsArray, int* piValueArray, int iArraySize);
PI_qWGC = PIGCS.PI_qWGC
PI_qWGC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qWGC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qWGI(int ID, const int* piWaveGeneratorIdsArray, int* piValueArray, int iArraySize);
PI_qWGI = PIGCS.PI_qWGI
PI_qWGI.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qWGI.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qWGN(int ID, const int* piWaveGeneratorIdsArray, int* piValueArray, int iArraySize);
PI_qWGN = PIGCS.PI_qWGN
PI_qWGN.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qWGN.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WSL(int ID, const int* piWaveGeneratorIdsArray, const int* piWaveTableIdsArray, int iArraySize);
PI_WSL = PIGCS.PI_WSL
PI_WSL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_WSL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qWSL(int ID, const int* piWaveGeneratorIdsArray, int* piWaveTableIdsArray, int iArraySize);
PI_qWSL = PIGCS.PI_qWSL
PI_qWSL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qWSL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DTC(int ID, const int* piDdlTableIdsArray, int iArraySize);
PI_DTC = PIGCS.PI_DTC
PI_DTC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_DTC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDTL(int ID, const int* piDdlTableIdsArray, int* piValueArray, int iArraySize);
PI_qDTL = PIGCS.PI_qDTL
PI_qDTL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qDTL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WCL(int ID, const int* piWaveTableIdsArray, int iArraySize);
PI_WCL = PIGCS.PI_WCL
PI_WCL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_WCL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTLT(int ID, int* piNumberOfDdlTables);
PI_qTLT = PIGCS.PI_qTLT
PI_qTLT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qTLT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qGWD_SYNC(int ID, int iWaveTableId, int iOffsetOfFirstPointInWaveTable, int iNumberOfValues, double* pdValueArray);
PI_qGWD_SYNC = PIGCS.PI_qGWD_SYNC
PI_qGWD_SYNC.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
PI_qGWD_SYNC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qGWD(int ID, const int* iWaveTableIdsArray, int iNumberOfWaveTables, int iOffset, int nrValues, double** pdValarray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
PI_qGWD = PIGCS.PI_qGWD
PI_qGWD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
PI_qGWD.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WOS(int ID, const int* iWaveTableIdsArray, const double* pdValueArray, int iArraySize);
PI_WOS = PIGCS.PI_WOS
PI_WOS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_WOS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qWOS(int ID, const int* iWaveTableIdsArray, double* pdValueArray, int iArraySize);
PI_qWOS = PIGCS.PI_qWOS
PI_qWOS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qWOS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WTR(int ID, const int* piWaveGeneratorIdsArray, const int* piTableRateArray, const int* piInterpolationTypeArray, int iArraySize);
PI_WTR = PIGCS.PI_WTR
PI_WTR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_WTR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qWTR(int ID, const int* piWaveGeneratorIdsArray, int* piTableRateArray, int* piInterpolationTypeArray, int iArraySize);
PI_qWTR = PIGCS.PI_qWTR
PI_qWTR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qWTR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DDL(int ID, int iDdlTableId,  int iOffsetOfFirstPointInDdlTable,  int iNumberOfValues, const double* pdValueArray);
PI_DDL = PIGCS.PI_DDL
PI_DDL.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
PI_DDL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDDL_SYNC(int ID,  int iDdlTableId,  int iOffsetOfFirstPointInDdlTable,  int iNumberOfValues, double* pdValueArray);
PI_qDDL_SYNC = PIGCS.PI_qDDL_SYNC
PI_qDDL_SYNC.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
PI_qDDL_SYNC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDDL(int ID, const int* iDdlTableIdsArray, int iNumberOfDdlTables, int iOffset, int nrValues, double** pdValarray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
PI_qDDL = PIGCS.PI_qDDL
PI_qDDL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
PI_qDDL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DPO(int ID, const char* szAxes);
PI_DPO = PIGCS.PI_DPO
PI_DPO.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_DPO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qWMS(int ID, const int* piWaveTableIds, int* iWaveTableMaximumSize, int iArraySize);
PI_qWMS = PIGCS.PI_qWMS
PI_qWMS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qWMS.restype = ctypes.c_bool

# Trigger commands.
# BOOL PI_FUNC_DECL PI_TWC(int ID);
PI_TWC = PIGCS.PI_TWC
PI_TWC.argtypes = [ctypes.c_int]
PI_TWC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_TWS(int ID, const int* piTriggerChannelIdsArray, const int* piPointNumberArray, const int* piSwitchArray, int iArraySize);
PI_TWS = PIGCS.PI_TWS
PI_TWS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_TWS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTWS(int ID, const int* iTriggerChannelIdsArray, int iNumberOfTriggerChannels, int iOffset, int nrValues, double** pdValarray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
PI_qTWS = PIGCS.PI_qTWS
PI_qTWS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
PI_qTWS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_CTO(int ID, const int* piTriggerOutputIdsArray, const int* piTriggerParameterArray, const double* pdValueArray, int iArraySize);
PI_CTO = PIGCS.PI_CTO
PI_CTO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_CTO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_CTOString(int ID, const int* piTriggerOutputIdsArray, const int* piTriggerParameterArray, const char* szValueArray, int iArraySize);
PI_CTOString = PIGCS.PI_CTOString
PI_CTOString.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
PI_CTOString.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qCTO(int ID, const int* piTriggerOutputIdsArray, const int* piTriggerParameterArray, double* pdValueArray, int iArraySize);
PI_qCTO = PIGCS.PI_qCTO
PI_qCTO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qCTO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qCTOString(int ID, const int* piTriggerOutputIdsArray, const int* piTriggerParameterArray, char* szValueArray, int iArraySize, int maxBufLen);
PI_qCTOString = PIGCS.PI_qCTOString
PI_qCTOString.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
PI_qCTOString.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_TRO(int ID, const int* piTriggerChannelIds, const BOOL* pbTriggerChannelEnabel, int iArraySize);
PI_TRO = PIGCS.PI_TRO
PI_TRO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
PI_TRO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTRO(int ID, const int* piTriggerChannelIds, BOOL* pbTriggerChannelEnabel, int iArraySize);
PI_qTRO = PIGCS.PI_qTRO
PI_qTRO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
PI_qTRO.restype = ctypes.c_bool

# Record tabel commands.
# BOOL PI_FUNC_DECL PI_qHDR(int ID, char* szBuffer, int iBufferSize);
PI_qHDR = PIGCS.PI_qHDR
PI_qHDR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qHDR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTNR(int ID, int* piNumberOfRecordCannels);
PI_qTNR = PIGCS.PI_qTNR
PI_qTNR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qTNR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DRC(int ID, const int* piRecordTableIdsArray, const char* szRecordSourceIds, const int* piRecordOptionArray);
PI_DRC = PIGCS.PI_DRC
PI_DRC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
PI_DRC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDRC(int ID, const int* piRecordTableIdsArray, char* szRecordSourceIds, int* piRecordOptionArray, int iRecordSourceIdsBufferSize, int iRecordOptionArraySize);
PI_qDRC = PIGCS.PI_qDRC
PI_qDRC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
PI_qDRC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDRR_SYNC(int ID,  int iRecordTablelId,  int iOffsetOfFirstPointInRecordTable,  int iNumberOfValues, double* pdValueArray);
PI_qDRR_SYNC = PIGCS.PI_qDRR_SYNC
PI_qDRR_SYNC.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
PI_qDRR_SYNC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDRR(int ID, const int* piRecTableIdIdsArray,  int iNumberOfRecChannels,  int iOffsetOfFirstPointInRecordTable,  int iNumberOfValues, double** pdValueArray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
PI_qDRR = PIGCS.PI_qDRR
PI_qDRR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
PI_qDRR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_DRT(int ID, const int* piRecordChannelIdsArray, const int* piTriggerSourceArray, const char* szValues, int iArraySize);
PI_DRT = PIGCS.PI_DRT
PI_DRT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
PI_DRT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDRT(int ID, const int* piRecordChannelIdsArray, int* piTriggerSourceArray, char* szValues, int iArraySize, int iValueBufferLength);
PI_qDRT = PIGCS.PI_qDRT
PI_qDRT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
PI_qDRT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_RTR(int ID, int piReportTableRate);
PI_RTR = PIGCS.PI_RTR
PI_RTR.argtypes = [ctypes.c_int, ctypes.c_int]
PI_RTR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qRTR(int ID, int* piReportTableRate);
PI_qRTR = PIGCS.PI_qRTR
PI_qRTR.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qRTR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_WGR(int ID);
PI_WGR = PIGCS.PI_WGR
PI_WGR.argtypes = [ctypes.c_int]
PI_WGR.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDRL(int ID, const int* piRecordChannelIdsArray, int* piNuberOfRecordedValuesArray, int iArraySize);
PI_qDRL = PIGCS.PI_qDRL
PI_qDRL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qDRL.restype = ctypes.c_bool

# Piezo-Channel commands.
# BOOL PI_FUNC_DECL PI_VMA(int ID, const int* piPiezoChannelsArray, const double* pdValueArray, int iArraySize);
PI_VMA = PIGCS.PI_VMA
PI_VMA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_VMA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qVMA(int ID, const int* piPiezoChannelsArray, double* pdValueArray, int iArraySize);
PI_qVMA = PIGCS.PI_qVMA
PI_qVMA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qVMA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_VMI(int ID, const int* piPiezoChannelsArray, const double* pdValueArray, int iArraySize);
PI_VMI = PIGCS.PI_VMI
PI_VMI.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_VMI.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qVMI(int ID, const int* piPiezoChannelsArray, double* pdValueArray, int iArraySize);
PI_qVMI = PIGCS.PI_qVMI
PI_qVMI.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qVMI.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_VOL(int ID, const int* piPiezoChannelsArray, const double* pdValueArray, int iArraySize);
PI_VOL = PIGCS.PI_VOL
PI_VOL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_VOL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qVOL(int ID, const int* piPiezoChannelsArray, double* pdValueArray, int iArraySize);
PI_qVOL = PIGCS.PI_qVOL
PI_qVOL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qVOL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTPC(int ID, int* piNumberOfPiezoChannels);
PI_qTPC = PIGCS.PI_qTPC
PI_qTPC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qTPC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_ONL(int ID, const int* iPiezoCannels, const int* piValueArray, int iArraySize);
PI_ONL = PIGCS.PI_ONL
PI_ONL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_ONL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qONL(int ID, const int* iPiezoCannels, int* piValueArray, int iArraySize);
PI_qONL = PIGCS.PI_qONL
PI_qONL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qONL.restype = ctypes.c_bool

# Sensor-Channel commands.
# BOOL PI_FUNC_DECL PI_qTAD(int ID, const int* piSensorsChannelsArray, int* piValueArray, int iArraySize);
PI_qTAD = PIGCS.PI_qTAD
PI_qTAD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qTAD.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTNS(int ID, const int* piSensorsChannelsArray, double* pdValueArray, int iArraySize);
PI_qTNS = PIGCS.PI_qTNS
PI_qTNS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qTNS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTSP(int ID, const int* piSensorsChannelsArray, double* pdValueArray, int iArraySize);
PI_qTSP = PIGCS.PI_qTSP
PI_qTSP.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qTSP.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SCN(int ID, const int* piSensorsChannelsArray, const int* piValueArray, int iArraySize);
PI_SCN = PIGCS.PI_SCN
PI_SCN.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_SCN.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSCN(int ID, const int* piSensorsChannelsArray, int* piValueArray, int iArraySize);
PI_qSCN = PIGCS.PI_qSCN
PI_qSCN.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qSCN.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTSC(int ID, int* piNumberOfSensorChannels);
PI_qTSC = PIGCS.PI_qTSC
PI_qTSC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qTSC.restype = ctypes.c_bool

# PIEZOWALK(R)-Channel commands.
# BOOL PI_FUNC_DECL PI_APG(int ID, const int* piPIEZOWALKChannelsArray, int iArraySize);
PI_APG = PIGCS.PI_APG
PI_APG.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_APG.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qAPG(int ID, const int* piPIEZOWALKChannelsArray, int* piValueArray, int iArraySize);
PI_qAPG = PIGCS.PI_qAPG
PI_qAPG.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qAPG.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_OAC(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
PI_OAC = PIGCS.PI_OAC
PI_OAC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_OAC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qOAC(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
PI_qOAC = PIGCS.PI_qOAC
PI_qOAC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qOAC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_OAD(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
PI_OAD = PIGCS.PI_OAD
PI_OAD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_OAD.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qOAD(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
PI_qOAD = PIGCS.PI_qOAD
PI_qOAD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qOAD.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_ODC(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
PI_ODC = PIGCS.PI_ODC
PI_ODC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_ODC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qODC(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
PI_qODC = PIGCS.PI_qODC
PI_qODC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qODC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_OCD(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
PI_OCD = PIGCS.PI_OCD
PI_OCD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_OCD.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qOCD(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
PI_qOCD = PIGCS.PI_qOCD
PI_qOCD.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qOCD.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_OSM(int ID, const int* piPIEZOWALKChannelsArray, const int* piValueArray, int iArraySize);
PI_OSM = PIGCS.PI_OSM
PI_OSM.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_OSM.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qOSM(int ID, const int* piPIEZOWALKChannelsArray, int* piValueArray, int iArraySize);
PI_qOSM = PIGCS.PI_qOSM
PI_qOSM.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qOSM.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_OSMf(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
PI_OSMf = PIGCS.PI_OSMf
PI_OSMf.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_OSMf.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qOSMf(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
PI_qOSMf = PIGCS.PI_qOSMf
PI_qOSMf.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qOSMf.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_OVL(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
PI_OVL = PIGCS.PI_OVL
PI_OVL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_OVL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qOVL(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
PI_qOVL = PIGCS.PI_qOVL
PI_qOVL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qOVL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qOSN(int ID, const int* piPIEZOWALKChannelsArray, int* piValueArray, int iArraySize);
PI_qOSN = PIGCS.PI_qOSN
PI_qOSN.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qOSN.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_SSA(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
PI_SSA = PIGCS.PI_SSA
PI_SSA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_SSA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSSA(int ID, const int* piPIEZOWALKChannelsArray, double* pdValueArray, int iArraySize);
PI_qSSA = PIGCS.PI_qSSA
PI_qSSA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qSSA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_RNP(int ID, const int* piPIEZOWALKChannelsArray, const double* pdValueArray, int iArraySize);
PI_RNP = PIGCS.PI_RNP
PI_RNP.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_RNP.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_PGS(int ID, const int* piPIEZOWALKChannelsArray, int iArraySize);
PI_PGS = PIGCS.PI_PGS
PI_PGS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_PGS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTAC(int ID, int* pnNrChannels);
PI_qTAC = PIGCS.PI_qTAC
PI_qTAC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qTAC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qTAV(int ID, const int* piChannelsArray, double* pdValueArray, int iArraySize);
PI_qTAV = PIGCS.PI_qTAV
PI_qTAV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qTAV.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_OMA(int ID, const char* szAxes, const double* pdValueArray);
PI_OMA = PIGCS.PI_OMA
PI_OMA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_OMA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qOMA(int ID, const char* szAxes, double* pdValueArray);
PI_qOMA = PIGCS.PI_qOMA
PI_qOMA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_qOMA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_OMR(int ID, const char* szAxes, const double* pdValueArray);
PI_OMR = PIGCS.PI_OMR
PI_OMR.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
PI_OMR.restype = ctypes.c_bool

# Joystick
# BOOL PI_FUNC_DECL PI_qJAS(int ID, const int* iJoystickIDsArray, const int* iAxesIDsArray, double* pdValueArray, int iArraySize);
PI_qJAS = PIGCS.PI_qJAS
PI_qJAS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qJAS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_JAX(int ID,  int iJoystickID,  int iAxesID, const char* szAxesBuffer);
PI_JAX = PIGCS.PI_JAX
PI_JAX.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
PI_JAX.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qJAX(int ID, const int* iJoystickIDsArray, const int* iAxesIDsArray, int iArraySize, char* szAxesBuffer, int iBufferSize);
PI_qJAX = PIGCS.PI_qJAX
PI_qJAX.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qJAX.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qJBS(int ID, const int* iJoystickIDsArray, const int* iButtonIDsArray, BOOL* pbValueArray, int iArraySize);
PI_qJBS = PIGCS.PI_qJBS
PI_qJBS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
PI_qJBS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_JDT(int ID, const int* iJoystickIDsArray, const int* iAxisIDsArray,const int* piValueArray, int iArraySize);
PI_JDT = PIGCS.PI_JDT
PI_JDT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_JDT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_JLT(int ID, int iJoystickID, int iAxisID, int iStartAdress, const double* pdValueArray,int iArraySize);
PI_JLT = PIGCS.PI_JLT
PI_JLT.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_JLT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qJLT(int ID, const int* iJoystickIDsArray, const int* iAxisIDsArray,  int iNumberOfTables,  int iOffsetOfFirstPointInTable,  int iNumberOfValues, double** pdValueArray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
PI_qJLT = PIGCS.PI_qJLT
PI_qJLT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
PI_qJLT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_JON(int ID, const int* iJoystickIDsArray, const BOOL* pbValueArray, int iArraySize);
PI_JON = PIGCS.PI_JON
PI_JON.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
PI_JON.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qJON(int ID, const int* iJoystickIDsArray, BOOL* pbValueArray, int iArraySize);
PI_qJON = PIGCS.PI_qJON
PI_qJON.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.c_int]
PI_qJON.restype = ctypes.c_bool

# fast scan commands
# BOOL PI_FUNC_DECL PI_AAP(int ID, const char* szAxis1, double dLength1, const char* szAxis2, double dLength2, double dAlignStep, int iNrRepeatedPositions, int iAnalogInput);
PI_AAP = PIGCS.PI_AAP
PI_AAP.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
PI_AAP.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_FIO(int ID, const char* szAxis1, double dLength1, const char* szAxis2, double dLength2, double dThreshold, double dLinearStep, double dAngleScan, int iAnalogInput);
PI_FIO = PIGCS.PI_FIO
PI_FIO.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
PI_FIO.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_FLM(int ID, const char* szAxis, double dLength, double dThreshold, int iAnalogInput, int iDirection);
PI_FLM = PIGCS.PI_FLM
PI_FLM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
PI_FLM.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_FLS(int ID, const char* szAxis, double dLength, double dThreshold, int iAnalogInput, int iDirection);
PI_FLS = PIGCS.PI_FLS
PI_FLS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
PI_FLS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_FSA(int ID, const char* szAxis1, double dLength1, const char* szAxis2, double dLength2, double dThreshold, double dDistance, double dAlignStep, int iAnalogInput);
PI_FSA = PIGCS.PI_FSA
PI_FSA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
PI_FSA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_FSC(int ID, const char* szAxis1, double dLength1, const char* szAxis2, double dLength2, double dThreshold, double dDistance, int iAnalogInput);
PI_FSC = PIGCS.PI_FSC
PI_FSC.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
PI_FSC.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_FSM(int ID, const char* szAxis1, double dLength1, const char* szAxis2, double dLength2, double dThreshold, double dDistance, int iAnalogInput);
PI_FSM = PIGCS.PI_FSM
PI_FSM.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_double, ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
PI_FSM.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qFSS(int ID, int* piResult);
PI_qFSS = PIGCS.PI_qFSS
PI_qFSS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
PI_qFSS.restype = ctypes.c_bool

# optical boards (hexapod)
# BOOL PI_FUNC_DECL PI_SGA(int ID, const int* piAnalogChannelIds, const int* piGainValues, int iArraySize);
PI_SGA = PIGCS.PI_SGA
PI_SGA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_SGA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qSGA(int ID, const int* piAnalogChannelIds, int* piGainValues, int iArraySize);
PI_qSGA = PIGCS.PI_qSGA
PI_qSGA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qSGA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_NAV(int ID, const int* piAnalogChannelIds, const int* piNrReadingsValues, int iArraySize);
PI_NAV = PIGCS.PI_NAV
PI_NAV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_NAV.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qNAV(int ID, const int* piAnalogChannelIds, int* piNrReadingsValues, int iArraySize);
PI_qNAV = PIGCS.PI_qNAV
PI_qNAV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qNAV.restype = ctypes.c_bool
# more hexapod specific
# BOOL	PI_FUNC_DECL	PI_GetDynamicMoveBufferSize(int ID, int *iSize);
PI_GetDynamicMoveBufferSize = PIGCS.PI_GetDynamicMoveBufferSize
PI_GetDynamicMoveBufferSize.argtypes = [ctypes.c_int, ctypes.c_int]
PI_GetDynamicMoveBufferSize.restype = ctypes.c_bool

# PIShift
# BOOL PI_FUNC_DECL PI_qCOV(int ID, const int* piChannelsArray, double* pdValueArray, int iArraySize);
PI_qCOV = PIGCS.PI_qCOV
PI_qCOV.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qCOV.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_MOD(int ID, const char* szItems, const unsigned int* iModeArray, const char* szValues);
PI_MOD = PIGCS.PI_MOD
PI_MOD.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p]
PI_MOD.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qMOD(int ID, const char* szItems, const unsigned int* iModeArray, char* szValues, int iMaxValuesSize);
PI_qMOD = PIGCS.PI_qMOD
PI_qMOD.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p, ctypes.c_int]
PI_qMOD.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qDIA(int ID, const unsigned int* iIDArray, char* szValues,  int iBufferSize, int iArraySize);
PI_qDIA = PIGCS.PI_qDIA
PI_qDIA.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
PI_qDIA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHDI(int ID, char* szBuffer,  int iBufferSize);
PI_qHDI = PIGCS.PI_qHDI
PI_qHDI.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qHDI.restype = ctypes.c_bool

# HID
# BOOL PI_FUNC_DECL PI_qHIS(int ID, char* szBuffer,  int iBufferSize);
PI_qHIS = PIGCS.PI_qHIS
PI_qHIS.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_qHIS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_HIS(int ID, const int* iDeviceIDsArray, const int* iItemIDsArray, const int* iPropertyIDArray, const char* szValues, int iArraySize);
PI_HIS = PIGCS.PI_HIS
PI_HIS.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_int]
PI_HIS.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHIE(int ID, const int* iDeviceIDsArray, const int* iAxesIDsArray, double* pdValueArray, int iArraySize);
PI_qHIE = PIGCS.PI_qHIE
PI_qHIE.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_qHIE.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHIB(int ID, const int* iDeviceIDsArray, const int* iButtonIDsArray, int* pbValueArray, int iArraySize);
PI_qHIB = PIGCS.PI_qHIB
PI_qHIB.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qHIB.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_HIL(int ID, const int* iDeviceIDsArray, const int* iLED_IDsArray, const int* pnValueArray, int iArraySize);
PI_HIL = PIGCS.PI_HIL
PI_HIL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_HIL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHIL(int ID, const int* iDeviceIDsArray, const int* iLED_IDsArray, int* pnValueArray, int iArraySize);
PI_qHIL = PIGCS.PI_qHIL
PI_qHIL.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qHIL.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_HIN(int ID, const char* szAxes, const BOOL* pbValueArray);
PI_HIN = PIGCS.PI_HIN
PI_HIN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_HIN.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHIN(int ID, const char* szAxes, BOOL* pbValueArray);
PI_qHIN = PIGCS.PI_qHIN
PI_qHIN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_bool)]
PI_qHIN.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_HIA(int ID, const char* szAxes, const int* iFunctionArray, const int* iDeviceIDsArray, const int* iAxesIDsArray);
PI_HIA = PIGCS.PI_HIA
PI_HIA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
PI_HIA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHIA(int ID, const char* szAxes, const int* iFunctionArray, int* iDeviceIDsArray, int* iAxesIDsArray);
PI_qHIA = PIGCS.PI_qHIA
PI_qHIA.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
PI_qHIA.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_HDT(int ID, const int* iDeviceIDsArray, const int* iAxisIDsArray, const int* piValueArray, int iArraySize);
PI_HDT = PIGCS.PI_HDT
PI_HDT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_HDT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHDT(int ID, const int* iDeviceIDsArray, const int* iAxisIDsArray, int* piValueArray, int iArraySize);
PI_qHDT = PIGCS.PI_qHDT
PI_qHDT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
PI_qHDT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_HIT(int ID, const int* piTableIdsArray, const int* piPointNumberArray, const double* pdValueArray, int iArraySize);
PI_HIT = PIGCS.PI_HIT
PI_HIT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.c_int]
PI_HIT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qHIT(int ID, const int* piTableIdsArray,  int iNumberOfTables,  int iOffsetOfFirstPointInTable,  int iNumberOfValues, double** pdValueArray, char* szGcsArrayHeader, int iGcsArrayHeaderMaxSize);
PI_qHIT = PIGCS.PI_qHIT
PI_qHIT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_char_p, ctypes.c_int]
PI_qHIT.restype = ctypes.c_bool
# BOOL PI_FUNC_DECL PI_qMAN(int ID, const char* szCommand, char* szBuffer,  int iBufferSize);
PI_qMAN = PIGCS.PI_qMAN
PI_qMAN.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
PI_qMAN.restype = ctypes.c_bool

# Spezial
# BOOL	PI_FUNC_DECL	PI_GetSupportedParameters(int ID, int* piParameterIdArray, int* piCommandLevelArray, int* piMemoryLocationArray, int* piDataTypeArray, int* piNumberOfItems, const int iiBufferSize, char* szParameterName, const int iMaxParameterNameSize);
PI_GetSupportedParameters = PIGCS.PI_GetSupportedParameters
PI_GetSupportedParameters.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
PI_GetSupportedParameters.restype = ctypes.c_bool
# BOOL	PI_FUNC_DECL	PI_GetSupportedControllers(char* szBuffer, int iBufferSize);
PI_GetSupportedControllers = PIGCS.PI_GetSupportedControllers
PI_GetSupportedControllers.argtypes = [ctypes.c_char_p, ctypes.c_int]
PI_GetSupportedControllers.restype = ctypes.c_bool
# int		PI_FUNC_DECL	PI_GetAsyncBufferIndex(int ID);
PI_GetAsyncBufferIndex = PIGCS.PI_GetAsyncBufferIndex
PI_GetAsyncBufferIndex.argtypes = [ctypes.c_int]
PI_GetAsyncBufferIndex.restype = ctypes.c_int
# BOOL	PI_FUNC_DECL	PI_GetAsyncBuffer(int ID, double** pdValueArray);
PI_GetAsyncBuffer = PIGCS.PI_GetAsyncBuffer
PI_GetAsyncBuffer.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double))]
PI_GetAsyncBuffer.restype = ctypes.c_bool
# BOOL	PI_FUNC_DECL	PI_AddStage(int ID, const char* szAxes);
PI_AddStage = PIGCS.PI_AddStage
PI_AddStage.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_AddStage.restype = ctypes.c_bool
# BOOL	PI_FUNC_DECL	PI_RemoveStage(int ID, const char* szStageName);
PI_RemoveStage = PIGCS.PI_RemoveStage
PI_RemoveStage.argtypes = [ctypes.c_int, ctypes.c_char_p]
PI_RemoveStage.restype = ctypes.c_bool
# BOOL	PI_FUNC_DECL	PI_OpenUserStagesEditDialog(int ID);
PI_OpenUserStagesEditDialog = PIGCS.PI_OpenUserStagesEditDialog
PI_OpenUserStagesEditDialog.argtypes = [ctypes.c_int]
PI_OpenUserStagesEditDialog.restype = ctypes.c_bool
# BOOL	PI_FUNC_DECL	PI_OpenPiStagesEditDialog(int ID);
PI_OpenPiStagesEditDialog = PIGCS.PI_OpenPiStagesEditDialog
PI_OpenPiStagesEditDialog.argtypes = [ctypes.c_int]
PI_OpenPiStagesEditDialog.restype = ctypes.c_bool

# for internal use
# BOOL	PI_FUNC_DECL	PI_DisableSingleStagesDatFiles(int ID,BOOL bDisable);
PI_DisableSingleStagesDatFiles = PIGCS.PI_DisableSingleStagesDatFiles
PI_DisableSingleStagesDatFiles.argtypes = [ctypes.c_int, ctypes.c_bool]
PI_DisableSingleStagesDatFiles.restype = ctypes.c_bool
# BOOL	PI_FUNC_DECL	PI_DisableUserStagesDatFiles(int ID,BOOL bDisable);
PI_DisableUserStagesDatFiles = PIGCS.PI_DisableUserStagesDatFiles
PI_DisableUserStagesDatFiles.argtypes = [ctypes.c_int, ctypes.c_bool]
PI_DisableUserStagesDatFiles.restype = ctypes.c_bool




