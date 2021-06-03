import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'DLLreaders'))
import Mobus_dll

import ctypes
import time
import numpy
import multiprocessing.connection


with multiprocessing.connection.Listener( ('localhost', 6100), authkey = b'hwlab' ) as server_claser:
	with server_claser.accept() as receiver:
		Mobus_dll.modbus_master_init(4, 9600, 0, 8, 1, 0.01)
		laser_power = [0, 0, 0, 0]
		laser_power_transformed = [laser_power[0], 0, laser_power[2], laser_power[3], laser_power[1], 0, 0, 0]
		while True:
			if receiver.poll(timeout = 0.001):
				laser_power_transformed = receiver.recv()
			# print(f'{laser_power_transformed}', end = '\r')
			if laser_power_transformed == 'end':
				break
			else:
				Mobus_dll.modbus_master_write_ao_all( 4, 15, (ctypes.c_int * 8)(* laser_power_transformed) )