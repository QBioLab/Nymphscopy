import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'DLLreaders'))
import PIGCS_dll

import ctypes
import time
import numpy
import serial

class PIPiezo:
	connected_flag = ctypes.c_bool(False)
	moving_flag = ctypes.c_bool(False)
	position = ctypes.c_double(0)
	position_targeted = ctypes.c_double(0)
	velocity = ctypes.c_double(13000.0)
	
	szBuffer = (ctypes.c_char * 128)(0)
	szFilter = ctypes.c_char_p( b'E-709' )
	ID = ctypes.c_int(0)
	szAxes = (ctypes.c_char * 8)(0)
	stagevo_mode = ctypes.c_bool(True)
	szNames = (ctypes.c_char * 32)(0)
	pnError = ctypes.c_int(0)
	
	piWaveTableIdsArray = (ctypes.c_int * 1)(1)
	piWaveGeneratorIdsArray = (ctypes.c_int * 1)(1)
	piTableRateArray = (ctypes.c_int * 1)(1)
	piNumberOfCyclesArray = (ctypes.c_int * 1)(1)
	pdValueArray = (ctypes.c_double * 1)(0)
	
	def __init__(self):		
		# Lists the identification strings of all controllers available via USB interfaces
		PIGCS_dll.PI_EnumerateUSB( self.szBuffer, 128, self.szFilter )
		# print(szBuffer.value.decode('UTF-8'))
		# Open an USB connection to a controller
		self.ID = ctypes.c_int( PIGCS_dll.PI_ConnectUSB( self.szBuffer ) )
		# print(ID.value)
		# Get the identifiers for all configured and unconfigured axes
		PIGCS_dll.PI_qSAI_ALL( self.ID, self.szAxes, 8 )
		# print(szAxes.value.decode('UTF-8'))
		# Set self.stagevo-control 'on' or 'off' (closed-loop/open-loop mode).
		PIGCS_dll.PI_SVO( self.ID, self.szAxes, self.stagevo_mode )
		# Get the current positions of szAxes.
		PIGCS_dll.PI_qPOS( self.ID, self.szAxes, self.position )
		PIGCS_dll.PI_qMOV( self.ID, self.szAxes, self.position_targeted )
		# print(f'Position: {position.value:.6f} μm\n')
		# Sets and gets the velocity value for szAxes.
		PIGCS_dll.PI_VEL( self.ID, self.szAxes, self.velocity )
		PIGCS_dll.PI_qVEL( self.ID, self.szAxes, self.velocity )
		# print(f'Velocity: {velocity.value} unit/s\n')
		# set the wave table rate
		piInterpolationTypeArray = (ctypes.c_int * 1)(0)
		PIGCS_dll.PI_WTR( self.ID, self.piWaveGeneratorIdsArray, self.piTableRateArray, piInterpolationTypeArray, 1 )
		PIGCS_dll.PI_qWTR( self.ID, self.piWaveGeneratorIdsArray, self.piTableRateArray, piInterpolationTypeArray, 1 )
		# print(f'rate = {self.piWaveGeneratorIdsArray[0]}')
		# set the number of wave cycles
		PIGCS_dll.PI_WGC( self.ID, self.piWaveGeneratorIdsArray, self.piNumberOfCyclesArray, 1 )
		PIGCS_dll.PI_qWGC( self.ID, self.piWaveGeneratorIdsArray, self.piNumberOfCyclesArray, 1 )
		# print(f'cycles = {self.piNumberOfCyclesArray[0]}')
		self.connected_flag = ctypes.c_bool( PIGCS_dll.PI_IsConnected( self.ID ) )
		# TO avoid numerical screening floating
		self.move_to(0.1)
	
	def close(self):
		self.move_to(0.0)
		# stop the wave generator
		iStartModArray = (ctypes.c_int * 1)(0)
		PIGCS_dll.PI_WGO( self.ID, self.piWaveGeneratorIdsArray, iStartModArray, 1)
		# Make sure not moving nor connected
		PIGCS_dll.PI_IsMoving ( self.ID, self.szAxes, self.moving_flag )
		while self.moving_flag.value:
			PIGCS_dll.PI_IsMoving ( self.ID, self.szAxes, self.moving_flag )
		if PIGCS_dll.PI_IsConnected( self.ID ):
			PIGCS_dll.PI_CloseConnection( self.ID )
		self.connected_flag = ctypes.c_bool(False)
		self.moving_flag = ctypes.c_bool(False)
	
	def information(self):
		if self.connected_flag.value:
			# Get identification string of the controller.
			PIGCS_dll.PI_qIDN( self.ID, self.szBuffer, 128 )
			print( self.szBuffer.value.decode('UTF-8') )
			# Reports the versions of the controller firmware and the underlying drivers and libraries.
			PIGCS_dll.PI_qVER( self.ID, self.szBuffer, 128 )
			print( self.szBuffer.value.decode('UTF-8') )
			# Get the type names of the stages associated with szAxes.
			PIGCS_dll.PI_qCST( self.ID, self.szAxes, self.szNames, 32)
			print( self.szNames.value.decode('UTF-8') )
			PIGCS_dll.PI_qPOS( self.ID, self.szAxes, self.position )
			print( f'position:\t\t{self.position.value:.4f} μm' )
			# Gets the velocity value for szAxes.
			PIGCS_dll.PI_qVEL( self.ID, self.szAxes, self.velocity )
			print( f'velocity:\t\t{self.velocity.value} μm/s' )
			# Get the wave table rate
			piInterpolationTypeArray = (ctypes.c_int * 1)(0)
			PIGCS_dll.PI_qWTR( self.ID, self.piWaveGeneratorIdsArray, self.piTableRateArray, piInterpolationTypeArray, 1 )
			print(f'rate:\t\t{self.piWaveGeneratorIdsArray[0]} × 0.1 ms')
			# Get the number of wave cycles
			PIGCS_dll.PI_qWGC( self.ID, self.piWaveGeneratorIdsArray, self.piNumberOfCyclesArray, 1 )
			print(f'cycles:\t\t{self.piNumberOfCyclesArray[0]}')
			# Get the number of wave points
			piParamereIdsArray = (ctypes.c_int * 1)(1)
			PIGCS_dll.PI_qWAV( self.ID, self.piWaveTableIdsArray, piParamereIdsArray, self.pdValueArray, 1 )
			print(f'points:\t\t{self.pdValueArray[0]}')
			# Read the commanded target positions for szAxes.
			PIGCS_dll.PI_qMOV( self.ID, self.szAxes, self.position_targeted ) # the inertial targeted position seemed unable to set
			print( f'position_targeted:\t{self.position_targeted.value} μm' )
	
	def error(self):
		if self.connected_flag.value:
			PIGCS_dll.PI_qERR( self.ID, self.pnError )
			PIGCS_dll.PI_TranslateError( self.pnError, self.szBuffer, 128 )
			print( f'error {self.pnError.value} - {self.szBuffer.value.decode("UTF-8")}\n' )
	
	def move_to(self, position):
		# The device is able to send commands while moving
		# PIGCS_dll.PI_IsMoving ( self.ID, self.szAxes, self.moving_flag )
		position = max(0.0, min(position, 399.99))
		if self.connected_flag.value and not( self.moving_flag.value ):
			PIGCS_dll.PI_MOV( self.ID, self.szAxes, ctypes.c_double(position) )
	
	def move_by(self, position):
		# The device is able to send commands while moving
		# PIGCS_dll.PI_IsMoving ( self.ID, self.szAxes, self.moving_flag )
		position_new = self.position.value + position
		position_new = max(0.0, min(position_new, 399.99))
		if self.connected_flag.value and not( self.moving_flag.value ):
			PIGCS_dll.PI_MVR( self.ID, self.szAxes, ctypes.c_double(position) )
	
	def position_update(self):
		if self.connected_flag.value:
			# It seems no need to judge connection
			# self.connected_flag = ctypes.c_bool( PIGCS_dll.PI_IsConnected( self.ID ) )
			# In almost cases, PIPiezo.position_targeted.value == host.piezo_targeted, then PI_qMOV() is not needed
			# PIGCS_dll.PI_qMOV( self.ID, self.szAxes, self.position_targeted ) # the inertial targeted position seemed unable to set
			PIGCS_dll.PI_qPOS( self.ID, self.szAxes, self.position )
	
	def z_stack_prepare(self, position):
		if self.connected_flag.value:
			# position = numpy.array([0, 10, 30, 100, 150, 270, 350, 399])
			offset = numpy.append(position[0], position[:-1])
			amplitude = position - offset # must <100 um 

			for i in range(position.shape[0]):
				iWaveTableId = ctypes.c_int(self.piWaveTableIdsArray[0])
				iOffsetOfFirstPointInWaveTable = ctypes.c_int(50) # 0.1 ms * rate
				iNumberOfPoints = ctypes.c_int(100) # 0.1 ms * rate
				if i == 0:
					iAddAppendWave = ctypes.c_int(0) # 0 for new, 2 for append
				else:
					iAddAppendWave = ctypes.c_int(2) # 0 for new, 2 for append
				iNumberOfSpeedUpDownPointsInWave = ctypes.c_int(10) # 0.1 ms * rate
				dAmplitudeOfWave = ctypes.c_double(amplitude[i]) # um
				dOffsetOfWave = ctypes.c_double(offset[i]) # um
				iSegmentLength = ctypes.c_int(200) # 0.1 ms * rate
				PIGCS_dll.PI_WAV_LIN( self.ID, iWaveTableId, iOffsetOfFirstPointInWaveTable, iNumberOfPoints, iAddAppendWave, iNumberOfSpeedUpDownPointsInWave, dAmplitudeOfWave, dOffsetOfWave, iSegmentLength )
			
			iStartModArray = (ctypes.c_int * 1)(2)
			PIGCS_dll.PI_MOV( self.ID, self.szAxes, ctypes.c_double(position[0]) )
			PIGCS_dll.PI_WSL( self.ID, self.piWaveGeneratorIdsArray, self.piWaveTableIdsArray, 1)
			PIGCS_dll.PI_WGO( self.ID, self.piWaveGeneratorIdsArray, iStartModArray, 1)
	
	def z_stack_finish(self):
		if self.connected_flag.value:
			iStartModArray = (ctypes.c_int * 1)(0)
			PIGCS_dll.PI_WGO( self.ID, self.piWaveGeneratorIdsArray, iStartModArray, 1)

	
	# class variables interface
	
	def position_export(self):
		self.position_update()
		return(self.position.value)
	

class ASIStage:
	stage = None
	
	position_x = 0.0 # 100 nm
	position_y = 0.0 # 100 nm
	
	def __init__(self):
		# the xy stage prefixing with 2H, the z stage with 1H, the filter wheel with 3F. Ref. http://micro-manager.3463995.n2.nabble.com/Contributing-to-Micro-Manager-tt6459068.html#a7579589
		self.stage = serial.Serial( 'COM5', 115200, timeout = 0.1 )
		self.stage.readlines()
		self.position_update()
		while self.position_x > 10 or self.position_y > 10:
			self.move_to([0.0, 0.0])
			self.position_update()
			time.sleep(0.01)
	
	def close(self):
		self.position_update()
		while not ( -10 < self.position_x < 10 or -10 < self.position_y < 10):
			self.move_to([0.0, 0.0])
			self.position_update()
			time.sleep(0.1)
		# self.stage.write(b'2H RESET \r')
		self.stage.readlines()
		self.stage.close()
	
	def information(self):
		self.stage.write(b'2H CDATE \r')
		for line in self.stage.readlines():
			line = line.replace(b'\r', b'\r\n')
			print(line.decode('UTF-8'))
		self.stage.write(b'2H INFO X\r')
		for line in self.stage.readlines():
			line = line.replace(b'\r', b'\r\n')
			print(line.decode('UTF-8'))
		self.stage.write(b'2H INFO Y\r')
		for line in self.stage.readlines():
			line = line.replace(b'\r', b'\r\n')
			print(line.decode('UTF-8'))
	
	def position_update(self):
		# self.stage.readlines()
		self.stage.write(b'2H WHERE X Y\r')
		line = self.stage.readline()
		info = line.split(b' ')
		if len(info) > 3:
			self.position_x = float(info[1])
			self.position_y = float(info[2])
	
	def move_to(self, position):
		# MOVREL command for 100 nm, new position is updated in AuxiliaryControl for every loop
		text = f'2H MOVE X={position[0] * 10000:.1f} Y={position[1] * 10000:.1f}\r'
		self.stage.write(text.encode())
		self.stage.readline()
	
	def move_by(self, position):
		# MOVREL command for 100 nm, new position is updated in AuxiliaryControl for every loop
		text = f'2H MOVREL X={position[0] * 10000:.1f} Y={position[1] * 10000:.1f}\r'
		self.stage.write(text.encode())
		self.stage.readline()
	
	# class variables interface
	
	def position_export(self):
		self.position_update()
		return(self.position_x / 10000, self.position_y / 10000) # mm
	

