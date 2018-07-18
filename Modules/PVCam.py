from Modules import PVCamDLL

import ctypes
import numpy
import time
import cv2

class Defines:
	# Data type used by #pl_get_param with #ATTR_TYPE.
	TYPE_INT16 = 1
	TYPE_INT32 = 2
	TYPE_FLT64 = 4
	TYPE_UNS8 = 5
	TYPE_UNS16 = 6
	TYPE_UNS32 = 7
	TYPE_UNS64 = 8
	TYPE_ENUM = 9
	TYPE_BOOLEAN = 11
	TYPE_INT8 = 12
	TYPE_CHAR_PTR = 13
	TYPE_VOID_PTR = 14
	TYPE_VOID_PTR_PTR = 15
	TYPE_INT64 = 16
	TYPE_SMART_STREAM_TYPE = 17
	TYPE_SMART_STREAM_TYPE_PTR = 18
	TYPE_FLT32 = 19

	# Defines for classes: Camera Communications, Configuration/Setup, Data Acuisition.
	CLASS0 = 0
	CLASS2 = 2
	CLASS3 = 3

	# CAMERA COMMUNICATION PARAMETERS
	PARAM_DD_INFO_LENGTH = (CLASS0<<16) + (TYPE_INT16<<24) + 1
	PARAM_DD_VERSION = (CLASS0<<16) + (TYPE_UNS16<<24) + 2
	PARAM_DD_RETRIES = (CLASS0<<16) + (TYPE_UNS16<<24) + 3
	PARAM_DD_TIMEOUT = (CLASS0<<16) + (TYPE_UNS16<<24) + 4
	PARAM_DD_INFO = (CLASS0<<16) + (TYPE_CHAR_PTR<<24) + 5
	PARAM_CAM_INTERFACE_TYPE = (CLASS0<<16) + (TYPE_ENUM<<24) + 10
	PARAM_CAM_INTERFACE_MODE = (CLASS0<<16) + (TYPE_ENUM<<24) + 11

	# Sensor Clearing
	PARAM_CLEAR_CYCLES = (CLASS2<<16) + (TYPE_UNS16<<24) + 97
	PARAM_CLEAR_MODE = (CLASS2<<16) + (TYPE_ENUM<<24) + 523

	# Temperature Control
	PARAM_COOLING_MODE = (CLASS2<<16) + (TYPE_ENUM<<24) + 214
	PARAM_TEMP = (CLASS2<<16) + (TYPE_INT16<<24) + 525
	PARAM_TEMP_SETPOINT = (CLASS2<<16) + (TYPE_INT16<<24) + 526
	PARAM_FAN_SPEED_SETPOINT = (CLASS2<<16) + (TYPE_ENUM<<24) + 710

	# Gain
	PARAM_GAIN_INDEX = (CLASS2<<16) + (TYPE_INT16<<24) + 512
	PARAM_GAIN_NAME = (CLASS2<<16) + (TYPE_CHAR_PTR<<24) + 514
	PARAM_GAIN_MULT_ENABLE = (CLASS2<<16) + (TYPE_BOOLEAN<<24) + 541
	PARAM_GAIN_MULT_FACTOR = (CLASS2<<16) + (TYPE_UNS16<<24) + 537
	PARAM_PREAMP_DELAY = (CLASS2<<16) + (TYPE_UNS16<<24) + 502
	PARAM_PREAMP_OFF_CONTROL = (CLASS2<<16) + (TYPE_UNS32<<24) + 507
	PARAM_ACTUAL_GAIN = (CLASS2<<16) + (TYPE_UNS16<<24) + 544

	# Shutter
	PARAM_SHTR_STATUS = (CLASS2<<16) + (TYPE_ENUM<<24) + 522
	PARAM_SHTR_CLOSE_DELAY = (CLASS2<<16) + (TYPE_UNS16<<24) + 519
	PARAM_SHTR_OPEN_DELAY = (CLASS2<<16) + (TYPE_UNS16<<24) + 520
	PARAM_SHTR_OPEN_MODE = (CLASS2<<16) + (TYPE_ENUM<<24) + 521

	# Capabilities
	PARAM_ACCUM_CAPABLE = (CLASS2<<16) + (TYPE_BOOLEAN<<24) + 538
	PARAM_FRAME_CAPABLE = (CLASS2<<16) + (TYPE_BOOLEAN<<24) + 509
	PARAM_MPP_CAPABLE = (CLASS2<<16) + (TYPE_ENUM<<24) + 224
	PARAM_FLASH_DWNLD_CAPABLE = (CLASS2<<16) + (TYPE_BOOLEAN<<24) + 539

	# I/O
	PARAM_IO_ADDR = (CLASS2<<16) + (TYPE_UNS16<<24) + 527
	PARAM_IO_BITDEPTH = (CLASS2<<16) + (TYPE_UNS16<<24) + 531
	PARAM_IO_DIRECTION = (CLASS2<<16) + (TYPE_ENUM<<24) + 529
	PARAM_IO_STATE = (CLASS2<<16) + (TYPE_FLT64<<24) + 530
	PARAM_IO_TYPE = (CLASS2<<16) + (TYPE_ENUM<<24) + 528

	# Post-Processing
	PARAM_PP_INDEX = (CLASS2<<16) + (TYPE_INT16<<24) + 543
	PARAM_PP_FEAT_NAME = (CLASS2<<16) + (TYPE_CHAR_PTR<<24) + 542
	PARAM_PP_PARAM_INDEX = (CLASS2<<16) + (TYPE_INT16<<24) + 545
	PARAM_PP_PARAM_NAME = (CLASS2<<16) + (TYPE_CHAR_PTR<<24) + 546
	PARAM_PP_PARAM = (CLASS2<<16) + (TYPE_UNS32<<24) + 547
	PARAM_PP_FEAT_ID = (CLASS2<<16) + (TYPE_UNS16<<24) + 549
	PARAM_PP_PARAM_ID = (CLASS2<<16) + (TYPE_UNS16<<24) + 550

	# Sensor Physical Attributes
	PARAM_COLOR_MODE = (CLASS2<<16) + (TYPE_ENUM<<24) + 504
	PARAM_FWELL_CAPACITY = (CLASS2<<16) + (TYPE_UNS32<<24) + 506
	PARAM_PAR_SIZE = (CLASS2<<16) + (TYPE_UNS16<<24) + 57
	PARAM_PIX_PAR_DIST = (CLASS2<<16) + (TYPE_UNS16<<24) + 500
	PARAM_PIX_PAR_SIZE = (CLASS2<<16) + (TYPE_UNS16<<24) + 63
	PARAM_PIX_SER_DIST = (CLASS2<<16) + (TYPE_UNS16<<24) + 501
	PARAM_PIX_SER_SIZE = (CLASS2<<16) + (TYPE_UNS16<<24) + 62
	PARAM_POSTMASK = (CLASS2<<16) + (TYPE_UNS16<<24) + 54
	PARAM_POSTSCAN = (CLASS2<<16) + (TYPE_UNS16<<24) + 56
	PARAM_PIX_TIME = (CLASS2<<16) + (TYPE_UNS16<<24) + 516
	PARAM_PREMASK = (CLASS2<<16) + (TYPE_UNS16<<24) + 53
	PARAM_PRESCAN = (CLASS2<<16) + (TYPE_UNS16<<24) + 55
	PARAM_SER_SIZE = (CLASS2<<16) + (TYPE_UNS16<<24) + 58
	PARAM_SUMMING_WELL = (CLASS2<<16) + (TYPE_BOOLEAN<<24) + 505

	# Sensor Readout
	PARAM_PMODE = (CLASS2<<16) + (TYPE_ENUM<<24) + 524
	PARAM_READOUT_PORT = (CLASS2<<16) + (TYPE_ENUM<<24) + 247
	PARAM_READOUT_TIME = (CLASS2<<16) + (TYPE_FLT64<<24) + 179
	PARAM_EXPOSURE_MODE = (CLASS2<<16) + (TYPE_ENUM<<24) + 535
	PARAM_EXPOSE_OUT_MODE = (CLASS2<<16) + (TYPE_ENUM<<24) + 560

	# ADC Attributes
	PARAM_ADC_OFFSET = (CLASS2<<16) + (TYPE_INT16<<24) + 195
	PARAM_BIT_DEPTH = (CLASS2<<16) + (TYPE_INT16<<24) + 511
	PARAM_SPDTAB_INDEX = (CLASS2<<16) + (TYPE_INT16<<24) + 513

	# S.M.A.R.T. Streaming
	PARAM_SMART_STREAM_MODE_ENABLED = (CLASS2<<16) + (TYPE_BOOLEAN<<24) + 700
	PARAM_SMART_STREAM_MODE = (CLASS2<<16) + (TYPE_UNS16<<24) + 701
	PARAM_SMART_STREAM_EXP_PARAMS = (CLASS2<<16) + (TYPE_VOID_PTR<<24) + 702
	PARAM_SMART_STREAM_DLY_PARAMS = (CLASS2<<16) + (TYPE_VOID_PTR<<24) + 703

	# Other
	PARAM_CAM_FW_VERSION = (CLASS2<<16) + (TYPE_UNS16<<24) + 532
	PARAM_CHIP_NAME = (CLASS2<<16) + (TYPE_CHAR_PTR<<24) + 129
	PARAM_SYSTEM_NAME = (CLASS2<<16) + (TYPE_CHAR_PTR<<24) + 130
	PARAM_VENDOR_NAME = (CLASS2<<16) + (TYPE_CHAR_PTR<<24) + 131
	PARAM_PRODUCT_NAME = (CLASS2<<16) + (TYPE_CHAR_PTR<<24) + 132
	PARAM_CAMERA_PART_NUMBER = (CLASS2<<16) + (TYPE_CHAR_PTR<<24) + 133
	PARAM_HEAD_SER_NUM_ALPHA = (CLASS2<<16) + (TYPE_CHAR_PTR<<24) + 533
	PARAM_PCI_FW_VERSION = (CLASS2<<16) + (TYPE_UNS16<<24) + 534
	PARAM_READ_NOISE = (CLASS2<<16) + (TYPE_UNS16<<24) + 548
	PARAM_CLEARING_TIME = (CLASS2<<16) + (TYPE_INT64<<24) + 180
	PARAM_POST_TRIGGER_DELAY = (CLASS2<<16) + (TYPE_INT64<<24) + 181
	PARAM_PRE_TRIGGER_DELAY = (CLASS2<<16) + (TYPE_INT64<<24) + 182
	PARAM_CAM_SYSTEMS_INFO = (CLASS2<<16) + (TYPE_CHAR_PTR<<24) + 536

	# ACQUISITION PARAMETERS
	PARAM_EXP_TIME = (CLASS3<<16) + (TYPE_UNS16<<24) + 1
	PARAM_EXP_RES = (CLASS3<<16) + (TYPE_ENUM<<24) + 2
	PARAM_EXP_RES_INDEX = (CLASS3<<16) + (TYPE_UNS16<<24) + 4
	PARAM_EXPOSURE_TIME = (CLASS3<<16) + (TYPE_UNS64<<24) + 8

	# PARAMETERS FOR BEGIN and END of FRAME Interrupts
	PARAM_BOF_EOF_ENABLE = (CLASS3<<16) + (TYPE_ENUM<<24) + 5
	PARAM_BOF_EOF_COUNT = (CLASS3<<16) + (TYPE_UNS32<<24) + 6
	PARAM_BOF_EOF_CLR = (CLASS3<<16) + (TYPE_BOOLEAN<<24) + 7
	PARAM_CIRC_BUFFER = (CLASS3<<16) + (TYPE_BOOLEAN<<24) + 299
	PARAM_FRAME_BUFFER_SIZE = (CLASS3<<16) + (TYPE_UNS64<<24) + 300

	# inning reported by camera
	PARAM_BINNING_SER = (CLASS3<<16) + (TYPE_ENUM<<24) + 165
	PARAM_BINNING_PAR = (CLASS3<<16) + (TYPE_ENUM<<24) + 166

	# Parameters related to multiple ROIs and Centroids
	PARAM_METADATA_ENABLED = (CLASS3<<16) + (TYPE_BOOLEAN<<24) + 168
	PARAM_ROI_COUNT = (CLASS3<<16) + (TYPE_UNS16<<24) + 169
	PARAM_CENTROIDS_ENABLED = (CLASS3<<16) + (TYPE_BOOLEAN<<24) + 170
	PARAM_CENTROIDS_RADIUS = (CLASS3<<16) + (TYPE_UNS16<<24) + 171
	PARAM_CENTROIDS_COUNT = (CLASS3<<16) + (TYPE_UNS16<<24) + 172
	PARAM_CENTROIDS_MODE = (CLASS3<<16) + (TYPE_ENUM<<24) + 173
	PARAM_CENTROIDS_BG_COUNT = (CLASS3<<16) + (TYPE_ENUM<<24) + 174
	PARAM_CENTROIDS_THRESHOLD = (CLASS3<<16) + (TYPE_UNS32<<24) + 175

	# Parameters related to triggering table
	PARAM_TRIGTAB_SIGNAL = (CLASS3<<16) + (TYPE_ENUM<<24) + 180
	PARAM_LAST_MUXED_SIGNAL = (CLASS3<<16) + (TYPE_UNS8<<24) + 181
	PARAM_FRAME_DELIVERY_MODE = (CLASS3<<16) + (TYPE_ENUM<<24) + 400

	# typedef enum PL_PARAM_ATTRIBUTES
	ATTR_CURRENT = 0
	ATTR_COUNT = 1
	ATTR_TYPE = 2
	ATTR_MIN = 3
	ATTR_MAX = 4
	ATTR_DEFAULT = 5
	ATTR_INCREMENT = 6
	ATTR_ACCESS = 7
	ATTR_AVAIL = 8

class EXPOSURE_MODES:
	# typedef enum PL_EXPOSURE_MODES
	# {
		#     TIMED_MODE,
		#     STROBED_MODE,
		#     BULB_MODE,
		#     TRIGGER_FIRST_MODE,
		#     FLASH_MODE, /**< @deprecated Not supported by any modern camera. */
		#     VARIABLE_TIMED_MODE,
		#     INT_STROBE_MODE, /**< @deprecated Not supported by any modern camera. */
		#     MAX_EXPOSE_MODE = 7,
		#     EXT_TRIG_INTERNAL = (7 + 0) << 8,
		#     EXT_TRIG_TRIG_FIRST = (7 + 1) << 8,
		#     EXT_TRIG_EDGE_RISING  = (7 + 2) << 8
	# }
	# PL_EXPOSURE_MODES;
	TIMED_MODE = ctypes.c_short(0)
	STROBED_MODE = ctypes.c_short(1)
	BULB_MODE = ctypes.c_short(2)
	TRIGGER_FIRST_MODE = ctypes.c_short(3)
	VARIABLE_TIMED_MODE = ctypes.c_short(4)

class CIRC_MODES:
	# typedef enum PL_CIRC_MODES
	# {
		#     CIRC_NONE = 0,
		#     CIRC_OVERWRITE,
		#     CIRC_NO_OVERWRITE
		# }
	# PL_CIRC_MODES;
	CIRC_NONE = ctypes.c_short(1)
	CIRC_OVERWRITE = ctypes.c_short(1)
	CIRC_NO_OVERWRITE = ctypes.c_short(2)

class ABORT_MODES:
	# typedef enum PL_CCS_ABORT_MODES
	# {
		# CCS_NO_CHANGE = 0,      /**< Do not alter the current state of the CCS.*/
		# CCS_HALT,               /**< Halt all CCS activity, and put the CCS into the idle state.*/
		# CCS_HALT_CLOSE_SHTR,    /**< Close the shutter, then halt all CCS activity, and put the CCS into the idle state.*/
		# CCS_CLEAR,              /**< Put the CCS into the continuous clearing state.*/
		# CCS_CLEAR_CLOSE_SHTR,   /**< Close the shutter, then put the CCS into the continuous clearing state.*/
		# CCS_OPEN_SHTR,          /**< Open the shutter, then halt all CCS activity, and put the CCS into the idle state.*/
		# CCS_CLEAR_OPEN_SHTR     /**< Open the shutter, then put the CCS into the continuous clearing state.*/
	# }
	# PL_CCS_ABORT_MODES;
	CCS_NO_CHANGE = ctypes.c_short(0)
	CCS_HALT = ctypes.c_short(1)
	CCS_HALT_CLOSE_SHTR = ctypes.c_short(2)
	CCS_CLEAR = ctypes.c_short(3)
	CCS_CLEAR_CLOSE_SHTR = ctypes.c_short(4)
	CCS_OPEN_SHTR = ctypes.c_short(5)
	CCS_CLEAR_OPEN_SHTR = ctypes.c_short(6)

class PVCam:
	pvcam = ctypes.windll.LoadLibrary("Libraries/pvcam64.dll")
	data_exist_flag = False # To judge if there are any image data
	
	continuous_mode = False
	buffer_size = 10
	dynamic_range = { "low":0, "high":65535 }
	region_of_interest = { "x1":0, "y1":0, "x2":2047, "y2":2047 }
	image_index = 0
	image_size = 1024
	image_color = [255, 255, 255]
	image_histogram = None # numpy.zeros( (0, 0, 3), dtype = numpy.uint8 )
	image_exhibition = None # numpy.zeros( (0, 0, 3), dtype = numpy.uint8 )
	
	hcam = ctypes.c_short(0)
	
	exp_total = ctypes.c_ushort(1)
	exp_mode = EXPOSURE_MODES.TIMED_MODE
	exposure_time = ctypes.c_uint(10)
	exp_bytes = ctypes.c_uint(0)
	buffer_mode = CIRC_MODES.CIRC_OVERWRITE
	pixel_stream = ((ctypes.c_ushort * 4194304) * buffer_size)()
	
	def __init__(self):
		# pixel_stream.value = numpy.zeros( (2028 * 2048, 10) ).tolist() # too slow, default is 0 anyway
		PVCamDLL.Functions(self.pvcam)
		self.open()
	
	def acquisition_setup(self):
		rgn_total = ctypes.c_ushort(1)
		rgn_array = PVCamDLL.rgn_type(0, 2047, 1, 0, 2047, 1)
		if self.continuous_mode:
			self.pvcam.pl_exp_setup_cont(self.hcam, rgn_total, rgn_array, self.exp_mode, self.exposure_time, self.exp_bytes, self.buffer_mode)
		else:
			self.pvcam.pl_exp_setup_seq(self.hcam, self.exp_total, rgn_total, rgn_array, self.exp_mode, self.exposure_time, self.exp_bytes)
	
	def acquisition(self):
		self.data_exist_flag = True
		if self.continuous_mode:
			self.pixel_stream = ( (ctypes.c_ushort * 4194304) * self.buffer_size )()
			size = ctypes.c_uint( self.buffer_size * 8388608 )
			self.pvcam.pl_exp_start_cont(self.hcam, self.pixel_stream, size)
		else:
			self.pixel_stream = ( (ctypes.c_ushort * 4194304) * int(self.exp_bytes.value / 8388608) )()
			self.pvcam.pl_exp_start_seq(self.hcam, self.pixel_stream)
	
	def acquisition_stop(self):
		cam_state = ABORT_MODES.CCS_HALT_CLOSE_SHTR # I guess...
		hbuf = ctypes.c_short(0)
		if self.continuous_mode:
			self.pvcam.pl_exp_stop_cont(self.hcam, cam_state)
		else:
			self.pvcam.pl_exp_finish_seq(self.hcam, self.pixel_stream, hbuf);
	
	def acquisition_index(self):
		status = ctypes.c_short(0)
		bytes_arrived = ctypes.c_uint(0)
		buffer_cnt = ctypes.c_uint(0)
		if self.continuous_mode:
			self.pvcam.pl_exp_check_cont_status( self.hcam, status, bytes_arrived, buffer_cnt )
		else:
			self.pvcam.pl_exp_check_status( self.hcam, status, bytes_arrived )
		# print(f'status = {status.value}, bytes_arrived = {bytes_arrived.value}, buffer_cnt = {buffer_cnt.value}')
		self.image_index = int( bytes_arrived.value / 8388608 ) - 1
	
	def histogram_generate(self):
		image_data = numpy.array( self.pixel_stream[self.image_index], dtype = numpy.uint16 )
		hist = numpy.histogram(
			cv2.resize(
				image_data.reshape(2048, 2048), 
				(256, 256), interpolation=cv2.INTER_NEAREST
			).reshape(256 * 256), 
			256, (0, 65536)
		)
		self.image_histogram = numpy.zeros( (128, 256, 3), dtype = numpy.uint8 )
		self.image_histogram += 255
		for i in range(256):
			if hist[0][i] >= 1024:
				for j in range(128):
					self.image_histogram[j, i] = [0, 0, 0]
			else:
				for j in range( 127 - int( hist[0][i] / 1024 * 127.999 ), 128 ):
					self.image_histogram[j, i] = [0, 0, 0]
	
	def image_generate(self):
		image_data = numpy.array( self.pixel_stream[self.image_index], dtype = numpy.uint16 )
		image_data_2D = image_data.reshape( 2048, 2048 )
		image_resized = image_data_2D[ self.region_of_interest["x1"]: self.region_of_interest["x2"], self.region_of_interest["y1"]: self.region_of_interest["y2"] ]
		image_resized = cv2.resize( image_resized, (self.image_size, self.image_size), interpolation=cv2.INTER_LANCZOS4 )
		image_resized_clip = numpy.clip( image_resized, self.dynamic_range["low"], self.dynamic_range["high"] )
		image_int8 = ( (image_resized_clip - self.dynamic_range["low"]) / (self.dynamic_range["high"] - self.dynamic_range["low"]) * 255.999 ).astype(numpy.uint8)
		self.image_exhibition = numpy.tensordot( image_int8, numpy.array(self.image_color, dtype = numpy.uint8) / 255, axes = 0 ).astype(numpy.uint8)
	
	def histogram_export(self):
		return(self.image_histogram)
	
	def image_export(self):
		return(self.image_exhibition)
	
	def color_reset(self, color):
		self.image_color = color
	
	def image_resize(self, size):
		self.image_size = size
	
	def buffer_resize(self, size):
		self.buffer_size = size
	
	def continuous_remode(self, mode):
		self.continuous_mode = mode
	
	def exposure_time_reset(self, time):
		self.exposure_time.value = time
	
	def exp_total_reset(self, number):
		self.exp_total = number
	
	def exp_mode_reset(self, mode):
		self.exp_mode = mode
	
	def buffer_mode_reset(self, mode):
		self.buffer_mode = mode
	
	def dynamic_range_resize(self, range):
		if range[0] > range[1]:
			self.dynamic_range["low"] = range[1]
			self.dynamic_range["high"] = range[0]
		elif range[0] == range[1]:
			self.dynamic_range["low"] = range[0]
			self.dynamic_range["high"] = range[0] + 1
		else:
			self.dynamic_range["low"] = range[0]
			self.dynamic_range["high"] = range[1]
	
	def data_exist(self):
		return(self.data_exist_flag)
	
	def roi_resize(self, region_of_selected):
		x1r, x2r, y1r, y2r = self.region_of_interest["x1"], self.region_of_interest["x2"], self.region_of_interest["y1"], self.region_of_interest["y2"]
		x1s = min( region_of_selected["x1"], region_of_selected["x2"] )
		x2s = max( region_of_selected["x1"], region_of_selected["x2"] )
		y1s = min( region_of_selected["y1"], region_of_selected["y2"] )
		y2s = max( region_of_selected["y1"], region_of_selected["y2"] )
		self.region_of_interest["x1"] = int( (x2r - x1r) * x1s / self.image_size ) + x1r
		self.region_of_interest["x2"] = int( (x2r - x1r) * x2s / self.image_size ) + x1r
		self.region_of_interest["y1"] = int( (y2r - y1r) * y1s / self.image_size ) + y1r
		self.region_of_interest["y2"] = int( (y2r - y1r) * y2s / self.image_size ) + y1r
		if self.region_of_interest["x2"] <= self.region_of_interest["x1"]:
			self.region_of_interest["x2"] = self.region_of_interest["x1"] + 1
		if self.region_of_interest["y2"] <= self.region_of_interest["y1"]:
			self.region_of_interest["y2"] = self.region_of_interest["y1"] + 1
	
	def roi_reset(self):
		self.region_of_interest = { "x1":0, "y1":0, "x2":2047, "y2":2047 }
	
	def roi_export(self):
		return([self.region_of_interest["x1"], self.region_of_interest["x2"], self.region_of_interest["y1"], self.region_of_interest["y2"]])
	
	def open(self):
		pvcam_version = ctypes.c_ushort(0)
		total_cams = ctypes.c_short(0)
		cam_name = (ctypes.c_char * 16)()
		# cam_name.value = numpy.zeros(16).tolist() # type error, default is 0 anyway
		# cam_name = ctypes.create_string_buffer(16) # may cause crash
		self.pvcam.pl_pvcam_get_ver(pvcam_version)
		# print('Version number for this edition of PVCAM:', self.pvcam_version.value)
		self.pvcam.pl_pvcam_init()
		self.pvcam.pl_cam_get_total(total_cams)
		# print('Number of cameras attached:', self.total_cams.value)
		self.pvcam.pl_cam_get_name(0, cam_name)
		# print('The name of camera #1:', self.cam_name.value)
		self.pvcam.pl_cam_open(cam_name, self.hcam, 0)
		# print('Camera handle of camera #1:', self.hcam.value)
		# This function will reset all post-processing modules to their default values.
		# print('Reset all post-processing modules:', self.pvcam.pl_pp_reset(self.hcam))
		self.pvcam.pl_pp_reset(self.hcam)
	
	def error(self):
		err_code = ctypes.c_short(0)
		err_msg = (ctypes.c_char * 256)()
		err_code = self.pvcam.pl_error_code()
		self.pvcam.pl_error_message(err_code, err_msg)
		print(''.join([ 'Error code: ', format(err_code, 'd'), '\n\t', err_msg.value.decode('utf-8') ]))
	
	def close(self):
		cam_state = ABORT_MODES.CCS_HALT_CLOSE_SHTR # I guess...
		self.pvcam.pl_exp_abort(self.hcam, cam_state)
		self.pvcam.pl_cam_close(self.hcam)
		self.pvcam.pl_pvcam_uninit()
	
	def set_param(self, param_id, param_mode):
		self.pvcam.pl_set_param(self.hcam, param_id, ctypes.pointer(ctypes.c_ushort(param_mode)))
	
	def information(self, param_id):
		param_value = ctypes.pointer(ctypes.c_uint(0))
		value = ctypes.c_int(0)
		desc = (ctypes.c_char * 32)(0)
		# desc = ctypes.create_string_buffer(32) # may cause crash
		length = ctypes.c_uint(0)
		
		self.pvcam.pl_get_param(self.hcam, param_id, Defines.ATTR_COUNT, param_value)
		print(''.join([ 'Count of the parameter: ', format(param_value.contents.value, 'd') ]))
		for i in range(param_value.contents.value):
			self.pvcam.pl_enum_str_length(self.hcam, param_id, i, length)
			self.pvcam.pl_get_enum_param(self.hcam, param_id, i, value, desc, length)
			print(''.join([ '\t', format(value.value, 'd'), '\t', desc.value.decode('utf-8') ]))
		self.pvcam.pl_get_param(self.hcam, param_id, Defines.ATTR_TYPE, param_value)
		print(''.join([ 'Data type:\t', format(param_value.contents.value, 'd') ]))
		self.pvcam.pl_get_param(self.hcam, param_id, Defines.ATTR_DEFAULT, param_value)
		print(''.join([ 'Default value:\t', format(param_value.contents.value, 'd') ]))
		self.pvcam.pl_get_param(self.hcam, param_id, Defines.ATTR_CURRENT, param_value)
		print(''.join([ 'Current value:\t', format(param_value.contents.value, 'd') ]))
		self.pvcam.pl_get_param(self.hcam, param_id, Defines.ATTR_AVAIL, param_value)
		print(''.join([ 'IF available:\t', format(param_value.contents.value, 'd') ]))
		self.pvcam.pl_get_param(self.hcam, param_id, Defines.ATTR_ACCESS, param_value)
		print(''.join([ 'Access status:\t', format(param_value.contents.value, 'd') ]))
		self.pvcam.pl_get_param(self.hcam, param_id, Defines.ATTR_MIN, param_value)
		print(''.join([ 'Min value:\t', format(param_value.contents.value, 'd') ]))
		self.pvcam.pl_get_param(self.hcam, param_id, Defines.ATTR_MAX, param_value)
		print(''.join([ 'Max value:\t', format(param_value.contents.value, 'd') ]))
		self.pvcam.pl_get_param(self.hcam, param_id, Defines.ATTR_INCREMENT, param_value)
		print(''.join([ 'Value incre.:\t', format(param_value.contents.value, 'd') ]))
		print('\r\n')

