import CSCBoardDLL

import ctypes
import time
import numpy
import PIL.Image
import multiprocessing.connection

class LaserBoard:
	CSC = ctypes.windll.LoadLibrary("../Libraries/CSCInterface.dll")
	markspeed = 15000.0
	close_flag = False
	# This class is temporarily taking charge of step motor
	position_z = 0.0
	position_z_limit_up = 8.5
	position_z_limit_down = 0.0

	def __init__(self):
		CSCBoardDLL.CSC(self.CSC)
		self.close_flag = False
		
		# Initialize board
		self.CSC.OpenUSB_Board(1, None)
		self.CSC.LoadFPGA_FirmwareProgram(b"../Libraries/FpgaFirmware.rbf")
		
		self.CSC.SetStepMotorLimitDirect(170)
		self.CSC.SetStepMotorParameters(2, 1, 0.1, 20000, 1, 1, 1, 20000, 200000, 1)
		# self.motor_move_to(7.5)
	
	def laser_mark(self, argument):
	
		#Calculate the pattern#
		size = 500
		path = self.markPath( size )
		pathSegment = self.markSegment( path )

		######################
		self.CSC.SetSystemParameters(110.0, 110.0, False, True, True, 0)
		self.CSC.SetCorrectParameters_0(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
		self.CSC.SetLaserMode(0, 0, 0.0, 0.0)

		markRange = 15.0
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

		for i in range( len(pathSegment) ):
			if i < len(pathSegment) - 1:
				distance = ( path[ pathSegment[i][1] ] - path[ pathSegment[i][1] + 2 ] ) * 2 * markRange / size
			else:
				# 1.0 is the jump shape correlation
				distance = ( path[ pathSegment[i][1] ] - path[ 0 ] ) * 2 * markRange / size * 1.0
			distanceLength = numpy.sqrt( numpy.power( distance[0], 2 ) + numpy.power( distance[1], 2 ) )
			segmentLength = pathSegment[i][1] - pathSegment[i][0] + 1
			pathX = ( ctypes.c_double * segmentLength )( * path[ pathSegment[i][0] : pathSegment[i][1] + 1 ][:, 0] * 2 * markRange / size - markRange )
			pathY = ( ctypes.c_double * segmentLength )( * path[ pathSegment[i][0] : pathSegment[i][1] + 1 ][:, 1] * 2 * markRange / size - markRange )
			self.CSC.MarkCommand_Vector(segmentLength, pathX, pathY)
			# 140 is the jumping delay
			self.CSC.OutputCommand(1, 1, 0, int( 1000000 * distanceLength / jumpSpeed ) + 140)
		self.CSC.OutputCommand(4, 1, 0, int( 1000000 * distanceLength / jumpSpeed ) + 140)
			
		#self.CSC.JumpCommand(-10.0, -10.0)
		#self.CSC.Write_IO_Port(0)
		#self.CSC.OutputCommand(1, 1, 0, 200000)
		#self.CSC.DelayCommand(5000)
		self.CSC.EndCommand()
		self.CSC.WriteDataEnd()
		
	def stop_mark(self, argument):
		self.CSC.StopMark()
	
	def motor_move_to(self, position):
		if position >= self.position_z_limit_down and position < self.position_z_limit_up:
			self.CSC.StartStepMotor_Z( position - self.position_z, 200000, 20000, 1 )
			self.position_z = position
	
	def motor_move_by(self, position):
		position_new = self.position_z + position
		if position_new >= self.position_z_limit_down and position_new < self.position_z_limit_up:
			self.CSC.StartStepMotor_Z( position, 200000, 20000, 1 )
			self.position_z = position_new
	
	def motor_position_value(self, argument):
		return(self.position_z)
	
	def close(self, argument):
		self.motor_move_to(0.0)
		self.position_z = 0.0
		time.sleep( self.position_z + 0.1 )
		self.CSC.StopMark()
		self.CSC.CloseUSB_Board()
		self.close_flag = True
	
	
	def markPath(self, size):

		lightOn = 125.0
		loghtOff = 125.0

		MarkGraphics = PIL.Image.open(b'../Images/MarkGraphics.jpg')

		MarkGraphics = MarkGraphics.resize( [size, size], resample = PIL.Image.LANCZOS )

		pixels = numpy.array( MarkGraphics.getdata() )

		# linear luminance from CIE 1931
		pixelsGrey = 0.2126 * pixels[:,0] + 0.7152 * pixels[:,1] + 0.0722 * pixels[:,2]

		path = numpy.array([], dtype = int)
		path.shape = (0,2)
		
		mark = False
		for y in range(size):
			if y % 2 == 0:
				for x in range(size):
					if mark and (pixelsGrey[y * size + x] <= loghtOff):
						if x != 0:
							path = numpy.append( path, [[x - 1, y]], axis = 0 )
						path = numpy.append( path, [[-1, -1]], axis = 0 )
						mark = False
					elif (not mark) and (pixelsGrey[y * size + x] > lightOn):
						path = numpy.append( path, [[x, y]], axis = 0 )
						mark = True
				if mark:
					path = numpy.append( path, [[size - 1, y]], axis = 0 )
			elif y % 2 == 1:
				for x in range(size):
					if mark and (pixelsGrey[y * size + size - 1 - x] <= loghtOff):
						if x != 0:
							path = numpy.append( path, [[size - x, y]], axis = 0 )
						path = numpy.append( path, [[-1, -1]], axis = 0 )
						mark = False
					elif (not mark) and (pixelsGrey[y * size + size - 1 - x] > lightOn):
						path = numpy.append( path, [[size - 1 - x, y]], axis = 0 )
						mark = True
				if mark:
					path = numpy.append( path, [[0, y]], axis = 0 )
					
		path = numpy.append( path, [[-1, -1]], axis = 0 )
		
		return( path )
		
	def markSegment(self, path):
		segment = numpy.array([], dtype = int)
		segment.shape = (0,2)

		i = 0;
		while i < len(path):
			for j in range ( i, len(path) ):
				if path[j][0] == -1:
					break
			segment = numpy.append( segment, [[i, j - 1]], axis = 0 )
			i = j + 1
		
		return( segment )
		
	def set_markspeed(self, speed):
		self.markspeed = speed
	
	def unknown_command(self, argument):
		pass
		
with multiprocessing.connection.Listener( ('localhost', 6000), authkey = b'Si Valetis Gaudeo' ) as server:
	with server.accept() as receiver:
		board = LaserBoard()
		command_mapping = { 0:board.close, 1:board.laser_mark, 2:board.stop_mark, 3:board.set_markspeed, 4:board.motor_move_to, 5:board.motor_move_by, 6:board.motor_position_value }
		command_feedback = { 0:'Marking closed', 1:'L-marking', 2:'L-standby', 3:board.markspeed, 4:'Motor moved', 5:'Motor relatively moved', 6:board.position_z }
		while True:
			message = receiver.recv()
			command = command_mapping.get( message[0], board.unknown_command )
			argument = message[1]
			command(argument)
			command_feedback = { 0:'Marking closed', 1:'L-marking', 2:'L-standby', 3:board.markspeed, 4:'Motor moved', 5:'Motor relatively moved', 6:board.position_z }
			feedback = command_feedback.get( message[0], 'WTF is that?' )
			receiver.send(feedback)
			if board.close_flag:
				break
