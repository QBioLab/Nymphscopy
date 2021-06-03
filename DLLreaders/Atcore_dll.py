# import re

# def atcoreDll():
	# file_write = open('atcoreDll.py', 'w')
	# text = f'import ctypes\n\n'
	# file_write.write(text)
	
	# res = {'int':'ctypes.c_int'}
	# arg = {'void*':'ctypes.c_void_p', 'AT_H':'ctypes.c_int', 'AT_BOOL':'ctypes.c_int', 'int':'ctypes.c_int', 'AT_H*':'ctypes.POINTER(ctypes.c_int)', 'AT_BOOL*':'ctypes.POINTER(ctypes.c_int)', 
			# 'int*':'ctypes.POINTER(ctypes.c_int)', 'AT_64':'ctypes.c_longlong', 'AT_64*':'ctypes.POINTER(ctypes.c_longlong)', 'AT_64&':'ctypes.POINTER(ctypes.c_longlong)', 'AT_U8':'ctypes.c_ubyte',
			# 'AT_U8*':'ctypes.POINTER(ctypes.c_ubyte)', 'AT_U8**':'ctypes.POINTER(ctypes.POINTER(ctypes.c_ubyte))', 'AT_WC':'ctypes.c_wchar', 'AT_WC*':'ctypes.c_wchar_p', 'double':'ctypes.c_double',
			# 'double*':'ctypes.POINTER(ctypes.c_double)', 'unsigned_int':'ctypes.c_uint', 'FeatureCallback':'FeatureCallback', 'AT_EXP_CONV':'' } # 'AT_EXP_CONV' is used in case for null args
	
	# text = f'def atcore_Functions(dll):\n'
	# file_write.write(text)
	# text = f'\t# typedef int (AT_EXP_CONV *FeatureCallback)(AT_H Hndl, const AT_WC* Feature, void* Context);\n'
	# file_write.write(text)
	# text = f'\tFeatureCallback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_wchar_p), ctypes.POINTER(ctypes.c_void_p))\n\n'
	# file_write.write(text)
	
	# file = open('atcore.h', 'r', encoding='utf-8')
	# for line in file:
		# linearray = re.split("[\t\n, ();]+", line)
		# if len(linearray) < 3:
			# continue
		# elif linearray[2] == 'AT_EXP_CONV' and linearray[0] == '':
			# for _ in range(linearray.count('const')):
				# linearray.remove('const')
			# for _ in range(linearray.count('unsigned')):
					# index = linearray.index('unsigned') + 1
					# linearray[index] = f'unsigned_{linearray[index]}'
					# linearray.remove('unsigned')
			# for i in range(1, len(linearray) - 1):
				# if linearray[i][0] == '*':
					# linearray[i - 1] = f'{linearray[i - 1]}*'
			# for i in range(4, len(linearray) -1 , 2):
				# if linearray[i] not in ('void*', 'AT_H', 'AT_BOOL', 'AT_BOOL*', 'int*',  'int', 'AT_H*', 'AT_64', 'AT_64*', 'AT_64&', 'AT_U8', 'AT_U8*', 'AT_U8**', 'AT_WC', 'AT_WC*', 'double', 'double*', 'unsigned_int', 'FeatureCallback' ):
					# print(f'arg: {linearray[i]}')
			# if linearray[1] not in ('int'):
				# print(f'res: {linearray[1]}')
			# text = f'\t#{line}'
			# file_write.write(text)
			# text = f'\tdll.{linearray[3]}.argtypes = ['
			# if len(linearray) > 4:
				# for i in range(4, len(linearray) - 3 , 2):
					# text = f'{text}{arg[linearray[i]]}, '
				# text = f'{text}{arg[linearray[len(linearray) - 3]]}]\n'
			# else:
				# text = f'{text[:-1]}None\n'
			# file_write.write(text)
			# text = f'\tdll.{linearray[3]}.restype = {res[linearray[1]]}\n'
			# file_write.write(text)
	# file.close()
	
	# text = f'\ndef atutility_Functions(dll):\n'
	# file_write.write(text)
	
	# file = open('atutility.h', 'r', encoding='utf-8')
	# for line in file:
		# linearray = re.split("[\t\n, ();]+", line)
		# if len(linearray) < 3:
			# continue
		# elif linearray[1] == 'AT_EXP_CONV':
			# for _ in range(linearray.count('const')):
				# linearray.remove('const')
			# for _ in range(linearray.count('unsigned')):
					# index = linearray.index('unsigned') + 1
					# linearray[index] = f'unsigned_{linearray[index]}'
					# linearray.remove('unsigned')
			# for i in range(1, len(linearray) - 1):
				# if linearray[i][0] == '*':
					# linearray[i - 1] = f'{linearray[i - 1]}*'
			# for i in range(3, len(linearray) -1 , 2):
				# if linearray[i] not in ('void*', 'AT_H', 'AT_BOOL', 'AT_BOOL*', 'int*',  'int', 'AT_H*', 'AT_64', 'AT_64*', 'AT_64&', 'AT_U8', 'AT_U8*', 'AT_U8**', 'AT_WC', 'AT_WC*', 'double', 'double*', 'unsigned_int', 'FeatureCallback' ):
					# print(f'arg: {linearray[i]}')
			# if linearray[0] not in ('int'):
				# print(f'res: {linearray[1]}')
			# text = f'\t#{line}'
			# file_write.write(text)
			# text = f'\tdll.{linearray[2]}.argtypes = ['
			# if len(linearray) > 3:
				# for i in range(3, len(linearray) - 3 , 2):
					# text = f'{text}{arg[linearray[i]]}, '
				# text = f'{text}{arg[linearray[len(linearray) - 3]]}]\n'
			# else:
				# text = f'{text[:-1]}None\n'
			# file_write.write(text)
			# text = f'\tdll.{linearray[2]}.restype = {res[linearray[0]]}\n'
			# file_write.write(text)
	# file.close()
	
	# file_write.close()

import ctypes
import os
import sys

os.environ["PATH"] += ';Libraries'
atcore = ctypes.windll.LoadLibrary('Libraries\\atcore.dll')
atutility = ctypes.windll.LoadLibrary('Libraries\\atutility.dll')

AT_INFINITE=0xFFFFFFFF

AT_CALLBACK_SUCCESS=0

AT_TRUE=1
AT_FALSE=0

AT_SUCCESS=0
AT_ERR_NOTINITIALISED=1
AT_ERR_NOTIMPLEMENTED=2
AT_ERR_READONLY=3
AT_ERR_NOTREADABLE=4
AT_ERR_NOTWRITABLE=5
AT_ERR_OUTOFRANGE=6
AT_ERR_INDEXNOTAVAILABLE=7
AT_ERR_INDEXNOTIMPLEMENTED=8
AT_ERR_EXCEEDEDMAXSTRINGLENGTH=9
AT_ERR_CONNECTION=10
AT_ERR_NODATA=11
AT_ERR_INVALIDHANDLE=12
AT_ERR_TIMEDOUT=13
AT_ERR_BUFFERFULL=14
AT_ERR_INVALIDSIZE=15
AT_ERR_INVALIDALIGNMENT=16
AT_ERR_COMM=17
AT_ERR_STRINGNOTAVAILABLE=18
AT_ERR_STRINGNOTIMPLEMENTED=19

AT_ERR_NULL_FEATURE=20
AT_ERR_NULL_HANDLE=21
AT_ERR_NULL_IMPLEMENTED_VAR=22
AT_ERR_NULL_READABLE_VAR=23
AT_ERR_NULL_READONLY_VAR=24
AT_ERR_NULL_WRITABLE_VAR=25
AT_ERR_NULL_MINVALUE=26
AT_ERR_NULL_MAXVALUE=27
AT_ERR_NULL_VALUE=28
AT_ERR_NULL_STRING=29
AT_ERR_NULL_COUNT_VAR=30
AT_ERR_NULL_ISAVAILABLE_VAR=31
AT_ERR_NULL_MAXSTRINGLENGTH=32
AT_ERR_NULL_EVCALLBACK=33
AT_ERR_NULL_QUEUE_PTR=34
AT_ERR_NULL_WAIT_PTR=35
AT_ERR_NULL_PTRSIZE=36
AT_ERR_NOMEMORY=37
AT_ERR_DEVICEINUSE=38
AT_ERR_DEVICENOTFOUND=39

AT_ERR_HARDWARE_OVERFLOW=100

AT_HANDLE_UNINITIALISED=-1
AT_HANDLE_SYSTEM=1

# typedef int (AT_EXP_CONV *FeatureCallback)(AT_H Hndl, const AT_WC* Feature, void* Context);
FeatureCallback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_wchar_p), ctypes.POINTER(ctypes.c_void_p))

# int AT_EXP_CONV AT_InitialiseLibrary();
AT_InitialiseLibrary = atcore.AT_InitialiseLibrary
AT_InitialiseLibrary.argtypes = []
AT_InitialiseLibrary.restype = ctypes.c_int
# int AT_EXP_CONV AT_FinaliseLibrary();
AT_FinaliseLibrary = atcore.AT_FinaliseLibrary
AT_FinaliseLibrary.argtypes = []
AT_FinaliseLibrary.restype = ctypes.c_int
# int AT_EXP_CONV AT_Open(int CameraIndex, AT_H *Hndl);
AT_Open = atcore.AT_Open
AT_Open.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
AT_Open.restype = ctypes.c_int
# int AT_EXP_CONV AT_Close(AT_H Hndl);
AT_Close = atcore.AT_Close
AT_Close.argtypes = [ctypes.c_int]
AT_Close.restype = ctypes.c_int
# int AT_EXP_CONV AT_RegisterFeatureCallback(AT_H Hndl, const AT_WC* Feature, FeatureCallback EvCallback, void* Context);
AT_RegisterFeatureCallback = atcore.AT_RegisterFeatureCallback
AT_RegisterFeatureCallback.argtypes = [ctypes.c_int, ctypes.c_wchar_p, FeatureCallback, ctypes.c_void_p]
AT_RegisterFeatureCallback.restype = ctypes.c_int
# int AT_EXP_CONV AT_UnregisterFeatureCallback(AT_H Hndl, const AT_WC* Feature, FeatureCallback EvCallback, void* Context);
AT_UnregisterFeatureCallback = atcore.AT_UnregisterFeatureCallback
AT_UnregisterFeatureCallback.argtypes = [ctypes.c_int, ctypes.c_wchar_p, FeatureCallback, ctypes.c_void_p]
AT_UnregisterFeatureCallback.restype = ctypes.c_int
# int AT_EXP_CONV AT_IsImplemented(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Implemented);
AT_IsImplemented = atcore.AT_IsImplemented
AT_IsImplemented.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int)]
AT_IsImplemented.restype = ctypes.c_int
# int AT_EXP_CONV AT_IsReadable(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Readable);
AT_IsReadable = atcore.AT_IsReadable
AT_IsReadable.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int)]
AT_IsReadable.restype = ctypes.c_int
# int AT_EXP_CONV AT_IsWritable(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Writable);
AT_IsWritable = atcore.AT_IsWritable
AT_IsWritable.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int)]
AT_IsWritable.restype = ctypes.c_int
# int AT_EXP_CONV AT_IsReadOnly(AT_H Hndl, const AT_WC* Feature, AT_BOOL* ReadOnly);
AT_IsReadOnly = atcore.AT_IsReadOnly
AT_IsReadOnly.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int)]
AT_IsReadOnly.restype = ctypes.c_int
# int AT_EXP_CONV AT_SetInt(AT_H Hndl, const AT_WC* Feature, AT_64 Value);
AT_SetInt = atcore.AT_SetInt
AT_SetInt.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_longlong]
AT_SetInt.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetInt(AT_H Hndl, const AT_WC* Feature, AT_64* Value);
AT_GetInt = atcore.AT_GetInt
AT_GetInt.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_longlong)]
AT_GetInt.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetIntMax(AT_H Hndl, const AT_WC* Feature, AT_64* MaxValue);
AT_GetIntMax = atcore.AT_GetIntMax
AT_GetIntMax.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_longlong)]
AT_GetIntMax.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetIntMin(AT_H Hndl, const AT_WC* Feature, AT_64* MinValue);
AT_GetIntMin = atcore.AT_GetIntMin
AT_GetIntMin.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_longlong)]
AT_GetIntMin.restype = ctypes.c_int
# int AT_EXP_CONV AT_SetFloat(AT_H Hndl, const AT_WC* Feature, double Value);
AT_SetFloat = atcore.AT_SetFloat
AT_SetFloat.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_double]
AT_SetFloat.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetFloat(AT_H Hndl, const AT_WC* Feature, double* Value);
AT_GetFloat = atcore.AT_GetFloat
AT_GetFloat.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_double)]
AT_GetFloat.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetFloatMax(AT_H Hndl, const AT_WC* Feature, double* MaxValue);
AT_GetFloatMax = atcore.AT_GetFloatMax
AT_GetFloatMax.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_double)]
AT_GetFloatMax.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetFloatMin(AT_H Hndl, const AT_WC* Feature, double* MinValue);
AT_GetFloatMin = atcore.AT_GetFloatMin
AT_GetFloatMin.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_double)]
AT_GetFloatMin.restype = ctypes.c_int
# int AT_EXP_CONV AT_SetBool(AT_H Hndl, const AT_WC* Feature, AT_BOOL Value);
AT_SetBool = atcore.AT_SetBool
AT_SetBool.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int]
AT_SetBool.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetBool(AT_H Hndl, const AT_WC* Feature, AT_BOOL* Value);
AT_GetBool = atcore.AT_GetBool
AT_GetBool.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int)]
AT_GetBool.restype = ctypes.c_int
# int AT_EXP_CONV AT_SetEnumerated(AT_H Hndl, const AT_WC* Feature, int Value);
AT_SetEnumerated = atcore.AT_SetEnumerated
AT_SetEnumerated.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int]
AT_SetEnumerated.restype = ctypes.c_int
# int AT_EXP_CONV AT_SetEnumeratedString(AT_H Hndl, const AT_WC* Feature, const AT_WC* String);
AT_SetEnumeratedString = atcore.AT_SetEnumeratedString
AT_SetEnumeratedString.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p]
AT_SetEnumeratedString.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetEnumerated(AT_H Hndl, const AT_WC* Feature, int* Value);
AT_GetEnumerated = atcore.AT_GetEnumerated
AT_GetEnumerated.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int)]
AT_GetEnumerated.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetEnumeratedCount(AT_H Hndl,const  AT_WC* Feature, int* Count);
AT_GetEnumeratedCount = atcore.AT_GetEnumeratedCount
AT_GetEnumeratedCount.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int)]
AT_GetEnumeratedCount.restype = ctypes.c_int
# int AT_EXP_CONV AT_IsEnumeratedIndexAvailable(AT_H Hndl, const AT_WC* Feature, int Index, AT_BOOL* Available);
AT_IsEnumeratedIndexAvailable = atcore.AT_IsEnumeratedIndexAvailable
AT_IsEnumeratedIndexAvailable.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
AT_IsEnumeratedIndexAvailable.restype = ctypes.c_int
# int AT_EXP_CONV AT_IsEnumeratedIndexImplemented(AT_H Hndl, const AT_WC* Feature, int Index, AT_BOOL* Implemented);
AT_IsEnumeratedIndexImplemented = atcore.AT_IsEnumeratedIndexImplemented
AT_IsEnumeratedIndexImplemented.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
AT_IsEnumeratedIndexImplemented.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetEnumeratedString(AT_H Hndl, const AT_WC* Feature, int Index, AT_WC* String, int StringLength);
AT_GetEnumeratedString = atcore.AT_GetEnumeratedString
AT_GetEnumeratedString.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int]
AT_GetEnumeratedString.restype = ctypes.c_int
# int AT_EXP_CONV AT_SetEnumIndex(AT_H Hndl, const AT_WC* Feature, int Value);
AT_SetEnumIndex = atcore.AT_SetEnumIndex
AT_SetEnumIndex.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int]
AT_SetEnumIndex.restype = ctypes.c_int
# int AT_EXP_CONV AT_SetEnumString(AT_H Hndl, const AT_WC* Feature, const AT_WC* String);
AT_SetEnumString = atcore.AT_SetEnumString
AT_SetEnumString.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p]
AT_SetEnumString.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetEnumIndex(AT_H Hndl, const AT_WC* Feature, int* Value);
AT_GetEnumIndex = atcore.AT_GetEnumIndex
AT_GetEnumIndex.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int)]
AT_GetEnumIndex.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetEnumCount(AT_H Hndl,const  AT_WC* Feature, int* Count);
AT_GetEnumCount = atcore.AT_GetEnumCount
AT_GetEnumCount.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int)]
AT_GetEnumCount.restype = ctypes.c_int
# int AT_EXP_CONV AT_IsEnumIndexAvailable(AT_H Hndl, const AT_WC* Feature, int Index, AT_BOOL* Available);
AT_IsEnumIndexAvailable = atcore.AT_IsEnumIndexAvailable
AT_IsEnumIndexAvailable.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
AT_IsEnumIndexAvailable.restype = ctypes.c_int
# int AT_EXP_CONV AT_IsEnumIndexImplemented(AT_H Hndl, const AT_WC* Feature, int Index, AT_BOOL* Implemented);
AT_IsEnumIndexImplemented = atcore.AT_IsEnumIndexImplemented
AT_IsEnumIndexImplemented.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
AT_IsEnumIndexImplemented.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetEnumStringByIndex(AT_H Hndl, const AT_WC* Feature, int Index, AT_WC* String, int StringLength);
AT_GetEnumStringByIndex = atcore.AT_GetEnumStringByIndex
AT_GetEnumStringByIndex.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int]
AT_GetEnumStringByIndex.restype = ctypes.c_int
# int AT_EXP_CONV AT_Command(AT_H Hndl, const AT_WC* Feature);
AT_Command = atcore.AT_Command
AT_Command.argtypes = [ctypes.c_int, ctypes.c_wchar_p]
AT_Command.restype = ctypes.c_int
# int AT_EXP_CONV AT_SetString(AT_H Hndl, const AT_WC* Feature, const AT_WC* String);
AT_SetString = atcore.AT_SetString
AT_SetString.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p]
AT_SetString.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetString(AT_H Hndl, const AT_WC* Feature, AT_WC* String, int StringLength);
AT_GetString = atcore.AT_GetString
AT_GetString.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_int]
AT_GetString.restype = ctypes.c_int
# int AT_EXP_CONV AT_GetStringMaxLength(AT_H Hndl, const AT_WC* Feature, int* MaxStringLength);
AT_GetStringMaxLength = atcore.AT_GetStringMaxLength
AT_GetStringMaxLength.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int)]
AT_GetStringMaxLength.restype = ctypes.c_int
# int AT_EXP_CONV AT_QueueBuffer(AT_H Hndl, AT_U8* Ptr, int PtrSize);
AT_QueueBuffer = atcore.AT_QueueBuffer
AT_QueueBuffer.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int]
AT_QueueBuffer.restype = ctypes.c_int
# int AT_EXP_CONV AT_WaitBuffer(AT_H Hndl, AT_U8** Ptr, int* PtrSize, unsigned int Timeout);
AT_WaitBuffer = atcore.AT_WaitBuffer
AT_WaitBuffer.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_ubyte)), ctypes.POINTER(ctypes.c_int), ctypes.c_uint]
AT_WaitBuffer.restype = ctypes.c_int
# int AT_EXP_CONV AT_Flush(AT_H Hndl);
AT_Flush = atcore.AT_Flush
AT_Flush.argtypes = [ctypes.c_int]
AT_Flush.restype = ctypes.c_int


#int AT_EXP_CONV AT_ConvertBuffer(AT_U8* inputBuffer, AT_U8* outputBuffer, AT_64 width, AT_64 height, AT_64 stride, const AT_WC* inputPixelEncoding, const AT_WC* outputPixelEncoding);
AT_ConvertBuffer = atutility.AT_ConvertBuffer
AT_ConvertBuffer.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_wchar_p]
AT_ConvertBuffer.restype = ctypes.c_int
#int AT_EXP_CONV AT_ConvertBufferUsingMetadata(AT_U8* inputBuffer, AT_U8* outputBuffer, AT_64 imagesizebytes, const AT_WC* outputPixelEncoding);
AT_ConvertBufferUsingMetadata = atutility.AT_ConvertBufferUsingMetadata
AT_ConvertBufferUsingMetadata.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_longlong, ctypes.c_wchar_p]
AT_ConvertBufferUsingMetadata.restype = ctypes.c_int
#int AT_EXP_CONV AT_GetWidthFromMetadata(AT_U8* inputBuffer, AT_64 imagesizebytes, AT_64& width);
AT_GetWidthFromMetadata = atutility.AT_GetWidthFromMetadata
AT_GetWidthFromMetadata.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
AT_GetWidthFromMetadata.restype = ctypes.c_int
#int AT_EXP_CONV AT_GetHeightFromMetadata(AT_U8* inputBuffer, AT_64 imagesizebytes, AT_64& height);
AT_GetHeightFromMetadata = atutility.AT_GetHeightFromMetadata
AT_GetHeightFromMetadata.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
AT_GetHeightFromMetadata.restype = ctypes.c_int
#int AT_EXP_CONV AT_GetStrideFromMetadata(AT_U8* inputBuffer, AT_64 imagesizebytes, AT_64& stride);
AT_GetStrideFromMetadata = atutility.AT_GetStrideFromMetadata
AT_GetStrideFromMetadata.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
AT_GetStrideFromMetadata.restype = ctypes.c_int
#int AT_EXP_CONV AT_GetPixelEncodingFromMetadata(AT_U8* inputBuffer, AT_64 imagesizebytes, AT_WC* pixelEncoding, int pixelEncodingSize);
AT_GetPixelEncodingFromMetadata = atutility.AT_GetPixelEncodingFromMetadata
AT_GetPixelEncodingFromMetadata.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_int]
AT_GetPixelEncodingFromMetadata.restype = ctypes.c_int
#int AT_EXP_CONV AT_GetTimeStampFromMetadata(AT_U8* inputBuffer, AT_64 imagesizebytes, AT_64& timeStamp);
AT_GetTimeStampFromMetadata = atutility.AT_GetTimeStampFromMetadata
AT_GetTimeStampFromMetadata.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
AT_GetTimeStampFromMetadata.restype = ctypes.c_int
#int AT_EXP_CONV AT_InitialiseUtilityLibrary();
AT_InitialiseUtilityLibrary = atutility.AT_InitialiseUtilityLibrary
AT_InitialiseUtilityLibrary.argtypes = []
AT_InitialiseUtilityLibrary.restype = ctypes.c_int
#int AT_EXP_CONV AT_FinaliseUtilityLibrary();
AT_FinaliseUtilityLibrary = atutility.AT_FinaliseUtilityLibrary
AT_FinaliseUtilityLibrary.argtypes = []
AT_FinaliseUtilityLibrary.restype = ctypes.c_int
