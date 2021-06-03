import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'DLLreaders'))
import CSC_dll

import ctypes
import time
import numpy
import multiprocessing.connection

class PhotoactiveBoard:
	mark_speed = 15000.0
	# This class is temporarily taking charge of step motor
	position_z = ctypes.c_float(0)
	
	def __init__(self):
		# Initialize board
		CSC_dll.OpenUSB_Board(1, None)
		path = f'{os.getcwd()}\\Libraries\\FpgaFirmware.rbf'
		CSC_dll.LoadFPGA_FirmwareProgram(path.encode())
		
		CSC_dll.SetStepMotorLimitDirect(170)
		CSC_dll.SetStepMotorParameters(2, 1, 0.1, 20000, 1, 1, 1, 20000, 200000, 1)
		CSC_dll.StartStepMotor_Z( -0.1, 200000, 20000, 1 )
		time.sleep(0.1)
		CSC_dll.StepMotorZeroCounter(2)
		CSC_dll.GetStepMotorPosition(2, self.position_z)
		# self.motor_move_to(7.5)
	
	def close(self, argument):
		CSC_dll.GetStepMotorPosition(2, self.position_z)
		while self.position_z.value > 0.0001:
			CSC_dll.StartStepMotor_Z( -self.position_z.value, 200000, 20000, 1 )
			CSC_dll.GetStepMotorPosition(2, self.position_z)
			time.sleep(0.1)
		CSC_dll.StartStepMotor_Z( -0.1, 200000, 20000, 1 )
		time.sleep(0.1)
		CSC_dll.StepMotorZeroCounter(2)
		CSC_dll.StopMark()
		CSC_dll.CloseUSB_Board()
		return('Marking closed')
	
	def laser_mark(self, argument):
		# Calculate the pattern
		# proc = NuclearFinder.NuclearFinder()
		# proc.background_normalize()
		# proc.difference_of_gaussians()
		# proc.watershed_segment()
		
		######################
		CSC_dll.SetSystemParameters(110.0, 110.0, False, False, False, 0)
		CSC_dll.SetCorrectParameters_0(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
		CSC_dll.SetLaserMode(0, 0, 0.0, 0.0)
		
		markCounts = 1 #标刻次数
		isBitmap = 1 #是否是位图
		# maximuim speed is 15000
		markSpeed = self.mark_speed #标刻速度(mm/s)
		jumpSpeed = 15000.0 #跳转速度(mm/s)
		# there are at least about 15 us jump or polygon delay
		jumpDelay = 0.0 #跳转延时(us)
		polygonDelay = 0.0 #拐点延时(us)
		# there are at least about 1.5 us laser on and off delay
		laserOnDelay = 0.0 #开光延时(us)
		laserOffDelay = 0.0 #关光延时(us)
		polygonKillerTime = 0.0 #拐点抑制时间(us)
		laserFrequency = 1000.0		#激光频率(kHZ)
		current = 100.0 #YAG、SPI电流、IPG能量(%)
		firstPulseKillerLength = 100.0 #YAG 首脉冲抑制脉宽(us)
		pulseWidth = 1.0 #脉冲宽度(us)
		firstPulseWidth = 10.0 #CO2首脉冲宽度(%)
		incrementStep = 10.0 #CO2首脉冲抑制增量步长(%)
		dotSpace = 0.1 #点间距,单位(mm))
		
		for index in range(10): #层号
			self.CSC.SetMarkParameter(index, markCounts, isBitmap, markSpeed, \
					jumpSpeed, jumpDelay, polygonDelay, laserOnDelay, laserOffDelay,\
					polygonKillerTime, laserFrequency, current, firstPulseKillerLength,\
					pulseWidth, firstPulseWidth, incrementStep ,dotSpace)
		
		CSC_dll.DownloadMarkParameters()
		CSC_dll.SetFirstMarkParameter(0)
		CSC_dll.ReadyMark()
		CSC_dll.StartReadDataThread()
		CSC_dll.SetOverallMarkCounts(0)
		# O means loop marking
		CSC_dll.ZeroCounter()
		
		# size_x = proc.image.shape[0]
		# size_y = proc.image.shape[1]
		# for i in range(len(proc.image_areas_centers)):
			# for j in range(proc.image_areas_points[i].shape[0]):
				# x = proc.image_areas_points[i][j, 0] / 2048 * 30.0 - 15.0
				# y = proc.image_areas_points[i][j, 1] / 2048 * 30.0 - 15.0
				# value = proc.image_areas_value[i][j]
				# print(x ,y)
				# self.CSC.MarkCommand_Point(x, y, 0, value)
			# x = proc.image_areas_centers[i][0] / size_x * 30.0 - 15.0
			# y = proc.image_areas_centers[i][1] / size_y * 30.0 - 15.0
			# value = proc.image_areas_weight[i]
			# self.CSC.MarkCommand_Point(y, x, 0, value)
			# self.CSC.DelayCommand(100)
		# self.CSC.MarkCommand_Point(-10, -10, 1, 1000)
		# self.CSC.MarkCommand_Point(7.5, -2.5, 1, 1000)
		# self.CSC.MarkCommand_Point(-5, 5, 1, 1000)
		# self.CSC.MarkCommand_Point(2.5, 7.5, 1, 1000)
		#self.CSC.JumpCommand(-10.0, -10.0)
		#self.CSC.Write_IO_Port(0)
		#self.CSC.OutputCommand(1, 1, 0, 200000)
		#self.CSC.DelayCommand(5000)
		
		segmentLength = 2
		pathX_Confocal = (ctypes.c_double * segmentLength)(-35.0, 25.0)
		pathY_Confocal = (ctypes.c_double * segmentLength)(-35.0, 25.0)
		CSC_dll.MarkCommand_Vector(segmentLength, pathX_Confocal, pathY_Confocal)
		
		CSC_dll.EndCommand()
		CSC_dll.WriteDataEnd()
		return('Photoactive marking.')
	
	def stop_mark(self, argument):
		CSC_dll.StopMark()
		return('Photoactive standby.')
	
	def mark_speed_reset(self, speed):
		speed = max(1500, min(speed, 15000))
		self.mark_speed = speed
		return(self.mark_speed)
	
	def motor_move_to(self, position):
		# self.CSC.StopStepMotor_Z()
		CSC_dll.GetStepMotorPosition(2, self.position_z)
		if not ( position - 0.0001 < self.position_z.value < position + 0.0001 ):
			CSC_dll.StartStepMotor_Z( position - self.position_z.value, 200000, 20000, 1 )
		CSC_dll.GetStepMotorPosition(2, self.position_z)
		return('Motor moved.')
	
	def motor_move_by(self, position): # This function is obsolete
		CSC_dll.GetStepMotorPosition(2, self.position_z)
		position_new = self.position_z.value + position
		# position_new = max( self.position_z_limit_down, min(position_new, self.position_z_limit_up) )
		# self.CSC.StopStepMotor_Z()
		while not ( position_new - 0.0001 < self.position_z.value < position_new + 0.0001 ):
			CSC_dll.StartStepMotor_Z( position_new - self.position_z.value, 200000, 20000, 1 )
			CSC_dll.GetStepMotorPosition(2, self.position_z)
			time.sleep(0.01)
		return('Motor relatively moved.')
	
	# output interface
	
	def mark_speed_export(self, argument):
		return(self.mark_speed)
	
	def motor_position_export(self, argument):
		CSC_dll.GetStepMotorPosition(2, self.position_z)
		return(self.position_z.value)
	
	def status_export(self, argument):
		CSC_dll.GetStepMotorPosition(2, self.position_z)
		message = {'mark_speed':self.mark_speed, 'motor_position':self.position_z.value}
		return(message)
	
	def unknown_command(self, argument):
		return('WTF is that?')
	
if __name__ == '__main__':
	with multiprocessing.connection.Listener( ('localhost', 6001), authkey = b'hwlab' ) as server_photoactive:
		with server_photoactive.accept() as receiver_photoactive:
			with multiprocessing.connection.Listener( ('localhost', 6101), authkey = b'hwlab' ) as server_motor:
				with server_motor.accept() as receiver_motor:
					photoactive = PhotoactiveBoard()
					message = None
					command = None
					argument = None
					command_mapping = { 'close':photoactive.close, 'laser_mark':photoactive.laser_mark, \
							'stop_mark':photoactive.stop_mark, 'mark_speed_reset':photoactive.mark_speed_reset, \
							'motor_move_to':photoactive.motor_move_to, 'motor_move_by':photoactive.motor_move_by, \
							'status':photoactive.status_export}
					while True:
						if not(receiver_motor.closed):
							if receiver_motor.poll(timeout = 0.001):
							# close by AuxiliaryVontrol, before receiver_photoactive
								message = receiver_motor.recv()
								command = command_mapping.get( message[0], photoactive.unknown_command )
								argument = message[1]
								if message[0] == 'close':
									receiver_motor.close()
								elif message[0] == 'status':
									receiver_motor.send(command(argument))
								else:
									command(argument)
						if receiver_photoactive.poll(timeout = 0.001):
						# close by Nymphscope
							message = receiver_photoactive.recv()
							command = command_mapping.get( message[0], photoactive.unknown_command )
							argument = message[1]
							if message[0] == 'close':
								command(argument)
								del photoactive
								break
							elif message[0] == 'status':
								receiver_photoactive.send(command(argument))
							else:
								command(argument)
