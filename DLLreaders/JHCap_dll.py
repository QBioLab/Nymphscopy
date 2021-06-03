# import re

# def JHCapDll():
	# import re
	# file = open('JHCap.h', 'r', encoding='utf-8')
	# file_write = open('JHCapDll.py', 'w')
	
	# res = {'API_STATUS':'ctypes.c_int'}
	# arg = {'int':'ctypes.c_int', 'int*':'ctypes.POINTER(ctypes.c_int)', 'UINT':'ctypes.c_uint',
			# 'char':'ctypes.c_char', 'char*':'ctypes.c_char_p', 'unsigned_char*':'ctypes.POINTER(ctypes.c_ubyte)',
			# 'double':'ctypes.c_double', 'double*':'ctypes.POINTER(ctypes.c_double)', 'void*':'ctypes.c_void_p', 
			# 'bool':'ctypes.c_bool', 'bool*':'ctypes.POINTER(ctypes.c_bool)', 'BOOL':'ctypes.c_bool',
			# 'BYTE*':'ctypes.c_char_p', 'HDC':'ctypes.c_char_p', 'HWND':'ctypes.c_char_p', 'HBITMAP*':'ctypes.c_char_p', 
			# 'CAPTURE_FRAME_PROC':'ctypes.c_char_p', 'CAPTURE_FRAME_PROC_EX':'ctypes.c_char_p' }
	# for line in file:
		# linearray = re.split("[\t\n, ();]+", line)
		# if len(linearray) < 3:
			# continue
		# elif linearray[0] == 'extern' and linearray[2] == 'DLL_EXPORT':
			# for _ in range(linearray.count('const')):
				# linearray.remove('const')
			# for i in range(1, len(linearray) - 1):
				# if linearray[i][0] == '*':
					# linearray[i - 1] = f'{linearray[i - 1]}*'
			# for _ in range(linearray.count('unsigned')):
				# index = linearray.index('unsigned') + 1
				# linearray[index] = f'unsigned_{linearray[index]}'
				# linearray.remove('unsigned')
			# for i in range(6, len(linearray) -1 , 2):
				# if linearray[i] not in ('int', 'int*', 'UINT',
										# 'char', 'char*', 'unsigned_char*',
										# 'double', 'double*', 'void*', 
										# 'bool', 'bool*', 'BOOL', 
										# 'BYTE*', 'HDC', 'HWND', 'HBITMAP*', 
										# 'CAPTURE_FRAME_PROC', 'CAPTURE_FRAME_PROC_EX' ):
					# print(f'arg: {linearray[i]}')
			# if linearray[3] not in ('API_STATUS'):
				# print(f'res: {linearray[3]}')
			# text = f'\t#{line}'
			# file_write.write(text)
			# text = f'\tdll.{linearray[5]}.argtypes = ['
			# for i in range(6, len(linearray) - 3 , 2):
				# text = f'{text}{arg[linearray[i]]}, '
			# text = f'{text}{arg[linearray[len(linearray) - 3]]}]\n'
			# file_write.write(text)
			# text = f'\tdll.{linearray[5]}.restype = {res[linearray[3]]}\n'
			# file_write.write(text)
	
	# file.close()
	# file_write.close()

import ctypes
import os
import sys

JHCap = ctypes.windll.LoadLibrary('Libraries\\JHCap2.dll')

#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetVersion(int *major, int *minor);
CameraGetVersion = JHCap.CameraGetVersion
CameraGetVersion.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
CameraGetVersion.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetFirmVersion(int index,int *ver);
CameraGetFirmVersion = JHCap.CameraGetFirmVersion
CameraGetFirmVersion.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetFirmVersion.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetCount(int *count);
CameraGetCount = JHCap.CameraGetCount
CameraGetCount.argtypes = [ctypes.POINTER(ctypes.c_int)]
CameraGetCount.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetName(int index, char *name, char *model);
CameraGetName = JHCap.CameraGetName
CameraGetName.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
CameraGetName.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetID(int index,int *modeID, int *productID);
CameraGetID = JHCap.CameraGetID
CameraGetID.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
CameraGetID.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetLastError(int *last_error);
CameraGetLastError = JHCap.CameraGetLastError
CameraGetLastError.argtypes = [ctypes.POINTER(ctypes.c_int)]
CameraGetLastError.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraInit(int device_id);
CameraInit = JHCap.CameraInit
CameraInit.argtypes = [ctypes.c_int]
CameraInit.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraFree(int device_id);
CameraFree = JHCap.CameraFree
CameraFree.argtypes = [ctypes.c_int]
CameraFree.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraReset(int device_id);
CameraReset = JHCap.CameraReset
CameraReset.argtypes = [ctypes.c_int]
CameraReset.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetOption(int device_id,int format);
CameraSetOption = JHCap.CameraSetOption
CameraSetOption.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetOption.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetOption(int device_id,int *format);
CameraGetOption = JHCap.CameraGetOption
CameraGetOption.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetOption.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetResolutionCount(int device_id, int *count);
CameraGetResolutionCount = JHCap.CameraGetResolutionCount
CameraGetResolutionCount.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetResolutionCount.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetResolutionMax(int device_id, int *width, int *height);
CameraGetResolutionMax = JHCap.CameraGetResolutionMax
CameraGetResolutionMax.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
CameraGetResolutionMax.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetResolutionMode(int device_id, int *mode);
CameraGetResolutionMode = JHCap.CameraGetResolutionMode
CameraGetResolutionMode.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetResolutionMode.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetResolutionMode(int device_id, int mode);
CameraSetResolutionMode = JHCap.CameraSetResolutionMode
CameraSetResolutionMode.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetResolutionMode.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetResolution(int device_id,int index,int *width, int *height);
CameraGetResolution = JHCap.CameraGetResolution
CameraGetResolution.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
CameraGetResolution.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetResolution(int device_id,int index,int *width, int *height);
CameraSetResolution = JHCap.CameraSetResolution
CameraSetResolution.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
CameraSetResolution.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetROI(int device_id,int offset_width, int offset_height, int width, int height);
CameraSetROI = JHCap.CameraSetROI
CameraSetROI.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
CameraSetROI.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetGain(int device_id,int gain);
CameraSetGain = JHCap.CameraSetGain
CameraSetGain.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetGain.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetAdvancedGain(int device_id,int *advanced_gain);
CameraGetAdvancedGain = JHCap.CameraGetAdvancedGain
CameraGetAdvancedGain.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetAdvancedGain.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetAdvancedGain(int device_id,int advanced_gain);
CameraSetAdvancedGain = JHCap.CameraSetAdvancedGain
CameraSetAdvancedGain.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetAdvancedGain.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetGain(int device_id,int *gain);
CameraGetGain = JHCap.CameraGetGain
CameraGetGain.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetGain.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetAGC(int device_id,bool agc);
CameraSetAGC = JHCap.CameraSetAGC
CameraSetAGC.argtypes = [ctypes.c_int, ctypes.c_bool]
CameraSetAGC.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetAGC(int device_id,bool *agc);
CameraGetAGC = JHCap.CameraGetAGC
CameraGetAGC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]
CameraGetAGC.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetWBGain(int device_id,double rg, double gg, double bg);
CameraSetWBGain = JHCap.CameraSetWBGain
CameraSetWBGain.argtypes = [ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double]
CameraSetWBGain.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetWBGain(int device_id,double *rg, double *gg, double *bg);
CameraGetWBGain = JHCap.CameraGetWBGain
CameraGetWBGain.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
CameraGetWBGain.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetExposure(int device_id,int exposure);
CameraSetExposure = JHCap.CameraSetExposure
CameraSetExposure.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetExposure.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetExposure(int device_id,int *exposure);
CameraGetExposure = JHCap.CameraGetExposure
CameraGetExposure.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetExposure.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetAvg(int device_id,int *avg);
CameraGetAvg = JHCap.CameraGetAvg
CameraGetAvg.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetAvg.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetExposureUnit(int device_id,double *exposure_unit);
CameraGetExposureUnit = JHCap.CameraGetExposureUnit
CameraGetExposureUnit.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
CameraGetExposureUnit.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetExposureTime(int device_id,double *exposure_time);
CameraGetExposureTime = JHCap.CameraGetExposureTime
CameraGetExposureTime.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
CameraGetExposureTime.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetTimeout(int device_id,int timeout);
CameraSetTimeout = JHCap.CameraSetTimeout
CameraSetTimeout.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetTimeout.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetTimeout(int device_id,int *timeout);
CameraGetTimeout = JHCap.CameraGetTimeout
CameraGetTimeout.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetTimeout.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetAEC(int device_id,bool aec);
CameraSetAEC = JHCap.CameraSetAEC
CameraSetAEC.argtypes = [ctypes.c_int, ctypes.c_bool]
CameraSetAEC.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetAEC(int device_id,bool *aec);
CameraGetAEC = JHCap.CameraGetAEC
CameraGetAEC.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]
CameraGetAEC.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetGamma(int device_id,double gamma);
CameraSetGamma = JHCap.CameraSetGamma
CameraSetGamma.argtypes = [ctypes.c_int, ctypes.c_double]
CameraSetGamma.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetGamma(int device_id,double *gamma);
CameraGetGamma = JHCap.CameraGetGamma
CameraGetGamma.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
CameraGetGamma.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetContrast(int device_id,double contrast);
CameraSetContrast = JHCap.CameraSetContrast
CameraSetContrast.argtypes = [ctypes.c_int, ctypes.c_double]
CameraSetContrast.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetContrast(int device_id,double *contrast);
CameraGetContrast = JHCap.CameraGetContrast
CameraGetContrast.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
CameraGetContrast.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetSaturation(int device_id,double saturation);
CameraSetSaturation = JHCap.CameraSetSaturation
CameraSetSaturation.argtypes = [ctypes.c_int, ctypes.c_double]
CameraSetSaturation.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetSaturation(int device_id,double *saturation);
CameraGetSaturation = JHCap.CameraGetSaturation
CameraGetSaturation.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
CameraGetSaturation.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetBlackLevel(int device_id,int black);
CameraSetBlackLevel = JHCap.CameraSetBlackLevel
CameraSetBlackLevel.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetBlackLevel.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetBlackLevel(int device_id,int *black);
CameraGetBlackLevel = JHCap.CameraGetBlackLevel
CameraGetBlackLevel.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetBlackLevel.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetAETarget(int device_id,int target);
CameraSetAETarget = JHCap.CameraSetAETarget
CameraSetAETarget.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetAETarget.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetAETarget(int device_id,int *target);
CameraGetAETarget = JHCap.CameraGetAETarget
CameraGetAETarget.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetAETarget.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraOnePushWB(int device_id);
CameraOnePushWB = JHCap.CameraOnePushWB
CameraOnePushWB.argtypes = [ctypes.c_int]
CameraOnePushWB.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetImageSize(int device_id,int *width, int *height);
CameraGetImageSize = JHCap.CameraGetImageSize
CameraGetImageSize.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
CameraGetImageSize.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetImageBufferSize(int device_id,int *size, int option);
CameraGetImageBufferSize = JHCap.CameraGetImageBufferSize
CameraGetImageBufferSize.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
CameraGetImageBufferSize.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetISPImageBufferSize(int device_id,int *size, int width, int height, int option);
CameraGetISPImageBufferSize = JHCap.CameraGetISPImageBufferSize
CameraGetISPImageBufferSize.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int]
CameraGetISPImageBufferSize.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraClearHostBuffer(int device_id);
CameraClearHostBuffer = JHCap.CameraClearHostBuffer
CameraClearHostBuffer.argtypes = [ctypes.c_int]
CameraClearHostBuffer.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraQueryImage(int device_id,unsigned char *imgbuf, int *length, int option);
CameraQueryImage = JHCap.CameraQueryImage
CameraQueryImage.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
CameraQueryImage.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraQueryImage2(int device_id,unsigned char *imgbuf, int *length, int *meta,int option);
CameraQueryImage2 = JHCap.CameraQueryImage2
CameraQueryImage2.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
CameraQueryImage2.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraISP(int device_id, unsigned char *pdata, unsigned char *imgbuf, int width, int height, int option);
CameraISP = JHCap.CameraISP
CameraISP.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int, ctypes.c_int, ctypes.c_int]
CameraISP.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraCaptureImage(int device_id,int index,unsigned char *imgbuf, int *length, int option);
CameraCaptureImage = JHCap.CameraCaptureImage
CameraCaptureImage.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
CameraCaptureImage.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetMirrorX(int device_id,bool mx);
CameraSetMirrorX = JHCap.CameraSetMirrorX
CameraSetMirrorX.argtypes = [ctypes.c_int, ctypes.c_bool]
CameraSetMirrorX.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetMirrorY(int device_id,bool my);
CameraSetMirrorY = JHCap.CameraSetMirrorY
CameraSetMirrorY.argtypes = [ctypes.c_int, ctypes.c_bool]
CameraSetMirrorY.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetRotate(int device_id,int rotate);
CameraSetRotate = JHCap.CameraSetRotate
CameraSetRotate.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetRotate.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetMirrorX(int device_id,bool *mx);
CameraGetMirrorX = JHCap.CameraGetMirrorX
CameraGetMirrorX.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]
CameraGetMirrorX.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetMirrorY(int device_id,bool *my);
CameraGetMirrorY = JHCap.CameraGetMirrorY
CameraGetMirrorY.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]
CameraGetMirrorY.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraReadSerialNumber(int device_id,char id[],int length);
CameraReadSerialNumber = JHCap.CameraReadSerialNumber
CameraReadSerialNumber.argtypes = [ctypes.c_int, ctypes.c_char, ctypes.c_int]
CameraReadSerialNumber.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraWriteUserData(int device_id,char data[],int length);
CameraWriteUserData = JHCap.CameraWriteUserData
CameraWriteUserData.argtypes = [ctypes.c_int, ctypes.c_char, ctypes.c_int]
CameraWriteUserData.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraReadUserData(int device_id,char data[],int length);
CameraReadUserData = JHCap.CameraReadUserData
CameraReadUserData.argtypes = [ctypes.c_int, ctypes.c_char, ctypes.c_int]
CameraReadUserData.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSaveParameter(int device_id,int group_no);
CameraSaveParameter = JHCap.CameraSaveParameter
CameraSaveParameter.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSaveParameter.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraLoadParameter(int device_id,int group_no);
CameraLoadParameter = JHCap.CameraLoadParameter
CameraLoadParameter.argtypes = [ctypes.c_int, ctypes.c_int]
CameraLoadParameter.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraEnableStrobe(int device_id, bool en);
CameraEnableStrobe = JHCap.CameraEnableStrobe
CameraEnableStrobe.argtypes = [ctypes.c_int, ctypes.c_bool]
CameraEnableStrobe.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetTriggerPolarity(int device_id, bool high);
CameraSetTriggerPolarity = JHCap.CameraSetTriggerPolarity
CameraSetTriggerPolarity.argtypes = [ctypes.c_int, ctypes.c_bool]
CameraSetTriggerPolarity.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetStrobePolarity(int device_id, bool high);
CameraSetStrobePolarity = JHCap.CameraSetStrobePolarity
CameraSetStrobePolarity.argtypes = [ctypes.c_int, ctypes.c_bool]
CameraSetStrobePolarity.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetSnapMode(int device_id, int *snap_mode);
CameraGetSnapMode = JHCap.CameraGetSnapMode
CameraGetSnapMode.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetSnapMode.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetSnapMode(int device_id, int snap_mode);
CameraSetSnapMode = JHCap.CameraSetSnapMode
CameraSetSnapMode.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetSnapMode.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraTriggerShot(int device_id);
CameraTriggerShot = JHCap.CameraTriggerShot
CameraTriggerShot.argtypes = [ctypes.c_int]
CameraTriggerShot.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetGPIO(int device_id,int *val);
CameraGetGPIO = JHCap.CameraGetGPIO
CameraGetGPIO.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetGPIO.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetGPIO(int device_id,int mask, int val);
CameraSetGPIO = JHCap.CameraSetGPIO
CameraSetGPIO.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
CameraSetGPIO.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetDelay(int device_id,int delay);
CameraSetDelay = JHCap.CameraSetDelay
CameraSetDelay.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetDelay.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetDelay(int device_id,int *delay);
CameraGetDelay = JHCap.CameraGetDelay
CameraGetDelay.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetDelay.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetAntiFlicker(int device_id,int flicker);
CameraSetAntiFlicker = JHCap.CameraSetAntiFlicker
CameraSetAntiFlicker.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetAntiFlicker.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetAntiFlicker(int device_id,int *flicker);
CameraGetAntiFlicker = JHCap.CameraGetAntiFlicker
CameraGetAntiFlicker.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetAntiFlicker.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetEnhancement(int device_id,bool enhance);
CameraSetEnhancement = JHCap.CameraSetEnhancement
CameraSetEnhancement.argtypes = [ctypes.c_int, ctypes.c_bool]
CameraSetEnhancement.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetEnhancement(int device_id,bool *enhance);
CameraGetEnhancement = JHCap.CameraGetEnhancement
CameraGetEnhancement.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]
CameraGetEnhancement.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetAWB(int device_id,bool awb);
CameraSetAWB = JHCap.CameraSetAWB
CameraSetAWB.argtypes = [ctypes.c_int, ctypes.c_bool]
CameraSetAWB.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetAWB(int device_id,bool *awb);
CameraGetAWB = JHCap.CameraGetAWB
CameraGetAWB.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]
CameraGetAWB.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetInterpolation(int device_id,int interpolation);
CameraSetInterpolation = JHCap.CameraSetInterpolation
CameraSetInterpolation.argtypes = [ctypes.c_int, ctypes.c_int]
CameraSetInterpolation.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetInterpolation(int device_id,int *interpolation);
CameraGetInterpolation = JHCap.CameraGetInterpolation
CameraGetInterpolation.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
CameraGetInterpolation.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSetHighspeed(int device_id, bool high);
CameraSetHighspeed = JHCap.CameraSetHighspeed
CameraSetHighspeed.argtypes = [ctypes.c_int, ctypes.c_bool]
CameraSetHighspeed.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraGetHighspeed(int device_id, bool *high);
CameraGetHighspeed = JHCap.CameraGetHighspeed
CameraGetHighspeed.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_bool)]
CameraGetHighspeed.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraReconnect(int device_id);
CameraReconnect = JHCap.CameraReconnect
CameraReconnect.argtypes = [ctypes.c_int]
CameraReconnect.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSaveHBITMAP(int device_id, HBITMAP* hBitmap);
CameraSaveHBITMAP = JHCap.CameraSaveHBITMAP
CameraSaveHBITMAP.argtypes = [ctypes.c_int, ctypes.c_char_p]
CameraSaveHBITMAP.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSaveImage(int device_id,char *fileName,bool color,int option);
CameraSaveImage = JHCap.CameraSaveImage
CameraSaveImage.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_bool, ctypes.c_int]
CameraSaveImage.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSaveBMP(char *fileName,BYTE *buf,UINT width,UINT height);
CameraSaveBMP = JHCap.CameraSaveBMP
CameraSaveBMP.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint]
CameraSaveBMP.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSaveBMP8(char *fileName,BYTE *buf,UINT width,UINT height);
CameraSaveBMP8 = JHCap.CameraSaveBMP8
CameraSaveBMP8.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint]
CameraSaveBMP8.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSaveBMPB(int device_id,char *fileName);
CameraSaveBMPB = JHCap.CameraSaveBMPB
CameraSaveBMPB.argtypes = [ctypes.c_int, ctypes.c_char_p]
CameraSaveBMPB.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSaveBufferImage(char *fileName, BYTE *dataBuf, UINT widthPix,UINT height, BOOL color,int quality,int option);
CameraSaveBufferImage = JHCap.CameraSaveBufferImage
CameraSaveBufferImage.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_bool, ctypes.c_int, ctypes.c_int]
CameraSaveBufferImage.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSaveJpeg(char *fileName, BYTE *dataBuf, UINT widthPix,UINT height, BOOL color,int quality);
CameraSaveJpeg = JHCap.CameraSaveJpeg
CameraSaveJpeg.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_bool, ctypes.c_int]
CameraSaveJpeg.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraSaveJpegB(int device_id,char *fileName,BOOL color); 
CameraSaveJpegB = JHCap.CameraSaveJpegB
CameraSaveJpegB.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_bool]
CameraSaveJpegB.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraShowImage(int device_id,HDC hdc,int x,int y,int cx,int cy, CAPTURE_FRAME_PROC proc);
CameraShowImage = JHCap.CameraShowImage
CameraShowImage.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
CameraShowImage.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraShowBufferImage(HWND hWnd,unsigned char *buf,int width,int height,bool color,bool showStretchMode);
CameraShowBufferImage = JHCap.CameraShowBufferImage
CameraShowBufferImage.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int, ctypes.c_int, ctypes.c_bool, ctypes.c_bool]
CameraShowBufferImage.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraPlayWithoutCallback(int device_id,HWND hWnd);
CameraPlayWithoutCallback = JHCap.CameraPlayWithoutCallback
CameraPlayWithoutCallback.argtypes = [ctypes.c_int, ctypes.c_char_p]
CameraPlayWithoutCallback.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraPlay(int device_id,HWND hWnd,CAPTURE_FRAME_PROC proc);
CameraPlay = JHCap.CameraPlay
CameraPlay.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
CameraPlay.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraPlayEx(int device_id,HWND hWnd,CAPTURE_FRAME_PROC_EX proc, void *param);
CameraPlayEx = JHCap.CameraPlayEx
CameraPlayEx.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p]
CameraPlayEx.restype = ctypes.c_int
#extern "C" DLL_EXPORT API_STATUS __stdcall CameraStop(int device_id);
CameraStop = JHCap.CameraStop
CameraStop.argtypes = [ctypes.c_int]
CameraStop.restype = ctypes.c_int
