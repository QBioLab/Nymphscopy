import ctypes
import time
import numpy
import os
import sys
import subprocess
import cv2
import multiprocessing.connection

class Nymphscope:
	client_confocal = None
	client_photoactive = None
	client_auxiliary = None
	client_camera = None
	application_label = 'Nymphscope main application'
	living_flag = False
	
	exposure_time = 10 # ms
	current_image = None
	savepath = 'C:/Data/'
	
	# confocal variables
	pinhole_label = 'Wide Field' # pinhole: 6.5='Wide Field', 16.5='50 μm', 26.5='30 μm', 36.5='20 μm'
	filter_label = 'Four Color' # emission filter: 50='447/60', 110='525/45', 170='586/20', 230='615/24', 350='676/29', 290='Four Color'(446/523/600/677)
	laser_on = [0, 0, 0, 0] # [405nm, 488nm, 561nm, 633nm]
	laser_power = [0, 0, 0, 0] # laser power output, 0-100, [405nm, 488nm, 561nm, 633nm]
	
	# image exhibition variables
	dynamic_range = { 'low':100, 'high':65535 }
	region_of_interest = { 'x1':0, 'y1':0, 'x2':2047, 'y2':2047 }
	point_of_selected = [0, 0, 0] # { 'x':0, 'y':0, 'intensity':0 }
	image_size = 1024
	image_color = [255, 255, 255]
	image_histogram = None # numpy.zeros( (0, 0, 3), dtype = numpy.uint8 )
	image_exhibition = None # numpy.zeros( (0, 0, 3), dtype = numpy.uint8 )
	
	# stage and other variables
	stage_x_current = 0.0 # mm
	stage_y_current = 0.0 # mm
	motor_current = 0.0 # mm
	piezo_current = 0.0 # μm
	stage_x_targeted = 0.0 # mm
	stage_y_targeted = 0.0 # mm
	motor_targeted = 0.0 # mm
	piezo_targeted = 0.0 # μm
	stage_relative = 0.01 # mm
	motor_relative = 0.1 # mm
	piezo_relative = 1.0 # μm
	stage_x_chosen = 0.0 # mm
	stage_y_chosen = 0.0 # mm
	photoactive_shutter = [0, 0, 0, 0]
	autofocus_laser_power = 0
	
	def __init__(self):
		self.application_label = 'Nymphscope opening boards...'
		subprocess.Popen(f'python {os.getcwd()}\\Modules\\ConfocalBoard.py')
		subprocess.Popen(f'python {os.getcwd()}\\Modules\\PhotoactiveBoard.py')
		subprocess.Popen(f'python {os.getcwd()}\\Modules\\AuxiliaryControl.py')
		subprocess.Popen(f'python {os.getcwd()}\\Modules\\CameraControl.py')
		self.client_confocal = multiprocessing.connection.Client( ('localhost', 6000), authkey = b'hwlab' )
		self.client_photoactive = multiprocessing.connection.Client( ('localhost', 6001), authkey = b'hwlab' )
		self.client_auxiliary = multiprocessing.connection.Client( ('localhost', 6002), authkey = b'hwlab' )
		self.client_camera = multiprocessing.connection.Client( ('localhost', 6003), authkey = b'hwlab' )
		time.sleep(5)
		
		# Initialize confocal settings
		self.client_confocal.send(['pinhole', self.pinhole_label])
		self.client_confocal.send(['filter_wheel', self.filter_label])
		self.client_confocal.send(['mark_speed_reset', self.exposure_time])
		self.client_confocal.send(['laser_on_reset', self.laser_on])
		self.client_confocal.send(['laser_power_reset', self.laser_power])
		time.sleep(1)
		
		# Initialize auxiliary control
		self.client_auxiliary.send(['refresh_targets', [self.stage_x_targeted, self.stage_y_targeted, self.motor_targeted, self.piezo_targeted, self.photoactive_shutter[0], self.photoactive_shutter[1], self.photoactive_shutter[2], self.photoactive_shutter[3], self.autofocus_laser_power]])
		time.sleep(1)
		
		# Initialize Camera settings
		self.client_camera.send(['exposure_time_reset', self.exposure_time])
		time.sleep(0.1)
		
		# Initialize complete
		self.application_label = 'Nymphscope main application'
	
	def close(self):
		self.application_label = 'Nymphscope closing boards...'
		self.client_confocal.send(['close', 'Null'])
		self.client_confocal.close()
		time.sleep(0.1)
		self.client_auxiliary.send(['close', 'Null'])
		self.client_auxiliary.close()
		time.sleep(0.1)
		self.client_photoactive.send(['close', 'Null'])
		self.client_photoactive.close()
		time.sleep(0.1)
		self.client_camera.send(['close', 'Null'])
		self.client_camera.close()
		time.sleep(5)
		self.application_label = 'Nymphscope main application'
	
	def update_status(self):
		# confocal variables
		self.client_confocal.send(['status', 'Null'])
		message = self.client_confocal.recv()
		self.pinhole_label = message['pinhole']
		self.filter_label = message['filter_wheel']
		# self.laser_on = message['laser_on'] # The laser is on only at recording
		self.laser_power = message['laser_power']
		speed = message['mark_speed']
		
		# self.client_photoactive.send(['status', 0])
		# message = client_photoactive.recv()
		
		# stage and other variables
		self.client_auxiliary.send(['status', 'Null'])
		status_auxiliary = self.client_auxiliary.recv()
		self.stage_x_current = status_auxiliary['stage_x_current']
		self.stage_y_current = status_auxiliary['stage_y_current']
		self.motor_current = status_auxiliary['motor_current']
		self.piezo_current = status_auxiliary['piezo_current']
		self.stage_x_targeted = status_auxiliary['stage_x_targeted']
		self.stage_y_targeted = status_auxiliary['stage_y_targeted']
		self.motor_targeted = status_auxiliary['motor_targeted']
		self.piezo_targeted = status_auxiliary['piezo_targeted']
		self.photoactive_shutter = status_auxiliary['photoactive_shutter']
		self.autofocus_laser_power = status_auxiliary['autofocus_laser_power']
		
		# camera export
		self.client_camera.send(['camera_export', 'Null'])
		message = self.client_camera.recv()
		exposure_time = message['exposure_time']
		if speed > 60.0*1.4142*1000/exposure_time*0.99 and speed < 60.0*1.4142*1000/exposure_time*1.01:
			self.exposure_time = exposure_time
		else:
			self.exposure_time = -1
		self.current_image = message['current_image']
		
		# image exhibition
		self.histogram_generate() # ~ 2 ms  （i5-8265U）
		self.image_generate() # ~ 33 ms （i5-8265U）
	
		
	# imaging operations
	
	def take_signal(self):
		self.application_label = 'Nymphscope taking signal'
		self.client_camera.send(['acquisition_capture', 'Null'])
		self.client_confocal.send(['confocal_mark_prepare', 1])
		self.client_confocal.recv()
		self.client_confocal.send(['confocal_mark', 'Null'])
		time.sleep(0.001+self.exposure_time*25/60/1000)
		self.client_confocal.send(['laser_on_reset', self.laser_on]) # open laser
		time.sleep((self.exposure_time+20)/1000)
		self.client_confocal.send(['laser_on_reset', [0, 0, 0, 0]]) # close laser
		self.application_label = 'Nymphscope main application'
	
	def live_signal(self):
		self.application_label = 'Nymphscope taking signal'
		self.client_camera.send(['acquisition_live', 'Null'])
		self.client_confocal.send(['confocal_mark_prepare', 0])
		self.client_confocal.recv()
		self.client_confocal.send(['confocal_mark', 'Null'])
		time.sleep(0.001+self.exposure_time*25/60/1000)
		self.client_confocal.send(['laser_on_reset', self.laser_on]) # open laser
	
	def live_stop(self):
		self.client_confocal.send(['stop_mark', 'Null'])
		time.sleep((self.exposure_time+20)/1000)
		self.client_confocal.send(['laser_on_reset', [0, 0, 0, 0]]) # close laser
		self.client_camera.send(['acquisition_stop', 'Null'])
		self.application_label = 'Nymphscope main application'
	
	def fast_timelapse(self, frames, path):
		self.application_label = 'Nymphscope taking fast timelapse'
		self.client_camera.send(['acquisition_fastlapse', path])
		self.client_confocal.send(['confocal_mark_prepare', frames])
		self.client_confocal.recv()
		self.client_confocal.send(['confocal_mark', 'Null'])
		time.sleep(0.001+self.exposure_time*25/60/1000)
		self.client_confocal.send(['laser_on_reset', self.laser_on]) # open laser
		time.sleep((self.exposure_time+20)/1000*frames + 0.02)
		self.client_confocal.send(['laser_on_reset', [0, 0, 0, 0]]) # close laser
		self.client_camera.send(['acquisition_stop', 'Null'])
		self.application_label = 'Nymphscope main application'
	
	def fast_z_stack_prepare(self, z_stack, path): # z_stack, i.e. numpy.array([0, 10, 30, 100, 150, 270, 350, 399, 300, 200, 50, 0])
		self.application_label = 'Nymphscope taking z stack'
		frames = z_stack.shape[0]
		self.client_auxiliary.send(['piezo_stack_prepare', z_stack])
		message = self.client_auxiliary.recv() # wait the initialization of piezo
		self.client_camera.send(['acquisition_fastlapse', path])
		self.client_confocal.send(['confocal_mark_prepare', frames])
		self.client_confocal.recv()
		return(frames)
	
	def fast_z_stack(self, frames):
		self.client_confocal.send(['confocal_mark', 'Null'])
		time.sleep(0.001+self.exposure_time*25/60/1000)
		self.client_confocal.send(['laser_on_reset', self.laser_on]) # open laser
		time.sleep((self.exposure_time+20)/1000*frames + 0.02)
		self.client_confocal.send(['laser_on_reset', [0, 0, 0, 0]]) # close laser
		self.client_camera.send(['acquisition_stop', 'Null'])
		self.client_auxiliary.send(['piezo_stack_finish', 'Null'])
		self.application_label = 'Nymphscope main application'
	
	def scan_6D(self):
		# Undeveloped
		return(0)
	
	def save_image(self, path):
		self.savepath = path
		self.client_camera.send(['single_serial_save', path])
	
	# confocal variable functions
	
	def exposure_time_reset(self, exposure_time):
		self.client_confocal.send(['mark_speed_reset', exposure_time])
		self.client_camera.send(['exposure_time_reset', exposure_time])
	
	def pinhole_reselect(self, pinhole_label):
		self.client_confocal.send(['pinhole', pinhole_label])
	
	def filter_reselect(self, filter_label):
		self.client_confocal.send(['filter_wheel', filter_label])
	
	def laser_on_reset(self, laser_on):
		self.laser_on = laser_on # The laser is on only at recording
	
	def laser_power_reset(self, laser_power):
		self.client_confocal.send(['laser_power_reset', laser_power])
	
	# auxiliary control functions
	
	def stage_x_move(self, value): # move by
		self.stage_x_targeted += value
		self.client_auxiliary.send(['refresh_targets', [self.stage_x_targeted, self.stage_y_targeted, self.motor_targeted, self.piezo_targeted, self.photoactive_shutter[0], self.photoactive_shutter[1], self.photoactive_shutter[2], self.photoactive_shutter[3], self.autofocus_laser_power]])
	
	def stage_y_move(self, value): # move by
		self.stage_y_targeted += value
		self.client_auxiliary.send(['refresh_targets', [self.stage_x_targeted, self.stage_y_targeted, self.motor_targeted, self.piezo_targeted, self.photoactive_shutter[0], self.photoactive_shutter[1], self.photoactive_shutter[2], self.photoactive_shutter[3], self.autofocus_laser_power]])
	
	def stage_xy_move(self, value_x, value_y): # move to
		self.stage_x_targeted = value_x
		self.stage_y_targeted = value_y
		self.client_auxiliary.send(['refresh_targets', [self.stage_x_targeted, self.stage_y_targeted, self.motor_targeted, self.piezo_targeted, self.photoactive_shutter[0], self.photoactive_shutter[1], self.photoactive_shutter[2], self.photoactive_shutter[3], self.autofocus_laser_power]])
	
	def motor_move(self, value, mode):
		if mode == 0: # move to
			self.motor_targeted = value
		elif mode == 1: # move by
			self.motor_targeted += value
		self.client_auxiliary.send(['refresh_targets', [self.stage_x_targeted, self.stage_y_targeted, self.motor_targeted, self.piezo_targeted, self.photoactive_shutter[0], self.photoactive_shutter[1], self.photoactive_shutter[2], self.photoactive_shutter[3], self.autofocus_laser_power]])
	
	def piezo_move(self, value, mode):
		if mode == 0: # move to
			self.piezo_targeted = value
		elif mode == 1: # move by
			self.piezo_targeted += value
		self.client_auxiliary.send(['refresh_targets', [self.stage_x_targeted, self.stage_y_targeted, self.motor_targeted, self.piezo_targeted, self.photoactive_shutter[0], self.photoactive_shutter[1], self.photoactive_shutter[2], self.photoactive_shutter[3], self.autofocus_laser_power]])
	
	def photoactive_shutter_reset(self, state, pin):
		self.photoactive_shutter[pin] = state
		self.client_auxiliary.send(['refresh_targets', [self.stage_x_targeted, self.stage_y_targeted, self.motor_targeted, self.piezo_targeted, self.photoactive_shutter[0], self.photoactive_shutter[1], self.photoactive_shutter[2], self.photoactive_shutter[3], self.autofocus_laser_power]])
	
	def autofocus_laser_power_reset(self, value):
		self.autofocus_laser_power = value
		self.client_auxiliary.send(['refresh_targets', [self.stage_x_targeted, self.stage_y_targeted, self.motor_targeted, self.piezo_targeted, self.photoactive_shutter[0], self.photoactive_shutter[1], self.photoactive_shutter[2], self.photoactive_shutter[3], self.autofocus_laser_power]])
	
	# image exhibition functions
	
	def histogram_generate(self):
		# draw histogram based on statistical data on image intensity
		hist = numpy.histogram(
			numpy.log10( cv2.resize(
				self.current_image, 
				(256, 256), interpolation=cv2.INTER_NEAREST
			).reshape(256 * 256) ), 
			256, (2.0, 4.81648)
		)
		self.image_histogram = numpy.zeros( (128, 256, 3), dtype = numpy.uint8 ) + 255
		for i in range(256):
			self.image_histogram[ max(127-int(hist[0][i]/1024*127.999), 0):128, i, : ] = 0
	
	def image_generate(self):
		image_clip = self.current_image[ self.region_of_interest['x1']: self.region_of_interest['x2'], self.region_of_interest['y1']: self.region_of_interest['y2'] ]
		image_resized = cv2.resize( image_clip, (self.image_size, self.image_size), interpolation=cv2.INTER_NEAREST )
		image_resized_clip = numpy.clip( image_resized, self.dynamic_range['low'], self.dynamic_range['high'] )
		image_int8 = ( (image_resized_clip - self.dynamic_range['low']) / (self.dynamic_range['high'] - self.dynamic_range['low']) * 255 ).astype(numpy.uint8)
		self.image_exhibition = numpy.tensordot( image_int8, numpy.array(self.image_color, dtype = numpy.uint8) / 255, axes = 0 ).astype(numpy.uint8)
	
	def dynamic_range_resize(self, dynamic_range):
		for i in range(2):
			dynamic_range[i] = max(100, min( dynamic_range[i], 65535 ))
		# convert list into tuple
		if dynamic_range[0] > dynamic_range[1]:
			self.dynamic_range['low'] = dynamic_range[1]
			self.dynamic_range['high'] = dynamic_range[0]
		elif dynamic_range[0] == dynamic_range[1]:
			self.dynamic_range['low'] = dynamic_range[0]
			self.dynamic_range['high'] = dynamic_range[0] + 1
		else:
			self.dynamic_range['low'] = dynamic_range[0]
			self.dynamic_range['high'] = dynamic_range[1]
	
	def roi_resize(self, region_of_selected):
		x1r, x2r, y1r, y2r = self.region_of_interest['x1'], self.region_of_interest['x2'], self.region_of_interest['y1'], self.region_of_interest['y2']
		x1s = min( region_of_selected['x1'], region_of_selected['x2'] )
		x2s = max( region_of_selected['x1'], region_of_selected['x2'] )
		y1s = min( region_of_selected['y1'], region_of_selected['y2'] )
		y2s = max( region_of_selected['y1'], region_of_selected['y2'] )
		self.region_of_interest['x1'] = int( (x2r - x1r) * x1s / self.image_size ) + x1r
		self.region_of_interest['x2'] = int( (x2r - x1r) * x2s / self.image_size ) + x1r
		self.region_of_interest['y1'] = int( (y2r - y1r) * y1s / self.image_size ) + y1r
		self.region_of_interest['y2'] = int( (y2r - y1r) * y2s / self.image_size ) + y1r
		if self.region_of_interest['x2'] <= self.region_of_interest['x1']:
			self.region_of_interest['x2'] = self.region_of_interest['x1'] + 1
		if self.region_of_interest['y2'] <= self.region_of_interest['y1']:
			self.region_of_interest['y2'] = self.region_of_interest['y1'] + 1
	
	def roi_reset(self):
		self.region_of_interest = { 'x1':0, 'y1':0, 'x2':2047, 'y2':2047 }
	
	def pos_reset(self, coordinate):
		x1r, x2r, y1r, y2r = self.region_of_interest['x1'], self.region_of_interest['x2'], self.region_of_interest['y1'], self.region_of_interest['y2']
		posx = int( (x2r - x1r) * coordinate[0] / self.image_size ) + x1r
		posy = int( (y2r - y1r) * coordinate[1] / self.image_size ) + y1r
		intensity = self.current_image[ posx, posy ] # not sure [x,y] or [y,x]
		self.point_of_selected = [posx, posy, intensity]
	
	def image_resize(self, size):
		self.image_size = size
	
	def image_color_reset(self, color):
		self.image_color = color
	
	

