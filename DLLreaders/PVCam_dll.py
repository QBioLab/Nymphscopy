import ctypes
import os
import sys

pvcam = ctypes.windll.LoadLibrary('Libraries\\pvcam64.dll')

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
	# ???????
	TIMED_MODE = ctypes.c_short(0)
	STROBED_MODE = ctypes.c_short(1)
	BULB_MODE = ctypes.c_short(2)
	TRIGGER_FIRST_MODE = ctypes.c_short(3)
	# VARIABLE_TIMED_MODE = ctypes.c_short(5)

class CIRC_MODES:
	# typedef enum PL_CIRC_MODES
	# {
		#     CIRC_NONE = 0,
		#     CIRC_OVERWRITE,
		#     CIRC_NO_OVERWRITE
		# }
	# PL_CIRC_MODES;
	CIRC_NONE = ctypes.c_short(0)
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

class smart_stream_type(ctypes.Structure):
	# typedef unsigned short rs_bool;
	# typedef signed char    int8;
	# typedef unsigned char  uns8;
	# typedef short          int16;
	# typedef unsigned short uns16;
	# typedef int            int32;
	# typedef unsigned int   uns32;
	# typedef float          flt32;
	# typedef double         flt64;
	# #if defined(_MSC_VER)
	#   typedef unsigned __int64   ulong64;
	#   typedef signed   __int64   long64;
	# #else
	#   typedef unsigned long long ulong64;
	#   typedef signed   long long long64;
	# #endif

	# typedef struct smart_stream_type
	# {
	#     uns16   entries;    /**< The number of entries in the array. */
	#     uns32*  params;     /**< The actual S.M.A.R.T. stream parameters. */
	# }
	# smart_stream_type;
	_fields_ = [("entries", ctypes.c_ushort),
				("params", ctypes.POINTER(ctypes.c_uint))]

class PVCAM_FRAME_INFO_GUID(ctypes.Structure):
	# typedef struct _TAG_PVCAM_FRAME_INFO_GUID
	# {
	#     uns32 f1;
	#     uns16 f2;
	#     uns16 f3;
	#     uns8  f4[8];
	# }
	# PVCAM_FRAME_INFO_GUID;
	_fields_ = [("f1", ctypes.c_uint),
				("f2", ctypes.c_ushort),
				("f3", ctypes.c_ushort),
				("f4", ctypes.c_ubyte * 8)]

class FRAME_INFO(ctypes.Structure):
	# typedef struct _TAG_FRAME_INFO
	# {
	#     PVCAM_FRAME_INFO_GUID FrameInfoGUID;
	#     int16 hCam;
	#     int32 FrameNr;
	#     long64 TimeStamp;
	#     int32 ReadoutTime;
	#     long64 TimeStampBOF;
	# }
	# FRAME_INFO;
	_fields_ = [("FrameInfoGUID", PVCAM_FRAME_INFO_GUID),
				("hCam", ctypes.c_short),
				("FrameNr", ctypes.c_int),
				("TimeStamp", ctypes.c_longlong),
				("ReadoutTime", ctypes.c_int),
				("TimeStampBOF", ctypes.c_longlong)]

class rgn_type(ctypes.Structure):
	# typedef struct rgn_type
	# {
	#     uns16 s1;   /**< First pixel in the serial register. */
	#     uns16 s2;   /**< Last pixel in the serial register. */
	#     uns16 sbin; /**< Serial binning for this region. */
	#     uns16 p1;   /**< First row in the parallel register. */
	#     uns16 p2;   /**< Last row in the parallel register. */
	#     uns16 pbin; /**< Parallel binning for this region. */
	# }
	# rgn_type;
	_fields_ = [("s1", ctypes.c_ushort),
				("s2", ctypes.c_ushort),
				("sbin", ctypes.c_ushort),
				("p1", ctypes.c_ushort),
				("p2", ctypes.c_ushort),
				("pbin", ctypes.c_ushort)]

class md_frame_header(ctypes.Structure):
	# typedef struct md_frame_header
	# {                                 /* TOTAL: 48 bytes */
	#     uns32       signature;        /**< 4B - Equal to PL_MD_FRAME_SIGNATURE. */
	#     uns8        version;          /**< 1B - Must be 1 in the first release. */

	#     uns32       frameNr;          /**< 4B - 1-based, reset with each acquisition. */
	#     uns16       roiCount;         /**< 2B - Number of ROIs in the frame, at least 1. */

	#     /** The final timestamp = timestampBOF * timestampResNs (in nano-seconds). */
	#     uns32       timestampBOF;     /**< 4B - Depends on resolution. */
	#     uns32       timestampEOF;     /**< 4B - Depends on resolution. */
	#     uns32       timestampResNs;   /**< 4B - 1=1ns, 1000=1us, 5000000=5ms, ... */

	#     /** The final exposure time = exposureTime * exposureTimeResNs (nano-seconds). */
	#     uns32       exposureTime;     /**< 4B - Depends on resolution. */
	#     uns32       exposureTimeResNs;/**< 4B - 1=1ns, 1000=1us, 5000000=5ms, ... */

	#     /** ROI timestamp resolution is stored here, no need to transfer with each ROI. */
	#     uns32       roiTimestampResNs;/**< 4B - ROI timestamps resolution. */

	#     uns8        bitDepth;         /**< 1B - Must be 10, 13, 14, 16, etc. */
	#     uns8        colorMask;        /**< 1B - Corresponds to PL_COLOR_MODES. */
	#     uns8        flags;            /**< 1B - Frame flags, see PL_MD_FRAME_FLAGS. */
	#     uns16       extendedMdSize;   /**< 2B - Must be 0 or actual ext md data size. */
	#     uns8        _reserved[8];
	# }
	# md_frame_header;
	_fields_ = [("signature", ctypes.c_uint),
				("version", ctypes.c_ubyte),
				("frameNr", ctypes.c_uint),
				("roiCount", ctypes.c_ushort),
				("timestampBOF", ctypes.c_uint),
				("timestampEOF", ctypes.c_uint),
				("timestampResNs", ctypes.c_uint),
				("exposureTime", ctypes.c_uint),
				("exposureTimeResNs", ctypes.c_uint),
				("roiTimestampResNs", ctypes.c_uint),
				("bitDepth", ctypes.c_ubyte),
				("colorMask", ctypes.c_ubyte),
				("flags", ctypes.c_ubyte),
				("extendedMdSize", ctypes.c_ushort),
				("_reserved", ctypes.c_ubyte * 8)]

class md_frame_roi_header(ctypes.Structure):
	# typedef struct md_frame_roi_header
	# {                              /* TOTAL: 32 bytes */
	#     uns16    roiNr;            /**< 2B - 1-based, reset with each frame. */

	#     /** The final timestamp = timestampBOR * roiTimestampResNs. */
	#     uns32    timestampBOR;     /**< 4B - Depends on md_frame_header.roiTimestampResNs. */
	#     uns32    timestampEOR;     /**< 4B - Depends on md_frame_header.roiTimestampResNs. */

	#     rgn_type roi;              /**< 12B - ROI coordinates and binning. */

	#     uns8     flags;            /**< 1B - ROI flags, see PL_MD_ROI_FLAGS. */
	#     uns16    extendedMdSize;   /**< 2B - Must be 0 or actual ext md data size in bytes. */
	#     uns8    _reserved[7];
	# }
	# md_frame_roi_header;
	_fields_ = [("roiNr", ctypes.c_ushort),
				("timestampBOR", ctypes.c_uint),
				("timestampBOR", ctypes.c_uint),
				("roi", rgn_type),
				("flags", ctypes.c_ubyte),
				("extendedMdSize", ctypes.c_ushort),
				("_reserved", ctypes.c_ubyte * 7)]

class md_frame_roi(ctypes.Structure):
	# typedef struct md_frame_roi
	# {
	#     md_frame_roi_header*    header;         /**< Points directly to the header within the buffer. */
	#     void*                   data;           /**< Points to the ROI image data. */
	#     uns32                   dataSize;       /**< Size of the ROI image data in bytes. */
	#     void*                   extMdData;      /**< Points directly to ext/ MD data within the buffer. */
	#     uns16                   extMdDataSize;  /**< Size of the ext. MD buffer. */
	# }
	# md_frame_roi;
	_fields_ = [("header", ctypes.POINTER(md_frame_roi_header)),
				("data", ctypes.c_void_p),
				("dataSize", ctypes.c_uint),
				("extMdData", ctypes.c_void_p),
				("extMdDataSize", ctypes.c_ushort)]

class md_frame(ctypes.Structure):
	# typedef struct md_frame
	# {
	#     md_frame_header*     header;       /**< Points directly to the header withing the buffer. */
	#     void*                extMdData;    /**< Points directly to ext/ MD data within the buffer. */
	#     uns16                extMdDataSize;/**< Size of the ext. MD buffer in bytes. */
	#     rgn_type             impliedRoi;   /**< Implied ROI calculated during decoding. */

	#     md_frame_roi*        roiArray;     /**< An array of ROI descriptors. */
	#     uns16                roiCapacity;  /**< Number of ROIs the structure can hold. */
	#     uns16                roiCount;     /**< Number of ROIs found during decoding. */
	# }
	# md_frame;
	_fields_ = [("header", ctypes.POINTER(md_frame_header)),
				("extMdData", ctypes.c_void_p),
				("extMdDataSize", ctypes.c_ushort),
				("impliedRoi", rgn_type),
				("roiArray", ctypes.POINTER(md_frame_roi)),
				("roiCapacity", ctypes.c_ushort),
				("roiCount", ctypes.c_ushort)]

class md_ext_item_info(ctypes.Structure):
	# typedef enum PL_MD_EXT_TAGS
	# {
	#     PL_MD_EXT_TAG_PARTICLE_ID = 0,
	#     PL_MD_EXT_TAG_PARTICLE_M0,
	#     PL_MD_EXT_TAG_PARTICLE_M2,
	#     PL_MD_EXT_TAG_MAX
	# }
	# PL_MD_EXT_TAGS;
	# typedef struct md_ext_item_info
	# {
	#     PL_MD_EXT_TAGS tag;
	#     uns16          type;
	#     uns16          size;
	#     const char*    name;
	# }
	# md_ext_item_info;
	_fields_ = [("tag", ctypes.c_int),
				("type", ctypes.c_ushort),
				("size", ctypes.c_ushort),
				("name", ctypes.c_char_p)]

class md_ext_item(ctypes.Structure):
	# typedef struct md_ext_item
	# {
	#     const md_ext_item_info* tagInfo;
	#     void*                   value;
	# }
	# md_ext_item;
	_fields_ = [("tagInfo", ctypes.POINTER(md_ext_item_info)),
				("value", ctypes.c_void_p)]

class md_ext_item_collection(ctypes.Structure):
	# #define PL_MD_EXT_TAGS_MAX_SUPPORTED 255
	# typedef struct md_ext_item_collection
	# {
	#     md_ext_item     list[PL_MD_EXT_TAGS_MAX_SUPPORTED];
	#     md_ext_item*    map[PL_MD_EXT_TAGS_MAX_SUPPORTED];
	#     uns16           count;
	# }
	# md_ext_item_collection;
	_fields_ = [("list", md_ext_item * 255),
				("map", ctypes.POINTER(md_ext_item) * 255),
				("count", ctypes.c_ushort)]

# Camera Communications Function Prototypes

# rs_bool PV_DECL pl_pvcam_get_ver(uns16* pvcam_version);
pl_pvcam_get_ver = pvcam.pl_pvcam_get_ver
pl_pvcam_get_ver.argtypes = [ctypes.POINTER(ctypes.c_ushort)]
pl_pvcam_get_ver.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_pvcam_init(void);
pl_pvcam_init = pvcam.pl_pvcam_init
pl_pvcam_init.argtypes = None
pl_pvcam_init.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_pvcam_uninit(void);
pl_pvcam_uninit = pvcam.pl_pvcam_uninit
pl_pvcam_uninit.argtypes = None
pl_pvcam_uninit.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_cam_close(int16 hcam);
pl_cam_close = pvcam.pl_cam_close
pl_cam_close.argtypes = [ctypes.c_short]
pl_cam_close.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_cam_get_name(int16 cam_num, char* camera_name);
pl_cam_get_name = pvcam.pl_cam_get_name
pl_cam_get_name.argtypes = [ctypes.c_short, ctypes.c_char_p]
pl_cam_get_name.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_cam_get_total(int16* totl_cams);
pl_cam_get_total = pvcam.pl_cam_get_total
pl_cam_get_total.argtypes = [ctypes.POINTER(ctypes.c_short)]
pl_cam_get_total.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_cam_open(char* camera_name, int16* hcam, int16 o_mode);
pl_cam_open = pvcam.pl_cam_open
pl_cam_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_short), ctypes.c_short]
pl_cam_open.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_cam_register_callback_ex3(int16 hcam, int32 callback_event, void* callback, void* context);
pl_cam_register_callback_ex3 = pvcam.pl_cam_register_callback_ex3
pl_cam_register_callback_ex3.argtypes = [ctypes.c_short, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
pl_cam_register_callback_ex3.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_cam_deregister_callback(int16 hcam, int32 callback_event);
pl_cam_deregister_callback = pvcam.pl_cam_deregister_callback
pl_cam_deregister_callback.argtypes = [ctypes.c_short, ctypes.c_int]
pl_cam_deregister_callback.restype = ctypes.c_ushort

# Error Reporting Function Prototypes
# int16   PV_DECL pl_error_code(void);
pl_error_code = pvcam.pl_error_code
pl_error_code.argtypes = None
pl_error_code.restype = ctypes.c_short
# rs_bool PV_DECL pl_error_message(int16 err_code, char* msg);
pl_error_message = pvcam.pl_error_message
pl_error_message.argtypes = [ctypes.c_short, ctypes.c_char_p]
pl_error_message.restype = ctypes.c_ushort

# Configuration/Setup Function Prototypes
# rs_bool PV_DECL pl_get_param(int16 hcam, uns32 param_id, int16 param_attribute, void* param_value);
pl_get_param = pvcam.pl_get_param
pl_get_param.argtypes = [ctypes.c_short, ctypes.c_uint, ctypes.c_short, ctypes.c_void_p]
pl_get_param.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_set_param(int16 hcam, uns32 param_id, void* param_value);
pl_set_param = pvcam.pl_set_param
pl_set_param.argtypes = [ctypes.c_short, ctypes.c_uint, ctypes.c_void_p]
pl_set_param.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_get_enum_param(int16 hcam, uns32 param_id, uns32 index, int32* value, char* desc, uns32 length);
pl_get_enum_param = pvcam.pl_get_enum_param
pl_get_enum_param.argtypes = [ctypes.c_short, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_uint]
pl_get_enum_param.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_enum_str_length(int16 hcam, uns32 param_id, uns32 index, uns32* length);
pl_enum_str_length = pvcam.pl_enum_str_length
pl_enum_str_length.argtypes = [ctypes.c_short, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_uint)]
pl_enum_str_length.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_pp_reset(int16 hcam);
pl_pp_reset = pvcam.pl_pp_reset
pl_pp_reset.argtypes = [ctypes.c_short]
pl_pp_reset.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_create_smart_stream_struct(smart_stream_type** array, uns16 entries);
pl_create_smart_stream_struct = pvcam.pl_create_smart_stream_struct
pl_create_smart_stream_struct.argtypes = [ctypes.POINTER(ctypes.POINTER(smart_stream_type)), ctypes.c_ushort]
pl_create_smart_stream_struct.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_release_smart_stream_struct(smart_stream_type** array);
pl_release_smart_stream_struct = pvcam.pl_release_smart_stream_struct
pl_release_smart_stream_struct.argtypes = [ctypes.POINTER(ctypes.POINTER(smart_stream_type))]
pl_release_smart_stream_struct.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_create_frame_info_struct(FRAME_INFO** new_frame);
pl_create_frame_info_struct = pvcam.pl_create_frame_info_struct
pl_create_frame_info_struct.argtypes = [ctypes.POINTER(ctypes.POINTER(FRAME_INFO))]
pl_create_frame_info_struct.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_release_frame_info_struct(FRAME_INFO* frame_to_delete);
pl_release_frame_info_struct = pvcam.pl_release_frame_info_struct
pl_release_frame_info_struct.argtypes = [ctypes.POINTER(FRAME_INFO)]
pl_release_frame_info_struct.restype = ctypes.c_ushort

# Data Acquisition Function Prototypes
# rs_bool PV_DECL pl_exp_setup_seq(int16 hcam, uns16 exp_total, uns16 rgn_total, const rgn_type* rgn_array, int16 exp_mode, uns32 exposure_time, uns32* exp_bytes);
pl_exp_setup_seq = pvcam.pl_exp_setup_seq
pl_exp_setup_seq.argtypes = [ctypes.c_short, ctypes.c_ushort, ctypes.c_ushort, ctypes.POINTER(rgn_type), ctypes.c_short, ctypes.c_uint, ctypes.POINTER(ctypes.c_uint)]
pl_exp_setup_seq.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_start_seq(int16 hcam, void* pixel_stream);
pl_exp_start_seq = pvcam.pl_exp_start_seq
pl_exp_start_seq.argtypes = [ctypes.c_short, ctypes.c_void_p]
pl_exp_start_seq.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_setup_cont(int16 hcam, uns16 rgn_total, const rgn_type* rgn_array, int16 exp_mode, uns32 exposure_time, uns32* exp_bytes, int16 buffer_mode);
pl_exp_setup_cont = pvcam.pl_exp_setup_cont
pl_exp_setup_cont.argtypes = [ctypes.c_short, ctypes.c_ushort, ctypes.POINTER(rgn_type), ctypes.c_short, ctypes.c_uint, ctypes.POINTER(ctypes.c_uint), ctypes.c_short]
pl_exp_setup_cont.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_start_cont(int16 hcam, void* pixel_stream, uns32 size);
pl_exp_start_cont = pvcam.pl_exp_start_cont
pl_exp_start_cont.argtypes = [ctypes.c_short, ctypes.c_void_p, ctypes.c_uint]
pl_exp_start_cont.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_check_status(int16 hcam, int16* status, uns32* bytes_arrived);
pl_exp_check_status = pvcam.pl_exp_check_status
pl_exp_check_status.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_uint)]
pl_exp_check_status.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_check_cont_status(int16 hcam, int16* status, uns32* bytes_arrived, uns32* buffer_cnt);
pl_exp_check_cont_status = pvcam.pl_exp_check_cont_status
pl_exp_check_cont_status.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint)]
pl_exp_check_cont_status.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_check_cont_status_ex(int16 hcam, int16* status, uns32* byte_cnt, uns32* buffer_cnt, FRAME_INFO* frame_info);
pl_exp_check_cont_status_ex = pvcam.pl_exp_check_cont_status_ex
pl_exp_check_cont_status_ex.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(FRAME_INFO)]
pl_exp_check_cont_status_ex.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_get_latest_frame(int16 hcam, void** frame);
pl_exp_get_latest_frame = pvcam.pl_exp_get_latest_frame
pl_exp_get_latest_frame.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_void_p)]
pl_exp_get_latest_frame.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_get_latest_frame_ex(int16 hcam, void** frame, FRAME_INFO* frame_info);
pl_exp_get_latest_frame_ex = pvcam.pl_exp_get_latest_frame_ex
pl_exp_get_latest_frame_ex.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(FRAME_INFO)]
pl_exp_get_latest_frame_ex.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_get_oldest_frame(int16 hcam, void** frame);
pl_exp_get_oldest_frame = pvcam.pl_exp_get_oldest_frame
pl_exp_get_oldest_frame.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_void_p)]
pl_exp_get_oldest_frame.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_get_oldest_frame_ex(int16 hcam, void** frame, FRAME_INFO* frame_info);
pl_exp_get_oldest_frame_ex = pvcam.pl_exp_get_oldest_frame_ex
pl_exp_get_oldest_frame_ex.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(FRAME_INFO)]
pl_exp_get_oldest_frame_ex.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_unlock_oldest_frame(int16 hcam);
pl_exp_unlock_oldest_frame = pvcam.pl_exp_unlock_oldest_frame
pl_exp_unlock_oldest_frame.argtypes = [ctypes.c_short]
pl_exp_unlock_oldest_frame.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_stop_cont(int16 hcam, int16 cam_state);
pl_exp_stop_cont = pvcam.pl_exp_stop_cont
pl_exp_stop_cont.argtypes = [ctypes.c_short, ctypes.c_short]
pl_exp_stop_cont.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_abort(int16 hcam, int16 cam_state);
pl_exp_abort = pvcam.pl_exp_abort
pl_exp_abort.argtypes = [ctypes.c_short, ctypes.c_short]
pl_exp_abort.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_exp_finish_seq(int16 hcam, void* pixel_stream, int16 hbuf);
pl_exp_finish_seq = pvcam.pl_exp_finish_seq
pl_exp_finish_seq.argtypes = [ctypes.c_short, ctypes.c_void_p, ctypes.c_short]
pl_exp_finish_seq.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_io_script_control(int16 hcam, uns16 addr, flt64 state, uns32 location);
pl_io_script_control = pvcam.pl_io_script_control
pl_io_script_control.argtypes = [ctypes.c_short, ctypes.c_ushort, ctypes.c_float, ctypes.c_uint]
pl_io_script_control.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_io_clear_script_control(int16 hcam);
pl_io_clear_script_control = pvcam.pl_io_clear_script_control
pl_io_clear_script_control.argtypes = [ctypes.c_short]
pl_io_clear_script_control.restype = ctypes.c_ushort

# Frame metadata functions
# rs_bool PV_DECL pl_md_frame_decode(md_frame* pDstFrame, void* pSrcBuf, uns32 srcBufSize);
pl_md_frame_decode = pvcam.pl_md_frame_decode
pl_md_frame_decode.argtypes = [ctypes.POINTER(md_frame), ctypes.c_void_p, ctypes.c_uint]
pl_md_frame_decode.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_md_frame_recompose(void* pDstBuf, uns16 offX, uns16 offY, uns16 dstWidth, uns16 dstHeight, md_frame* pSrcFrame);
pl_md_frame_recompose = pvcam.pl_md_frame_recompose
pl_md_frame_recompose.argtypes = [ctypes.c_void_p, ctypes.c_ushort, ctypes.c_ushort, ctypes.c_ushort, ctypes.c_ushort, ctypes.POINTER(md_frame)]
pl_md_frame_recompose.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_md_create_frame_struct_cont(md_frame** pFrame, uns16 roiCount);
pl_md_create_frame_struct_cont = pvcam.pl_md_create_frame_struct_cont
pl_md_create_frame_struct_cont.argtypes = [ctypes.POINTER(ctypes.POINTER(md_frame)), ctypes.c_ushort]
pl_md_create_frame_struct_cont.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_md_create_frame_struct(md_frame** pFrame, void* pSrcBuf, uns32 srcBufSize);
pl_md_create_frame_struct = pvcam.pl_md_create_frame_struct
pl_md_create_frame_struct.argtypes = [ctypes.POINTER(ctypes.POINTER(md_frame)), ctypes.c_void_p, ctypes.c_uint]
pl_md_create_frame_struct.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_md_release_frame_struct(md_frame* pFrame);
pl_md_release_frame_struct = pvcam.pl_md_release_frame_struct
pl_md_release_frame_struct.argtypes = [ctypes.POINTER(ctypes.POINTER(md_frame))]
pl_md_release_frame_struct.restype = ctypes.c_ushort
# rs_bool PV_DECL pl_md_read_extended(md_ext_item_collection* pOutput, void* pExtMdPtr, uns32 extMdSize);
pl_md_read_extended = pvcam.pl_md_read_extended
pl_md_read_extended.argtypes = [ctypes.POINTER(md_ext_item_collection), ctypes.c_void_p, ctypes.c_uint]
pl_md_read_extended.restype = ctypes.c_ushort

