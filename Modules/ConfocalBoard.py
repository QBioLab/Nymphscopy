import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'DLLreaders'))
import CSC_dll

import ctypes
import time
import numpy
import subprocess
import multiprocessing.connection

class ConfocalBoard:
	# I am tired of translate python types to ctypes, though it is safer to do so
	
	client_claser = None
	
	# Class arguments
	pinhole_label = None
	filter_label = None
	position_z = ctypes.c_float(0)
	position_r = ctypes.c_float(0)
	mark_speed = 5000.0
	# 405/ 488 / 561 / 640, need to be transformed later
	laser_on = [0, 0, 0, 0]
	laser_power = numpy.array([0, 0, 0, 0])
	
	def __init__(self):
		
		# Initialize CSC board
		CSC_dll.OpenUSB_Board(0, None)
		path = f'{os.getcwd()}\\Libraries\\FpgaFirmware.rbf'
		CSC_dll.LoadFPGA_FirmwareProgram(path.encode())
		
		# Initialize mobus thread
		subprocess.Popen(f'python {os.getcwd()}\\Modules\\ConfocalLaser.py')
		self.client_claser = multiprocessing.connection.Client( ('localhost', 6100), authkey = b'hwlab' )
		
		# initialize z and r axis
		CSC_dll.SetStepMotorLimitDirect(170)
		CSC_dll.SetStepMotorParameters(2, 1, 50.271999, 3200, 1, 1, 1, 1000, 1000, 1)
		CSC_dll.ReturnHome_Z(3200)
		self.pinhole_label = 'None'
		time.sleep(0.8)
		CSC_dll.GetStepMotorPosition(2, self.position_z)
		CSC_dll.StepMotorZeroCounter(2)
		CSC_dll.SetStepMotorParameters(3, 1, 4, 3200, 1, 1, 6, 1000, 16000, 50)
		CSC_dll.ReturnHome_R(16000)
		self.filter_label = 'None'
		time.sleep(1.2)
		# I can't figure position_r from self.CSC.GetStepMotorPosition(3, self.position_r) for it sometimes beyonds 8600
		self.position_r = ctypes.c_float(0)
	
	def close(self, argument):
		CSC_dll.Write_IO_Port(0)
		self.client_claser.send('end')
		self.client_claser.close()
		CSC_dll.StopMark()
		time.sleep(0.1)
		CSC_dll.ReturnHome_Z(3200)
		time.sleep(0.8)
		CSC_dll.ReturnHome_R(16000)
		time.sleep(1.2)
		CSC_dll.CloseUSB_Board()
	
	def pinhole(self, pinhole_label):
		label = { 'Wide Field':6.5, '50 μm':16.5, '30 μm':26.5, '20 μm':36.5 }
		self.pinhole_label = pinhole_label
		position = label[pinhole_label]
		CSC_dll.GetStepMotorPosition(2, self.position_z)
		CSC_dll.StartStepMotor_Z(position - self.position_z.value, 3200, 1000, 1)
		time.sleep( numpy.absolute( position - self.position_z.value ) / 50 )
		CSC_dll.GetStepMotorPosition(2, self.position_z)
	
	def filter_wheel(self, filter_label):
		label = { '447/60':50, '525/45':110, '586/20':170, '615/24':230, '676/29':350, 'Four Color':290 }
		self.filter_label = filter_label
		position = label[filter_label]
		CSC_dll.StartStepMotor_R(position - self.position_r.value, 16000, 1000, 50)
		# 60 degrees for a round
		time.sleep( numpy.absolute( position - self.position_r.value ) / 300 )
		self.position_r = ctypes.c_float( position )
	
	def confocal_mark_prepare(self, counts): # ~240 ms
		CSC_dll.SetSystemParameters(110.0, 110.0, False, True, True, 0) # ~2 us
		CSC_dll.SetCorrectParameters_0(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0) # ~2 us
		CSC_dll.SetLaserMode(0, 0, 0.0, 0.0) # ~2 ms
		
		markCounts = 1 #标刻次数
		isBitmap = 0 #是否是位图
		# maximuim speed is 15000
		markSpeed = self.mark_speed #标刻速度(mm/s)
		jumpSpeed = 15000.0 #跳转速度(mm/s) the interval should be longer than the readout time
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
		
		for index in range(10): #层号 < 1 ms
			CSC_dll.SetMarkParameter(index, markCounts, isBitmap, markSpeed, jumpSpeed, jumpDelay, polygonDelay, laserOnDelay, laserOffDelay, polygonKillerTime, laserFrequency, current, firstPulseKillerLength, pulseWidth, firstPulseWidth, incrementStep ,dotSpace)
		
		CSC_dll.DownloadMarkParameters() # ~230 ms
		CSC_dll.SetFirstMarkParameter(0) # ~6 ms
		CSC_dll.ReadyMark() # ~2 ms
		CSC_dll.StartReadDataThread() # < 1 ms
		CSC_dll.SetOverallMarkCounts(counts) # < 1 ms
		# 0 means loop marking
		CSC_dll.ZeroCounter() # < 1 ms
		
		# time ~ 50.0 / markSpeed
		segmentLength = 2
		# the width of mirror is 17.5 while the ccd 29.0, the upper board 4.0, but 25.0 is a experimental parameter
		# self.CSC.DelayCommand(10000) #-35, 25
		pathX_Confocal = (ctypes.c_double * segmentLength)(-35.0, 25.0)
		pathY_Confocal = (ctypes.c_double * segmentLength)(-35.0, 25.0)
		# markSpeed =  60.0 * 1.4142 * 1000 / exposure_time
		CSC_dll.MarkCommand_Vector(segmentLength, pathX_Confocal, pathY_Confocal) # < 1 ms
		CSC_dll.JumpCommand(-60.0, -60.0) # < 1 ms
		# jump from 25 to -60: 8 ms; delay 1 ms
		CSC_dll.DelayCommand(7630) # outside the light port, < 1 ms
		# jump from -60 to -35: 2.37 ms; delay 1 ms
		# total delay: 12.37 + DelayCommandTime; photobleaching on roi: 5.65 ms; photobleaching outside roi: 6.71 ms
		# expected delay: 12.37 + 7630/1000 = 20 ms, measured delay: 20.0 \pm 1.0 ms
		
		CSC_dll.EndCommand() # < 1 ms
		return('Mark Standby')
	
	def confocal_mark(self, argument):
		CSC_dll.WriteDataEnd() # < 400 ns
	
	def stop_mark(self, argument):
		CSC_dll.StopMark()
	
	def mark_speed_reset(self, speed):
		# exposure time
		speed = max(10, min(speed, 1000))
		# ms -> mm / s
		self.mark_speed = 60.0 * 1.4142 * 1000 / speed
	
	def laser_on_reset(self, state): # ~ 200 us
		# state should be boolean value, and need to be translated into int value here
		self.laser_on = state
		laser_port = self.laser_on[0] * 1 + self.laser_on[1] * 2 + self.laser_on[2] * 4 + self.laser_on[3] * 8
		CSC_dll.Write_IO_Port(laser_port)
	
	def laser_power_reset(self, value):
		self.laser_power = numpy.array(value) * 655
		self.laser_power = numpy.clip(self.laser_power, 0 ,65535)
		# Modules ID is 15 by default according to Sheng-Xun
		# 405/ 488 / 561 / 640 -> 405 / null / 561 / 640 / 488 / null / null / null
		laser_power_transformed = [self.laser_power[0], 0, self.laser_power[2], self.laser_power[3], self.laser_power[1], 0, 0, 0]
		self.client_claser.send(laser_power_transformed)
	
	# output interface
	
	def pinhole_label_export(self):
		return(self.pinhole_label)
	
	def filter_label_export(self):
		return(self.filter_label)
	
	def mark_speed_export(self):
		return(self.mark_speed)
	
	def laser_on_export(self):
		return( self.laser_on )
	
	def laser_power_export(self):
		laser_power = self.laser_power * numpy.array(self.laser_on)
		return(laser_power)
	
	def status_export(self, argument):
		message = {'pinhole':self.pinhole_label, 'filter_wheel':self.filter_label, 'mark_speed':self.mark_speed, 'laser_on':self.laser_on, 'laser_power':list(self.laser_power)}
		return(message)
	
	def unknown_command(self, argument):
		return('WTF is that?')
	
with multiprocessing.connection.Listener( ('localhost', 6000), authkey = b'hwlab' ) as server_confocal:
	with server_confocal.accept() as receiver:
		confocal = ConfocalBoard()
		message = None
		command = None
		argument = None
		command_mapping = { 'close':confocal.close, 'pinhole':confocal.pinhole, 'filter_wheel':confocal.filter_wheel, 'confocal_mark_prepare':confocal.confocal_mark_prepare, 'confocal_mark':confocal.confocal_mark, 'stop_mark':confocal.stop_mark, 'mark_speed_reset':confocal.mark_speed_reset, 'laser_on_reset':confocal.laser_on_reset, 'laser_power_reset':confocal.laser_power_reset, 'status':confocal.status_export }
		while True:
			if receiver.poll(timeout = 0.001):
				message = receiver.recv()
				command = command_mapping.get( message[0], confocal.unknown_command )
				argument = message[1]
				if message[0] == 'close':
					command(argument)
					del confocal
					break
				elif message[0] == 'status' or message[0] == 'confocal_mark_prepare':
					receiver.send(command(argument))
				else:
					command(argument)
