import time
import numpy
import serial

class Arduino:
	port = None
	laser_on = [0, 0, 0, 0]
	focus_power = 0
	axis_x = 0.0
	axis_x_change = 0.0
	axis_y = 0.0
	axis_y_change = 0.0
	axis_z = 0.0
	axis_z_change = 0.0
	coarse_xy = 0
	coarse_z = 0
	
	def __init__(self):
		self.port = serial.Serial( 'COM3', 115200, timeout = 0.001 )
		# self.port.readline()
		command = '0254\n'.encode()
		self.port.write(command)
	
	def close(self):
		command = '0255\n'.encode()
		self.port.write(command)
		self.port.close()
	
	def pin_write(self, pin, action):
		# to convert int into char
		action_string = ''
		for _ in range(3):
			res = action % 10
			action = action // 10
			action_string = f'{chr(res + 48)}{action_string}'
		command = f'{chr(pin + 48)}{action_string}\n'.encode()
		self.port.write(command)
	
	# class variables interface
	
	def laser_on_reset(self, state):
		for pin in range(0, 4):
			self.pin_write( pin + 1, state[pin] )
		self.laser_on = state
	
	def laser_on_export(self):
		return( self.laser_on )
	
	def focus_power_reset(self, action):
		pin = 9
		action = max(0, min(action, 255))
		self.pin_write(pin, action)
		self.focus_power = action
	
	def focus_power_export(self):
		return( self.focus_power )
	
	def axis_reset(self):
		change = False
		coarse_map = {0:0.001, 1:0.05}
		pin = 0
		action = 0
		self.pin_write(pin, action)
		axis_x_line = self.port.readline()
		axis_y_line = self.port.readline()
		axis_z_line = self.port.readline()
		coarse_line = self.port.readline()
		try:
			self.coarse_xy = int(coarse_line) % 2
			self.coarse_z = int(coarse_line) // 2
			axis_x_read = int(axis_x_line)
			axis_y_read = int(axis_y_line)
			axis_z_read = int(axis_z_line)
		except ValueError:
			axis_x_change = 0
			axis_y_change = 0
			axis_z_change = 0
		else:
			change = bool(axis_x_read-self.axis_x) or bool(axis_y_read-self.axis_y) or bool(axis_z_read-self.axis_z)
			# Stick movement is detected by arduino
			self.axis_x_change = (axis_x_read - self.axis_x) * coarse_map[self.coarse_xy]
			self.axis_x = axis_x_read
			self.axis_y_change = (axis_y_read - self.axis_y) * coarse_map[self.coarse_xy]
			self.axis_y = axis_y_read
			self.axis_z_change = - (axis_z_read - self.axis_z) * coarse_map[self.coarse_z] / 5
			self.axis_z = axis_z_read
		return(change)
	
	def axis_export(self):
		# The change or itself?
		return(self.axis_x_change, self.axis_y_change, self.axis_z_change)
	

