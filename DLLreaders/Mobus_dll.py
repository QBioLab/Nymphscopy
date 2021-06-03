import ctypes
import os
import sys

Mobus = ctypes.windll.LoadLibrary('Libraries\\Modbus_master_ao_dll.dll')

# unsigned char modbus_master_init(int portNumber,long buard,int parity,int dataBits,int stopBits,double timeout_seconds);
modbus_master_init = Mobus.modbus_master_init
modbus_master_init.argtypes = [ctypes.c_int, ctypes.c_long, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double]
modbus_master_init.restype = ctypes.c_ubyte
# unsigned char modbus_master_write_ao_all(int portNumber,unsigned char slave_add,int ao[8]);
modbus_master_write_ao_all = Mobus.modbus_master_write_ao_all
modbus_master_write_ao_all.argtypes = [ctypes.c_int, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_int)]
modbus_master_write_ao_all.restype = ctypes.c_ubyte