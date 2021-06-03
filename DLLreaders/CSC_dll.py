import ctypes
import os
import sys

CSC = ctypes.windll.LoadLibrary('Libraries\\CSCInterface.dll')

# Ref: https://docs.python.org/3.6/library/ctypes.html#fundamental-data-types
# class ctypes.WinDLL(name, mode=DEFAULT_MODE, handle=None, use_errno=False, use_last_error=False). Windows only: Instances of this class represent loaded shared libraries, functions in these libraries use the stdcall calling convention, and are assumed to return int by default. On Windows CE only the standard calling convention is used, for convenience the WinDLL and OleDLL use the standard calling convention on this platform.
# class ctypes.c_char_p represents the C char * datatype when it points to a zero-terminated string. For a general character pointer that may also point to binary data, POINTER(c_char) must be used. The constructor accepts an integer address, or a bytes object.

#pragma once #define IN #define OUT

# Basic Functions
# int __stdcall OpenUSB_Board(int deviceIndex,void *handle);
OpenUSB_Board = CSC.OpenUSB_Board
OpenUSB_Board.argtypes = [ctypes.c_int, ctypes.c_void_p]
OpenUSB_Board.restype = ctypes.c_int
# int __stdcall LoadFPGA_FirmwareProgram(IN char* rbfFilePath);
LoadFPGA_FirmwareProgram = CSC.LoadFPGA_FirmwareProgram
LoadFPGA_FirmwareProgram.argtypes = [ctypes.c_char_p]
LoadFPGA_FirmwareProgram.restype = ctypes.c_int
# int __stdcall SetLaserMode(IN int laserType,IN int standby,IN float frequency,IN float pulseWidth);
SetLaserMode = CSC.SetLaserMode
SetLaserMode.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float]
SetLaserMode.restype = ctypes.c_int
# int  __stdcall SetSystemParameters(IN double rangeX, IN double rangeY, IN bool exchangeXY, IN bool invertX, IN bool invertY, IN int startMarkMode);
SetSystemParameters = CSC.SetSystemParameters
SetSystemParameters.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_int]
SetSystemParameters.restype = ctypes.c_int
# int  __stdcall SetCorrectParameters_0(IN double xCorrection, IN double yCorrection, IN double xShear, IN double yShear, IN double xLadder, IN double yLadder, IN double ratioX, IN double ratioY, IN double ratioZ);
SetCorrectParameters_0 = CSC.SetCorrectParameters_0
SetCorrectParameters_0.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
SetCorrectParameters_0.restype = ctypes.c_int
# int  __stdcall SetCorrectParameters_1(IN double ratioX, IN double ratioY, IN double ratioZ, IN char* filePath);
SetCorrectParameters_1 = CSC.SetCorrectParameters_1
SetCorrectParameters_1.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_char_p]
SetCorrectParameters_1.restype = ctypes.c_int
# void __stdcall WriteDataEnd();
WriteDataEnd = CSC.WriteDataEnd
WriteDataEnd.argtypes = None
WriteDataEnd.restype = None
# void __stdcall SetOverallMarkCounts(IN int count);
SetOverallMarkCounts = CSC.SetOverallMarkCounts
SetOverallMarkCounts.argtypes = [ctypes.c_int]
SetOverallMarkCounts.restype = None
# bool __stdcall IsReadDataEnd(); This function does not exists
#dll.IsReadDataEnd.argtypes = None
#dll.IsReadDataEnd.restype = ctypes.c_bool
# bool __stdcall IsMarkEnd();
IsMarkEnd = CSC.IsMarkEnd
IsMarkEnd.argtypes = None
IsMarkEnd.restype = ctypes.c_bool
# bool __stdcall StartMark();
StartMark = CSC.StartMark
StartMark.argtypes = None
StartMark.restype = ctypes.c_bool
# unsigned __int64 __stdcall GetProducedData();
GetProducedData = CSC.GetProducedData
GetProducedData.argtypes = None
GetProducedData.restype = ctypes.c_ulonglong
# int __stdcall SetMarkParameter(IN int index, IN int markCounts, IN int isBitmap, IN float markSpeed, IN float jumpSpeed, IN float jumpDelay, IN float polygonDelay, IN float laserOnDelay, IN float laserOffDelay, IN float polygonKillerTime, IN float laserFrequency, IN float current, IN float firstPulseKillerLength, IN float pulseWidth, IN float firstPulseWidth, IN float incrementStep, IN float dotSpace);
SetMarkParameter = CSC.SetMarkParameter
SetMarkParameter.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
SetMarkParameter.restype = ctypes.c_int
# bool  __stdcall DownloadMarkParameters();
DownloadMarkParameters = CSC.DownloadMarkParameters
DownloadMarkParameters.argtypes = None
DownloadMarkParameters.restype = ctypes.c_bool
# bool __stdcall SetFirstMarkParameter(IN int pen);
SetFirstMarkParameter = CSC.SetFirstMarkParameter
SetFirstMarkParameter.argtypes = [ctypes.c_int]
SetFirstMarkParameter.restype = ctypes.c_bool
# bool __stdcall ReadyMark();
ReadyMark = CSC.ReadyMark
ReadyMark.argtypes = None
ReadyMark.restype = ctypes.c_bool
# bool __stdcall ReadyPreview();
ReadyPreview = CSC.ReadyPreview
ReadyPreview.argtypes = None
ReadyPreview.restype = ctypes.c_bool
# bool __stdcall StartReadDataThread();
StartReadDataThread = CSC.StartReadDataThread
StartReadDataThread.argtypes = None
StartReadDataThread.restype = ctypes.c_bool
# int __stdcall ZeroCounter();
ZeroCounter = CSC.ZeroCounter
ZeroCounter.argtypes = None
ZeroCounter.restype = ctypes.c_int
# bool __stdcall StopMark();
StopMark = CSC.StopMark
StopMark.argtypes = None
StopMark.restype = ctypes.c_bool
# bool __stdcall StopPreview();
StopPreview = CSC.StopPreview
StopPreview.argtypes = None
StopPreview.restype = ctypes.c_bool
# bool __stdcall StopCalcData();
StopCalcData = CSC.StopCalcData
StopCalcData.argtypes = None
StopCalcData.restype = ctypes.c_bool
# bool __stdcall SetDelayPA_MO(IN float delay);
SetDelayPA_MO = CSC.SetDelayPA_MO
SetDelayPA_MO.argtypes = [ctypes.c_float]
SetDelayPA_MO.restype = ctypes.c_bool
# bool __stdcall SPI_SimmerCurrent(IN double simmer);
SPI_SimmerCurrent = CSC.SPI_SimmerCurrent
SPI_SimmerCurrent.argtypes = [ctypes.c_double]
SPI_SimmerCurrent.restype = ctypes.c_bool
# bool __stdcall SPI_ModeSelect(IN int mode);
SPI_ModeSelect = CSC.SPI_ModeSelect
SPI_ModeSelect.argtypes = [ctypes.c_int]
SPI_ModeSelect.restype = ctypes.c_bool
# bool __stdcall SPI_WaveForm(IN int wave);
SPI_WaveForm = CSC.SPI_WaveForm
SPI_WaveForm.argtypes = [ctypes.c_int]
SPI_WaveForm.restype = ctypes.c_bool
# int __stdcall SetExternalStartSignalMode(IN int mode);
SetExternalStartSignalMode = CSC.SetExternalStartSignalMode
SetExternalStartSignalMode.argtypes = [ctypes.c_int]
SetExternalStartSignalMode.restype = ctypes.c_int
# int __stdcall GetCSCInterfaceVersion(OUT char *version);
GetCSCInterfaceVersion = CSC.GetCSCInterfaceVersion
GetCSCInterfaceVersion.argtypes = [ctypes.c_char_p]
GetCSCInterfaceVersion.restype = ctypes.c_int
# bool __stdcall OpenGuideLight();
OpenGuideLight = CSC.OpenGuideLight
OpenGuideLight.argtypes = None
OpenGuideLight.restype = ctypes.c_bool
# bool __stdcall CloseGuideLight();
CloseGuideLight = CSC.CloseGuideLight
CloseGuideLight.argtypes = None
CloseGuideLight.restype = ctypes.c_bool
# void __stdcall  CloseUSB_Board();
CloseUSB_Board = CSC.CloseUSB_Board
CloseUSB_Board.argtypes = None
CloseUSB_Board.restype = None

# Functions Reading Information of CSC-USB Board
# bool __stdcall GetMarkStatus();
GetMarkStatus = CSC.GetMarkStatus
GetMarkStatus.argtypes = None
GetMarkStatus.restype = ctypes.c_bool
# unsigned long __stdcall GetMarkTime();
GetMarkTime = CSC.GetMarkTime
GetMarkTime.argtypes = None
GetMarkTime.restype = ctypes.c_ulong
# bool __stdcall GetMarkCounts(OUT unsigned char &internalMarkCounts, OUT unsigned char &externalMarkCounts);
GetMarkCounts = CSC.GetMarkCounts
GetMarkCounts.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte)]
GetMarkCounts.restype = ctypes.c_bool
# int __stdcall GetUSB_BoardCounts();
GetUSB_BoardCounts = CSC.GetUSB_BoardCounts
GetUSB_BoardCounts.argtypes = None
GetUSB_BoardCounts.restype = ctypes.c_int
# int __stdcall GetUSB_FirmwareVersion(OUT char *version); 
GetUSB_FirmwareVersion = CSC.GetUSB_FirmwareVersion
GetUSB_FirmwareVersion.argtypes = [ctypes.c_char_p]
GetUSB_FirmwareVersion.restype = ctypes.c_int
# int __stdcall GetFPGA_FirmwareVersion(OUT char *version);
GetFPGA_FirmwareVersion = CSC.GetFPGA_FirmwareVersion
GetFPGA_FirmwareVersion.argtypes = [ctypes.c_char_p]
GetFPGA_FirmwareVersion.restype = ctypes.c_int
# bool __stdcall GetLaserAndScannerStatus(OUT int &laserStatus, OUT int &scannerStatus);
GetLaserAndScannerStatus = CSC.GetLaserAndScannerStatus
GetLaserAndScannerStatus.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
GetLaserAndScannerStatus.restype = ctypes.c_bool
# int __stdcall ReadUSB_BoardSN(OUT char *boardSN);
ReadUSB_BoardSN = CSC.ReadUSB_BoardSN
ReadUSB_BoardSN.argtypes = [ctypes.c_char_p]
ReadUSB_BoardSN.restype = ctypes.c_int
# int __stdcall ReadUSB_BoardSN_ByIndex(IN int index, OUT char *boardSN);
ReadUSB_BoardSN_ByIndex = CSC.ReadUSB_BoardSN_ByIndex
ReadUSB_BoardSN_ByIndex.argtypes = [ctypes.c_int, ctypes.c_char_p]
ReadUSB_BoardSN_ByIndex.restype = ctypes.c_int
# bool __stdcall GetScannerPosition(OUT float& xPos, OUT float& yPos);
GetScannerPosition = CSC.GetScannerPosition
GetScannerPosition.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]
GetScannerPosition.restype = ctypes.c_bool

# Commands Opening Lasers
# bool __stdcall LaserSignalOn();
LaserSignalOn = CSC.LaserSignalOn
LaserSignalOn.argtypes = None
LaserSignalOn.restype = ctypes.c_bool
# bool __stdcall LaserSignalOff();
LaserSignalOff = CSC.LaserSignalOff
LaserSignalOff.argtypes = None
LaserSignalOff.restype = ctypes.c_bool

# AD Commands
# bool __stdcall InitAD();
InitAD = CSC.InitAD
InitAD.argtypes = None
InitAD.restype = ctypes.c_bool
# int __stdcall GetAD();
GetAD = CSC.GetAD
GetAD.argtypes = None
GetAD.restype = ctypes.c_int

# I/O Control Commands
# bool __stdcall Write_IO_Port(IN unsigned char port);
Write_IO_Port = CSC.Write_IO_Port
Write_IO_Port.argtypes = [ctypes.c_ubyte]
Write_IO_Port.restype = ctypes.c_bool
# unsigned char __stdcall GetOutputPortState();
GetOutputPortState = CSC.GetOutputPortState
GetOutputPortState.argtypes = None
GetOutputPortState.restype = ctypes.c_ubyte
# unsigned short __stdcall Read_IO_Port();
Read_IO_Port = CSC.Read_IO_Port
Read_IO_Port.argtypes = None
Read_IO_Port.restype = ctypes.c_ushort
# bool __stdcall GetExternalStartStopSignal(OUT int &start, OUT int &stop);
GetExternalStartStopSignal = CSC.GetExternalStartStopSignal
GetExternalStartStopSignal.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
GetExternalStartStopSignal.restype = ctypes.c_bool
# bool __stdcall ResetStartStopSignal();
ResetStartStopSignal = CSC.ResetStartStopSignal
ResetStartStopSignal.argtypes = None
ResetStartStopSignal.restype = ctypes.c_bool

# I/O List Commands
# int  __stdcall  InputCommand(IN unsigned char port);
InputCommand = CSC.InputCommand
InputCommand.argtypes = [ctypes.c_ubyte]
InputCommand.restype = ctypes.c_int
# int  __stdcall  OutputCommand(IN unsigned char port, IN int outMode, IN int level, IN int outputPulseWidth);
OutputCommand = CSC.OutputCommand
OutputCommand.argtypes = [ctypes.c_ubyte, ctypes.c_int, ctypes.c_int, ctypes.c_int]
OutputCommand.restype = ctypes.c_int

# Step Motor Control Commands
# int __stdcall SetStepMotorParameters(IN int motorType, IN int direction, IN float pitch, IN float pulsePerRevolution, IN float subdivision, IN float correctionFactor, IN float reductionRatio, IN float startSpeed, IN float speed, IN float speedupTime);
SetStepMotorParameters = CSC.SetStepMotorParameters
SetStepMotorParameters.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
SetStepMotorParameters.restype = ctypes.c_int
# bool __stdcall SetStepMotorLimitDirect(IN int direction);
SetStepMotorLimitDirect = CSC.SetStepMotorLimitDirect
SetStepMotorLimitDirect.argtypes = [ctypes.c_int]
SetStepMotorLimitDirect.restype = ctypes.c_bool
# bool __stdcall StepMotorZeroCounter(IN int type);
StepMotorZeroCounter = CSC.StepMotorZeroCounter
StepMotorZeroCounter.argtypes = [ctypes.c_int]
StepMotorZeroCounter.restype = ctypes.c_bool
# bool __stdcall GetStepMotorPosition(IN int stepMotorType, OUT float &motorCurPos);
GetStepMotorPosition = CSC.GetStepMotorPosition
GetStepMotorPosition.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
GetStepMotorPosition.restype = ctypes.c_bool
# void __stdcall GetStepMotorHomeStatus(OUT bool &xhome,OUT bool &yhome,OUT bool &zhome,OUT bool &rhome);
GetStepMotorHomeStatus = CSC.GetStepMotorHomeStatus
GetStepMotorHomeStatus.argtypes = [ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool)]
GetStepMotorHomeStatus.restype = None
# void __stdcall GetStepMotorLimitStatus(OUT bool &xlimit,OUT bool &ylimit,OUT bool &zlimit,OUT bool &rlimit);
GetStepMotorLimitStatus = CSC.GetStepMotorLimitStatus
GetStepMotorLimitStatus.argtypes = [ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool)]
GetStepMotorLimitStatus.restype = None
# void __stdcall GetStepMotorStatus(OUT bool &xMotor,OUT bool &yMotor,OUT bool &zMotor,OUT bool &rMotor);
GetStepMotorStatus = CSC.GetStepMotorStatus
GetStepMotorStatus.argtypes = [ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool)]
GetStepMotorStatus.restype = None
# bool __stdcall ReturnHome_X(IN unsigned long frequency);
ReturnHome_X = CSC.ReturnHome_X
ReturnHome_X.argtypes = [ctypes.c_ulong] # frequency = speed
ReturnHome_X.restype = ctypes.c_bool
# bool __stdcall StartStepMotor_X(IN float distance, IN unsigned long frequency, IN unsigned long startFrequency, IN unsigned long speedUpTime);
StartStepMotor_X = CSC.StartStepMotor_X
StartStepMotor_X.argtypes = [ctypes.c_float, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong] # frequency = speed, startFrequency = startSpeed
StartStepMotor_X.restype = ctypes.c_bool
# bool __stdcall StopStepMotor_X();
StopStepMotor_X = CSC.StopStepMotor_X
StopStepMotor_X.argtypes = None
StopStepMotor_X.restype = ctypes.c_bool
# bool __stdcall ReturnHome_Y(IN unsigned long frequency);
ReturnHome_Y = CSC.ReturnHome_Y
ReturnHome_Y.argtypes = [ctypes.c_ulong] # frequency = speed
ReturnHome_Y.restype = ctypes.c_bool
# bool __stdcall StartStepMotor_Y(IN float distance, IN unsigned long frequency, IN unsigned long startFrequency, IN unsigned long speedUpTime);
StartStepMotor_Y = CSC.StartStepMotor_Y
StartStepMotor_Y.argtypes = [ctypes.c_float, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong] # frequency = speed, startFrequency = startSpeed
StartStepMotor_Y.restype = ctypes.c_bool
# bool __stdcall StopStepMotor_Y();
StopStepMotor_Y = CSC.StopStepMotor_Y
StopStepMotor_Y.argtypes = None
StopStepMotor_Y.restype = ctypes.c_bool
# bool __stdcall ReturnHome_Z(IN unsigned long frequency);
ReturnHome_Z = CSC.ReturnHome_Z
ReturnHome_Z.argtypes = [ctypes.c_ulong] # frequency = speed
ReturnHome_Z.restype = ctypes.c_bool
# bool __stdcall StartStepMotor_Z(IN float distance, IN unsigned long frequency, IN unsigned long startFrequency, IN unsigned long speedUpTime);
StartStepMotor_Z = CSC.StartStepMotor_Z
StartStepMotor_Z.argtypes = [ctypes.c_float, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong] # frequency = speed, startFrequency = startSpeed
StartStepMotor_Z.restype = ctypes.c_bool
# bool __stdcall StopStepMotor_Z();
StopStepMotor_Z = CSC.StopStepMotor_Z
StopStepMotor_Z.argtypes = None
StopStepMotor_Z.restype = ctypes.c_bool
# bool __stdcall ReturnHome_R(IN unsigned long frequency);
ReturnHome_R = CSC.ReturnHome_R
ReturnHome_R.argtypes = [ctypes.c_ulong] # frequency = speed
ReturnHome_R.restype = ctypes.c_bool
# bool __stdcall StartStepMotor_R(IN float angle, IN unsigned long frequency, IN unsigned long startFrequency, IN unsigned long speedUpTime);
StartStepMotor_R = CSC.StartStepMotor_R
StartStepMotor_R.argtypes = [ctypes.c_float, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong] # frequency = speed, startFrequency = startSpeed
StartStepMotor_R.restype = ctypes.c_bool
# bool __stdcall StopStepMotor_R();
StopStepMotor_R = CSC.StopStepMotor_R
StopStepMotor_R.argtypes = None
StopStepMotor_R.restype = ctypes.c_bool

# Step Motor List Commands
# int __stdcall MoveStepMotorCommand_XY(IN double startPositionX, IN double startPositionY, IN double endPositionX, IN double endPositionY);
MoveStepMotorCommand_XY = CSC.MoveStepMotorCommand_XY
MoveStepMotorCommand_XY.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
MoveStepMotorCommand_XY.restype = ctypes.c_int
# int  __stdcall  MoveStepMotorCommand_Z(IN double startPosition, IN double endPosition);
MoveStepMotorCommand_Z = CSC.MoveStepMotorCommand_Z
MoveStepMotorCommand_Z.argtypes = [ctypes.c_double, ctypes.c_double]
MoveStepMotorCommand_Z.restype = ctypes.c_int
# int  __stdcall  RotateStepMotorCommand_R(IN float angle);
RotateStepMotorCommand_R = CSC.RotateStepMotorCommand_R
RotateStepMotorCommand_R.argtypes = [ctypes.c_float]
RotateStepMotorCommand_R.restype = ctypes.c_int
# Delay Command
# int  __stdcall  DelayCommand(IN int delay);
DelayCommand = CSC.DelayCommand
DelayCommand.argtypes = [ctypes.c_int]
DelayCommand.restype = ctypes.c_int
# Mark Commands
# int __stdcall MarkCommand_Point(IN double x, IN double y, IN int type, IN int tp);
MarkCommand_Point = CSC.MarkCommand_Point
MarkCommand_Point.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
MarkCommand_Point.restype = ctypes.c_int
# int __stdcall MarkCommand_Vector( IN int length, IN double* sitsetX, IN double* sitsetY);
MarkCommand_Vector = CSC.MarkCommand_Vector
MarkCommand_Vector.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
MarkCommand_Vector.restype = ctypes.c_int
# int  __stdcall  MarkCommand_Bitmap( IN int length, IN double* sitsetX, IN double* sitsetY, IN int* sitsetGray);
MarkCommand_Bitmap = CSC.MarkCommand_Bitmap
MarkCommand_Bitmap.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int)]
MarkCommand_Bitmap.restype = ctypes.c_int
# Command Change Pens
# int __stdcall ChangePensCommand(IN unsigned char pen);
ChangePensCommand = CSC.ChangePensCommand
ChangePensCommand.argtypes = [ctypes.c_ubyte]
ChangePensCommand.restype = ctypes.c_int
# Ending Mark Command
# int  __stdcall  EndCommand();
EndCommand = CSC.EndCommand
EndCommand.argtypes = None
EndCommand.restype = ctypes.c_int
# Jumping Control Commands
# int __stdcall Goto_XY(IN double x, IN double y);
Goto_XY = CSC.Goto_XY
Goto_XY.argtypes = [ctypes.c_double, ctypes.c_double]
Goto_XY.restype = ctypes.c_int
# int  __stdcall Offset_Z(IN double offsetZ);
Offset_Z = CSC.Offset_Z
Offset_Z.argtypes = [ctypes.c_double]
Offset_Z.restype = ctypes.c_int
# Jumping List Commands
# bool __stdcall JumpCommand(IN double x, IN double y);
JumpCommand = CSC.JumpCommand
JumpCommand.argtypes = [ctypes.c_double, ctypes.c_double]
JumpCommand.restype = ctypes.c_bool
# int  __stdcall JumpCommand_Z(IN double offsetZ);
JumpCommand_Z = CSC.JumpCommand_Z
JumpCommand_Z.argtypes = [ctypes.c_double]
JumpCommand_Z.restype = ctypes.c_int
# Getting Correct Commands
# bool __stdcall EnableCorrect(IN int able);
EnableCorrect = CSC.EnableCorrect
EnableCorrect.argtypes = [ctypes.c_int]
EnableCorrect.restype = ctypes.c_bool
# int __stdcall GetCorrectionData (OUT unsigned short &xCoordinate, OUT unsigned short &yCoordinate, OUT unsigned short &number); 
GetCorrectionData = CSC.GetCorrectionData
GetCorrectionData.argtypes = [ctypes.POINTER(ctypes.c_ushort), ctypes.POINTER(ctypes.c_ushort), ctypes.POINTER(ctypes.c_ushort)]
GetCorrectionData.restype = ctypes.c_int
# Dynamic Axis License Command
# bool __stdcall License(IN char* filePath);
License = CSC.License
License.argtypes = [ctypes.c_char_p]
License.restype = ctypes.c_bool