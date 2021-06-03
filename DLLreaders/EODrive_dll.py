# import re

# def EODriveDll():
	# file = open('eo-drive.h', 'r', encoding='utf-8')
	# file_write = open('EODriveDll.py', 'w')
	
	# res = {'int':'ctypes.c_int', 'void': 'None'}
	# arg = {'short':'ctypes.c_short', 'int':'ctypes.c_int', 'int*':'ctypes.POINTER(ctypes.c_int)',
			# 'double':'ctypes.c_double', 'double*':'ctypes.POINTER(ctypes.c_double)', 'void*':'ctypes.c_void_p' }
	# for line in file:
		# linearray = re.split("[\t\n, ();]+", line)
		# if len(linearray) < 3:
			# continue
		# elif linearray[0] == 'EO_API':
			# for i in range(1, len(linearray) - 1):
				# if linearray[i][0] == '*':
					# linearray[i - 1] = f'{linearray[i - 1]}*'
			# for i in range(3, len(linearray) -1 , 2):
				# if linearray[i] not in ('short', 'int', 'int*',
										# 'double', 'double*' ):
					# print(f'arg: {linearray[i]}')
			# if linearray[1] not in ('int', 'void'):
				# print(f'res: {linearray[1]}')
			# text = f'\t#{line}'
			# file_write.write(text)
			# text = f'\tdll.{linearray[2]}.argtypes = ['
			# if len(linearray) > 4:
				# for i in range(4, len(linearray) - 3 , 2):
					# text = f'{text}{arg[linearray[i]]}, '
				# text = f'{text}{arg[linearray[len(linearray) - 3]]}]\n'
			# else:
				# text = f'{text[:-1]}None\n'
			# file_write.write(text)
			# text = f'\tdll.{linearray[2]}.restype = {res[linearray[1]]}\n'
			# file_write.write(text)
	
	# file.close()
	# file_write.close()

import ctypes
import os
import sys

EODrive = ctypes.windll.LoadLibrary('Libraries\\EO-Drive.dll')

#EO_API int EO_GetHandleBySerial(short serial);
EO_GetHandleBySerial = EODrive.EO_GetHandleBySerial
EO_GetHandleBySerial.argtypes = [ctypes.c_short]
EO_GetHandleBySerial.restype = ctypes.c_int
#EO_API int EO_InitHandle();
EO_InitHandle = EODrive.EO_InitHandle
EO_InitHandle.argtypes = None
EO_InitHandle.restype = ctypes.c_int
#EO_API int EO_InitAllHandles();
EO_InitAllHandles = EODrive.EO_InitAllHandles
EO_InitAllHandles.argtypes = None
EO_InitAllHandles.restype = ctypes.c_int
#EO_API int EO_GetAllHandles(int *handles, int size);
EO_GetAllHandles = EODrive.EO_GetAllHandles
EO_GetAllHandles.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
EO_GetAllHandles.restype = ctypes.c_int
#EO_API int EO_NumberOfCurrentHandles();
EO_NumberOfCurrentHandles = EODrive.EO_NumberOfCurrentHandles
EO_NumberOfCurrentHandles.argtypes = None
EO_NumberOfCurrentHandles.restype = ctypes.c_int
#EO_API void EO_ReleaseHandle(int handle);
EO_ReleaseHandle = EODrive.EO_ReleaseHandle
EO_ReleaseHandle.argtypes = [ctypes.c_int]
EO_ReleaseHandle.restype = None
#EO_API void EO_ReleaseAllHandles();
EO_ReleaseAllHandles = EODrive.EO_ReleaseAllHandles
EO_ReleaseAllHandles.argtypes = None
EO_ReleaseAllHandles.restype = None
#EO_API int EO_Move(int handle, double position);
EO_Move = EODrive.EO_Move
EO_Move.argtypes = [ctypes.c_int, ctypes.c_double]
EO_Move.restype = ctypes.c_int
#EO_API int EO_GetMaxCommand(int handle, double *maxCommand);
EO_GetMaxCommand = EODrive.EO_GetMaxCommand
EO_GetMaxCommand.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
EO_GetMaxCommand.restype = ctypes.c_int
#EO_API int EO_GetCommandPosition(int handle, double *position);
EO_GetCommandPosition = EODrive.EO_GetCommandPosition
EO_GetCommandPosition.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
EO_GetCommandPosition.restype = ctypes.c_int
#EO_API int EO_GetSerialNumber(int handle, int *serial);
EO_GetSerialNumber = EODrive.EO_GetSerialNumber
EO_GetSerialNumber.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
EO_GetSerialNumber.restype = ctypes.c_int
