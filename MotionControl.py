from Modules import PIGCSDLL

import ctypes
import time
import numpy
import serial

class PIPiezo:
	piezo = ctypes.windll.LoadLibrary("Libraries/PI_GCS2_DLL_x64.dll")
	
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
	
	def __init__(self):
		PIGCSDLL.PIGCS(self.piezo)
		
		# Lists the identification strings of all controllers available via USB interfaces
		self.piezo.PI_EnumerateUSB( self.szBuffer, 128, self.szFilter )
		# print(szBuffer.value.decode('UTF-8'))
		# Open an USB connection to a controller
		self.ID = ctypes.c_int( self.piezo.PI_ConnectUSB( self.szBuffer ) )
		# print(ID.value)
		# Get the identifiers for all configured and unconfigured axes
		self.piezo.PI_qSAI_ALL( self.ID, self.szAxes, 8 )
		# print(szAxes.value.decode('UTF-8'))
		# Set self.stagevo-control "on" or "off" (closed-loop/open-loop mode).
		self.piezo.PI_SVO( self.ID, self.szAxes, self.stagevo_mode )
		# Get the current positions of szAxes.
		self.piezo.PI_qPOS( self.ID, self.szAxes, self.position )
		self.piezo.PI_qMOV( self.ID, self.szAxes, self.position_targeted )
		# print(f'Position: {position.value:.6f} μm\n')
		# Sets and gets the velocity value for szAxes.
		self.piezo.PI_VEL( self.ID, self.szAxes, self.velocity )
		self.piezo.PI_qVEL( self.ID, self.szAxes, self.velocity )
		# print(f'Velocity: {velocity.value} unit/s\n')
		self.connected_flag = ctypes.c_bool( self.piezo.PI_IsConnected( self.ID ) )
		# TO avoid numerical screening floating
		self.move_to(0.1)
	
	def close(self):
		self.move_to(0.0)
		# Make sure not moving nor connected
		self.piezo.PI_IsMoving ( self.ID, self.szAxes, self.moving_flag )
		while self.moving_flag.value:
			self.piezo.PI_IsMoving ( self.ID, self.szAxes, self.moving_flag )
		if self.piezo.PI_IsConnected( self.ID ):
			self.piezo.PI_CloseConnection( self.ID )
		self.connected_flag = ctypes.c_bool(False)
		self.moving_flag = ctypes.c_bool(False)
	
	def information(self):
		if self.connected_flag.value:
			# Get identification string of the controller.
			self.piezo.PI_qIDN( self.ID, self.szBuffer, 128 )
			print( self.szBuffer.value.decode('UTF-8') )
			# Reports the versions of the controller firmware and the underlying drivers and libraries.
			self.piezo.PI_qVER( self.ID, self.szBuffer, 128 )
			print( self.szBuffer.value.decode('UTF-8') )
			# Get the type names of the stages associated with szAxes.
			self.piezo.PI_qCST( self.ID, self.szAxes, self.szNames, 32)
			print( self.szNames.value.decode('UTF-8') )
			self.piezo.PI_qPOS( self.ID, self.szAxes, self.position )
			print( f'position:\t\t{self.position.value:.4f} μm\n' )
			# Gets the velocity value for szAxes.
			self.piezo.PI_qVEL( self.ID, self.szAxes, self.velocity )
			print( f'velocity:\t\t{self.velocity.value} μm/s\n' )
			# Read the commanded target positions for szAxes.
			self.piezo.PI_qMOV( self.ID, self.szAxes, self.position_targeted ) # the inertial targeted position seemed unable to set
			print( f'position_targeted:\t{self.position_targeted.value} μm\n' )
	
	def error(self):
		if self.connected_flag.value:
			self.piezo.PI_qERR( self.ID, self.pnError )
			self.piezo.PI_TranslateError( self.pnError, self.szBuffer, 128 )
			print( f'error {self.pnError.value} - "{self.szBuffer.value.decode("UTF-8")}"\n' )
	
	def move_to(self, position):
		# The device is able to send commands while moving
		# self.piezo.PI_IsMoving ( self.ID, self.szAxes, self.moving_flag )
		if self.connected_flag.value and not( self.moving_flag.value ):
			self.piezo.PI_MOV( self.ID, self.szAxes, ctypes.c_double(position) )
	
	def move_by(self, position):
		# The device is able to send commands while moving
		# self.piezo.PI_IsMoving ( self.ID, self.szAxes, self.moving_flag )
		if self.connected_flag.value and not( self.moving_flag.value ):
			self.piezo.PI_MVR( self.ID, self.szAxes, ctypes.c_double(position) )
	
	def position_update(self):
		if self.connected_flag.value:
			# It seems no need to judge connection
			# self.connected_flag = ctypes.c_bool( self.piezo.PI_IsConnected( self.ID ) )
			# In almost cases, PIPiezo.position_targeted.value == host.piezo_targeted, then PI_qMOV() is not needed
			# self.piezo.PI_qMOV( self.ID, self.szAxes, self.position_targeted ) # the inertial targeted position seemed unable to set
			self.piezo.PI_qPOS( self.ID, self.szAxes, self.position )
	
	def position_value(self):
		return(self.position.value)
	
class ASIStage:
	stage = None
	
	position_x = 0.0
	position_y = 0.0
	position_x_limit_up = 40.0 * 10000
	position_x_limit_down = -40.0 * 10000
	position_y_limit_up = 20.0 * 10000
	position_y_limit_down = -40.0 * 10000
	
	def __init__(self):
		# the xy stage prefixing with 2H, the z stage with 1H, the filter wheel with 3F. Ref. http://micro-manager.3463995.n2.nabble.com/Contributing-to-Micro-Manager-tt6459068.html#a7579589
		self.stage = serial.Serial( 'COM5', 115200, timeout = 0.1 )
		self.stage.readlines()
	
	def close(self):
		self.move_to([0.0, 0.0])
		time_sleep = max( self.position_x, self.position_y ) / 10000
		time.sleep( time_sleep / 5 ) # not enough?
		self.stage.write(b'2H RESET \r')
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
	
	def position_value(self):
		return(numpy.array([self.position_x, self.position_y]))
	
	def move_to(self, position):
		# MOVE command for 100 nm
		if position[0] > self.position_x_limit_down and position[0] < self.position_x_limit_up and position[1] > self.position_y_limit_down and position[1] < self.position_y_limit_up:
			text = f'2H MOVE X={position[0]:.1f} Y={position[1]:.1f}\r'
			self.stage.write(text.encode())
			self.stage.readline()
	
	def move_by(self, position):
		# MOVREL command for 100 nm
		position_new = [self.position_x, self.position_y] + position
		if position_new[0] > self.position_x_limit_down and position_new[0] < self.position_x_limit_up and position_new[1] > self.position_y_limit_down and position_new[1] < self.position_y_limit_up:
			text = f'2H MOVREL X={position[0]:.1f} Y={position[1]:.1f}\r'
			self.stage.write(text.encode())
			self.stage.readline()
	
		