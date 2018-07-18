import ctypes

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

def Functions(dll):
	# Camera Communications Function Prototypes
	
	# rs_bool PV_DECL pl_pvcam_get_ver(uns16* pvcam_version);
	dll.pl_pvcam_get_ver.argtypes = [ctypes.POINTER(ctypes.c_ushort)]
	dll.pl_pvcam_get_ver.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_pvcam_init(void);
	dll.pl_pvcam_init.argtypes = None
	dll.pl_pvcam_init.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_pvcam_uninit(void);
	dll.pl_pvcam_uninit.argtypes = None
	dll.pl_pvcam_uninit.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_cam_close(int16 hcam);
	dll.pl_cam_close.argtypes = [ctypes.c_short]
	dll.pl_cam_close.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_cam_get_name(int16 cam_num, char* camera_name);
	dll.pl_cam_get_name.argtypes = [ctypes.c_short, ctypes.c_char_p]
	dll.pl_cam_get_name.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_cam_get_total(int16* totl_cams);
	dll.pl_cam_get_total.argtypes = [ctypes.POINTER(ctypes.c_short)]
	dll.pl_cam_get_total.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_cam_open(char* camera_name, int16* hcam, int16 o_mode);
	dll.pl_cam_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_short), ctypes.c_short]
	dll.pl_cam_open.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_cam_register_callback_ex3(int16 hcam, int32 callback_event, void* callback, void* context);
	dll.pl_cam_register_callback_ex3.argtypes = [ctypes.c_short, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
	dll.pl_cam_register_callback_ex3.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_cam_deregister_callback(int16 hcam, int32 callback_event);
	dll.pl_cam_deregister_callback.argtypes = [ctypes.c_short, ctypes.c_int]
	dll.pl_cam_deregister_callback.restype = ctypes.c_ushort
	
	# Error Reporting Function Prototypes
	# int16   PV_DECL pl_error_code(void);
	dll.pl_error_code.argtypes = None
	dll.pl_error_code.restype = ctypes.c_short
	# rs_bool PV_DECL pl_error_message(int16 err_code, char* msg);
	dll.pl_error_message.argtypes = [ctypes.c_short, ctypes.c_char_p]
	dll.pl_error_message.restype = ctypes.c_ushort
	
	# Configuration/Setup Function Prototypes
	# rs_bool PV_DECL pl_get_param(int16 hcam, uns32 param_id, int16 param_attribute, void* param_value);
	dll.pl_get_param.argtypes = [ctypes.c_short, ctypes.c_uint, ctypes.c_short, ctypes.c_void_p]
	dll.pl_get_param.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_set_param(int16 hcam, uns32 param_id, void* param_value);
	dll.pl_set_param.argtypes = [ctypes.c_short, ctypes.c_uint, ctypes.c_void_p]
	dll.pl_set_param.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_get_enum_param(int16 hcam, uns32 param_id, uns32 index, int32* value, char* desc, uns32 length);
	dll.pl_get_enum_param.argtypes = [ctypes.c_short, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_uint]
	dll.pl_get_enum_param.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_enum_str_length(int16 hcam, uns32 param_id, uns32 index, uns32* length);
	dll.pl_enum_str_length.argtypes = [ctypes.c_short, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_uint)]
	dll.pl_enum_str_length.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_pp_reset(int16 hcam);
	dll.pl_pp_reset.argtypes = [ctypes.c_short]
	dll.pl_pp_reset.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_create_smart_stream_struct(smart_stream_type** array, uns16 entries);
	dll.pl_create_smart_stream_struct.argtypes = [ctypes.POINTER(ctypes.POINTER(smart_stream_type)), ctypes.c_ushort]
	dll.pl_create_smart_stream_struct.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_release_smart_stream_struct(smart_stream_type** array);
	dll.pl_release_smart_stream_struct.argtypes = [ctypes.POINTER(ctypes.POINTER(smart_stream_type))]
	dll.pl_release_smart_stream_struct.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_create_frame_info_struct(FRAME_INFO** new_frame);
	dll.pl_create_frame_info_struct.argtypes = [ctypes.POINTER(ctypes.POINTER(FRAME_INFO))]
	dll.pl_create_frame_info_struct.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_release_frame_info_struct(FRAME_INFO* frame_to_delete);
	dll.pl_release_frame_info_struct.argtypes = [ctypes.POINTER(FRAME_INFO)]
	dll.pl_release_frame_info_struct.restype = ctypes.c_ushort
	
	# Data Acquisition Function Prototypes
	# rs_bool PV_DECL pl_exp_setup_seq(int16 hcam, uns16 exp_total, uns16 rgn_total, const rgn_type* rgn_array, int16 exp_mode, uns32 exposure_time, uns32* exp_bytes);
	dll.pl_exp_setup_seq.argtypes = [ctypes.c_short, ctypes.c_ushort, ctypes.c_ushort, ctypes.POINTER(rgn_type), ctypes.c_short, ctypes.c_uint, ctypes.POINTER(ctypes.c_uint)]
	dll.pl_exp_setup_seq.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_start_seq(int16 hcam, void* pixel_stream);
	dll.pl_exp_start_seq.argtypes = [ctypes.c_short, ctypes.c_void_p]
	dll.pl_exp_start_seq.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_setup_cont(int16 hcam, uns16 rgn_total, const rgn_type* rgn_array, int16 exp_mode, uns32 exposure_time, uns32* exp_bytes, int16 buffer_mode);
	dll.pl_exp_setup_cont.argtypes = [ctypes.c_short, ctypes.c_ushort, ctypes.POINTER(rgn_type), ctypes.c_short, ctypes.c_uint, ctypes.POINTER(ctypes.c_uint), ctypes.c_short]
	dll.pl_exp_setup_cont.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_start_cont(int16 hcam, void* pixel_stream, uns32 size);
	dll.pl_exp_start_cont.argtypes = [ctypes.c_short, ctypes.c_void_p, ctypes.c_uint]
	dll.pl_exp_start_cont.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_check_status(int16 hcam, int16* status, uns32* bytes_arrived);
	dll.pl_exp_check_status.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_uint)]
	dll.pl_exp_check_status.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_check_cont_status(int16 hcam, int16* status, uns32* bytes_arrived, uns32* buffer_cnt);
	dll.pl_exp_check_cont_status.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint)]
	dll.pl_exp_check_cont_status.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_check_cont_status_ex(int16 hcam, int16* status, uns32* byte_cnt, uns32* buffer_cnt, FRAME_INFO* frame_info);
	dll.pl_exp_check_cont_status_ex.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_short), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(FRAME_INFO)]
	dll.pl_exp_check_cont_status_ex.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_get_latest_frame(int16 hcam, void** frame);
	dll.pl_exp_get_latest_frame.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_void_p)]
	dll.pl_exp_get_latest_frame.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_get_latest_frame_ex(int16 hcam, void** frame, FRAME_INFO* frame_info);
	dll.pl_exp_get_latest_frame_ex.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(FRAME_INFO)]
	dll.pl_exp_get_latest_frame_ex.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_get_oldest_frame(int16 hcam, void** frame);
	dll.pl_exp_get_oldest_frame.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_void_p)]
	dll.pl_exp_get_oldest_frame.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_get_oldest_frame_ex(int16 hcam, void** frame, FRAME_INFO* frame_info);
	dll.pl_exp_get_oldest_frame_ex.argtypes = [ctypes.c_short, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(FRAME_INFO)]
	dll.pl_exp_get_oldest_frame_ex.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_unlock_oldest_frame(int16 hcam);
	dll.pl_exp_unlock_oldest_frame.argtypes = [ctypes.c_short]
	dll.pl_exp_unlock_oldest_frame.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_stop_cont(int16 hcam, int16 cam_state);
	dll.pl_exp_stop_cont.argtypes = [ctypes.c_short, ctypes.c_short]
	dll.pl_exp_stop_cont.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_abort(int16 hcam, int16 cam_state);
	dll.pl_exp_abort.argtypes = [ctypes.c_short, ctypes.c_short]
	dll.pl_exp_abort.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_exp_finish_seq(int16 hcam, void* pixel_stream, int16 hbuf);
	dll.pl_exp_finish_seq.argtypes = [ctypes.c_short, ctypes.c_void_p, ctypes.c_short]
	dll.pl_exp_finish_seq.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_io_script_control(int16 hcam, uns16 addr, flt64 state, uns32 location);
	dll.pl_io_script_control.argtypes = [ctypes.c_short, ctypes.c_ushort, ctypes.c_float, ctypes.c_uint]
	dll.pl_io_script_control.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_io_clear_script_control(int16 hcam);
	dll.pl_io_clear_script_control.argtypes = [ctypes.c_short]
	dll.pl_io_clear_script_control.restype = ctypes.c_ushort
	
	# Frame metadata functions
	# rs_bool PV_DECL pl_md_frame_decode(md_frame* pDstFrame, void* pSrcBuf, uns32 srcBufSize);
	dll.pl_md_frame_decode.argtypes = [ctypes.POINTER(md_frame), ctypes.c_void_p, ctypes.c_uint]
	dll.pl_md_frame_decode.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_md_frame_recompose(void* pDstBuf, uns16 offX, uns16 offY, uns16 dstWidth, uns16 dstHeight, md_frame* pSrcFrame);
	dll.pl_md_frame_recompose.argtypes = [ctypes.c_void_p, ctypes.c_ushort, ctypes.c_ushort, ctypes.c_ushort, ctypes.c_ushort, ctypes.POINTER(md_frame)]
	dll.pl_md_frame_recompose.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_md_create_frame_struct_cont(md_frame** pFrame, uns16 roiCount);
	dll.pl_md_create_frame_struct_cont.argtypes = [ctypes.POINTER(ctypes.POINTER(md_frame)), ctypes.c_ushort]
	dll.pl_md_create_frame_struct_cont.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_md_create_frame_struct(md_frame** pFrame, void* pSrcBuf, uns32 srcBufSize);
	dll.pl_md_create_frame_struct.argtypes = [ctypes.POINTER(ctypes.POINTER(md_frame)), ctypes.c_void_p, ctypes.c_uint]
	dll.pl_md_create_frame_struct.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_md_release_frame_struct(md_frame* pFrame);
	dll.pl_md_release_frame_struct.argtypes = [ctypes.POINTER(ctypes.POINTER(md_frame))]
	dll.pl_md_release_frame_struct.restype = ctypes.c_ushort
	# rs_bool PV_DECL pl_md_read_extended(md_ext_item_collection* pOutput, void* pExtMdPtr, uns32 extMdSize);
	dll.pl_md_read_extended.argtypes = [ctypes.POINTER(md_ext_item_collection), ctypes.c_void_p, ctypes.c_uint]
	dll.pl_md_read_extended.restype = ctypes.c_ushort

