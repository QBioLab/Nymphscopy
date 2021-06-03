import Nymphscope
import tkinter
import tkinter.filedialog
import webbrowser
import multiprocessing.connection
import os
import time
import numpy
import PIL.Image
import PIL.ImageTk

class Application(tkinter.Frame):
	nymphscope = None
	
	# GUI interface flags and variables
	intact_flag = True # exists or not
	close_flag = True
	dynamic_range_select_flag = [False, False]
	roi_set_flag = False
	region_of_selected = {'x1':0, 'y1':0, 'x2':0, 'y2':0}
	stage_popup_flag = False
	
	def __init__(self, master = None):
		self.intact_flag = True
		super().__init__(master)
		self.pack()
		
		self.create_frames()
		self.create_control_frame()
		self.create_status_frame()
		self.create_motion_frame()
		self.create_image_frame()
		
		master.protocol( 'WM_DELETE_WINDOW', self.exit ) # set win.close to self.exit
		# master.geometry( '1920x1080' )
		master.title('Nymphscope main application')
		master.iconbitmap('Icons/Nymphscope.ico')
	
	def open_board(self):
		self.master.title( 'Nymphscope opening boards...' )
		self.nymphscope = Nymphscope.Nymphscope()
		self.master.title( 'Nymphscope main application' )
		self.close_flag = False
	
	def exit(self):
		self.master.title( 'Nymphscope closing boards...' )
		self.nymphscope.close()
		self.intact_flag = False
		self.master.title( 'Nymphscope main application' )
		self.master.destroy()
	
	def information(self):
		version = '2.1 alpha'
		date = '11 Jan. 2020'
		information_message = f'Nymphscope version {version}\n\nBuild time: {date}\n\nAuthor: WANG Yuhao\n\ngjwtry.ifp.caep@gmail.com\n\nProf. HUANG Wei\'s lab in SUSTech'
		
		top = tkinter.Toplevel()
		top.title('About Nymphscope')
		
		msg = tkinter.Label( top, text = information_message, font = ('Roman', 20), height = 10, width = 40, relief = tkinter.GROOVE, borderwidth = 6)
		msg.pack()
		
		button = tkinter.Button( top, text = 'Dismiss', height = 3, width = 20, font = ('Arial', 20), relief = tkinter.RAISED, command = top.destroy )
		button.pack()
	
	def help(self):
		webbrowser.open_new(r'file://C:\Nymphscope_manual\Nymphscope_User_Manual.pdf')
	
	# Frame widgets construction
	
	def create_frames(self):
		self.control_frame = tkinter.Frame( self, width = 552, height = 350, borderwidth = 10, relief = tkinter.GROOVE)
		self.control_frame.grid( row = 0, column = 0, rowspan = 1, columnspan = 1 )
		self.control_frame.grid_propagate(0) # disable changing the size
		for i in range(8):
			self.control_frame.grid_rowconfigure( index = i, minsize = 38)
		for i in range(14):
			self.control_frame.grid_columnconfigure( index = i, minsize = 38)
		
		self.status_frame = tkinter.Frame( self, width = 552, height = 350, borderwidth = 10, relief = tkinter.RIDGE)
		self.status_frame.grid( row = 1, column = 0, rowspan = 1, columnspan = 1 )
		self.status_frame.grid_propagate(0) # disable changing the size
		for i in range(8):
			self.status_frame.grid_rowconfigure( index = i, minsize = 38)
		for i in range(14):
			self.status_frame.grid_columnconfigure( index = i, minsize = 38)
		
		self.motion_frame = tkinter.Frame( self, width = 552, height = 324, borderwidth = 10, relief = tkinter.RAISED)
		self.motion_frame.grid( row = 2, column = 0, rowspan = 1, columnspan = 1 )
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
		self.main_button = tkinter.Menubutton( self.control_frame, height = 1, width = 6, font = 'Arial', relief = tkinter.RAISED )
		self.main_button['text'] = 'Program'
		self.main_button.grid( row = 0, column = 0, rowspan = 1, columnspan = 2 )
		
		self.main_menu = tkinter.Menu( self.main_button, tearoff = 0 )
		self.main_button['menu'] = self.main_menu
		# self.main_menu.add_command( label = 'Open Boards', command = self.open_board )
		self.main_menu.add_command( label = 'Quit', command = self.exit )
		self.main_menu.add_command( label = 'Help', command = self.help )
		self.main_menu.add_command( label = 'About', command = self.information )
		
		# pinhole menubar
		self.pinhole_button = tkinter.Menubutton( self.control_frame, height = 1, width = 6, font = 'Arial', relief = tkinter.RAISED )
		self.pinhole_button['text'] = 'Pinhole'
		self.pinhole_button.grid( row = 0, column = 2, rowspan = 1, columnspan = 2 )
		
		self.pinhole_menu = tkinter.Menu( self.pinhole_button, tearoff = 0 )
		self.pinhole_button['menu'] = self.pinhole_menu
		self.pinhole_menu.add_command( label = 'Wide Field', command = lambda label = 'Wide Field': self.pinhole_command(label) )
		self.pinhole_menu.add_command( label = '50 μm', command = lambda label = '50 μm': self.pinhole_command(label) )
		self.pinhole_menu.add_command( label = '30 μm', command = lambda label = '30 μm': self.pinhole_command(label) )
		self.pinhole_menu.add_command( label = '20 μm', command = lambda label = '20 μm': self.pinhole_command(label) )
		
		# filter wheel menubar
		self.filter_wheel_button = tkinter.Menubutton( self.control_frame, height = 1, width = 6, font = 'Arial', relief = tkinter.RAISED )
		self.filter_wheel_button['text'] = 'Filter'
		self.filter_wheel_button.grid( row = 0, column = 4, rowspan = 1, columnspan = 2 )
		
		self.filter_wheel_menu = tkinter.Menu( self.filter_wheel_button, tearoff = 0 )
		self.filter_wheel_button['menu'] = self.filter_wheel_menu
		self.filter_wheel_menu.add_command( label = '447/60', command = lambda label = '447/60': self.filter_command(label) )
		self.filter_wheel_menu.add_command( label = '525/45', command = lambda label = '525/45': self.filter_command(label) )
		self.filter_wheel_menu.add_command( label = '586/20', command = lambda label = '586/20': self.filter_command(label) )
		self.filter_wheel_menu.add_command( label = '615/24', command = lambda label = '615/24': self.filter_command(label) )
		self.filter_wheel_menu.add_command( label = '676/29', command = lambda label = '676/29': self.filter_command(label) )
		self.filter_wheel_menu.add_command( label = '446/523/600/677', command = lambda position = 'Four Color': self.filter_command(position) )
		
		# mark label
		self.mark_label = tkinter.Label( self.control_frame, text = 'Scanner', font = 'Consolas', height = 1, width = 7, relief = tkinter.GROOVE, borderwidth = 2 )
		self.mark_label.grid( row = 1, column = 0, rowspan = 1, columnspan = 2 )
		
		self.mark_speed_label = tkinter.Label( self.control_frame, text = 'Speed', font = 'Consolas', height = 1, width = 7, relief = tkinter.GROOVE, borderwidth = 2 )
		self.mark_speed_label.grid( row = 1, column = 2, rowspan = 1, columnspan = 2 )
		
		self.mark_set_label = tkinter.Label( self.control_frame, text = '⏎', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.mark_set_label.grid( row = 1, column = 4, rowspan = 1, columnspan = 1 )
		
		# confocal mark
		self.confocal_mark_button = tkinter.Button( self.control_frame, height = 1, width = 7, font = 'Arial', relief = tkinter.RAISED )
		self.confocal_mark_button['text'] = 'DebugOnly'
		self.confocal_mark_button['command'] = self.confocal_mark_button_command
		self.confocal_mark_button.grid( row = 2, column = 0, rowspan = 1, columnspan = 2 )
		self.confocal_mark_button['state'] = tkinter.DISABLED
		
		self.confocal_mark_entry = tkinter.Entry( self.control_frame, textvariable = tkinter.StringVar(self, value = 0), width = 7, borderwidth = 6 )
		self.confocal_mark_entry.grid( row = 2, column = 2, rowspan = 1, columnspan = 2, sticky = tkinter.W )
		self.confocal_mark_entry.bind('<Return>', self.confocal_mark_entry_command)
		
		self.confocal_mark_set_button = tkinter.Button( self.control_frame, height = 1, width = 3, font = 'Arial', relief = tkinter.RAISED )
		self.confocal_mark_set_button['text'] = 'Set'
		self.confocal_mark_set_button['command'] = lambda string = None: self.confocal_mark_entry_command(string)
		self.confocal_mark_set_button.grid( row = 2, column = 4, rowspan = 1, columnspan = 1 )
		
		# photoactive mark
		self.photoactive_mark_button = tkinter.Button( self.control_frame, height = 1, width = 7, font = 'Arial', relief = tkinter.RAISED )
		self.photoactive_mark_button['text'] = 'DebugOnly'
		self.photoactive_mark_button['command'] = self.photoactive_mark_button_command
		self.photoactive_mark_button.grid( row = 3, column = 0, rowspan = 1, columnspan = 2 )
		self.photoactive_mark_button['state'] = tkinter.DISABLED
		
		self.photoactive_mark_entry = tkinter.Entry( self.control_frame, textvariable = tkinter.StringVar(self, value = 0), width = 7, borderwidth = 6 )
		self.photoactive_mark_entry.grid( row = 3, column = 2, rowspan = 1, columnspan = 2, sticky = tkinter.W )
		self.photoactive_mark_entry.bind('<Return>', self.photoactive_mark_entry_command)
		
		self.photoactive_mark_set_button = tkinter.Button( self.control_frame, height = 1, width = 3, font = 'Arial', relief = tkinter.RAISED )
		self.photoactive_mark_set_button['text'] = 'Set'
		self.photoactive_mark_set_button['command'] = lambda string = None: self.photoactive_mark_entry_command(string)
		self.photoactive_mark_set_button.grid( row = 3, column = 4, rowspan = 1, columnspan = 1 )
		
		# confocal lasers
		self.confocal_laser_label = tkinter.Label( self.control_frame, text = 'Lasers', font = 'Consolas', height = 1, width = 7, relief = tkinter.GROOVE, borderwidth = 2 )
		self.confocal_laser_label.grid( row = 1, column = 6, rowspan = 1, columnspan = 2 )
		
		self.confocal_laser_power_label = tkinter.Label( self.control_frame, text = 'Power', font = 'Consolas', height = 1, width = 7, relief = tkinter.GROOVE, borderwidth = 2 )
		self.confocal_laser_power_label.grid( row = 1, column = 8, rowspan = 1, columnspan = 2 )
		
		self.confocal_laser_set_label = tkinter.Label( self.control_frame, text = '⏎', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.confocal_laser_set_label.grid( row = 1, column = 10, rowspan = 1, columnspan = 1 )
		
		self.confocal_laser_button = [0, 0, 0, 0]
		self.confocal_laser_text = {0:'405 nm', 1:'488 nm', 2:'561 nm', 3:'640 nm'} # Dictionaries
		self.confocal_laser_entry = [0, 0, 0, 0]
		self.confocal_laser_set_button = [0, 0, 0, 0]
		for i in range(4):
			self.confocal_laser_button[i] = tkinter.Button( self.control_frame, height = 1, width = 7, font = 'Arial', relief = tkinter.RAISED )
			self.confocal_laser_button[i]['text'] = self.confocal_laser_text[i]
			self.confocal_laser_button[i]['command'] = lambda index = i: self.confocal_laser_button_command(index)
			self.confocal_laser_button[i].grid( row = 2 + i, column = 6, rowspan = 1, columnspan = 2 )
			
			self.confocal_laser_entry[i] = tkinter.Entry( self.control_frame, textvariable = tkinter.StringVar(self, value = 0), width = 7, borderwidth = 6 )
			self.confocal_laser_entry[i].grid( row = 2 + i, column = 8, rowspan = 1, columnspan = 2, sticky = tkinter.W )
			self.confocal_laser_entry[i].bind( '<Return>', lambda string = None, index = i: self.confocal_laser_entry_command(string, index) )
			
			self.confocal_laser_set_button[i] = tkinter.Button( self.control_frame, height = 1, width = 3, font = 'Arial', relief = tkinter.RAISED )
			self.confocal_laser_set_button[i]['text'] = 'Set'
			self.confocal_laser_set_button[i]['command'] = lambda string = None, index = i: self.confocal_laser_entry_command(string, index)
			self.confocal_laser_set_button[i].grid( row = 2 + i, column = 10, rowspan = 1, columnspan = 1 )
		
		# photoactive lasers controlled by Arduino
		self.photoactive_laser_label = tkinter.Label( self.control_frame, text = 'Photo\nActive\nLasers', font = 'Consolas', height = 4, width = 7, relief = tkinter.GROOVE, borderwidth = 2 )
		self.photoactive_laser_label.grid( row = 6, column = 6, rowspan = 2, columnspan = 2 )
		
		self.photoactive_laser_button = [0, 0, 0, 0]
		self.photoactive_laser_text = {0:'Laser 1', 1:'Laser 2', 2:'Femto', 3:'Focus'}
		photoactive_laser_button_row = [6 ,6 ,7, 7]
		photoactive_laser_button_column = [8 ,10 ,8, 10]
		for i in range(4):
			self.photoactive_laser_button[i] = tkinter.Button( self.control_frame, height = 1, width = 7, font = 'Arial', relief = tkinter.RAISED )
			self.photoactive_laser_button[i]['text'] = self.photoactive_laser_text[i]
			self.photoactive_laser_button[i]['command'] = lambda index = i: self.photoactive_laser_button_command(index)
			self.photoactive_laser_button[i].grid( row = photoactive_laser_button_row[i], column = photoactive_laser_button_column[i], rowspan = 1, columnspan = 2 )
		
		# Autofocus Laser Power
		self.autofocus_laser_label = tkinter.Label( self.control_frame, text = 'Auto\nFocus\nLaser\nPower', font = 'Consolas', height = 4, width = 7, relief = tkinter.GROOVE, borderwidth = 2 )
		self.autofocus_laser_label.grid( row = 4, column = 12, rowspan = 2, columnspan = 2 )
		
		self.autofocus_laser_entry = tkinter.Entry( self.control_frame, textvariable = tkinter.StringVar(self, value = 0), width = 7, borderwidth = 6 )
		self.autofocus_laser_entry.grid( row = 6, column = 12, rowspan = 1, columnspan = 2, sticky = tkinter.N + tkinter.S )
		self.autofocus_laser_entry.bind('<Return>', self.autofocus_laser_entry_command)
		
		self.autofocus_laser_set_button = tkinter.Button( self.control_frame, height = 1, width = 3, font = 'Arial', relief = tkinter.RAISED )
		self.autofocus_laser_set_button['text'] = 'Set'
		self.autofocus_laser_set_button['command'] = lambda string = None: self.autofocus_laser_entry_command(string)
		self.autofocus_laser_set_button.grid( row = 7, column = 12, rowspan = 1, columnspan = 2 )
		
		# information panel
		text = 'None'
		self.control_frame_information_label = tkinter.Label( self.control_frame, text = text, font = 'Consolas', height = 8, width = 23, relief = tkinter.GROOVE, borderwidth = 6, anchor = tkinter.W)
		self.control_frame_information_label.grid( row = 4, column = 0, rowspan = 4, columnspan = 6 )
	
	def create_status_frame(self):
		# capture
		
		self.acquisition_capture_button = tkinter.Button( self.status_frame, height = 1, width = 6, font = 'Arial', relief = tkinter.RAISED )
		self.acquisition_capture_button['text'] = 'Capture'
		self.acquisition_capture_button['command'] = self.acquisition_capture_command
		self.acquisition_capture_button.grid( row = 0, column = 4, rowspan = 1, columnspan = 2 )
		
		self.acquisition_live_button = tkinter.Button( self.status_frame, height = 1, width = 6, font = 'Arial', relief = tkinter.RAISED )
		self.acquisition_live_button['text'] = 'Live'
		self.acquisition_live_button['command'] = self.acquisition_live_command
		self.acquisition_live_button.grid( row = 0, column = 6, rowspan = 1, columnspan = 2 )
		
		self.acquisition_fast_timelapse_button = tkinter.Button( self.status_frame, height = 1, width = 6, font = 'Arial', relief = tkinter.RAISED )
		self.acquisition_fast_timelapse_button['text'] = 'T Lapse'
		self.acquisition_fast_timelapse_button['command'] = self.acquisition_fast_timelapse_command
		self.acquisition_fast_timelapse_button.grid( row = 0, column = 8, rowspan = 1, columnspan = 2 )
		
		self.acquisition_z_stack_button = tkinter.Button( self.status_frame, height = 1, width = 6, font = 'Arial', relief = tkinter.RAISED )
		self.acquisition_z_stack_button['text'] = 'Z Stack'
		self.acquisition_z_stack_button['command'] = self.acquisition_z_stack_command
		self.acquisition_z_stack_button.grid( row = 0, column = 10, rowspan = 1, columnspan = 2 )
		
		self.save_image_button = tkinter.Button( self.status_frame, height = 1, width = 6, font = 'Arial', relief = tkinter.RAISED )
		self.save_image_button['text'] = 'Save'
		self.save_image_button['command'] = self.save_image_button_command
		self.save_image_button.grid( row = 0, column = 12, rowspan = 1, columnspan = 2 )
		
		# exposure time
		self.exposure_label = tkinter.Label( self.status_frame, text = 'Time/ms', font = 'Consolas', height = 1, width = 7, relief = tkinter.GROOVE, borderwidth = 2 )
		self.exposure_label.grid( row = 1, column = 4, rowspan = 1, columnspan = 2 )
		
		self.exposure_entry = tkinter.Entry( self.status_frame, textvariable = tkinter.StringVar(self, value = 10), width = 7, borderwidth = 6 )
		self.exposure_entry.grid( row = 1, column = 6, rowspan = 1, columnspan = 2 )
		self.exposure_entry.bind('<Return>', self.exposure_entry_command)
		
		self.exposure_set_button = tkinter.Button( self.status_frame, height = 1, width = 3, font = 'Arial', relief = tkinter.RAISED )
		self.exposure_set_button['text'] = 'Set'
		self.exposure_set_button['command'] = lambda string = None: self.exposure_entry_command(string)
		self.exposure_set_button.grid( row = 1, column = 8, rowspan = 1, columnspan = 1 )
		
		# histogram
		self.status_frame_canvas = tkinter.Canvas( self.status_frame, bg = 'white', width = 265, height = 128 )
		self.status_frame_canvas.grid( row = 2, column = 4, rowspan = 4, columnspan = 7 )
		self.image_histogram = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/no_histogram.jpg') )
		self.status_frame_histogram = self.status_frame_canvas.create_image( 5, 0, image = self.image_histogram, anchor = tkinter.NW )
		self.image_histogram_redline = self.status_frame_canvas.create_line( 5, 0, 5, 127, fill = 'red', width = 3 )
		self.image_histogram_blueline = self.status_frame_canvas.create_line( 260, 0, 260, 127, fill = 'blue', width = 3 )
		# it seems that canvas widget is easier than panel widget
		# self.image_histogram_ranged = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/no_histogram.jpg') )
		# self.status_frame_panel = tkinter.Label(self.status_frame, image = self.image_histogram_ranged)
		# self.status_frame_panel.grid( row = 1, column = 1, rowspan = 4, columnspan = 2 )
		# self.status_frame_panel.image = self.image_histogram_ranged # keep a reference!
		self.status_frame_canvas.bind('<Motion>', self.status_frame_motion)
		self.status_frame_canvas.bind('<ButtonPress-1>', self.status_frame_click_drag_release)
		self.status_frame_canvas.bind('<B1-Motion>', self.status_frame_click_drag_release)
		self.status_frame_canvas.bind('<ButtonRelease-1>', self.status_frame_click_drag_release)
		
		# dynamic range
		self.dynamic_range_label = tkinter.Label( self.status_frame, text = 'Dynamic\nRange', font = 'Consolas', height = 2, width = 11, relief = tkinter.GROOVE, borderwidth = 2 )
		self.dynamic_range_label.grid( row = 1, column = 11, rowspan = 2, columnspan = 3 )
		
		self.dynamic_range_entry = [0, 0]
		dynamic_range = [100, 65535]
		for i in range(2):
			self.dynamic_range_entry[i] = tkinter.Entry( self.status_frame, textvariable = tkinter.StringVar(self, value = dynamic_range[i]), width = 7, borderwidth = 6 )
			self.dynamic_range_entry[i].grid( row = 3 + i, column = 11, rowspan = 1, columnspan = 3 )
			self.dynamic_range_entry[i].bind('<Return>', lambda string = None, index = i: self.dynamic_range_entry_command(string, index))
		
		self.dynamic_range_set_button = tkinter.Button( self.status_frame, height = 1, width = 3, font = 'Arial', relief = tkinter.RAISED )
		self.dynamic_range_set_button['text'] = 'Set'
		self.dynamic_range_set_button['command'] = lambda string = None, index = 2: self.dynamic_range_entry_command(string, index)
		self.dynamic_range_set_button.grid( row = 5, column = 11, rowspan = 1, columnspan = 3 )
		
		# preview setting
		self.roi_set_button = tkinter.Button( self.status_frame, height = 1, width = 6, font = 'Arial', relief = tkinter.RAISED )
		self.roi_set_button['text'] = 'ROI'
		self.roi_set_button['command'] = self.roi_set_button_command
		self.roi_set_button.grid( row = 6, column = 4, rowspan = 1, columnspan = 2 )
		
		self.full_image_button = tkinter.Button( self.status_frame, height = 1, width = 6, font = 'Arial', relief = tkinter.RAISED )
		self.full_image_button['text'] = 'Full'
		self.full_image_button['command'] = self.full_image_button_command
		self.full_image_button.grid( row = 6, column = 6, rowspan = 1, columnspan = 2 )
		
		self.image_color_button = tkinter.Menubutton( self.status_frame, height = 1, width = 6, font = 'Arial', relief = tkinter.RAISED )
		self.image_color_button['text'] = 'Color'
		self.image_color_button.grid( row = 6, column = 8, rowspan = 1, columnspan = 2 )
		
		self.image_color_menu = tkinter.Menu( self.image_color_button, tearoff = 0 )
		self.image_color_button['menu'] = self.image_color_menu
		self.image_color_menu.add_command( label = 'gray', command = lambda color = [255, 255, 255]: self.image_color_command(color) )
		self.image_color_menu.add_command( label = 'red', command = lambda color = [255, 0, 0]: self.image_color_command(color) )
		self.image_color_menu.add_command( label = 'blue', command = lambda color = [0, 0, 255]: self.image_color_command(color) )
		self.image_color_menu.add_command( label = 'green', command = lambda color = [0, 255, 0]: self.image_color_command(color) )
		self.image_color_menu.add_command( label = 'yellow', command = lambda color = [255, 255, 0]: self.image_color_command(color) )
		self.image_color_menu.add_command( label = 'orange', command = lambda color = [255, 127, 0]: self.image_color_command(color) )
		
		# information panel
		
		text = 'None'
		self.status_frame_information_label = tkinter.Label( self.status_frame, text = text, font = 'Consolas', height = 17, width = 15, relief = tkinter.GROOVE, borderwidth = 2, anchor = tkinter.W )
		self.status_frame_information_label.grid( row = 0, column = 0, rowspan = 8, columnspan = 4 )
	
	def create_motion_frame(self):
		# ASI stage for x-y
		self.stage_logo_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Logo_ASI.png') )
		self.stage_logo_label = tkinter.Label( self.motion_frame, image = self.stage_logo_image, height = 64, width = 64 )
		self.stage_logo_label.grid( row = 0, column = 0, rowspan = 2, columnspan = 2 )
		
		self.stage_popup_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.stage_popup_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/popup.png') )
		self.stage_popup_button['image'] = self.stage_popup_image
		self.stage_popup_button['command'] = self.stage_popup_button_command
		self.stage_popup_button.grid( row = 2, column = 2, rowspan = 1, columnspan = 1 )
		
		self.stage_left_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.stage_left_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Left.png') )
		self.stage_left_button['image'] = self.stage_left_image
		self.stage_left_button['command'] = lambda index_x = 1, index_y = 0: self.stage_relative_command(index_x, index_y)
		self.stage_left_button.grid( row = 2, column = 1, rowspan = 1, columnspan = 1 )
		
		self.stage_right_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.stage_right_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Right.png') )
		self.stage_right_button['image'] = self.stage_right_image
		self.stage_right_button['command'] = lambda index_x = -1, index_y = 0: self.stage_relative_command(index_x, index_y)
		self.stage_right_button.grid( row = 2, column = 3, rowspan = 1, columnspan = 1 )
		
		self.stage_forward_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.stage_forward_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Down.png') )
		self.stage_forward_button['image'] = self.stage_forward_image
		self.stage_forward_button['command'] = lambda index_x = 0, index_y = 1: self.stage_relative_command(index_x, index_y)
		self.stage_forward_button.grid( row = 3, column = 2, rowspan = 1, columnspan = 1 )
		
		self.stage_backward_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.stage_backward_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Up.png') )
		self.stage_backward_button['image'] = self.stage_backward_image
		self.stage_backward_button['command'] = lambda index_x = 0, index_y = -1: self.stage_relative_command(index_x, index_y)
		self.stage_backward_button.grid( row = 1, column = 2, rowspan = 1, columnspan = 1 )
		
		self.stage_left_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.stage_left_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Left_ultra.png') )
		self.stage_left_ultra_button['image'] = self.stage_left_ultra_image
		self.stage_left_ultra_button['command'] = lambda index_x = 10, index_y = 0: self.stage_relative_command(index_x, index_y)
		self.stage_left_ultra_button.grid( row = 2, column = 0, rowspan = 1, columnspan = 1 )
		
		self.stage_right_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.stage_right_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Right_ultra.png') )
		self.stage_right_ultra_button['image'] = self.stage_right_ultra_image
		self.stage_right_ultra_button['command'] = lambda index_x = -10, index_y = 0: self.stage_relative_command(index_x, index_y)
		self.stage_right_ultra_button.grid( row = 2, column = 4, rowspan = 1, columnspan = 1 )
		
		self.stage_forward_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.stage_forward_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Down_ultra.png') )
		self.stage_forward_ultra_button['image'] = self.stage_forward_ultra_image
		self.stage_forward_ultra_button['command'] = lambda index_x = 0, index_y = 10: self.stage_relative_command(index_x, index_y)
		self.stage_forward_ultra_button.grid( row = 4, column = 2, rowspan = 1, columnspan = 1 )
		
		self.stage_backward_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.stage_backward_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Up_ultra.png') )
		self.stage_backward_ultra_button['image'] = self.stage_backward_ultra_image
		self.stage_backward_ultra_button['command'] = lambda index_x = 0, index_y = -10: self.stage_relative_command(index_x, index_y)
		self.stage_backward_ultra_button.grid( row = 0, column = 2, rowspan = 1, columnspan = 1 )
		
		self.stage_x_targeted_label = tkinter.Label( self.motion_frame, text = 'X➢', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.stage_x_targeted_label.grid( row = 0, column = 3, rowspan = 1, columnspan = 1, sticky = tkinter.E)
		
		self.stage_x_targeted_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = 0), width = 7, borderwidth = 6 )
		self.stage_x_targeted_entry.grid( row = 0, column = 4, rowspan = 1, columnspan = 2, sticky = tkinter.W )
		self.stage_x_targeted_entry.bind('<Return>', self.stage_targeted_button_command)
		
		self.stage_y_targeted_label = tkinter.Label( self.motion_frame, text = 'Y➢', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.stage_y_targeted_label.grid( row = 1, column = 3, rowspan = 1, columnspan = 1, sticky = tkinter.E)
		
		self.stage_y_targeted_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = 0), width = 7, borderwidth = 6 )
		self.stage_y_targeted_entry.grid( row = 1, column = 4, rowspan = 1, columnspan = 2, sticky = tkinter.W )
		self.stage_y_targeted_entry.bind('<Return>', self.stage_targeted_button_command)
		
		self.stage_home_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.stage_home_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Home.png') )
		self.stage_home_button['image'] = self.stage_home_image
		self.stage_home_button['command'] = self.stage_targeted_home_command
		self.stage_home_button.grid( row = 4, column = 4, rowspan = 1, columnspan = 1 )
		
		self.stage_targeted_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.stage_targeted_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Move.png') )
		self.stage_targeted_button['image'] = self.stage_targeted_image
		self.stage_targeted_button['command'] = self.stage_targeted_button_command
		self.stage_targeted_button.grid( row = 3, column = 4, rowspan = 1, columnspan = 1 )
		
		self.stage_relative_label = tkinter.Label( self.motion_frame, text = '▶=', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.stage_relative_label.grid( row = 3, column = 0, rowspan = 1, columnspan = 1)
		
		self.stage_relative_button = tkinter.Button( self.motion_frame, height = 1, width = 3, font = 'Arial', relief = tkinter.RAISED )
		self.stage_relative_button['text'] = 'Set'
		self.stage_relative_button['command'] = lambda string = None: self.stage_relative_entry_command(string)
		self.stage_relative_button.grid( row = 3, column = 1, rowspan = 1, columnspan = 1)
		
		self.stage_relative_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = 0.01), width = 7, borderwidth = 6 )
		self.stage_relative_entry.grid( row = 4, column = 0, rowspan = 1, columnspan = 2)
		self.stage_relative_entry.bind('<Return>', self.stage_relative_entry_command)
		
		# Step motor for z
		self.piezo_motor_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Logo_motor.png') )
		self.piezo_motor_label = tkinter.Label( self.motion_frame, image = self.piezo_motor_image, height = 96, width = 32)
		self.piezo_motor_label.grid( row = 0, column = 6, rowspan = 3, columnspan = 1 )
		
		self.motor_up_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.motor_up_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Up.png') )
		self.motor_up_button['image'] = self.motor_up_image
		self.motor_up_button['command'] = lambda index = 1: self.motor_relative_command(index)
		self.motor_up_button.grid( row = 1, column = 7, rowspan = 1, columnspan = 1 )
		
		self.motor_down_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.motor_down_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Down.png') )
		self.motor_down_button['image'] = self.motor_down_image
		self.motor_down_button['command'] = lambda index = -1: self.motor_relative_command(index)
		self.motor_down_button.grid( row = 2, column = 7, rowspan = 1, columnspan = 1 )
		
		self.motor_up_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.motor_up_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Up_ultra.png') )
		self.motor_up_ultra_button['image'] = self.motor_up_ultra_image
		self.motor_up_ultra_button['command'] = lambda index = 10: self.motor_relative_command(index)
		self.motor_up_ultra_button.grid( row = 0, column = 7, rowspan = 1, columnspan = 1 )
		
		self.motor_down_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32 )
		self.motor_down_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Down_ultra.png') )
		self.motor_down_ultra_button['image'] = self.motor_down_ultra_image
		self.motor_down_ultra_button['command'] = lambda index = -10: self.motor_relative_command(index)
		self.motor_down_ultra_button.grid( row = 3, column = 7, rowspan = 1, columnspan = 1 )
		
		self.motor_targeted_label = tkinter.Label( self.motion_frame, text = 'Motor➢', font = 'Consolas', height = 1, width = 6, relief = tkinter.GROOVE, borderwidth = 2 )
		self.motor_targeted_label.grid( row = 0, column = 8, rowspan = 1, columnspan = 2 )
		
		self.motor_targeted_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = 0), width = 7, borderwidth = 6 )
		self.motor_targeted_entry.grid( row = 1, column = 8, rowspan = 1, columnspan = 2 )
		self.motor_targeted_entry.bind('<Return>', self.motor_targeted_entry_command)
		
		self.motor_home_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.motor_home_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Home.png') )
		self.motor_home_button['image'] = self.motor_home_image
		self.motor_home_button['command'] = self.motor_targeted_home_command
		self.motor_home_button.grid( row = 2, column = 9, rowspan = 1, columnspan = 1 )
		
		self.motor_targeted_button = tkinter.Button( self.motion_frame, height = 32, width = 32, font = 'Arial', relief = tkinter.RAISED )
		self.motor_targeted_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Move.png') )
		self.motor_targeted_button['image'] = self.motor_targeted_image
		self.motor_targeted_button['command'] = lambda string = None: self.motor_targeted_entry_command(string)
		self.motor_targeted_button.grid( row = 2, column = 8, rowspan = 1, columnspan = 1 )
		
		self.motor_relative_label = tkinter.Label( self.motion_frame, text = '▲=', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.motor_relative_label.grid( row = 3, column = 8, rowspan = 1, columnspan = 1, sticky = tkinter.E)
		
		self.motor_relative_button = tkinter.Button( self.motion_frame, height = 1, width = 3, font = 'Arial', relief = tkinter.RAISED )
		self.motor_relative_button['text'] = 'Set'
		self.motor_relative_button['command'] = lambda string = None: self.motor_relative_entry_command(string)
		self.motor_relative_button.grid( row = 3, column = 9, rowspan = 1, columnspan = 1 )
		
		self.motor_relative_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = 0.1), width = 7, borderwidth = 6 )
		self.motor_relative_entry.grid( row = 4, column = 8, rowspan = 1, columnspan = 2 )
		self.motor_relative_entry.bind('<Return>', self.motor_relative_entry_command)
		
		# Physik Instrumente piezo for micro-z
		self.piezo_logo_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Logo_PI.jpg') )
		self.piezo_logo_label = tkinter.Label( self.motion_frame, image = self.piezo_logo_image, height = 96, width = 32)
		self.piezo_logo_label.grid( row = 0, column = 10, rowspan = 3, columnspan = 1 )
		
		self.piezo_up_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.piezo_up_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Up.png') )
		self.piezo_up_button['image'] = self.piezo_up_image
		self.piezo_up_button['command'] = lambda index = 1: self.piezo_relative_command(index)
		self.piezo_up_button.grid( row = 1, column = 11, rowspan = 1, columnspan = 1 )
		
		self.piezo_down_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.piezo_down_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Down.png') )
		self.piezo_down_button['image'] = self.piezo_down_image
		self.piezo_down_button['command'] = lambda index = -1: self.piezo_relative_command(index)
		self.piezo_down_button.grid( row = 2, column = 11, rowspan = 1, columnspan = 1 )
		
		self.piezo_up_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.piezo_up_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Up_ultra.png') )
		self.piezo_up_ultra_button['image'] = self.piezo_up_ultra_image
		self.piezo_up_ultra_button['command'] = lambda index = 10: self.piezo_relative_command(index)
		self.piezo_up_ultra_button.grid( row = 0, column = 11, rowspan = 1, columnspan = 1 )
		
		self.piezo_down_ultra_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.piezo_down_ultra_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Down_ultra.png') )
		self.piezo_down_ultra_button['image'] = self.piezo_down_ultra_image
		self.piezo_down_ultra_button['command'] = lambda index = -10: self.piezo_relative_command(index)
		self.piezo_down_ultra_button.grid( row = 3, column = 11, rowspan = 1, columnspan = 1 )
		
		self.piezo_targeted_label = tkinter.Label( self.motion_frame, text = 'Piezo➢', font = 'Consolas', height = 1, width = 6, relief = tkinter.GROOVE, borderwidth = 2 )
		self.piezo_targeted_label.grid( row = 0, column = 12, rowspan = 1, columnspan = 2 )
		
		self.piezo_targeted_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = 0), width = 7, borderwidth = 6 )
		self.piezo_targeted_entry.grid( row = 1, column = 12, rowspan = 1, columnspan = 2 )
		self.piezo_targeted_entry.bind('<Return>', self.piezo_targeted_entry_command)
		
		self.piezo_home_button = tkinter.Button( self.motion_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.piezo_home_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Home.png') )
		self.piezo_home_button['image'] = self.piezo_home_image
		self.piezo_home_button['command'] = self.piezo_targeted_home_command
		self.piezo_home_button.grid( row = 2, column = 13, rowspan = 1, columnspan = 1 )
		
		self.piezo_targeted_button = tkinter.Button( self.motion_frame, height = 32, width = 32, font = 'Arial', relief = tkinter.RAISED )
		self.piezo_targeted_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Move.png') )
		self.piezo_targeted_button['image'] = self.piezo_targeted_image
		self.piezo_targeted_button['command'] = lambda string = None: self.piezo_targeted_entry_command(string)
		self.piezo_targeted_button.grid( row = 2, column = 12, rowspan = 1, columnspan = 1 )
		
		self.piezo_relative_label = tkinter.Label( self.motion_frame, text = '▲=', font = 'Consolas', height = 1, width = 3, relief = tkinter.GROOVE, borderwidth = 2 )
		self.piezo_relative_label.grid( row = 3, column = 12, sticky = tkinter.E)
		
		self.piezo_relative_button = tkinter.Button( self.motion_frame, height = 1, width = 3, font = 'Arial', relief = tkinter.RAISED )
		self.piezo_relative_button['text'] = 'Set'
		self.piezo_relative_button['command'] = lambda string = None: self.piezo_relative_entry_command(string)
		self.piezo_relative_button.grid( row = 3, column = 13, rowspan = 1, columnspan = 1 )
		
		self.piezo_relative_entry = tkinter.Entry( self.motion_frame, textvariable = tkinter.StringVar(self, value = 1), width = 7, borderwidth = 6 )
		self.piezo_relative_entry.grid( row = 4, column = 12, rowspan = 1, columnspan = 2 )
		self.piezo_relative_entry.bind('<Return>', self.piezo_relative_entry_command)
		
		# information panel
		text = 'None'
		self.motion_frame_information_label = tkinter.Label( self.motion_frame, text = text, font = 'Consolas', height = 3, width = 55, relief = tkinter.GROOVE, borderwidth = 6, anchor = tkinter.W)
		self.motion_frame_information_label.grid( row = 5, column = 0, rowspan = 3, columnspan = 14 )
	
	def create_image_frame(self):
		self.image_frame_canvas = tkinter.Canvas( self.image_frame, bg = 'white', width = 1024, height = 1024)
		self.image_frame_canvas.grid( row = 0, column = 0, rowspan = 1, columnspan = 1 )
		self.image_exhibition = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/no_image.jpg') )
		self.image_frame_image = self.image_frame_canvas.create_image( 512, 512, image = self.image_exhibition, anchor = tkinter.CENTER )
		self.image_frame_rect = self.image_frame_canvas.create_rectangle( 0, 0, 2047, 2047, width = 0.0 )
		self.image_frame_canvas.bind('<Motion>', self.image_frame_motion)
		self.image_frame_canvas.bind('<ButtonPress-1>', self.image_frame_click)
		self.image_frame_canvas.bind('<B1-Motion>', self.image_frame_drag)
		self.image_frame_canvas.bind('<ButtonRelease-1>', self.image_frame_release)
	
	# Control frame widgets commands
	
	def pinhole_command(self, label):
		self.master.title( 'Nymphscope moving pinholes...' )
		self.nymphscope.pinhole_reselect(label)
		time.sleep(1)
		self.master.title( 'Nymphscope main application' )
	
	def filter_command(self, label):
		self.master.title( 'Nymphscope turning filters...' )
		self.nymphscope.filter_reselect(label)
		time.sleep(1)
		self.master.title( 'Nymphscope main application' )
	
	def confocal_mark_button_command(self):
		print(0)
	
	def confocal_mark_entry_command(self, string):
		print(0)
	
	def photoactive_mark_button_command(self):
		print(0)
	
	def photoactive_mark_entry_command(self, string):
		print(0)
	
	def confocal_laser_button_command(self, index):
		laser_on = self.nymphscope.laser_on
		if bool(laser_on[index]):
			self.confocal_laser_button[index].config( bg = 'white', relief = tkinter.RAISED )
		else:
			self.confocal_laser_button[index].config( bg = 'red', relief = tkinter.SUNKEN )
		laser_on[index] = 1 - laser_on[index]
		self.nymphscope.laser_on_reset(laser_on)
	
	def confocal_laser_entry_command(self, string, index):
		laser_power = self.nymphscope.laser_power
		try:
			laser_power[index] = int( self.confocal_laser_entry[index].get() )
		except ValueError:
			print('not a valid number')
		else:
			self.nymphscope.laser_power_reset( laser_power )
	
	def photoactive_laser_button_command(self, index):
		photoactive_shutter = self.nymphscope.photoactive_shutter
		if bool(photoactive_shutter[index]):
			self.photoactive_laser_button[index].config( bg = 'white', relief = tkinter.RAISED )
		else:
			self.photoactive_laser_button[index].config( bg = 'red', relief = tkinter.SUNKEN )
		photoactive_shutter[index] = 1 - photoactive_shutter[index]
		self.nymphscope.photoactive_shutter_reset(photoactive_shutter[index], index)
	
	def autofocus_laser_entry_command(self, string):
		autofocus_laser_power = self.nymphscope.autofocus_laser_power
		try:
			autofocus_laser_power = int( self.autofocus_laser_entry.get() )
		except ValueError:
			print('not a valid number')
		else:
			self.nymphscope.autofocus_laser_power_reset(autofocus_laser_power)
	
	# Status frame widgets commands
	
	def acquisition_capture_command(self):
		self.nymphscope.take_signal()
	
	def acquisition_live_command(self):
		if self.nymphscope.living_flag:
			self.acquisition_capture_button['state'] = tkinter.NORMAL
			self.acquisition_fast_timelapse_button['state'] = tkinter.NORMAL
			self.acquisition_z_stack_button['state'] = tkinter.NORMAL
			self.nymphscope.live_stop()
			self.acquisition_live_button.config( bg = 'white', relief = tkinter.RAISED )
			self.nymphscope.living_flag = False
		else:
			self.acquisition_capture_button['state'] = tkinter.DISABLED
			self.acquisition_fast_timelapse_button['state'] = tkinter.DISABLED
			self.acquisition_z_stack_button['state'] = tkinter.DISABLED
			self.nymphscope.live_signal()
			self.acquisition_live_button.config( bg = 'red', relief = tkinter.SUNKEN )
			self.nymphscope.living_flag = True
	
	def acquisition_fast_timelapse_command(self):
		self.fast_timelapse_popup = tkinter.Toplevel(height = 134, width = 248) # it seems that the master is not important and the popup could be properly closed, but I'm not very sure
		self.fast_timelapse_popup.attributes('-topmost', 'true')
		self.fast_timelapse_popup.title('Fast Timelapse')
		self.fast_timelapse_popup.protocol( 'WM_DELETE_WINDOW', self.fast_timelapse_popup.destroy )
		
		self.fast_timelapse_popup_frame = tkinter.Frame( self.fast_timelapse_popup, width = 248, height = 134, borderwidth = 10, relief = tkinter.GROOVE)
		self.fast_timelapse_popup_frame.grid( row = 0, column = 0, rowspan = 1, columnspan = 1 )
		self.fast_timelapse_popup_frame.grid_propagate(0) # disable changing the size
		for i in range(3):
			self.fast_timelapse_popup_frame.grid_rowconfigure( index = i, minsize = 38)
		for i in range(6):
			self.fast_timelapse_popup_frame.grid_columnconfigure( index = i, minsize = 38)
		
		self.fast_timelapse_popup_label = tkinter.Label( self.fast_timelapse_popup_frame, text = 'Fast Timelapse Setup', font = 'Consolas', height = 1, width = 24, relief = tkinter.GROOVE, borderwidth = 2 )
		self.fast_timelapse_popup_label.grid( row = 0, column = 0, rowspan = 1, columnspan = 6 )
		
		self.fast_timelapse_frames_label = tkinter.Label( self.fast_timelapse_popup_frame, text = 'Total Frames', font = 'Consolas', height = 1, width = 12, relief = tkinter.GROOVE, borderwidth = 2 )
		self.fast_timelapse_frames_label.grid( row = 1, column = 0, rowspan = 1, columnspan = 4 )
		
		self.fast_timelapse_frames_entry = tkinter.Entry( self.fast_timelapse_popup_frame, textvariable = tkinter.StringVar(self, value = 10), width = 7, borderwidth = 6 )
		self.fast_timelapse_frames_entry.grid( row = 1, column = 4, rowspan = 1, columnspan = 2 )
		
		self.acquisition_fast_timelapse_button = tkinter.Button( self.fast_timelapse_popup_frame, height = 1, width = 18, font = 'Arial', relief = tkinter.RAISED )
		self.acquisition_fast_timelapse_button['text'] = 'Capture and Save'
		self.acquisition_fast_timelapse_button['command'] = self.acquisition_fast_timelapse_start
		self.acquisition_fast_timelapse_button.grid( row = 2, column = 0, rowspan = 1, columnspan = 6 )
	
	def acquisition_fast_timelapse_start(self):
		try:
			frames = int( self.fast_timelapse_frames_entry.get() )
		except ValueError:
			print('not a valid number')
		else:
			frames = max(1, frames)
		savepath = tkinter.filedialog.askdirectory(initialdir = self.nymphscope.savepath)
		self.fast_timelapse_popup.destroy()
		
		information_message = 'Fast Timelapse Capturing and Saving ...'
		self.master.title(information_message)
		self.nymphscope.fast_timelapse(frames, savepath)
		
		information_message = 'Fast Timelapse Finishing ...'
		self.master.title(information_message)
		time.sleep(1)
		
		information_message = 'Nymphscope main application'
		self.master.title(information_message)
	
	def acquisition_z_stack_command(self):
		stack_file_name = tkinter.filedialog.askopenfilenames( initialdir = './', defaultextension = 'text', title = 'Select z stack file', filetypes = (('text files', '*.txt'), ('all files', '*.*')) )[0]
		stack = numpy.zeros(80, dtype = numpy.float) - 1
		stack_file = open(stack_file_name, 'r', encoding='utf-8')
		line_number = 0
		for line in stack_file:
			try:
				stack[line_number] = float(line)
			except ValueError:
				print('not a valid number')
			else:
				stack[line_number] = min( max(0.0, stack[line_number]), 399.99)
				line_number += 1
		stack = stack[stack != -1]
		
		self.z_stack_popup = tkinter.Toplevel(height = 134, width = 248) # it seems that the master is not important and the popup could be properly closed, but I'm not very sure
		self.z_stack_popup.attributes('-topmost', 'true')
		self.z_stack_popup.title('Fast Z Stack')
		self.z_stack_popup.protocol( 'WM_DELETE_WINDOW', self.z_stack_popup.destroy )
		
		self.z_stack_popup_frame = tkinter.Frame( self.z_stack_popup, width = 248, height = 400, borderwidth = 10, relief = tkinter.GROOVE)
		self.z_stack_popup_frame.grid( row = 0, column = 0, rowspan = 1, columnspan = 1 )
		self.z_stack_popup_frame.grid_propagate(0) # disable changing the size
		for i in range(10):
			self.z_stack_popup_frame.grid_rowconfigure( index = i, minsize = 38)
		for i in range(6):
			self.z_stack_popup_frame.grid_columnconfigure( index = i, minsize = 38)
		
		self.z_stack_popup_label = tkinter.Label( self.z_stack_popup_frame, text = 'Fast Timelapse Setup', font = 'Consolas', height = 1, width = 24, relief = tkinter.GROOVE, borderwidth = 2 )
		self.z_stack_popup_label.grid( row = 0, column = 0, rowspan = 1, columnspan = 6 )
		
		self.z_stack_information_frame = tkinter.Frame( self.z_stack_popup_frame, width = 228, height = 304, borderwidth = 0)
		self.z_stack_information_frame.grid( row = 1, column = 0, rowspan = 8, columnspan = 6 )
		
		self.z_stack_information_label = tkinter.Label( self.z_stack_information_frame, text = 'number\tposition(um)', font = 'Consolas', height = 1, width = 24, relief = tkinter.GROOVE, borderwidth = 2 )
		self.z_stack_information_label.pack( side = tkinter.TOP, fill = tkinter.X )
		
		self.z_stack_information_scrollbar = tkinter.Scrollbar( self.z_stack_information_frame )
		self.z_stack_information_scrollbar.pack( side = tkinter.RIGHT, fill = tkinter.Y )
		
		self.z_stack_information_listbox = tkinter.Listbox( self.z_stack_information_frame, font = 'Consolas', borderwidth = 2, yscrollcommand = self.z_stack_information_scrollbar.set )
		for i in range(line_number):
			self.z_stack_information_listbox.insert( tkinter.END, f'  {i+1:3d}      {stack[i]:7.3f}' )
		self.z_stack_information_listbox.pack( side = tkinter.LEFT, fill = tkinter.BOTH )
		self.z_stack_information_scrollbar.config( command = self.z_stack_information_listbox.yview )
		
		self.acquisition_z_stack_button = tkinter.Button( self.z_stack_popup_frame, height = 1, width = 18, font = 'Arial', relief = tkinter.RAISED )
		self.acquisition_z_stack_button['text'] = 'Capture and Save'
		self.acquisition_z_stack_button['command'] = lambda z_stack = stack: self.acquisition_z_stack_start(z_stack)
		self.acquisition_z_stack_button.grid( row = 9, column = 0, rowspan = 1, columnspan = 6 )
	
	def acquisition_z_stack_start(self, z_stack):
		savepath = tkinter.filedialog.askdirectory(initialdir = self.nymphscope.savepath)
		self.z_stack_popup.destroy()
		
		information_message = 'Fast Z Stack Preparing ... This would take minutes.'
		self.master.title(information_message)
		frames = self.nymphscope.fast_z_stack_prepare(z_stack, savepath)
		
		information_message = 'Fast Z Stack Capturing and Saving ...'
		self.master.title(information_message)
		self.nymphscope.fast_z_stack(frames)
		
		information_message = 'Fast Z Stack Finishing ...'
		self.master.title(information_message)
		time.sleep(1)
		
		information_message = 'Nymphscope main application'
		self.master.title(information_message)
	
	def save_image_button_command(self):
		# savepath = tkinter.filedialog.asksaveasfilename( initialdir = self.nymphscope.savepath, defaultextension = 'tiff', title = 'Select file', filetypes = (('tiff files', '*.tiff'), ('all files', '*.*')) )
		savepath = tkinter.filedialog.askdirectory(initialdir = self.nymphscope.savepath)
		self.nymphscope.save_image(savepath)
	
	def exposure_entry_command(self, value):
		exposure_time = self.nymphscope.exposure_time
		try:
			exposure_time = int( self.exposure_entry.get() )
		except ValueError:
			print('not a valid number')
		else:
			self.nymphscope.exposure_time_reset(exposure_time)
	
	def roi_set_button_command(self):
		if self.roi_set_flag:
			self.roi_set_button.config( bg = 'white', relief = tkinter.RAISED )
			self.roi_set_flag = False
		else:
			self.roi_set_button.config( bg = 'red', relief = tkinter.SUNKEN )
			self.roi_set_flag = True
	
	def full_image_button_command(self):
		self.nymphscope.roi_reset()
	
	def image_color_command(self, color):
		self.nymphscope.image_color_reset(color)
	
	def status_frame_motion(self, coordinate):
		dynamic_range = [self.nymphscope.dynamic_range['low'], self.nymphscope.dynamic_range['high']]
		red_line = int( (numpy.log10(dynamic_range[0]) - 2.0) * 90.893 ) + 5
		blue_line = int( (numpy.log10(dynamic_range[1]) - 2.0) * 90.893 ) + 5
		if coordinate.x > red_line - 5 and coordinate.x < red_line + 5:
			self.dynamic_range_select_flag = [True, False]
			self.status_frame_canvas['cursor'] = 'sb_h_double_arrow'
		elif coordinate.x > blue_line - 5 and coordinate.x < blue_line + 5:
			self.dynamic_range_select_flag = [False, True]
			self.status_frame_canvas['cursor'] = 'sb_h_double_arrow'
		else:
			self.dynamic_range_select_flag = [False, False]
			self.status_frame_canvas['cursor'] = 'arrow'
	
	def status_frame_click_drag_release(self, coordinate):
		coordinate.x = max(6, min(coordinate.x, 261))
		dynamic_range = [self.nymphscope.dynamic_range['low'], self.nymphscope.dynamic_range['high']]
		if self.dynamic_range_select_flag[0]:
			dynamic_range[0] = int( numpy.power(10.0, (coordinate.x -5.0) / 90.893 + 2.0) )
			self.status_frame_canvas.coords( self.image_histogram_redline, coordinate.x, 0, coordinate.x, 127 )
			self.dynamic_range_entry[0]['textvariable'] = tkinter.StringVar(self, value = dynamic_range[0])
		elif self.dynamic_range_select_flag[1]:
			dynamic_range[1] = int( numpy.power(10.0, (coordinate.x -5.0) / 90.893 + 2.0) )
			self.status_frame_canvas.coords( self.image_histogram_blueline, coordinate.x, 0, coordinate.x, 127 )
			self.dynamic_range_entry[1]['textvariable'] = tkinter.StringVar(self, value = dynamic_range[1])
		self.nymphscope.dynamic_range_resize(dynamic_range)
	
	def dynamic_range_entry_command(self, string, index):
		dynamic_range = [self.nymphscope.dynamic_range['low'], self.nymphscope.dynamic_range['high']]
		try:
			if index == 0:
				dynamic_range[0] = int( self.dynamic_range_entry[0].get() )
			elif index == 1:
				dynamic_range[1] = int( self.dynamic_range_entry[1].get() )
			elif index == 2:
				dynamic_range[0] = int( self.dynamic_range_entry[0].get() )
				dynamic_range[1] = int( self.dynamic_range_entry[1].get() )
		except ValueError:
			print('not a valid number')
		else:
			self.nymphscope.dynamic_range_resize(dynamic_range)
			dynamic_range = [self.nymphscope.dynamic_range['low'], self.nymphscope.dynamic_range['high']]
			x = (numpy.int16( (numpy.log10(dynamic_range) - 2.0) * 90.893) + 5).tolist()
			self.status_frame_canvas.coords( self.image_histogram_redline, x[0], 0, x[0], 127 )
			self.status_frame_canvas.coords( self.image_histogram_blueline, x[1], 0, x[1], 127 )
	
	# Motion frame widgets commands
	
	def stage_targeted_home_command(self):
		self.nymphscope.stage_xy_move(0, 0)
	
	def stage_relative_command(self, index_x, index_y):
		if index_x != 0:
			self.nymphscope.stage_x_move(index_x*self.nymphscope.stage_relative)
		if index_y != 0:
			self.nymphscope.stage_y_move(index_y*self.nymphscope.stage_relative)
	
	def stage_targeted_button_command(self, *args):
		try:
			stage_x_targeted = float( self.stage_x_targeted_entry.get() )
			stage_y_targeted = float( self.stage_y_targeted_entry.get() )
		except ValueError:
			print('not a valid number')
		else:
			self.nymphscope.stage_xy_move(stage_x_targeted, stage_y_targeted)
	
	def stage_relative_entry_command(self, string):
		try:
			stage_relative = float( self.stage_relative_entry.get() )
		except ValueError:
			print('not a valid number')
		else:
			self.nymphscope.stage_relative = max(0.0, min(stage_relative, 1.0))
	
	def motor_targeted_home_command(self):
		self.nymphscope.motor_move(0, 0)
	
	def motor_relative_command(self, index):
		self.nymphscope.motor_move(index*self.nymphscope.motor_relative, 1)
	
	def motor_targeted_entry_command(self, string):
		try:
			motor_targeted = float( self.motor_targeted_entry.get() )
		except ValueError:
			print('not a valid number')
		else:
			self.nymphscope.motor_move(motor_targeted, 0)
	
	def motor_relative_entry_command(self, string):
		try:
			motor_relative = float( self.motor_relative_entry.get() )
		except ValueError:
			print('not a valid number')
		else:
			self.nymphscope.motor_relative = max(0.0, min(motor_relative, 1.0))
	
	def piezo_targeted_home_command(self):
		self.nymphscope.piezo_move(0, 0)
	
	def piezo_relative_command(self, index):
		self.nymphscope.piezo_move(index*self.nymphscope.piezo_relative, 1)
	
	def piezo_targeted_entry_command(self, string):
		try:
			piezo_targeted = float( self.piezo_targeted_entry.get() )
		except ValueError:
			print('not a valid number')
		else:
			self.nymphscope.piezo_move(piezo_targeted, 0)
	
	def piezo_relative_entry_command(self, string):
		try:
			piezo_relative = float( self.piezo_relative_entry.get() )
		except ValueError:
			print('not a valid number')
		else:
			self.nymphscope.piezo_relative = max(0.0, min(piezo_relative, 10.0))
	
	# Image frame widgets commands
	
	def image_frame_motion(self, coordinate):
		self.nymphscope.pos_reset([coordinate.y, coordinate.x])
	
	def image_frame_click(self, coordinate):
		self.region_of_selected['x1'] = coordinate.x
		self.region_of_selected['y1'] = coordinate.y
		self.region_of_selected['x2'] = coordinate.x
		self.region_of_selected['y2'] = coordinate.y
		self.image_frame_canvas.itemconfig( self.image_frame_rect, dash = (4, 4), width = 5.0 )
		self.image_frame_canvas.coords( self.image_frame_rect, self.region_of_selected['x1'], self.region_of_selected['y1'], self.region_of_selected['x2'], self.region_of_selected['y2'] )
	
	def image_frame_drag(self, coordinate):
		self.region_of_selected['x2'] = coordinate.x
		self.region_of_selected['y2'] = coordinate.y
		self.image_frame_canvas.coords( self.image_frame_rect, self.region_of_selected['x1'], self.region_of_selected['y1'], self.region_of_selected['x2'], self.region_of_selected['y2'] )
	
	def image_frame_release(self, coordinate):
		self.region_of_selected['x2'] = coordinate.x
		self.region_of_selected['y2'] = coordinate.y
		self.image_frame_canvas.coords( self.image_frame_rect, self.region_of_selected['x1'], self.region_of_selected['y1'], self.region_of_selected['x2'], self.region_of_selected['y2'] )
		
		if self.roi_set_flag:
			# x <-> y, and set range
			self.region_of_selected = {'x1':self.region_of_selected['y1'], 'y1':self.region_of_selected['x1'], 'x2':self.region_of_selected['y2'], 'y2':self.region_of_selected['x2']}
			for i in ('x1', 'x2', 'y1', 'y2'):
				self.region_of_selected[i] = max(0, min(self.region_of_selected[i], 1027))
			self.nymphscope.roi_resize(self.region_of_selected)
		
		self.region_of_selected = {'x1':0, 'y1':0, 'x2':0, 'y2':0}
		self.image_frame_canvas.itemconfig(self.image_frame_rect, dash = (), width = 0.0 )
		self.image_frame_canvas.coords( 0, 0, 0, 0 )
	
	# Update All Canvases
	
	def control_frame_information_update(self):
		pinhole_label = self.nymphscope.pinhole_label
		filter_label = self.nymphscope.filter_label
		laser_on = self.nymphscope.laser_on
		state_dictionaty = {0:'Off', 1:'On '}
		laser_on_state = [state_dictionaty[laser_on[0]], state_dictionaty[laser_on[1]], state_dictionaty[laser_on[2]], state_dictionaty[laser_on[3]]]
		laser_power = self.nymphscope.laser_power
		text = f'Pinhole: {pinhole_label:10}   \nFilter: {filter_label:10}    \n  Laser Energy State \n405: {laser_power[0]:5d}   {laser_on_state[0]}\n488: {laser_power[1]:5d}   {laser_on_state[1]}\n561: {laser_power[2]:5d}   {laser_on_state[2]}\n640: {laser_power[3]:5d}   {laser_on_state[3]}'
		self.control_frame_information_label['text'] = text
	
	def status_frame_information_update(self):
		exposure_time = self.nymphscope.exposure_time
		pos = self.nymphscope.point_of_selected
		dynamic_range = [self.nymphscope.dynamic_range['low'], self.nymphscope.dynamic_range['high']]
		roi = [self.nymphscope.region_of_interest['x1'], self.nymphscope.region_of_interest['y1'], self.nymphscope.region_of_interest['x2'], self.nymphscope.region_of_interest['y2']]
		text = f'Exposure Time \n  (ms): {exposure_time:4d}  \n\n  Intensity:  \n ({pos[0]:4d}, {pos[1]:4d}) \n (A.U.) {pos[2]:5d} \n\n  ROI: (px.)  \nx:{roi[0]:4d} -> {roi[1]:4d}\ny:{roi[2]:4d} -> {roi[3]:4d}\n\nDynamic Range:\n{dynamic_range[0]:5d} -> {dynamic_range[1]:5d}\n'
		self.status_frame_information_label['text'] = text
	
	def motion_frame_information_update(self):
		stage_x_position = self.nymphscope.stage_x_current
		stage_y_position = self.nymphscope.stage_y_current
		motor_position = self.nymphscope.motor_current
		piezo_position = self.nymphscope.piezo_current
		stage_relative = self.nymphscope.stage_relative # mm
		motor_relative = self.nymphscope.motor_relative # mm
		piezo_relative = self.nymphscope.piezo_relative # μm
		if self.stage_popup_flag:
			self.stage_popup_frame_update(stage_x_position, stage_y_position)
		text = f'stage(mm):  X ={stage_x_position:8.3f},  Y ={stage_y_position:8.3f},  step ={stage_relative:6.3f} \nmotor(mm):     position ={motor_position:9.4f},     step ={motor_relative:7.4f}\npiezo(μm):     position ={piezo_position:9.4f},     step ={piezo_relative:7.4f}'
		self.motion_frame_information_label['text'] = text
	
	def image_histogram_update(self):
		image = self.nymphscope.image_exhibition
		self.image_exhibition = PIL.ImageTk.PhotoImage( PIL.Image.fromarray(image) )
		self.image_frame_canvas.itemconfig( self.image_frame_image, image = self.image_exhibition )
		histogram = self.nymphscope.image_histogram
		self.image_histogram = PIL.ImageTk.PhotoImage( PIL.Image.fromarray(histogram) )
		self.status_frame_canvas.itemconfig( self.status_frame_histogram, image = self.image_histogram )
	
	# Stage position popup modules
	
	def stage_popup_button_command(self):
		self.stage_popup_flag = True
		self.nymphscope.stage_x_chosen = 0.0
		self.nymphscope.stage_y_chosen = 0.0
		
		self.popup = tkinter.Toplevel(height = 1024, width = 1024) # it seems that the master is not important and the popup could be properly closed, but I'm not very sure
		self.popup.attributes('-topmost', 'true')
		self.popup.title('Stage Position')
		self.popup.protocol( 'WM_DELETE_WINDOW', self.stage_popup_exit )

		self.popup_frame = tkinter.Frame( self.popup, width = 820, height = 720, borderwidth = 10, relief = tkinter.GROOVE)
		self.popup_frame.grid( row = 0, column = 0, rowspan = 1, columnspan = 1 )
		self.popup_frame.grid_propagate(0) # disable changing the size
		for i in range(7):
			self.popup_frame.grid_rowconfigure( index = i, minsize = 100)
		for i in range(8):
			self.popup_frame.grid_columnconfigure( index = i, minsize = 100)
		
		self.popup_frame_canvas = tkinter.Canvas( self.popup_frame, bg = 'grey', width = 800, height = 600 )
		self.popup_frame_canvas.grid( row = 0, column = 0, rowspan = 6, columnspan = 8 )
		self.popup_current_position = self.popup_frame_canvas.create_oval((0, 0, 0, 0), fill = 'red', outline = 'red')
		self.popup_targeted_position_a = self.popup_frame_canvas.create_line((0, 0, 0, 0), fill = 'purple', width = 5.0)
		self.popup_targeted_position_b = self.popup_frame_canvas.create_line((0, 0, 0, 0), fill = 'purple', width = 5.0)
		self.popup_chosen_position = self.popup_frame_canvas.create_oval((0, 0, 0, 0), fill = 'blue', outline = 'blue')
		self.popup_frame_canvas.bind('<ButtonPress-1>', self.stage_popup_frame_click)
		
		text = 'None'
		self.popup_frame_label = tkinter.Label( self.popup_frame, text = text, font = 'Consolas', height = 4, width = 64, relief = tkinter.GROOVE, borderwidth = 6, anchor = tkinter.W)
		self.popup_frame_label.grid( row = 6, column = 0, rowspan = 1, columnspan = 6 )
		
		self.popup_frame_label_canvas = tkinter.Canvas( self.popup_frame, bg = 'grey', width = 40, height = 70 )
		self.popup_frame_label_canvas.grid( row = 6, column = 0, rowspan = 1, columnspan = 1 )
		self.popup_current_position_label = self.popup_frame_label_canvas.create_oval((15, 12, 25, 22), fill = 'red', outline = 'red')
		self.popup_targeted_position_a_label = self.popup_frame_label_canvas.create_line((15, 32, 25, 42), fill = 'purple', width = 5.0)
		self.popup_targeted_position_b_label = self.popup_frame_label_canvas.create_line((15, 42, 25, 32), fill = 'purple', width = 5.0)
		self.popup_chosen_position_label = self.popup_frame_label_canvas.create_oval((15, 52, 25, 62), fill = 'blue', outline = 'blue')
		
		self.popup_frame_button = tkinter.Button( self.popup_frame, height = 32, width = 32, relief = tkinter.RAISED )
		self.popup_frame_button_image = PIL.ImageTk.PhotoImage( PIL.Image.open('Icons/Move.png') )
		self.popup_frame_button['image'] = self.popup_frame_button_image
		self.popup_frame_button['command'] = self.stage_popup_frame_button_command
		self.popup_frame_button.grid( row = 6, column = 6, rowspan = 1, columnspan = 2 )
	
	def stage_popup_exit(self):
		self.popup.destroy()
		self.stage_popup_flag = False
		
	def stage_popup_frame_click(self, coordinate):
		self.popup_frame_canvas.coords( self.popup_chosen_position, coordinate.x - 5, coordinate.y - 5, coordinate.x + 5, coordinate.y + 5 )
		self.nymphscope.stage_x_chosen = (coordinate.x - 400) / 10
		self.nymphscope.stage_y_chosen = - (coordinate.y - 300) / 10
	
	def stage_popup_frame_button_command(self):
		self.nymphscope.stage_x_move(self.nymphscope.stage_x_chosen, 0)
		self.nymphscope.stage_y_move(self.nymphscope.stage_y_chosen, 0)
	
	def stage_popup_frame_update(self, x, y):
		text = f'       Current: ({x:8.3f},{y:8.3f} )\n       Target : ({self.nymphscope.stage_x_targeted:8.3f},{self.nymphscope.stage_y_targeted:8.3f} )\n       Chosen : ({self.nymphscope.stage_x_chosen:8.3f},{self.nymphscope.stage_y_chosen:8.3f} )'
		self.popup_frame_label['text'] = text
		self.popup_frame_canvas.coords( self.popup_current_position, x * 10 + 400 - 7, -y * 10 + 300 - 7, x * 10 + 400 + 7, -y * 10 + 300 + 7 )
		self.popup_frame_canvas.coords( self.popup_targeted_position_a, self.nymphscope.stage_x_targeted * 10 + 400 - 10, -self.nymphscope.stage_y_targeted * 10 + 300 - 10, self.nymphscope.stage_x_targeted * 10 + 400 + 10, -self.nymphscope.stage_y_targeted * 10 + 300 + 10 )
		self.popup_frame_canvas.coords( self.popup_targeted_position_b, self.nymphscope.stage_x_targeted * 10 + 400 - 10, -self.nymphscope.stage_y_targeted * 10 + 300 + 10, self.nymphscope.stage_x_targeted * 10 + 400 + 10, -self.nymphscope.stage_y_targeted * 10 + 300 - 10 )
	

root = tkinter.Tk()
application = Application( master = root )
# substitution of mainloop()
while application.intact_flag:
	application.update_idletasks()
	application.update()
	if application.close_flag:
		application.open_board()
	if application.intact_flag:
		application.nymphscope.update_status()
		application.control_frame_information_update()
		application.status_frame_information_update()
		application.motion_frame_information_update()
		application.image_histogram_update()
# application.mainloop()