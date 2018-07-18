from Modules import ConfocalBoard
from Modules import PVCam
from Modules import MotionControl
from Modules import Arduino

import tkinter
import multiprocessing.connection
import os
import time
import PIL.Image
import PIL.ImageTk

class Application(tkinter.Frame):
	confocalBoard = None
	pvcam = None
	client = None
	piezo = None
	stage = None
	arduino = None
	
	# class flags
	intact_flag = True # exists or not
	close_flag = True
	confocal_laser_flag = 0 # send command to Modus board on every 100 loops
	confocal_mark_flag = False
	photoactive_mark_flag = False
	continuous_living_flag = False
	
	# class variables used for scales, etc.
	continuous_mode = False
	confocal_mark_speed = 10 # ms
	photoactive_mark_speed = 15000 # mm/s
	confocal_laser_on = [0, 0, 0, 0]
	confocal_laser_power = [0, 0, 0, 0]
	combined_laser_on = [False, False, False, False]
	exposure_time = 10 # ms
	dynamic_range = [0, 65535]
	stage_x_targeted = 0.0 # mm
	stage_y_targeted = 0.0 # mm
	stage_relative = 0.01 # mm
	motor_targeted = 0.0 # mm
	motor_relative = 0.1 # mm
	piezo_targeted = 0.0 # μm
	piezo_relative = 1.0 # μm
	
	# images
	image_exhibition = 0
	image_histogram = 0
	region_of_selected = {"x1":0, "y1":0, "x2":0, "y2":0}
	
	def __init__(self, master = None):
		self.intact_flag = True
		super().__init__(master)
		self.pack()
		
		self.create_frames()
		self.create_control_frame()
		self.create_status_frame()
		self.create_image_frame()
		self.create_motion_frame()
		
		master.protocol( 'WM_DELETE_WINDOW', self.exit ) # set win.close to self.exit
		# master.geometry( "1920x1080" )
		master.title( "Nymphscopy main application" )
	
	def create_frames(self):
		self.control_frame = tkinter.Frame( self, width = 552, height = 350, borderwidth = 10, relief = tkinter.GROOVE)
		self.control_frame.grid( row = 0, column = 0 )
		self.control_frame.grid_propagate(0) # disable changing the size
		for i in range(8):
			self.control_frame.grid_rowconfigure( index = i, minsize = 40)
		for i in range(4):
			self.control_frame.grid_columnconfigure( index = i, minsize = 138)
		
		self.status_frame = tkinter.Frame( self, width = 552, height = 350, borderwidth = 10, relief = tkinter.RIDGE)
		self.status_frame.grid( row = 1, column = 0 )
		self.status_frame.grid_propagate(0) # disable changing the size
		for i in range(8):
			self.status_frame.grid_rowconfigure( index = i, minsize = 40)
		for i in range(4):
			self.status_frame.grid_columnconfigure( index = i, minsize = 138)
		
		self.motion_frame = tkinter.Frame( self, width = 552, height = 324, borderwidth = 10, relief = tkinter.RAISED)
		self.motion_frame.grid( row = 2, column = 0 )
		self.motion_frame.grid_propagate(0) # disable changing the size
		for i in range(8):
			self.motion_frame.grid_rowconfigure( index = i, minsize = 38)
		for i in range(14):
			self.motion_frame.grid_columnconfigure( index = i, minsize = 38)
		
		self.image_frame = tkinter.Frame( self, width = 1024, height = 1024, borderwidth = 10, relief = tkinter.SUNKEN)
		self.image_frame.grid( row = 0, column = 1, rowspan = 3, columnspan = 1 )
		self.image_frame.grid_propagate(0) # disable changing the size
		for i in range(1):
			self.image_frame.grid_rowconfigure( index = i, minsize = 1024)
		for i in range(1):
			self.image_frame.grid_columnconfigure( index = i, minsize = 1024)
	
	def create_control_frame(self):
		# main menubar
		self.main_button = tkinter.Menubutton( self.control_frame, text = "File", relief = tkinter.RAISED)
		self.main_button.grid( row = 0, column = 0 )
		
		self.main_menu = tkinter.Menu( self.main_button, tearoff = 0 )
		self.main_button["menu"] = self.main_menu
		# self.main_menu.add_command( label = "Open Boards", command = self.open_board )
		self.main_menu.add_command( label = "Quit", command = self.exit )
		
		# pinhole menubar
		self.pinhole_button = tkinter.Menubutton( self.control_frame, text = "Pinholes", relief = tkinter.RAISED)
		self.pinhole_button.grid( row = 0, column = 1 )
		
		self.pinhole_menu = tkinter.Menu( self.pinhole_button, tearoff = 0 )
		self.pinhole_button["menu"] = self.pinhole_menu
		self.pinhole_menu.add_command( label = "Wide Field", command = lambda position = 6.5: self.pinhole_command(position) )
		self.pinhole_menu.add_command( label = "50 μm", command = lambda position = 16.5: self.pinhole_command(position) )
		self.pinhole_menu.add_command( label = "30 μm", command = lambda position = 26.5: self.pinhole_command(position) )
		self.pinhole_menu.add_command( label = "20 μm", command = lambda position = 36.5: self.pinhole_command(position) )
		
		# filter wheel menubar
		self.filter_wheel_button = tkinter.Menubutton( self.control_frame, text = "Filters", relief = tkinter.RAISED)
		self.filter_wheel_button.grid( row = 0, column = 2 )
		
		self.filter_wheel_menu = tkinter.Menu( self.filter_wheel_button, tearoff = 0 )
		self.filter_wheel_button["menu"] = self.filter_wheel_menu
		self.filter_wheel_menu.add_command( label = "447/60", command = lambda position = 50: self.filter_command(position) )
		self.filter_wheel_menu.add_command( label = "525/45", command = lambda position = 110: self.filter_command(position) )
		self.filter_wheel_menu.add_command( label = "586/20", command = lambda position = 170: self.filter_command(position) )
		self.filter_wheel_menu.add_command( label = "615/24", command = lambda position = 230: self.filter_command(position) )
		self.filter_wheel_menu.add_command( label = "676/29", command = lambda position = 350: self.filter_command(position) )
		self.filter_wheel_menu.add_command( label = "446/523/600/677", command = lambda position = 290: self.filter_command(position) )
		
		# confocal mark
		self.confocal_mark_button = tkinter.Button(self.control_frame)
		self.confocal_mark_button["text"] = "Confocal"
		self.confocal_mark_button["command"] = self.confocal_mark_button_command
		self.confocal_mark_button.grid( row = 1, column = 0 )
		
		self.confocal_mark_scale = tkinter.Scale(
			self.control_frame,
			from_ = 10, to = 1000, # from is a reserved keyword in Python, add _
			orient = tkinter.HORIZONTAL,
			length = 256, sliderlength = 20,
			variable = tkinter.IntVar( value = self.confocal_mark_speed ),
			command = lambda value: self.confocal_mark_scale_command(value)
		) # the "value" arg seems to be a reserved word in scale class, but I don't understand it well
		self.confocal_mark_scale.grid( row = 1, column = 1, columnspan = 2 )
		
		# photoactive mark
		self.photoactive_mark_button = tkinter.Button(self.control_frame)
		self.photoactive_mark_button["text"] = "Photon"
		self.photoactive_mark_button["command"] = self.photoactive_mark_button_command
		self.photoactive_mark_button.grid( row = 2, column = 0 )
		
		self.photoactive_mark_scale = tkinter.Scale(
			self.control_frame,
			from_ = 1000, to = 15000,
			orient = tkinter.HORIZONTAL,
			length = 256, sliderlength = 20,
			variable = tkinter.IntVar( value = self.photoactive_mark_speed ),
			command = lambda value: self.photoactive_mark_scale_command(value)
		)
		self.photoactive_mark_scale.grid( row = 2, column = 1, columnspan = 2 )
		
		# confocal lasers
		self.confocal_laser_button = [0, 0, 0, 0]
		self.confocal_laser_text = {0:'405', 1:'488', 2:'561', 3:'640'} # Dictionaries
		self.confocal_laser_scale = [0, 0, 0, 0]
		for i in range(4):
			self.confocal_laser_button[i] = tkinter.Button(self.control_frame)
			self.confocal_laser_button[i]["text"] = self.confocal_laser_text[i]
			self.confocal_laser_button[i]["command"] = lambda index = i: self.confocal_laser_button_command(index)
			self.confocal_laser_button[i].grid( row = 3 + i, column = 0 )
			
			self.confocal_laser_scale[i] = tkinter.Scale(
				self.control_frame,
				from_ = 0, to = 65535,
				orient = tkinter.HORIZONTAL,
				length = 256, sliderlength = 20,
				variable = tkinter.IntVar( value = self.confocal_laser_power[i] ),
				command = lambda value, index = i: self.confocal_laser_scale_command(value, index)
			)
			self.confocal_laser_scale[i].grid( row = 3 + i, column = 1, columnspan = 2 )
		
		# combined lasers controlled by Arduino
		self.combined_laser_button = [0, 0, 0, 0]
		self.combined_laser_text = {0:'Laser 1', 1:'Laser 2', 2:'Femto', 3:'Auto Focus'} # Dictionaries
		for i in range(4):
			self.combined_laser_button[i] = tkinter.Button(self.control_frame)
			self.combined_laser_button[i]["text"] = self.combined_laser_text[i]
			self.combined_laser_button[i]["command"] = lambda index = i: self.combined_laser_button_command(index)
			self.combined_laser_button[i].grid( row = 7, column = i )
		
	
	def create_status_frame(self):
		# snap
		self.continuous_mode_button = tkinter.Menubutton( self.status_frame, text = "Mode", relief = tkinter.RAISED)
		self.continuous_mode_button.grid( row = 0, column = 0 )
		self.continuous_mode_button_menu = tkinter.Menu( self.continuous_mode_button, tearoff = 0 )
		self.continuous_mode_button["menu"] = self.continuous_mode_button_menu
		self.continuous_mode_button_menu.add_command( label = "Continuous", command = lambda mode = True: self.continuous_mode_command(mode) )
		self.continuous_mode_button_menu.add_command( label = "Single Snap", command = lambda mode = False: self.continuous_mode_command(mode) )
		
		self.exposure_mode_button = tkinter.Menubutton( self.status_frame, text = "Exposure", relief = tkinter.RAISED)
		self.exposure_mode_button.grid( row = 0, column = 1 )
		self.exposure_mode_button_menu = tkinter.Menu( self.exposure_mode_button, tearoff = 0 )
		self.exposure_mode_button["menu"] = self.exposure_mode_button_menu
		self.exposure_mode_button_menu.add_command( label = "Internal", command = lambda mode = PVCam.EXPOSURE_MODES.TIMED_MODE: self.exposure_mode_command(mode) )
		# self.exposure_mode_button_menu.add_command( label = "Internal Variable", command = lambda mode = PVCam.EXPOSURE_MODES.VARIABLE_TIMED_MODE: self.exposure_mode_command(mode) ) # not available now
		self.exposure_mode_button_menu.add_command( label = "External", command = lambda mode = PVCam.EXPOSURE_MODES.STROBED_MODE: self.exposure_mode_command(mode) )
		self.exposure_mode_button_menu.add_command( label = "External First", command = lambda mode = PVCam.EXPOSURE_MODES.TRIGGER_FIRST_MODE: self.exposure_mode_command(mode) )
		self.exposure_mode_button_menu.add_command( label = "External Exposure", command = lambda mode = PVCam.EXPOSURE_MODES.BULB_MODE: self.exposure_mode_command(mode) )
		
		self.take_photo_button = tkinter.Button(self.status_frame)
		self.take_photo_button["text"] = "Acquire"
		self.take_photo_button["command"] = self.take_photo_command
		self.take_photo_button.grid( row = 0, column = 2 )
		
		self.exposure_entry = tkinter.Entry( self.status_frame, textvariable = tkinter.StringVar(self, value = self.exposure_time), width = 7, borderwidth = 6 )
		self.exposure_entry.grid( row = 0, column = 3 )
		self.exposure_entry.bind('<Return>', self.exposure_entry_command)
		
		self.exposure_button = tkinter.Button( self.status_frame, font = 'Consolas' )
		self.exposure_button["text"] = 'Exposure'
		self.exposure_button["command"] = lambda string = None: self.exposure_entry_command(string)
		self.exposure_button.grid( row = 1, column = 3 )
		
		# histogram
		self.status_frame_canvas = tkinter.Canvas( self.status_frame, bg = "white", width = 256, height = 128)
		self.status_frame_canvas.grid( row = 1, column = 1, rowspan = 4, columnspan = 2 )
		self.image_histogram = PIL.ImageTk.PhotoImage( PIL.Image.open("Images/no_histogram.jpg") )
		self.status_frame_histogram = self.status_frame_canvas.create_image( 0, 0, image = self.image_histogram, anchor = tkinter.NW )
		self.image_histogram_redline = self.status_frame_canvas.create_line( int( self.dynamic_range[0] / 256 ), 0, int( self.dynamic_range[0] / 256 ), 127, fill = "red", width = 3 )
		self.image_histogram_blueline = self.status_frame_canvas.create_line( int( self.dynamic_range[1] / 256 ), 0, int( self.dynamic_range[1] / 256 ), 127, fill = "blue", width = 3 )
		# it seems that canvas widget is easier than panel widget
		# self.image_histogram_ranged = PIL.ImageTk.PhotoImage( PIL.Image.open("Images/no_histogram.jpg") )
		# self.status_frame_panel = tkinter.Label(self.status_frame, image = self.image_histogram_ranged)
		# self.status_frame_panel.grid( row = 1, column = 1, rowspan = 4, columnspan = 2 )
		# self.status_frame_panel.image = self.image_histogram_ranged # keep a reference!
		
		# image_controls
		text = "ROI\t\nNone\t"
		self.roi_status_panel = tkinter.Label( self.status_frame, text = text, font = "Consolas" )
		self.roi_status_panel.grid( row = 1, column = 0, rowspan = 4 )
		
		self.full_image_button = tkinter.Button(self.status_frame)
		self.full_image_button["text"] = "Full"
		self.full_image_button["command"] = self.full_image_button_command
		self.full_image_button.grid( row = 2, column = 3 )
		
		# image_color
		self.image_color_button = tkinter.Menubutton( self.status_frame, text = "Color", relief = tkinter.RAISED)
		self.image_color_button.grid( row = 3, column = 3 )
		self.image_color_menu = tkinter.Menu( self.image_color_button, tearoff = 0 )
		self.image_color_button["menu"] = self.image_color_menu
		self.image_color_menu.add_command( label = "gray", command = lambda color = [255, 255, 255]: self.image_color_command(color) )
		self.image_color_menu.add_command( label = "red", command = lambda color = [255, 0, 0]: self.image_color_command(color) )
		self.image_color_menu.add_command( label = "blue", command = lambda color = [0, 0, 255]: self.image_color_command(color) )
		self.image_color_menu.add_command( label = "green", command = lambda color = [0, 255, 0]: self.image_color_command(color) )
		self.image_color_menu.add_command( label = "yellow", command = lambda color = [255, 255, 0]: self.image_color_command(color) )
		self.image_color_menu.add_command( label = "orange", command = lambda color = [255, 127, 0]: self.image_color_command(color) )
		
		# dynamic_range
		self.dynamic_range_label = [0, 0]
		self.dynamic_range_scale = [0, 0]
		for i in range(2):
			self.dynamic_range_label[i] = tkinter.Label( self.status_frame, text = str(self.dynamic_range[i]) )
			self.dynamic_range_label[i].grid( row = 5 + i, column = 0 )
			self.dynamic_range_scale[i] = tkinter.Scale(
				self.status_frame,
				from_ = 0, to = 65535,
				orient = tkinter.HORIZONTAL, showvalue = 0,
				length = 256, sliderlength = 5,
				variable = tkinter.IntVar( value = self.dynamic_range[i] ),
				command = lambda value, index = i: self.dynamic_range_scale_command(value, index)
			)
			self.dynamic_range_scale[i].grid( row = 5 + i, column = 1, columnspan = 2 )
	
	def create_motion_frame(self):
		# ASI stage for x-y
		self.stage_logo_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Logo_ASI.png") )
		self.stage_logo_label = tkinter.Label( self.motion_frame, image = self.stage_logo_image, height = 64, width = 64)
		self.stage_logo_label.grid( row = 0, column = 0, rowspan = 2, columnspan = 2 )
		
		self.stage_home_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.stage_home_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Home.png") )
		self.stage_home_button["image"] = self.stage_home_image
		self.stage_home_button["command"] = self.stage_targeted_home_command
		self.stage_home_button.grid( row = 2, column = 2 )
		
		self.stage_left_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.stage_left_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Left.png") )
		self.stage_left_button["image"] = self.stage_left_image
		self.stage_left_button["command"] = lambda index_x = 1, index_y = 0: self.stage_relative_command(index_x, index_y)
		self.stage_left_button.grid( row = 2, column = 1 )
		
		self.stage_right_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.stage_right_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Right.png") )
		self.stage_right_button["image"] = self.stage_right_image
		self.stage_right_button["command"] = lambda index_x = -1, index_y = 0: self.stage_relative_command(index_x, index_y)
		self.stage_right_button.grid( row = 2, column = 3 )
		
		self.stage_forward_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.stage_forward_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Down.png") )
		self.stage_forward_button["image"] = self.stage_forward_image
		self.stage_forward_button["command"] = lambda index_x = 0, index_y = 1: self.stage_relative_command(index_x, index_y)
		self.stage_forward_button.grid( row = 3, column = 2 )
		
		self.stage_backward_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.stage_backward_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Up.png") )
		self.stage_backward_button["image"] = self.stage_backward_image
		self.stage_backward_button["command"] = lambda index_x = 0, index_y = -1: self.stage_relative_command(index_x, index_y)
		self.stage_backward_button.grid( row = 1, column = 2 )
		
		self.stage_left_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.stage_left_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Left_ultra.png") )
		self.stage_left_ultra_button["image"] = self.stage_left_ultra_image
		self.stage_left_ultra_button["command"] = lambda index_x = 10, index_y = 0: self.stage_relative_command(index_x, index_y)
		self.stage_left_ultra_button.grid( row = 2, column = 0 )
		
		self.stage_right_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.stage_right_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Right_ultra.png") )
		self.stage_right_ultra_button["image"] = self.stage_right_ultra_image
		self.stage_right_ultra_button["command"] = lambda index_x = -10, index_y = 0: self.stage_relative_command(index_x, index_y)
		self.stage_right_ultra_button.grid( row = 2, column = 4 )
		
		self.stage_forward_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.stage_forward_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Down_ultra.png") )
		self.stage_forward_ultra_button["image"] = self.stage_forward_ultra_image
		self.stage_forward_ultra_button["command"] = lambda index_x = 0, index_y = 10: self.stage_relative_command(index_x, index_y)
		self.stage_forward_ultra_button.grid( row = 4, column = 2 )
		
		self.stage_backward_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.stage_backward_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Up_ultra.png") )
		self.stage_backward_ultra_button["image"] = self.stage_backward_ultra_image
		self.stage_backward_ultra_button["command"] = lambda index_x = 0, index_y = -10: self.stage_relative_command(index_x, index_y)
		self.stage_backward_ultra_button.grid( row = 0, column = 2 )
		
		self.stage_x_targeted_label = tkinter.Label( self.motion_frame, text = 'X➢', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.stage_x_targeted_label.grid( row = 0, column = 3, sticky = tkinter.E)
		
		self.stage_x_targeted_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = self.stage_x_targeted), width = 7, borderwidth = 6 )
		self.stage_x_targeted_entry.grid( row = 0, column = 4, columnspan = 2, sticky = tkinter.W )
		self.stage_x_targeted_entry.bind('<Return>', self.stage_x_targeted_entry_command)
		
		self.stage_y_targeted_label = tkinter.Label( self.motion_frame, text = 'Y➢', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.stage_y_targeted_label.grid( row = 1, column = 3, sticky = tkinter.E)
		
		self.stage_y_targeted_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = self.stage_y_targeted), width = 7, borderwidth = 6 )
		self.stage_y_targeted_entry.grid( row = 1, column = 4, columnspan = 2, sticky = tkinter.W )
		self.stage_y_targeted_entry.bind('<Return>', self.stage_y_targeted_entry_command)
		
		self.stage_targeted_button = tkinter.Button( self.motion_frame, height = 2, width = 6, font = 'Consolas' )
		self.stage_targeted_button["text"] = 'Move!'
		self.stage_targeted_button["command"] = self.stage_targeted_button_command
		self.stage_targeted_button.grid( row = 3, column = 3, rowspan = 2, columnspan = 3 )
		
		self.stage_relative_label = tkinter.Label( self.motion_frame, text = '▶=', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.stage_relative_label.grid( row = 3, column = 0)
		
		self.stage_relative_button = tkinter.Button( self.motion_frame, height = 1, width = 3, font = 'Consolas' )
		self.stage_relative_button["text"] = 'Set'
		self.stage_relative_button["command"] = lambda string = None: self.stage_relative_entry_command(string)
		self.stage_relative_button.grid( row = 3, column = 1)
		
		self.stage_relative_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = self.stage_relative), width = 7, borderwidth = 6 )
		self.stage_relative_entry.grid( row = 4, column = 0, columnspan = 2)
		self.stage_relative_entry.bind('<Return>', self.stage_relative_entry_command)
		
		# Step motor for z
		self.piezo_motor_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Logo_motor.png") )
		self.piezo_motor_label = tkinter.Label( self.motion_frame, image = self.piezo_motor_image, height = 96, width = 32)
		self.piezo_motor_label.grid( row = 0, column = 6, rowspan = 3, columnspan = 1 )
		
		self.motor_home_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.motor_home_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Home.png") )
		self.motor_home_button["image"] = self.motor_home_image
		self.motor_home_button["command"] = self.motor_targeted_home_command
		self.motor_home_button.grid( row = 2, column = 7 )
		
		self.motor_up_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.motor_up_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Up.png") )
		self.motor_up_button["image"] = self.motor_up_image
		self.motor_up_button["command"] = lambda index = 1: self.motor_relative_command(index)
		self.motor_up_button.grid( row = 1, column = 7 )
		
		self.motor_down_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.motor_down_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Down.png") )
		self.motor_down_button["image"] = self.motor_down_image
		self.motor_down_button["command"] = lambda index = -1: self.motor_relative_command(index)
		self.motor_down_button.grid( row = 3, column = 7 )
		
		self.motor_up_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.motor_up_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Up_ultra.png") )
		self.motor_up_ultra_button["image"] = self.motor_up_ultra_image
		self.motor_up_ultra_button["command"] = lambda index = 10: self.motor_relative_command(index)
		self.motor_up_ultra_button.grid( row = 0, column = 7 )
		
		self.motor_down_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.motor_down_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Down_ultra.png") )
		self.motor_down_ultra_button["image"] = self.motor_down_ultra_image
		self.motor_down_ultra_button["command"] = lambda index = -10: self.motor_relative_command(index)
		self.motor_down_ultra_button.grid( row = 4, column = 7 )
		
		self.motor_targeted_label = tkinter.Label( self.motion_frame, text = 'Motor➢', font = 'Consolas', height = 1, width = 6, relief = tkinter.GROOVE, borderwidth = 2 )
		self.motor_targeted_label.grid( row = 0, column = 8, columnspan = 2 )
		
		self.motor_targeted_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = self.motor_targeted), width = 7, borderwidth = 6 )
		self.motor_targeted_entry.grid( row = 1, column = 8, columnspan = 2 )
		self.motor_targeted_entry.bind('<Return>', self.motor_targeted_entry_command)
		
		self.motor_targeted_button = tkinter.Button( self.motion_frame, height = 1, width = 6, font = 'Consolas' )
		self.motor_targeted_button["text"] = 'Move!'
		self.motor_targeted_button["command"] = lambda string = None: self.motor_targeted_entry_command(string)
		self.motor_targeted_button.grid( row = 2, column = 8, columnspan = 2 )
		
		self.motor_relative_label = tkinter.Label( self.motion_frame, text = '▲=', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.motor_relative_label.grid( row = 3, column = 8, sticky = tkinter.E)
		
		self.motor_relative_button = tkinter.Button( self.motion_frame, height = 1, width = 3, font = 'Consolas' )
		self.motor_relative_button["text"] = 'Set'
		self.motor_relative_button["command"] = self.motor_relative_entry_command
		self.motor_relative_button.grid( row = 3, column = 9 )
		
		self.motor_relative_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = self.motor_relative), width = 7, borderwidth = 6 )
		self.motor_relative_entry.grid( row = 4, column = 8, columnspan = 2 )
		self.motor_relative_entry.bind('<Return>', self.motor_relative_entry_command)
		
		# Physik Instrumente piezo for micro-z
		self.piezo_logo_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Logo_PI.jpg") )
		self.piezo_logo_label = tkinter.Label( self.motion_frame, image = self.piezo_logo_image, height = 96, width = 32)
		self.piezo_logo_label.grid( row = 0, column = 10, rowspan = 3, columnspan = 1 )
		
		self.piezo_home_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.piezo_home_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Home.png") )
		self.piezo_home_button["image"] = self.piezo_home_image
		self.piezo_home_button["command"] = self.piezo_targeted_home_command
		self.piezo_home_button.grid( row = 2, column = 11 )
		
		self.piezo_up_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.piezo_up_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Up.png") )
		self.piezo_up_button["image"] = self.piezo_up_image
		self.piezo_up_button["command"] = lambda index = 1: self.piezo_relative_command(index)
		self.piezo_up_button.grid( row = 1, column = 11 )
		
		self.piezo_down_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.piezo_down_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Down.png") )
		self.piezo_down_button["image"] = self.piezo_down_image
		self.piezo_down_button["command"] = lambda index = -1: self.piezo_relative_command(index)
		self.piezo_down_button.grid( row = 3, column = 11 )
		
		self.piezo_up_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.piezo_up_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Up_ultra.png") )
		self.piezo_up_ultra_button["image"] = self.piezo_up_ultra_image
		self.piezo_up_ultra_button["command"] = lambda index = 10: self.piezo_relative_command(index)
		self.piezo_up_ultra_button.grid( row = 0, column = 11 )
		
		self.piezo_down_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.piezo_down_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open("Icons/Down_ultra.png") )
		self.piezo_down_ultra_button["image"] = self.piezo_down_ultra_image
		self.piezo_down_ultra_button["command"] = lambda index = -10: self.piezo_relative_command(index)
		self.piezo_down_ultra_button.grid( row = 4, column = 11 )
		
		self.piezo_targeted_label = tkinter.Label( self.motion_frame, text = 'Piezo➢', font = 'Consolas', height = 1, width = 6, relief = tkinter.GROOVE, borderwidth = 2 )
		self.piezo_targeted_label.grid( row = 0, column = 12, columnspan = 2 )
		
		self.piezo_targeted_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = self.piezo_targeted), width = 7, borderwidth = 6 )
		self.piezo_targeted_entry.grid( row = 1, column = 12, columnspan = 2 )
		self.piezo_targeted_entry.bind('<Return>', self.piezo_targeted_entry_command)
		
		self.piezo_targeted_button = tkinter.Button( self.motion_frame, height = 1, width = 6, font = 'Consolas' )
		self.piezo_targeted_button["text"] = 'Move!'
		self.piezo_targeted_button["command"] = lambda string = None: self.piezo_targeted_entry_command(string)
		self.piezo_targeted_button.grid( row = 2, column = 12, columnspan = 2 )
		
		self.piezo_relative_label = tkinter.Label( self.motion_frame, text = '▲=', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.piezo_relative_label.grid( row = 3, column = 12, sticky = tkinter.E)
		
		self.piezo_relative_button = tkinter.Button( self.motion_frame, height = 1, width = 3, font = 'Consolas' )
		self.piezo_relative_button["text"] = 'Set'
		self.piezo_relative_button["command"] = self.piezo_relative_entry_command
		self.piezo_relative_button.grid( row = 3, column = 13 )
		
		self.piezo_relative_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = self.piezo_relative), width = 7, borderwidth = 6 )
		self.piezo_relative_entry.grid( row = 4, column = 12, columnspan = 2 )
		self.piezo_relative_entry.bind('<Return>', self.piezo_relative_entry_command)
		
		# Showing status
		text = ''
		self.status_label = tkinter.Label( self.motion_frame, text = text, font = 'Consolas', height = 3, width = 55, relief = tkinter.GROOVE, borderwidth = 6, anchor = tkinter.W)
		self.status_label.grid( row = 5, column = 0, rowspan = 3, columnspan = 14 )
	
	def create_image_frame(self):
		self.image_frame_canvas = tkinter.Canvas( self.image_frame, bg = "white", width = 1024, height = 1024)
		self.image_frame_canvas.grid( row = 0, column = 0 )
		self.image_exhibition = PIL.ImageTk.PhotoImage( PIL.Image.open("Images/no_image.jpg") )
		self.image_frame_image = self.image_frame_canvas.create_image( 512, 512, image = self.image_exhibition, anchor = tkinter.CENTER )
		self.image_frame_rect = self.image_frame_canvas.create_rectangle( self.region_of_selected["x1"], self.region_of_selected["y1"], self.region_of_selected["x2"], self.region_of_selected["y2"], width = 0.0 )
		self.image_frame_canvas.bind("<ButtonPress-1>", self.image_frame_click)
		self.image_frame_canvas.bind("<B1-Motion>", self.image_frame_drag)
		self.image_frame_canvas.bind("<ButtonRelease-1>", self.image_frame_release)
	
	def open_board(self):
		self.master.title( "Nymphscopy opening boards..." )
		self.confocalBoard = ConfocalBoard.ConfocalBoard()
		self.pvcam = PVCam.PVCam()
		# os.system('powershell python .\LaserBoard.py')
		# not python 3 standard with-as syntax
		self.client = multiprocessing.connection.Client( ('localhost', 6000), authkey = b'Si Valetis Gaudeo' )
		self.piezo = MotionControl.PIPiezo()
		self.stage = MotionControl.ASIStage()
		self.arduino = Arduino.Arduino()
		
		self.pvcam.exposure_time_reset(self.exposure_time)
		self.pvcam.acquisition_setup()
		self.pvcam.dynamic_range_resize(self.dynamic_range)
		
		self.master.title( "Nymphscopy main application" )
		self.close_flag = False
	
	def exit(self):
		self.master.title( "Nymphscopy closing boards..." )
		self.confocalBoard.close()
		self.pvcam.close()
		self.client.send( [0, 0] )
		self.client.recv()
		self.client.close()
		self.piezo.close()
		self.stage.close()
		self.arduino.close()
		# time.sleep(5)
		del self.confocalBoard
		del self.pvcam
		del self.client
		del self.piezo
		del self.stage
		self.intact_flag = False
		self.master.title( "Nymphscopy main application" )
		self.master.destroy()
	
	def pinhole_command(self, position):
		self.master.title( "Nymphscopy moving pinholes..." )
		self.confocalBoard.pinhole(position)
		self.master.title( "Nymphscopy main application" )
	
	def filter_command(self, position):
		self.master.title( "Nymphscopy turning filters..." )
		self.confocalBoard.filter_wheel(position)
		self.master.title( "Nymphscopy main application" )
	
	def confocal_mark_button_command(self):
		if self.confocal_mark_flag:
			self.confocalBoard.stop_mark()
			self.confocal_mark_button["text"] = "C-standby"
			self.confocal_mark_button.config( bg = "white", relief = tkinter.RAISED )
			self.confocal_mark_flag = False
		else:
			self.confocalBoard.confocal_mark()
			self.confocal_mark_button["text"] = "C-marking" 
			self.confocal_mark_button.config( bg = "red", relief = tkinter.SUNKEN )
			self.confocal_mark_flag = True
	
	def confocal_mark_scale_command(self, value):
		self.confocal_mark_speed = int(value)
		self.confocalBoard.markspeed = 46.5 * 1000 / self.confocal_mark_speed
	
	def photoactive_mark_button_command(self):
		if self.photoactive_mark_flag:
#			 self.confocalBoard.stop_mark()
			self.client.send( [2, 0] )
			text = self.client.recv()
			self.photoactive_mark_button["text"] = text
			self.photoactive_mark_button.config( bg = "white", relief = tkinter.RAISED )
			self.confocal_mark_flag = False
			self.photoactive_mark_flag = False
		else:
#			 self.confocalBoard.markspeed = 15000.0
#			 self.confocalBoard.confocal_mark()
			self.client.send( [1, 0] )
			text = self.client.recv()
			self.photoactive_mark_button["text"] = text
			self.photoactive_mark_button.config( bg = "red", relief = tkinter.SUNKEN )
			self.confocal_mark_flag = True
			self.photoactive_mark_flag = True
	
	def photoactive_mark_scale_command(self, value):
		self.photoactive_mark_speed = int(value)
		self.client.send([3, self.photoactive_mark_speed])
		self.client.recv()
	
	def confocal_laser_button_command(self, index):
		if self.confocal_laser_on[index] == 0:
			self.confocal_laser_on[index] = 1
			self.confocal_laser_button[index].config( bg = "red", relief = tkinter.SUNKEN )
		else:
			self.confocal_laser_on[index] = 0
			self.confocal_laser_button[index].config( bg = "white", relief = tkinter.RAISED )
		self.confocalBoard.laser_on[index] = self.confocal_laser_on[index]
	
	def confocal_laser_scale_command(self, value, index):
		self.confocal_laser_power[index] = int(value)
		self.confocalBoard.laser_power[index] = self.confocal_laser_power[index]
	
	def combined_laser_button_command(self, index):
		pin = index + 2
		if self.combined_laser_on[index]:
			self.arduino.digital_write( pin, 0 )
			self.combined_laser_on[index] = False
			self.combined_laser_button[index].config( bg = "white", relief = tkinter.RAISED )
		else:
			self.arduino.digital_write( pin, 1 )
			self.combined_laser_on[index] = True
			self.combined_laser_button[index].config( bg = "red", relief = tkinter.SUNKEN )
	
	def continuous_mode_command(self, mode):
		self.continuous_mode = mode
		self.pvcam.continuous_remode( mode )
	
	def exposure_mode_command(self, mode):
		self.pvcam.exp_mode_reset(mode)
	
	def take_photo_command(self):
		# This could let it slow, but what can I do?
		self.pvcam.acquisition_setup()
		if self.continuous_mode:
			if self.continuous_living_flag:
				self.pvcam.acquisition_stop()
				self.take_photo_button.config( bg = "white", relief = tkinter.RAISED )
				self.continuous_living_flag = False
			else:
				self.pvcam.acquisition()
				self.take_photo_button.config( bg = "red", relief = tkinter.SUNKEN )
				self.continuous_living_flag = True
		else:
			# Warning: the motion is not stopped!
			self.pvcam.acquisition()
	
	def exposure_entry_command(self, value):
		try:
			self.exposure_time = int( self.exposure_entry.get() )
		except ValueError:
			print("not a valid number")
		else:
			# This could be optimized
			if self.exposure_time < 1:
				self.exposure_time = 1
			self.pvcam.exposure_time_reset(self.exposure_time)
	
	def full_image_button_command(self):
		self.pvcam.roi_reset()
	
	def image_color_command(self, color):
		self.pvcam.color_reset(color)
	
	def dynamic_range_scale_command(self, value, index):
		self.dynamic_range[index] = int(value)
		self.dynamic_range_label[index]["text"] = str(self.dynamic_range[index])
		self.pvcam.dynamic_range_resize(self.dynamic_range)
		if index == 0:
			self.status_frame_canvas.coords( self.image_histogram_redline, int( self.dynamic_range[0] / 256 ), 0, int( self.dynamic_range[0] / 256 ), 127 )
		else:
			self.status_frame_canvas.coords( self.image_histogram_blueline, int( self.dynamic_range[1] / 256 ), 0, int( self.dynamic_range[1] / 256 ), 127 )
	
	def show_image(self):
		self.pvcam.image_generate()
		image = self.pvcam.image_export()
		self.image_exhibition = PIL.ImageTk.PhotoImage( PIL.Image.fromarray(image) )
		self.image_frame_canvas.itemconfig( self.image_frame_image, image = self.image_exhibition )
	
	def show_histogram(self):
		roi = self.pvcam.roi_export()
		text = f'ROI:\t\nx1: {roi[0]}\nx2: {roi[1]}\ny1: {roi[2]}\ny2: {roi[3]}\n'
		self.roi_status_panel["text"] = text
		self.pvcam.histogram_generate()
		histogram = self.pvcam.histogram_export()
		self.image_histogram = PIL.ImageTk.PhotoImage( PIL.Image.fromarray(histogram) )
		self.status_frame_canvas.itemconfig( self.status_frame_histogram, image = self.image_histogram )
	
	def image_frame_click(self, coordinate):
		self.region_of_selected["x1"] = coordinate.x
		self.region_of_selected["y1"] = coordinate.y
		self.region_of_selected["x2"] = coordinate.x
		self.region_of_selected["y2"] = coordinate.y
		self.image_frame_canvas.itemconfig( self.image_frame_rect, dash = (4, 4), width = 5.0 )
		self.image_frame_canvas.coords( self.image_frame_rect, self.region_of_selected["x1"], self.region_of_selected["y1"], self.region_of_selected["x2"], self.region_of_selected["y2"] )
	
	def image_frame_drag(self, coordinate):
		self.region_of_selected["x2"] = coordinate.x
		self.region_of_selected["y2"] = coordinate.y
		self.image_frame_canvas.coords( self.image_frame_rect, self.region_of_selected["x1"], self.region_of_selected["y1"], self.region_of_selected["x2"], self.region_of_selected["y2"] )
	
	def image_frame_release(self, coordinate):
		self.region_of_selected["x2"] = coordinate.x
		self.region_of_selected["y2"] = coordinate.y
		self.image_frame_canvas.coords( self.image_frame_rect, self.region_of_selected["x1"], self.region_of_selected["y1"], self.region_of_selected["x2"], self.region_of_selected["y2"] )
		
		# x <-> y, and set range
		self.region_of_selected = {"x1":self.region_of_selected["y1"], "y1":self.region_of_selected["x1"], "x2":self.region_of_selected["y2"], "y2":self.region_of_selected["x2"]}
		for i in ("x1", "x2", "y1", "y2"):
			if self.region_of_selected[i] < 0:
				self.region_of_selected[i] = 0
			elif self.region_of_selected[i] > 1027:
				self.region_of_selected[i] = 1027
		self.pvcam.roi_resize(self.region_of_selected)
		
		self.region_of_selected = {"x1":0, "y1":0, "x2":0, "y2":0}
		self.image_frame_canvas.itemconfig(self.image_frame_rect, dash = (), width = 0.0 )
		self.image_frame_canvas.coords( 0, 0, 0, 0 )
	
	def stage_targeted_home_command(self):
		self.stage.move_to([0.0, 0.0])
	
	def stage_relative_command(self, index_x, index_y):
		position = [index_x * self.stage_relative * 10000, index_y * self.stage_relative * 10000]
		self.stage.move_by(position)
	
	def stage_x_targeted_entry_command(self, string):
		try:
			self.stage_x_targeted = float( self.stage_x_targeted_entry.get() )
		except ValueError:
			print("not a valid number")
		else:
			position = self.stage.position_value()
			position[0] = self.stage_x_targeted * 10000
			self.stage.move_to(position)
	
	def stage_y_targeted_entry_command(self, string):
		try:
			self.stage_y_targeted = float( self.stage_y_targeted_entry.get() )
		except ValueError:
			print("not a valid number")
		else:
			position = self.stage.position_value()
			position[1] = self.stage_y_targeted * 10000
			self.stage.move_to(position)
	
	def stage_targeted_button_command(self):
		try:
			self.stage_x_targeted = float( self.stage_x_targeted_entry.get() )
			self.stage_y_targeted = float( self.stage_y_targeted_entry.get() )
		except ValueError:
			print("not a valid number")
		else:
			position = [self.stage_x_targeted * 10000, self.stage_y_targeted * 10000]
			self.stage.move_to(position)
	
	def stage_relative_entry_command(self, string):
		try:
			self.stage_relative = float( self.stage_relative_entry.get() )
		except ValueError:
			print("not a valid number")
		else:
			if self.stage_relative < 0.0:
				self.stage_relative = 0.0
	
	def motor_targeted_home_command(self):
		self.client.send( [4, 0] )
		self.client.recv()
	
	def motor_relative_command(self, index):
		position = index * self.motor_relative
		self.client.send( [5, position] )
		self.client.recv()
	
	def motor_targeted_entry_command(self, string):
		try:
			self.motor_targeted = float( self.motor_targeted_entry.get() )
		except ValueError:
			print("not a valid number")
		else:
			self.client.send( [4, self.motor_targeted] )
			self.client.recv()
	
	def motor_relative_entry_command(self, string):
		try:
			self.motor_relative = float( self.motor_relative_entry.get() )
		except ValueError:
			print("not a valid number")
		else:
			if self.motor_relative < 0.0:
				self.motor_relative = 0.0
	
	def piezo_targeted_home_command(self):
		self.piezo.move_to(0.0)
	
	def piezo_relative_command(self, index):
		position = index * self.piezo_relative
		self.piezo.move_by(position)
	
	def piezo_targeted_entry_command(self, string):
		try:
			self.piezo_targeted = float( self.piezo_targeted_entry.get() )
		except ValueError:
			print("not a valid number")
		else:
			self.piezo.move_to(self.piezo_targeted)
	
	def piezo_relative_entry_command(self, string):
		try:
			self.piezo_relative = float( self.piezo_relative_entry.get() )
		except ValueError:
			print("not a valid number")
		else:
			if self.piezo_relative < 0:
				self.piezo_relative = 0
	
	def motion_frame_status(self):
		self.stage.position_update()
		self.client.send( [6, 0] )
		self.piezo.position_update()
		stage_position = self.stage.position_value() / 10000
		motor_position = self.client.recv()
		piezo_position = self.piezo.position_value()
		text = f'stage(mm):  X ={stage_position[0]:8.3f},  Y ={stage_position[1]:8.3f},  step ={self.stage_relative:6.3f} \nmotor(mm):     position ={motor_position:9.4f},     step ={self.motor_relative:7.4f}\npiezo(μm):     position ={piezo_position:9.4f},     step ={self.piezo_relative:7.4f}'
		self.status_label['text'] = text
	
root = tkinter.Tk()
application = Application( master = root )
# substitution of mainloop()
while application.intact_flag:
	application.update_idletasks()
	application.update()
	if application.close_flag:
		application.open_board()
	if application.intact_flag:
		application.motion_frame_status()
		application.confocalBoard.laser_power_output()
		# I invoke class variable here!
		if application.pvcam.data_exist():
			application.show_histogram()
			application.show_image()
		# too slow!
		# if application.confocal_laser_flag == 0:
		# 	application.confocalBoard.laser_power_output()
		# application.confocal_laser_flag += 1
		# application.confocal_laser_flag = application.confocal_laser_flag % 10
# application.mainloop()