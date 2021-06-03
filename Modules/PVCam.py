import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'DLLreaders'))
import PVCam_dll

import ctypes
import numpy
import time

# TODO: add hight QE model

class PVCam:
	buffer_size = 50
	circle_old = 0
	circle_index = 0
	image_old = 0
	image_index = 0
	
	hcam = ctypes.c_short(0)
	continuous_mode = False
	exp_total = ctypes.c_ushort(1)
	exp_mode = PVCam_dll.EXPOSURE_MODES.STROBED_MODE
	exposure_time = ctypes.c_uint(10)
	exp_bytes = ctypes.c_uint(0)
	buffer_mode = PVCam_dll.CIRC_MODES.CIRC_OVERWRITE
	pixel_stream = ((ctypes.c_ushort * 4194304) * buffer_size)()
	
	def __init__(self):
		# pixel_stream.value = numpy.zeros( (2028 * 2048, 10) ).tolist() # too slow, default is 0 anyway
		pvcam_version = ctypes.c_ushort(0)
		total_cams = ctypes.c_short(0)
		cam_name = (ctypes.c_char * 16)()
		# cam_name.value = numpy.zeros(16).tolist() # type error, default is 0 anyway
		# cam_name = ctypes.create_string_buffer(16) # may cause crash
		PVCam_dll.pl_pvcam_get_ver(pvcam_version)
		# print('Version number for this edition of PVCAM:', PVCam_dll_version.value)
		PVCam_dll.pl_pvcam_init()
		PVCam_dll.pl_cam_get_total(total_cams)
		# print('Number of cameras attached:', self.total_cams.value)
		PVCam_dll.pl_cam_get_name(0, cam_name)
		# print('The name of camera #1:', self.cam_name.value)
		PVCam_dll.pl_cam_open(cam_name, self.hcam, 0)
		# print('Camera handle of camera #1:', self.hcam.value)
		# This function will reset all post-processing modules to their default values.
		# print('Reset all post-processing modules:', PVCam_dll.pl_pp_reset(self.hcam))
		PVCam_dll.pl_pp_reset(self.hcam)
	
	def acquisition_capture(self, argument):
		self.continuous_mode = False
		self.exp_total = 1
		rgn_total = ctypes.c_ushort(1)
		rgn_array = PVCam_dll.rgn_type(0, 2047, 1, 0, 2047, 1)
		PVCam_dll.pl_exp_setup_seq(self.hcam, self.exp_total, rgn_total, rgn_array, self.exp_mode, self.exposure_time, self.exp_bytes)
		self.pixel_stream = ( (ctypes.c_ushort * 4194304) * int(self.exp_bytes.value / 8388608) )()
		PVCam_dll.pl_exp_start_seq(self.hcam, self.pixel_stream)
	
	def acquisition_serial(self, frames):
		# This function corrupts the motion sequence and thus need to be modified
		self.continuous_mode = False
		self.exp_total = frames
		rgn_total = ctypes.c_ushort(1)
		rgn_array = PVCam_dll.rgn_type(0, 2047, 1, 0, 2047, 1)
		PVCam_dll.pl_exp_setup_seq(self.hcam, self.exp_total, rgn_total, rgn_array, self.exp_mode, self.exposure_time, self.exp_bytes)
		self.pixel_stream = ( (ctypes.c_ushort * 4194304) * int(self.exp_bytes.value / 8388608) )()
		PVCam_dll.pl_exp_start_seq(self.hcam, self.pixel_stream)
	
	def acquisition_live(self, argument):
		self.continuous_mode = True
		self.exp_total = 1
		rgn_total = ctypes.c_ushort(1)
		rgn_array = PVCam_dll.rgn_type(0, 2047, 1, 0, 2047, 1)
		PVCam_dll.pl_exp_setup_cont(self.hcam, rgn_total, rgn_array, self.exp_mode, self.exposure_time, self.exp_bytes, self.buffer_mode)
		self.pixel_stream = ( (ctypes.c_ushort * 4194304) * self.buffer_size )()
		size = ctypes.c_uint( self.buffer_size * 8388608 )
		PVCam_dll.pl_exp_start_cont(self.hcam, self.pixel_stream, size)
	
	def acquisition_stop(self, argument):
		self.continuous_mode = False
		cam_state = PVCam_dll.ABORT_MODES.CCS_HALT_CLOSE_SHTR # I guess...
		hbuf = ctypes.c_short(0)
		self.exp_total = 1
		if self.continuous_mode:
			PVCam_dll.pl_exp_stop_cont(self.hcam, cam_state)
		else:
			PVCam_dll.pl_exp_finish_seq(self.hcam, self.pixel_stream, hbuf);
	
	def acquisition_index(self):
		# obsolete after version 2.0
		self.circle_old = self.circle_index
		self.image_old = self.image_index
		status = ctypes.c_short(0)
		bytes_arrived = ctypes.c_uint(0)
		buffer_cnt = ctypes.c_uint(0)
		if self.continuous_mode:
			PVCam_dll.pl_exp_check_cont_status( self.hcam, status, bytes_arrived, buffer_cnt )
			self.circle_index = buffer_cnt.value
		else:
			PVCam_dll.pl_exp_check_status( self.hcam, status, bytes_arrived )
		# print(f'status = {status.value}, bytes_arrived = {bytes_arrived.value}, buffer_cnt = {buffer_cnt.value}')
		self.image_index = int( bytes_arrived.value / 8388608 )
	
	def error(self):
		err_code = ctypes.c_short(0)
		err_msg = (ctypes.c_char * 256)()
		err_code = PVCam_dll.pl_error_code()
		PVCam_dll.pl_error_message(err_code, err_msg)
		print(''.join([ 'Error code: ', format(err_code, 'd'), '\n\t', err_msg.value.decode('utf-8') ]))
	
	def close(self):
		cam_state = PVCam_dll.ABORT_MODES.CCS_HALT_CLOSE_SHTR # I guess...
		PVCam_dll.pl_exp_abort(self.hcam, cam_state)
		PVCam_dll.pl_cam_close(self.hcam)
		PVCam_dll.pl_pvcam_uninit()
	
	def set_param(self, param_id, param_mode):
		PVCam_dll.pl_set_param(self.hcam, param_id, ctypes.pointer(ctypes.c_ushort(param_mode)))
	
	def information(self, param_id):
		param_value = ctypes.pointer(ctypes.c_uint(0))
		value = ctypes.c_int(0)
		desc = (ctypes.c_char * 32)(0)
		# desc = ctypes.create_string_buffer(32) # may cause crash
		length = ctypes.c_uint(0)
		
		PVCam_dll.pl_get_param(self.hcam, param_id, PVCam_dll.ATTR_COUNT, param_value)
		print(''.join([ 'Count of the parameter: ', format(param_value.contents.value, 'd') ]))
		for i in range(param_value.contents.value):
			PVCam_dll.pl_enum_str_length(self.hcam, param_id, i, length)
			PVCam_dll.pl_get_enum_param(self.hcam, param_id, i, value, desc, length)
			print(''.join([ '\t', format(value.value, 'd'), '\t', desc.value.decode('utf-8') ]))
		PVCam_dll.pl_get_param(self.hcam, param_id, PVCam_dll.ATTR_TYPE, param_value)
		print(''.join([ 'Data type:\t', format(param_value.contents.value, 'd') ]))
		PVCam_dll.pl_get_param(self.hcam, param_id, PVCam_dll.ATTR_DEFAULT, param_value)
		print(''.join([ 'Default value:\t', format(param_value.contents.value, 'd') ]))
		PVCam_dll.pl_get_param(self.hcam, param_id, PVCam_dll.ATTR_CURRENT, param_value)
		print(''.join([ 'Current value:\t', format(param_value.contents.value, 'd') ]))
		PVCam_dll.pl_get_param(self.hcam, param_id, PVCam_dll.ATTR_AVAIL, param_value)
		print(''.join([ 'IF available:\t', format(param_value.contents.value, 'd') ]))
		PVCam_dll.pl_get_param(self.hcam, param_id, PVCam_dll.ATTR_ACCESS, param_value)
		print(''.join([ 'Access status:\t', format(param_value.contents.value, 'd') ]))
		PVCam_dll.pl_get_param(self.hcam, param_id, PVCam_dll.ATTR_MIN, param_value)
		print(''.join([ 'Min value:\t', format(param_value.contents.value, 'd') ]))
		PVCam_dll.pl_get_param(self.hcam, param_id, PVCam_dll.ATTR_MAX, param_value)
		print(''.join([ 'Max value:\t', format(param_value.contents.value, 'd') ]))
		PVCam_dll.pl_get_param(self.hcam, param_id, PVCam_dll.ATTR_INCREMENT, param_value)
		print(''.join([ 'Value incre.:\t', format(param_value.contents.value, 'd') ]))
		print('\r\n')
	# class variables interface
	
	def buffer_resize(self, size):
		self.buffer_size = size
	
	def exp_total_reset(self, number):
		self.exp_total = number
	
	def buffer_mode_reset(self, mode):
		self.buffer_mode = mode


