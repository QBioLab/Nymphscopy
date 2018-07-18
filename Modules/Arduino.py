import time
import numpy
import serial

class Arduino:
	port = None
	
	def __init__(self):
		self.port = serial.Serial( 'COM3', 9600, timeout = 0.1 )
		self.port.readline()
	
	def close(self):
		self.port.close()
	
	def digital_write(self, pin, action):
		# to convert int into char
		pin = pin + 48
		action = action + 48
		command = ''.join([ chr(pin), chr(action), '\n' ]).encode()
		self.port.write(command)
	
