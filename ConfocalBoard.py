from Modules import CSCBoardDLL

import ctypes
import time
import numpy

class ConfocalBoard:
	CSC = ctypes.windll.LoadLibrary("Libraries/CSCInterface.dll")
	Mobus = ctypes.windll.LoadLibrary("Libraries/Modbus_master_ao_dll.dll")
	
	# Class arguments
	position_z = ctypes.c_float(0)
	position_r = ctypes.c_float(0)
	markspeed = 4650.0
	# 405/ 488 / 561 / 640, need to be transformed later
	laser_on = [0, 0, 0, 0]
	laser_power = [0, 0, 0, 0]

	def __init__(self):
		CSCBoardDLL.CSC(self.CSC)
		CSCBoardDLL.Mobus(self.Mobus)
		
		# Initialize CSC board and mobus
		self.CSC.OpenUSB_Board(0, None)
		self.CSC.LoadFPGA_FirmwareProgram(b"Libraries/FpgaFirmware.rbf")
		# timeout_seconds set as 200 ms according to Feng-Xingshan
		self.Mobus.modbus_master_init(4, 9600, 0, 8, 1, 0.01)
		
		# initialize z and r axis
		self.CSC.SetStepMotorLimitDirect(170)
		self.CSC.SetStepMotorParameters(2, 1, 50.271999, 3200, 1, 1, 1, 1000, 1000, 1)
		self.CSC.ReturnHome_Z(3200)
		time.sleep(0.8)
		self.CSC.GetStepMotorPosition(2, self.position_z)
		self.CSC.StepMotorZeroCounter(2)
		self.CSC.SetStepMotorParameters(3, 1, 4, 3200, 1, 1, 6, 1000, 16000, 50)
		self.CSC.ReturnHome_R(16000)
		time.sleep(1.2)
		# I can't figure position_r from self.CSC.GetStepMotorPosition(3, self.position_z) for it sometimes beyonds 8600
		self.position_r = ctypes.c_float(0)
		
	def pinhole(self, position):
		self.CSC.GetStepMotorPosition(2, self.position_z)
		self.CSC.StartStepMotor_Z(position - self.position_z.value, 3200, 1000, 1)
		time.sleep( numpy.absolute( position - self.position_z.value ) / 50 )
		self.CSC.GetStepMotorPosition(2, self.position_z)
		
	def filter_wheel(self, position):
		self.CSC.StartStepMotor_R(position - self.position_r.value, 16000, 1000, 50)
		# 60 degrees for a round
		time.sleep( numpy.absolute( position - self.position_r.value ) / 300 )
		self.position_r = ctypes.c_float( position )
		# I can't figure position_r from self.CSC.GetStepMotorPosition(3, self.position_z) for it sometimes beyonds 8600
		
	def laser_power_output(self):
		# 405/ 488 / 561 / 640 -> 640 / 561 / 488 / 405
		laser_port = self.laser_on[0] * 1 + self.laser_on[1] * 2 + self.laser_on[2] * 4 + self.laser_on[3] * 8
		self.CSC.Write_IO_Port(laser_port)
		# Modules ID is 15 by default according to Sheng-Xun
		# 405/ 488 / 561 / 640 -> 405 / null / 561 / 640 / 488 / null / null / null
		laser_power_transformed = [self.laser_power[0], 0, self.laser_power[2], self.laser_power[3], self.laser_power[1], 0, 0, 0]
		self.Mobus.modbus_master_write_ao_all(4, 15, ( ctypes.c_int * 8 )( * laser_power_transformed ) )
		
	def confocal_mark(self):
		self.CSC.SetSystemParameters(110.0, 110.0, False, True, True, 0)
		self.CSC.SetCorrectParameters_0(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
		self.CSC.SetLaserMode(0, 0, 0.0, 0.0)

		markCounts = 1 #标刻次数
		isBitmap = 0 #是否是位图
		# maximuim speed is 15000
		markSpeed = self.markspeed #标刻速度(mm/s)
		jumpSpeed = 15000.0 #跳转速度(mm/s)
		jumpDelay = 0.0 #跳转延时(us)
		polygonDelay = 0.0 #拐点延时(us)
		laserOnDelay = 0.0 #开光延时(us)
		laserOffDelay = 0.0 #关光延时(us)
		polygonKillerTime = 0.0 #拐点抑制时间(us)
		laserFrequency = 0.001 #激光频率(kHZ)
		current = 100.0 #YAG、SPI电流、IPG能量(%)
		firstPulseKillerLength = 100.0 #YAG 首脉冲抑制脉宽(us)
		pulseWidth = 500.0 #脉冲宽度(us)
		firstPulseWidth = 10.0 #CO2首脉冲宽度(%)
		incrementStep = 10.0 #CO2首脉冲抑制增量步长(%)
		dotSpace = 0.1 #点间距,单位(mm))

		index = 0; #层号
		while index < 10:
			self.CSC.SetMarkParameter(index, markCounts, isBitmap, markSpeed, jumpSpeed, jumpDelay, polygonDelay, laserOnDelay, laserOffDelay, polygonKillerTime, laserFrequency, current, firstPulseKillerLength, pulseWidth, firstPulseWidth, incrementStep ,dotSpace)
			index += 1

		self.CSC.DownloadMarkParameters()
		self.CSC.SetFirstMarkParameter(0)
		self.CSC.ReadyMark()
		self.CSC.StartReadDataThread()
		self.CSC.SetOverallMarkCounts(0)
		# O means loop marking
		self.CSC.ZeroCounter()
		
		# time ~ 46.5 / markSpeed
		segmentLength = 2
		# the width of mirror is 17.5 while the ccd 29.0, the upper board 4.0
		pathX_Confocal = (ctypes.c_double * segmentLength)(25.0, -25.0)
		pathY_Confocal = (ctypes.c_double * segmentLength)(25.0, -25.0)
		self.CSC.MarkCommand_Vector(segmentLength, pathX_Confocal, pathY_Confocal)

		self.CSC.EndCommand()
		self.CSC.WriteDataEnd()
		
	def stop_mark( self ):
		self.CSC.StopMark()
	
	def close(self):
		self.CSC.Write_IO_Port(0)
		self.CSC.StopMark()
		time.sleep(0.1)
		self.CSC.ReturnHome_Z(3200)
		time.sleep(0.8)
		self.CSC.ReturnHome_R(16000)
		time.sleep(1.2)
		self.CSC.CloseUSB_Board()

