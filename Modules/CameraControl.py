import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'Modules'))
import PVCam

import ctypes
import numpy
import time
import cv2
import PIL.Image
import multiprocessing.connection

class CameraControl:
	camera = None
	continuous_save_flag = False
	
	exp_mode_label = 'External'
	savepath = 'C:/Data/'
	current_image = None
	# exhibition_number = 0
	
	def __init__(self):
		self.camera = PVCam.PVCam()
	
	def close(self, argument):
		self.camera.close()
		del self.camera
	
	def current_image_extract(self):
		self.camera.acquisition_index() # (~ 10 us)
		current_stream = self.camera.pixel_stream[self.camera.image_index - 1]
		self.current_image = numpy.array( current_stream, dtype = numpy.uint16 ).reshape(2048, 2048)
	
	def single_serial_save(self, savepath):
		# only work in single and serial capture
		self.savepath = savepath
		for i in range(self.camera.exp_total):
			image_data = numpy.array( self.camera.pixel_stream[i], dtype = numpy.uint16 )
			image_data_2D = image_data.reshape( 2048, 2048 )
			filename = f'{self.savepath}/image-{i}.tiff'
			PIL.Image.fromarray(image_data_2D).save(filename)
			# cv2.imwrite(filename, image_data_2D)
	
	def continuous_save(self):
		self.camera.acquisition_index() # (~ 10 us)
		if self.camera.circle_index == self.camera.circle_old:
			for i in range(self.camera.image_old, self.camera.image_index):
				image_data = numpy.array( self.camera.pixel_stream[i], dtype = numpy.uint16 )
				image_data_2D = image_data.reshape( 2048, 2048 )
				filename = f'{self.savepath}/image-{self.camera.circle_old * self.camera.buffer_size + i}.tiff'
				PIL.Image.fromarray(image_data_2D).save(filename)
				# cv2.imwrite(filename, image_data_2D)
		elif self.camera.circle_index > self.camera.circle_old:
			for i in range(self.camera.image_old, self.camera.buffer_size):
				image_data = numpy.array( self.camera.pixel_stream[i], dtype = numpy.uint16 )
				image_data_2D = image_data.reshape( 2048, 2048 )
				filename = f'{self.savepath}/image-{self.camera.circle_old * self.camera.buffer_size + i}.tiff'
				PIL.Image.fromarray(image_data_2D).save(filename)
				# cv2.imwrite(filename, image_data_2D)
			for i in range(0, self.camera.image_index):
				image_data = numpy.array( self.camera.pixel_stream[i], dtype = numpy.uint16 )
				image_data_2D = image_data.reshape( 2048, 2048 )
				filename = f'{self.savepath}/image-{self.camera.circle_index * self.camera.buffer_size + i}.tiff'
				PIL.Image.fromarray(image_data_2D).save(filename)
				# cv2.imwrite(filename, image_data_2D)
	
	# class variables interface
	
	def exp_mode_reset(self, mode):
		label = { 0:'Internal Mode', 1: 'External Mode', 3:'External First', 2:'External Exp.' }
		self.exp_mode_label = label[mode.value]
		self.camera.exp_mode = mode
	
	def exposure_time_reset(self, time):
		time = max(1, min(time, 1000))
		self.camera.exposure_time.value = time
	
	# def exhibition_number_reset(self, number):
		# -1 for the last frame captured, >0 otherwise
		# if number == -1:
			# self.camera.acquisition_index()
			# self.exhibition_number = self.camera.image_index
		# else:
			# number = max(0, min(number, self.camera.exp_total - 1))
			# self.exhibition_number = number
	
	# output interface
	
	def exp_mode_export(self):
		return(self.exp_mode_label)
	
	def exposure_time_export(self):
		return(self.camera.exposure_time.value)
	
	# def exhibition_number_export(self):
		# return(self.exhibition_number)
	
	def camera_export(self, argument):
		self.current_image_extract() # < 1 us （i5-8265U） + camera.acquisition_index (~ 10 us)
		# self.histogram_generate() # ~ 2 ms  （i5-8265U）, taken by the main application
		# self.image_generate() # ~ 33 ms （i5-8265U）, taken by the main application
		message = {'current_image':self.current_image, 'exp_mode':self.exp_mode_label, 'exposure_time':self.camera.exposure_time.value}
		return(message)
	
	def unknown_command(self, argument):
		return('WTF is that?')
	
with multiprocessing.connection.Listener( ('localhost', 6003), authkey = b'hwlab' ) as server_camera:
	with server_camera.accept() as receiver:
		camera_control = CameraControl()
		message = None
		command = None
		argument = None
		command_mapping = { 'close':camera_control.close, 'acquisition_capture':camera_control.camera.acquisition_capture, 'acquisition_live':camera_control.camera.acquisition_live, 'acquisition_fastlapse':camera_control.camera.acquisition_live, 'acquisition_stop':camera_control.camera.acquisition_stop, 'single_serial_save':camera_control.single_serial_save, 'exp_mode_reset':camera_control.exp_mode_reset, 'exposure_time_reset':camera_control.exposure_time_reset, 'camera_export':camera_control.camera_export}
		while True:
			if receiver.poll(timeout = 0.001):
				message = receiver.recv()
				command = command_mapping.get( message[0], camera_control.unknown_command )
				argument = message[1]
				if message[0] == 'close':
					command(argument)
					del camera_control
					break
				elif message[0] == 'acquisition_fastlapse':
					command(argument)
					camera_control.savepath = argument
					camera_control.continuous_save_flag = True
				elif message[0] == 'acquisition_stop':
					command(argument)
					camera_control.continuous_save_flag = False
				elif message[0] == 'camera_export':
					receiver.send(command(argument))
				else:
					command(argument)
			if camera_control.continuous_save_flag:
				camera_control.continuous_save()
				# To test whether the writing speed is fast enough
				# if camera_control.camera.circle_old != camera_control.camera.circle_index or camera_control.camera.image_old != camera_control.camera.image_index :
					# print(f'({camera_control.camera.circle_old, camera_control.camera.image_old}) -> ({camera_control.camera.circle_index, camera_control.camera.image_index})')
	
