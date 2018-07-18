import re
file = open('MotionControlDLL.py', 'r')
file_write = open('MotionControlDLL_fixed.py', 'w')
index = 0
res = {'BOOL':'ctypes.c_bool', 'int':'ctypes.c_int', 'void': 'None'}
arg = {'char':'ctypes.c_char', 'char*':'ctypes.c_char_p', 'BOOL':'ctypes.c_bool', 'BOOL*':'ctypes.POINTER(ctypes.c_bool)', 'int':'ctypes.c_int', 'int*':'ctypes.POINTER(ctypes.c_int)', '__int64*':'ctypes.POINTER(ctypes.c_longlong)', 'unsigned_int*':'ctypes.POINTER(ctypes.c_uint)', 'double':'ctypes.c_double', 'double*':'ctypes.POINTER(ctypes.c_double)', 'double**':'ctypes.POINTER(ctypes.POINTER(ctypes.c_double))'}
for line in file:
	index = index+1
	linearray = re.split("[\t\n, ();]+", line)
	for _ in range(linearray.count('const')):
		linearray.remove('const')
	for _ in range(linearray.count('unsigned')):
		linearray[ linearray.index('unsigned') + 1 ] = ''.join([ 'unsigned_', linearray[ linearray.index('unsigned') + 1 ] ])
		linearray.remove('unsigned')
	if len(linearray) < 3:
		file_write.write(line)
		continue
	if linearray[2] == 'PI_FUNC_DECL':
#		 if linearray[1] in ('BOOL', 'int', 'void'):
#			 continue
#			 print(linearray[1])
#		 for i in range(4, len(linearray) - 1 , 2):
#			 if linearray[i] in ('char', 'char*', 'BOOL*', 'int', 'int*', '__int64*', 'unsigned_int*', 'BOOL', 'double', 'double*', 'double**'):
#				 continue
#			 print(linearray[i], '\t:', index)
		text = ''.join([ '\t# ', line[1:] ])
		file_write.write(text)
		text = ''.join([ '\tdll.', linearray[3], '.argtypes = [' ])
		for i in range(4, len(linearray) - 3 , 2):
			text = ''.join([ text, arg[linearray[i]], ', ' ])
		text = ''.join([ text, arg[linearray[len(linearray) - 3]], ']\n' ])
		file_write.write(text)
		text = ''.join([ '\tdll.', linearray[3], '.restype = ', res[linearray[1]], '\n' ])
		file_write.write(text)
		continue
	file_write.write(line)
file.close()
file_write.close()