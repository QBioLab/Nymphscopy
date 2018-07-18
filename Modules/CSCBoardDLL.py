import ctypes

def CSC(dll):
	# Ref: https://docs.python.org/3.6/library/ctypes.html#fundamental-data-types
	# class ctypes.WinDLL(name, mode=DEFAULT_MODE, handle=None, use_errno=False, use_last_error=False). Windows only: Instances of this class represent loaded shared libraries, functions in these libraries use the stdcall calling convention, and are assumed to return int by default. On Windows CE only the standard calling convention is used, for convenience the WinDLL and OleDLL use the standard calling convention on this platform.
	# class ctypes.c_char_p represents the C char * datatype when it points to a zero-terminated string. For a general character pointer that may also point to binary data, POINTER(c_char) must be used. The constructor accepts an integer address, or a bytes object.
	
	#pragma once #define IN #define OUT
	
	# Basic Functions
	# int __stdcall OpenUSB_Board(int deviceIndex,void *handle);
	dll.OpenUSB_Board.argtypes = [ctypes.c_int, ctypes.c_void_p]
	dll.OpenUSB_Board.restype = ctypes.c_int
	# int __stdcall LoadFPGA_FirmwareProgram(IN char* rbfFilePath);
	dll.LoadFPGA_FirmwareProgram.argtypes = [ctypes.c_char_p]
	dll.LoadFPGA_FirmwareProgram.restype = ctypes.c_int
	# int __stdcall SetLaserMode(IN int laserType,IN int standby,IN float frequency,IN float pulseWidth);
	dll.SetLaserMode.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float]
	dll.LoadFPGA_FirmwareProgram.restype = ctypes.c_int
	# int  __stdcall SetSystemParameters(IN double rangeX, IN double rangeY, IN bool exchangeXY, IN bool invertX, IN bool invertY, IN int startMarkMode);
	dll.SetSystemParameters.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_int]
	dll.SetSystemParameters.restype = ctypes.c_int
	# int  __stdcall SetCorrectParameters_0(IN double xCorrection, IN double yCorrection, IN double xShear, IN double yShear, IN double xLadder, IN double yLadder, IN double ratioX, IN double ratioY, IN double ratioZ);
	dll.SetCorrectParameters_0.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
	dll.SetCorrectParameters_0.restype = ctypes.c_int
	# int  __stdcall SetCorrectParameters_1(IN double ratioX, IN double ratioY, IN double ratioZ, IN char* filePath);
	dll.SetCorrectParameters_1.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_char_p]
	dll.SetCorrectParameters_1.restype = ctypes.c_int
	# void __stdcall WriteDataEnd();
	dll.WriteDataEnd.argtypes = None
	dll.WriteDataEnd.restype = None
	# void __stdcall SetOverallMarkCounts(IN int count);
	dll.SetOverallMarkCounts.argtypes = [ctypes.c_int]
	dll.SetOverallMarkCounts.restype = None
	# bool __stdcall IsReadDataEnd(); This function does not exists
	#dll.IsReadDataEnd.argtypes = None
	#dll.IsReadDataEnd.restype = ctypes.c_bool
	# bool __stdcall IsMarkEnd();
	dll.IsMarkEnd.argtypes = None
	dll.IsMarkEnd.restype = ctypes.c_bool
	# bool __stdcall StartMark();
	dll.StartMark.argtypes = None
	dll.StartMark.restype = ctypes.c_bool
	# unsigned __int64 __stdcall GetProducedData();
	dll.GetProducedData.argtypes = None
	dll.GetProducedData.restype = ctypes.c_ulonglong
	# int __stdcall SetMarkParameter(IN int index, IN int markCounts, IN int isBitmap, IN float markSpeed, IN float jumpSpeed, IN float jumpDelay, IN float polygonDelay, IN float laserOnDelay, IN float laserOffDelay, IN float polygonKillerTime, IN float laserFrequency, IN float current, IN float firstPulseKillerLength, IN float pulseWidth, IN float firstPulseWidth, IN float incrementStep, IN float dotSpace);
	dll.SetMarkParameter.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
	dll.SetMarkParameter.restype = ctypes.c_int
	# bool  __stdcall DownloadMarkParameters();
	dll.DownloadMarkParameters.argtypes = None
	dll.DownloadMarkParameters.restype = ctypes.c_bool
	# bool __stdcall SetFirstMarkParameter(IN int pen);
	dll.SetFirstMarkParameter.argtypes = [ctypes.c_int]
	dll.SetFirstMarkParameter.restype = ctypes.c_bool
	# bool __stdcall ReadyMark();
	dll.ReadyMark.argtypes = None
	dll.ReadyMark.restype = ctypes.c_bool
	# bool __stdcall ReadyPreview();
	dll.ReadyPreview.argtypes = None
	dll.ReadyPreview.restype = ctypes.c_bool
	# bool __stdcall StartReadDataThread();
	dll.StartReadDataThread.argtypes = None
	dll.StartReadDataThread.restype = ctypes.c_bool
	# int __stdcall ZeroCounter();
	dll.ZeroCounter.argtypes = None
	dll.ZeroCounter.restype = ctypes.c_int
	# bool __stdcall StopMark();
	dll.StopMark.argtypes = None
	dll.StopMark.restype = ctypes.c_bool
	# bool __stdcall StopPreview();
	dll.StopPreview.argtypes = None
	dll.StopPreview.restype = ctypes.c_bool
	# bool __stdcall StopCalcData();
	dll.StopCalcData.argtypes = None
	dll.StopCalcData.restype = ctypes.c_bool
	# bool __stdcall SetDelayPA_MO(IN float delay);
	dll.SetDelayPA_MO.argtypes = [ctypes.c_float]
	dll.SetDelayPA_MO.restype = ctypes.c_bool
	# bool __stdcall SPI_SimmerCurrent(IN double simmer);
	dll.SPI_SimmerCurrent.argtypes = [ctypes.c_double]
	dll.SPI_SimmerCurrent.restype = ctypes.c_bool
	# bool __stdcall SPI_ModeSelect(IN int mode);
	dll.SPI_ModeSelect.argtypes = [ctypes.c_int]
	dll.SPI_ModeSelect.restype = ctypes.c_bool
	# bool __stdcall SPI_WaveForm(IN int wave);
	dll.SPI_WaveForm.argtypes = [ctypes.c_int]
	dll.SPI_WaveForm.restype = ctypes.c_bool
	# int __stdcall SetExternalStartSignalMode(IN int mode);
	dll.SetExternalStartSignalMode.argtypes = [ctypes.c_int]
	dll.SetExternalStartSignalMode.restype = ctypes.c_int
	# int __stdcall GetCSCInterfaceVersion(OUT char *version);
	dll.GetCSCInterfaceVersion.argtypes = [ctypes.c_char_p]
	dll.GetCSCInterfaceVersion.restype = ctypes.c_int
	# bool __stdcall OpenGuideLight();
	dll.OpenGuideLight.argtypes = None
	dll.OpenGuideLight.restype = ctypes.c_bool
	# bool __stdcall CloseGuideLight();
	dll.CloseGuideLight.argtypes = None
	dll.CloseGuideLight.restype = ctypes.c_bool
	# void __stdcall  CloseUSB_Board();
	dll.CloseUSB_Board.argtypes = None
	dll.CloseUSB_Board.restype = None
	
	# Functions Reading Information of CSC-USB Board
	# bool __stdcall GetMarkStatus();
	dll.GetMarkStatus.argtypes = None
	dll.GetMarkStatus.restype = ctypes.c_bool
	# unsigned long __stdcall GetMarkTime();
	dll.GetMarkTime.argtypes = None
	dll.GetMarkTime.restype = ctypes.c_ulong
	# bool __stdcall GetMarkCounts(OUT unsigned char &internalMarkCounts, OUT unsigned char &externalMarkCounts);
	dll.GetMarkCounts.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)]
	dll.GetMarkCounts.restype = ctypes.c_bool
	# int __stdcall GetUSB_BoardCounts();
	dll.GetUSB_BoardCounts.argtypes = None
	dll.GetUSB_BoardCounts.restype = ctypes.c_int
	# int __stdcall GetUSB_FirmwareVersion(OUT char *version); 
	dll.GetUSB_FirmwareVersion.argtypes = [ctypes.c_char_p]
	dll.GetUSB_FirmwareVersion.restype = ctypes.c_int
	# int __stdcall GetFPGA_FirmwareVersion(OUT char *version);
	dll.GetFPGA_FirmwareVersion.argtypes = [ctypes.c_char_p]
	dll.GetFPGA_FirmwareVersion.restype = ctypes.c_int
	# bool __stdcall GetLaserAndScannerStatus(OUT int &laserStatus, OUT int &scannerStatus);
	dll.GetLaserAndScannerStatus.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
	dll.GetLaserAndScannerStatus.restype = ctypes.c_bool
	# int __stdcall ReadUSB_BoardSN(OUT char *boardSN);
	dll.ReadUSB_BoardSN.argtypes = [ctypes.c_char_p]
	dll.ReadUSB_BoardSN.restype = ctypes.c_int
	# int __stdcall ReadUSB_BoardSN_ByIndex(IN int index, OUT char *boardSN);
	dll.ReadUSB_BoardSN_ByIndex.argtypes = [ctypes.c_int, ctypes.c_char_p]
	dll.ReadUSB_BoardSN_ByIndex.restype = ctypes.c_int
	# bool __stdcall GetScannerPosition(OUT float& xPos, OUT float& yPos);
	dll.GetScannerPosition.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]
	dll.GetScannerPosition.restype = ctypes.c_bool
	
	# Commands Opening Lasers
	# bool __stdcall LaserSignalOn();
	dll.LaserSignalOn.argtypes = None
	dll.LaserSignalOn.restype = ctypes.c_bool
	# bool __stdcall LaserSignalOff();
	dll.LaserSignalOff.argtypes = None
	dll.LaserSignalOff.restype = ctypes.c_bool
	
	# AD Commands
	# bool __stdcall InitAD();
	dll.InitAD.argtypes = None
	dll.InitAD.restype = ctypes.c_bool
	# int __stdcall GetAD();
	dll.GetAD.argtypes = None
	dll.GetAD.restype = ctypes.c_int
	
	# I/O Control Commands
	# bool __stdcall Write_IO_Port(IN unsigned char port);
	dll.Write_IO_Port.argtypes = [ctypes.c_ubyte]
	dll.Write_IO_Port.restype = ctypes.c_bool
	# unsigned char __stdcall GetOutputPortState();
	dll.GetOutputPortState.argtypes = None
	dll.GetOutputPortState.restype = ctypes.c_ubyte
	# unsigned short __stdcall Read_IO_Port();
	dll.Read_IO_Port.argtypes = None
	dll.Read_IO_Port.restype = ctypes.c_ushort
	# bool __stdcall GetExternalStartStopSignal(OUT int &start, OUT int &stop);
	dll.GetExternalStartStopSignal.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
	dll.GetExternalStartStopSignal.restype = ctypes.c_bool
	# bool __stdcall ResetStartStopSignal();
	dll.ResetStartStopSignal.argtypes = None
	dll.ResetStartStopSignal.restype = ctypes.c_bool
	
	# I/O List Commands
	# int  __stdcall  InputCommand(IN unsigned char port);
	dll.InputCommand.argtypes = [ctypes.c_ubyte]
	dll.InputCommand.restype = ctypes.c_int
	# int  __stdcall  OutputCommand(IN unsigned char port, IN int outMode, IN int level, IN int outputPulseWidth);
	dll.OutputCommand.argtypes = [ctypes.c_ubyte, ctypes.c_int, ctypes.c_int, ctypes.c_int]
	dll.OutputCommand.restype = ctypes.c_int
	
	# Step Motor Control Commands
	# int __stdcall SetStepMotorParameters(IN int motorType, IN int direction, IN float pitch, IN float pulsePerRevolution, IN float subdivision, IN float correctionFactor, IN float reductionRatio, IN float startSpeed, IN float speed, IN float speedupTime);
	dll.SetStepMotorParameters.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
	dll.SetStepMotorParameters.restype = ctypes.c_int
	# bool __stdcall SetStepMotorLimitDirect(IN int direction);
	dll.SetStepMotorLimitDirect.argtypes = [ctypes.c_int]
	dll.SetStepMotorLimitDirect.restype = ctypes.c_bool
	# bool __stdcall StepMotorZeroCounter(IN int type);
	dll.StepMotorZeroCounter.argtypes = [ctypes.c_int]
	dll.StepMotorZeroCounter.restype = ctypes.c_bool
	# bool __stdcall GetStepMotorPosition(IN int stepMotorType, OUT float &motorCurPos);
	dll.GetStepMotorPosition.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
	dll.GetStepMotorPosition.restype = ctypes.c_bool
	# void __stdcall GetStepMotorHomeStatus(OUT bool &xhome,OUT bool &yhome,OUT bool &zhome,OUT bool &rhome);
	dll.GetStepMotorHomeStatus.argtypes = [ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool)]
	dll.GetStepMotorHomeStatus.restype = None
	# void __stdcall GetStepMotorLimitStatus(OUT bool &xlimit,OUT bool &ylimit,OUT bool &zlimit,OUT bool &rlimit);
	dll.GetStepMotorLimitStatus.argtypes = [ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool)]
	dll.GetStepMotorLimitStatus.restype = None
	# void __stdcall GetStepMotorStatus(OUT bool &xMotor,OUT bool &yMotor,OUT bool &zMotor,OUT bool &rMotor);
	dll.GetStepMotorStatus.argtypes = [ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool)]
	dll.GetStepMotorStatus.restype = None
	# bool __stdcall ReturnHome_X(IN unsigned long frequency);
	dll.ReturnHome_X.argtypes = [ctypes.c_ulong] # frequency = speed
	dll.ReturnHome_X.restype = ctypes.c_bool
	# bool __stdcall StartStepMotor_X(IN float distance, IN unsigned long frequency, IN unsigned long startFrequency, IN unsigned long speedUpTime);
	dll.StartStepMotor_X.argtypes = [ctypes.c_float, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong] # frequency = speed, startFrequency = startSpeed
	dll.StartStepMotor_X.restype = ctypes.c_bool
	# bool __stdcall StopStepMotor_X();
	dll.StopStepMotor_X.argtypes = None
	dll.StopStepMotor_X.restype = ctypes.c_bool
	# bool __stdcall ReturnHome_Y(IN unsigned long frequency);
	dll.ReturnHome_Y.argtypes = [ctypes.c_ulong] # frequency = speed
	dll.ReturnHome_Y.restype = ctypes.c_bool
	# bool __stdcall StartStepMotor_Y(IN float distance, IN unsigned long frequency, IN unsigned long startFrequency, IN unsigned long speedUpTime);
	dll.StartStepMotor_Y.argtypes = [ctypes.c_float, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong] # frequency = speed, startFrequency = startSpeed
	dll.StartStepMotor_Y.restype = ctypes.c_bool
	# bool __stdcall StopStepMotor_Y();
	dll.StopStepMotor_Y.argtypes = None
	dll.StopStepMotor_Y.restype = ctypes.c_bool
	# bool __stdcall ReturnHome_Z(IN unsigned long frequency);
	dll.ReturnHome_Z.argtypes = [ctypes.c_ulong] # frequency = speed
	dll.ReturnHome_Z.restype = ctypes.c_bool
	# bool __stdcall StartStepMotor_Z(IN float distance, IN unsigned long frequency, IN unsigned long startFrequency, IN unsigned long speedUpTime);
	dll.StartStepMotor_Z.argtypes = [ctypes.c_float, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong] # frequency = speed, startFrequency = startSpeed
	dll.StartStepMotor_Z.restype = ctypes.c_bool
	# bool __stdcall StopStepMotor_Z();
	dll.StopStepMotor_Z.argtypes = None
	dll.StopStepMotor_Z.restype = ctypes.c_bool
	# bool __stdcall ReturnHome_R(IN unsigned long frequency);
	dll.ReturnHome_R.argtypes = [ctypes.c_ulong] # frequency = speed
	dll.ReturnHome_R.restype = ctypes.c_bool
	# bool __stdcall StartStepMotor_R(IN float angle, IN unsigned long frequency, IN unsigned long startFrequency, IN unsigned long speedUpTime);
	dll.StartStepMotor_R.argtypes = [ctypes.c_float, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong] # frequency = speed, startFrequency = startSpeed
	dll.StartStepMotor_R.restype = ctypes.c_bool
	# bool __stdcall StopStepMotor_R();
	dll.StopStepMotor_R.argtypes = None
	dll.StopStepMotor_R.restype = ctypes.c_bool
	
	# Step Motor List Commands
	# int __stdcall MoveStepMotorCommand_XY(IN double startPositionX, IN double startPositionY, IN double endPositionX, IN double endPositionY);
	dll.MoveStepMotorCommand_XY.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
	dll.MoveStepMotorCommand_XY.restype = ctypes.c_int
	# int  __stdcall  MoveStepMotorCommand_Z(IN double startPosition, IN double endPosition);
	dll.MoveStepMotorCommand_Z.argtypes = [ctypes.c_double, ctypes.c_double]
	dll.MoveStepMotorCommand_Z.restype = ctypes.c_int
	# int  __stdcall  RotateStepMotorCommand_R(IN float angle);
	dll.RotateStepMotorCommand_R.argtypes = [ctypes.c_float]
	dll.RotateStepMotorCommand_R.restype = ctypes.c_int
	
	# Delay Command
	# int  __stdcall  DelayCommand(IN int delay);
	dll.DelayCommand.argtypes = [ctypes.c_int]
	dll.DelayCommand.restype = ctypes.c_int
	
	# Mark Commands
	# int __stdcall MarkCommand_Point(IN double x, IN double y, IN int type, IN int tp);
	dll.MarkCommand_Point.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
	dll.MarkCommand_Point.restype = ctypes.c_int
	# int __stdcall MarkCommand_Vector( IN int length, IN double* sitsetX, IN double* sitsetY);
	dll.MarkCommand_Vector.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
	dll.MarkCommand_Vector.restype = ctypes.c_int
	# int  __stdcall  MarkCommand_Bitmap( IN int length, IN double* sitsetX, IN double* sitsetY, IN int* sitsetGray);
	dll.MarkCommand_Bitmap.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int)]
	dll.MarkCommand_Bitmap.restype = ctypes.c_int
	
	# Command Change Pens
	# int __stdcall ChangePensCommand(IN unsigned char pen);
	dll.ChangePensCommand.argtypes = [ctypes.c_ubyte]
	dll.ChangePensCommand.restype = ctypes.c_int
	
	# Ending Mark Command
	# int  __stdcall  EndCommand();
	dll.EndCommand.argtypes = None
	dll.EndCommand.restype = ctypes.c_int
	
	# Jumping Control Commands
	# int __stdcall Goto_XY(IN double x, IN double y);
	dll.Goto_XY.argtypes = [ctypes.c_double, ctypes.c_double]
	dll.Goto_XY.restype = ctypes.c_int
	# int  __stdcall Offset_Z(IN double offsetZ);
	dll.Offset_Z.argtypes = [ctypes.c_double]
	dll.Offset_Z.restype = ctypes.c_int
	
	# Jumping List Commands
	# bool __stdcall JumpCommand(IN double x, IN double y);
	dll.JumpCommand.argtypes = [ctypes.c_double, ctypes.c_double]
	dll.JumpCommand.restype = ctypes.c_bool
	# int  __stdcall JumpCommand_Z(IN double offsetZ);
	dll.JumpCommand_Z.argtypes = [ctypes.c_double]
	dll.JumpCommand_Z.restype = ctypes.c_int
	
	# Getting Correct Commands
	# bool __stdcall EnableCorrect(IN int able);
	dll.EnableCorrect.argtypes = [ctypes.c_int]
	dll.EnableCorrect.restype = ctypes.c_bool
	# int __stdcall GetCorrectionData (OUT unsigned short &xCoordinate, OUT unsigned short &yCoordinate, OUT unsigned short &number); 
	dll.GetCorrectionData.argtypes = [ctypes.POINTER(ctypes.c_ushort), ctypes.POINTER(ctypes.c_ushort), ctypes.POINTER(ctypes.c_ushort)]
	dll.GetCorrectionData.restype = ctypes.c_int
	
	# Dynamic Axis License Command
	# bool __stdcall License(IN char* filePath);
	dll.License.argtypes = [ctypes.c_char_p]
	dll.License.restype = ctypes.c_bool
	
def Mobus(dll):
	# unsigned char modbus_master_init(int portNumber,long buard,int parity,int dataBits,int stopBits,double timeout_seconds);
	dll.modbus_master_init.argtypes = [ctypes.c_int, ctypes.c_long, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double]
	dll.modbus_master_init.restype = ctypes.c_ubyte
	# unsigned char modbus_master_write_ao_all(int portNumber,unsigned char slave_add,int ao[8]);
	dll.modbus_master_write_ao_all.argtypes = [ctypes.c_int, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_int)]
	dll.modbus_master_write_ao_all.restype = ctypes.c_ubyte
	
