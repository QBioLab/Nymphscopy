import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'Modules'))
import Stages
import Arduino

import ctypes
import time
import numpy
import multiprocessing.connection

class AuxiliaryControl:
	client_motor = None
	piezo = None
	stage = None
	arduino = None
	
	# old_variables
	stage_x_current = 0.0 # mm
	stage_y_current = 0.0 # mm
	motor_current = 0.0 # mm
	piezo_current = 0.0 # μm
	photoactive_shutter_current = [0, 0, 0, 0]
	autofocus_laser_power_current = 0
	
	# variables
	stage_x_targeted = 0.0 # mm
	stage_y_targeted = 0.0 # mm
	motor_targeted = 0.0 # mm
	piezo_targeted = 0.0 # μm
	photoactive_shutter_targeted = [0, 0, 0, 0]
	autofocus_laser_power_targeted = 0
	
	
	# motion limitations, need to be reset
	stage_x_limit_up = 40.0 # * 10000 # 100 nm
	stage_x_limit_down = -40.0 # * 10000 # 100 nm
	stage_y_limit_up = 20.0 # * 10000 # 100 nm
	stage_y_limit_down = -40.0 # * 10000 # 100 nm
	motor_limit_up = 10.0 # mm
	motor_limit_down = 0.0 # mm
	piezo_limit_up = 399.99 # μm
	piezo_limit_down = 0.0 # μm
	# change_threshold = 0.001 # mm
	
	def __init__(self):
		#TODO: require better logic to connect motor
		self.client_motor = multiprocessing.connection.Client( ('localhost', 6101), authkey = b'hwlab' )
		self.piezo = Stages.PIPiezo()
		self.stage = Stages.ASIStage()
		self.arduino = Arduino.Arduino()
	
	def close(self, argument):
		self.client_motor.send(['close', 0])
		self.client_motor.close()
		self.piezo.close()
		self.stage.close()
		self.arduino.close()
		del self.client_motor
		del self.piezo
		del self.stage
	
	def read_arduino(self):
		# refresh all x, y, and z targeted value from arduino
		change = self.arduino.axis_reset()
		axis_x_change, axis_y_change, axis_z_change = self.arduino.axis_export()
		self.stage_x_targeted = self.stage_x_targeted + axis_x_change
		self.stage_y_targeted = self.stage_y_targeted + axis_y_change
		self.motor_targeted = self.motor_targeted + axis_z_change
		return(change)
	
	def read_nymphscope(self, argument):
		# refresh all x, y, and z targeted value from the main application
		self.stage_x_targeted = argument[0]
		self.stage_y_targeted = argument[1]
		self.motor_targeted = argument[2]
		self.piezo_targeted = argument[3]
		self.photoactive_shutter_targeted = [argument[4], argument[5], argument[6], argument[7]]
		self.autofocus_laser_power_targeted = argument[8]
	
	def control_all(self):
		# PI Piezo
		if numpy.abs(self.piezo_current-self.piezo_targeted)>0.05:
			self.piezo_targeted = max( self.piezo_limit_down, min(self.piezo_targeted, self.piezo_limit_up) )
			self.piezo.move_to(self.piezo_targeted)
		
		# ASI stage
		if numpy.abs(self.stage_x_current-self.stage_x_targeted)>0.002 or numpy.abs(self.stage_y_current-self.stage_y_targeted)>0.002:
			self.stage_x_targeted = max( self.stage_x_limit_down, min(self.stage_x_targeted, self.stage_x_limit_up) )
			self.stage_y_targeted = max( self.stage_y_limit_down, min(self.stage_y_targeted, self.stage_y_limit_up) )
			self.stage.move_by([self.stage_x_targeted - self.stage_x_current, self.stage_y_targeted - self.stage_y_current])
		
		# Step motor
		if numpy.abs(self.motor_current-self.motor_targeted)>0.002:
			self.motor_targeted = max( self.motor_limit_down, min(self.motor_targeted, self.motor_limit_up) )
			self.client_motor.send( ['motor_move_to', self.motor_targeted] )
		
		# Photoactive shutter
		if self.photoactive_shutter_current != self.photoactive_shutter_targeted:
			self.arduino.laser_on_reset(self.photoactive_shutter_targeted)
		
		# Autofocus laser
		if self.autofocus_laser_power_current != self.autofocus_laser_power_targeted:
			self.arduino.focus_power_reset(self.autofocus_laser_power_targeted)
	
	def status_hardware_update(self):
		# hardware current status
		self.stage_x_current, self.stage_y_current = self.stage.position_export()
		self.client_motor.send( ['status', 0] )
		message = self.client_motor.recv()
		self.motor_current = message['motor_position']
		self.piezo_current = self.piezo.position_export()
		self.photoactive_shutter_current = self.arduino.laser_on_export()
		self.autofocus_laser_power_current = self.arduino.focus_power_export()
	
	def status_export(self, argument):
		# hardware current status
		status = {'stage_x_targeted':self.stage_x_targeted, 'stage_y_targeted':self.stage_y_targeted, 'motor_targeted':self.motor_targeted, 'piezo_targeted':self.piezo_targeted, 'stage_x_current':self.stage_x_current, 'stage_y_current':self.stage_y_current, 'motor_current':self.motor_current, 'piezo_current':self.piezo_current, 'photoactive_shutter':self.photoactive_shutter_current, 'autofocus_laser_power':self.autofocus_laser_power_current}
		return(status)
	
	def piezo_stack_prepare(self, position):
		self.piezo.z_stack_prepare(position)
		return('Standby')
	
	def piezo_stack_finish(self, argument):
		self.piezo.z_stack_finish()
	
	def unknown_command(self, argument):
		return('WTF is that?')

if __name__ == '__main__':
	with multiprocessing.connection.Listener( ('localhost', 6002), authkey = b'hwlab' ) as server_auxliary:
		with server_auxliary.accept() as receiver:
			control = AuxiliaryControl()
			message = None
			command = None
			argument = None
			command_mapping = { 'close':control.close, 'status':control.status_export, \
					'piezo_stack_prepare':control.piezo_stack_prepare, \
					'piezo_stack_finish':control.piezo_stack_finish, \
					'refresh_targets':control.read_nymphscope }
			while True:
				# refresh hardware variables
				control.status_hardware_update()
				if receiver.poll(timeout = 0.05):
					message = receiver.recv()
					command = command_mapping.get( message[0], control.unknown_command )
					argument = message[1]
					if message[0] == 'close':
						command(argument)
						del control
						break
					elif message[0] == 'refresh_targets' or message[0] == 'piezo_stack_finish':
						command(argument)
						control.control_all()
					else:
						receiver.send(command(argument))
				if control.read_arduino():
					# Stick movement is detected by arduino
					control.control_all()
				# time.sleep(0.002)
				# the refresh rate should be longer than the arduino serial transmission sequence
