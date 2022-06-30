"""
 Copyright (C) 2018 Xilinx, Inc
 Author(s): Ryan Radjabi
            Shivangi Agarwal
            Sonal Santan
 ctypes based Python binding for XRT

 Licensed under the Apache License, Version 2.0 (the "License"). You may
 not use this file except in compliance with the License. A copy of the
 License is located at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 License for the specific language governing permissions and limitations
 under the License.
"""

import ctypes
import os
import warnings
from .xclbin import *
from numbers import Integral

libc = None
XRT_SUPPORTED = False

if 'XILINX_XRT' in os.environ:
    XRT_SUPPORTED = True
    XRT_EMULATION = False
    xrt_path = os.environ['XILINX_XRT']
    libcoreutil = ctypes.CDLL(xrt_path + "/lib/libxrt_coreutil.so")
    libc = ctypes.CDLL(xrt_path + "/lib/libxrt_core.so")

    if "XCL_EMULATION_MODE" in os.environ:
        emulation_mode = os.environ["XCL_EMULATION_MODE"]
        if emulation_mode == "hw_emu":
            xrt_lib = os.path.join(
                xrt_path, 'lib', 'libxrt_hwemu.so')
            libc = ctypes.CDLL(xrt_lib)
            XRT_EMULATION = True
        elif emulation_mode == "sw_emu":
            warnings.warn("PYNQ doesn't support software emulation: either "
                          "unset XCL_EMULATION_MODE or set it hw_emu")
        else:
            warnings.warn("Unknown emulation mode: " + emulation_mode)

xclDeviceHandle = ctypes.c_void_p
xrtDeviceHandle = ctypes.c_void_p
xrtKernelHandle = ctypes.c_void_p
xrtXclbinHandle = ctypes.c_void_p
xrtRunHandle = ctypes.c_void_p
xrtKernelRunHandle = ctypes.c_void_p
xrtBufferHandle = ctypes.c_void_p
xrtBufferFlags = ctypes.c_ulonglong
xrtMemoryGroup = ctypes.c_uint


class xclDeviceInfo2(ctypes.Structure):
    # "_fields_" is a required keyword
    _fields_ = [
     ("mMagic", ctypes.c_uint),
     ("mName", ctypes.c_char*256),
     ("mHALMajorVersion", ctypes.c_ushort),
     ("mHALMinorVersion", ctypes.c_ushort),
     ("mVendorId", ctypes.c_ushort),
     ("mDeviceId", ctypes.c_ushort),
     ("mSubsystemId", ctypes.c_ushort),
     ("mSubsystemVendorId", ctypes.c_ushort),
     ("mDeviceVersion", ctypes.c_ushort),
     ("mDDRSize", ctypes.c_size_t),
     ("mDataAlignment", ctypes.c_size_t),
     ("mDDRFreeSize", ctypes.c_size_t),
     ("mMinTransferSize", ctypes.c_size_t),
     ("mDDRBankCount", ctypes.c_ushort),
     ("mOCLFrequency", ctypes.c_ushort*4),
     ("mPCIeLinkWidth", ctypes.c_ushort),
     ("mPCIeLinkSpeed", ctypes.c_ushort),
     ("mDMAThreads", ctypes.c_ushort),
     ("mOnChipTemp", ctypes.c_short),
     ("mFanTemp", ctypes.c_short),
     ("mVInt", ctypes.c_ushort),
     ("mVAux", ctypes.c_ushort),
     ("mVBram", ctypes.c_ushort),
     ("mCurrent", ctypes.c_float),
     ("mNumClocks", ctypes.c_ushort),
     ("mFanSpeed", ctypes.c_ushort),
     ("mMigCalib", ctypes.c_bool),
     ("mXMCVersion", ctypes.c_ulonglong),
     ("mMBVersion", ctypes.c_ulonglong),
     ("m12VPex", ctypes.c_short),
     ("m12VAux", ctypes.c_short),
     ("mPexCurr", ctypes.c_ulonglong),
     ("mAuxCurr", ctypes.c_ulonglong),
     ("mFanRpm", ctypes.c_ushort),
     ("mDimmTemp", ctypes.c_ushort*4),
     ("mSE98Temp", ctypes.c_ushort*4),
     ("m3v3Pex", ctypes.c_ushort),
     ("m3v3Aux", ctypes.c_ushort),
     ("mDDRVppBottom",ctypes.c_ushort),
     ("mDDRVppTop", ctypes.c_ushort),
     ("mSys5v5", ctypes.c_ushort),
     ("m1v2Top", ctypes.c_ushort),
     ("m1v8Top", ctypes.c_ushort),
     ("m0v85", ctypes.c_ushort),
     ("mMgt0v9", ctypes.c_ushort),
     ("m12vSW", ctypes.c_ushort),
     ("mMgtVtt", ctypes.c_ushort),
     ("m1v2Bottom", ctypes.c_ushort),
     ("mDriverVersion, ", ctypes.c_ulonglong),
     ("mPciSlot", ctypes.c_uint),
     ("mIsXPR", ctypes.c_bool),
     ("mTimeStamp", ctypes.c_ulonglong),
     ("mFpga", ctypes.c_char*256),
     ("mPCIeLinkWidthMax", ctypes.c_ushort),
     ("mPCIeLinkSpeedMax", ctypes.c_ushort),
     ("mVccIntVol", ctypes.c_ushort),
     ("mVccIntCurr", ctypes.c_ushort),
     ("mNumCDMA", ctypes.c_ushort)
    ]

class xclMemoryDomains:
    XCL_MEM_HOST_RAM    = 0
    XCL_MEM_DEVICE_RAM  = 1
    XCL_MEM_DEVICE_BRAM = 2
    XCL_MEM_SVM         = 3
    XCL_MEM_CMA         = 4
    XCL_MEM_DEVICE_REG  = 5

class xclDDRFlags:
    XCL_DEVICE_RAM_BANK0 = 0
    XCL_DEVICE_RAM_BANK1 = 2
    XCL_DEVICE_RAM_BANK2 = 4
    XCL_DEVICE_RAM_BANK3 = 8

class xclBOKind:
    XCL_BO_SHARED_VIRTUAL           = 0
    XCL_BO_SHARED_PHYSICAL          = 1
    XCL_BO_MIRRORED_VIRTUAL         = 2
    XCL_BO_DEVICE_RAM               = 3
    XCL_BO_DEVICE_BRAM              = 4
    XCL_BO_DEVICE_PREALLOCATED_BRAM = 5

class xclBOSyncDirection:
    XCL_BO_SYNC_BO_TO_DEVICE   = 0
    XCL_BO_SYNC_BO_FROM_DEVICE = 1

class xclAddressSpace:
    XCL_ADDR_SPACE_DEVICE_FLAT    = 0  # Absolute address space
    XCL_ADDR_SPACE_DEVICE_RAM     = 1  # Address space for the DDR memory
    XCL_ADDR_KERNEL_CTRL          = 2  # Address space for the OCL Region control port
    XCL_ADDR_SPACE_DEVICE_PERFMON = 3  # Address space for the Performance monitors
    XCL_ADDR_SPACE_DEVICE_CHECKER = 5  # Address space for protocol checker
    XCL_ADDR_SPACE_MAX = 8

class xclVerbosityLevel:
    XCL_QUIET = 0
    XCL_INFO  = 1
    XCL_WARN  = 2
    XCL_ERROR = 3

class xrtLogMsgLevel:
    XRT_EMERGENCY = 0
    XRT_ALERT     = 1
    XRT_CRITICAL  = 2
    XRT_ERROR     = 3
    XRT_WARNING   = 4
    XRT_NOTICE    = 5
    XRT_INFO      = 6
    XRT_DEBUG     = 7

class xclResetKind:
    XCL_RESET_KERNEL = 0
    XCL_RESET_FULL   = 1
    XCL_USER_RESET   = 2

class xclDeviceUsage (ctypes.Structure):
    _fields_ = [
     ("h2c", ctypes.c_size_t*8),
     ("c2h", ctypes.c_size_t*8),
     ("ddeMemUsed", ctypes.c_size_t*8),
     ("ddrBOAllocated", ctypes.c_uint *8),
     ("totalContents", ctypes.c_uint),
     ("xclbinId", ctypes.c_ulonglong),
     ("dma_channel_cnt", ctypes.c_uint),
     ("mm_channel_cnt", ctypes.c_uint),
     ("memSize", ctypes.c_ulonglong*8)
    ]

class xclBOProperties (ctypes.Structure):
    _fields_ = [
     ("handle", ctypes.c_uint),
     ("flags" , ctypes.c_uint),
     ("size", ctypes.c_ulonglong),
     ("paddr", ctypes.c_ulonglong),
     ("reserved", ctypes.c_uint), # not implemented
    ]

def xclProbe():
    """
    xclProbe() - Enumerate devices found in the system
    :return: count of devices found
    """
    return libc.xclProbe()

def xrtDeviceOpen(deviceIndex):
    """
    xrtDeviceOpen(): Open a device and obtain its xrt device handle
    :param deviceIndex: (unsigned int) Slot number of device 0 for first device, 1 for the second device...
    """
    libcoreutil.xrtDeviceOpen.restype = ctypes.POINTER(xrtDeviceHandle)
    libcoreutil.xrtDeviceOpen.argTypes = [ctypes.c_uint]
    return _valueOrError(libcoreutil.xrtDeviceOpen(deviceIndex))

def xrtDeviceOpenByBDF(bdf):
    """
    xrtDeviceOpenByBDF(): Open a device and obtain its xrt device handle
    :param bdf: (const char *bdf) PCIe BDF identifying the device to open
    """
    libcoreutil.xrtDeviceOpenByBDF.restype = ctypes.POINTER(xrtDeviceHandle)
    libcoreutil.xrtDeviceOpenByBDF.argTypes = [ctypes.c_char_p]
    return _valueOrError(libcoreutil.xrtDeviceOpenByBDF(bdf))

def xrtDeviceOpenFromXcl(xcldevhandler):
    """
    xrtDeviceOpenFromXcl(): Open a device from a shim xclDeviceHandle
    :param deviceIndex: (unsigned int) Slot number of device 0 for first device, 1 for the second device...
    """
    libcoreutil.xrtDeviceOpenFromXcl.restype = ctypes.POINTER(xrtDeviceHandle)
    libcoreutil.xrtDeviceOpenFromXcl.argTypes = ctypes.POINTER(xclDeviceHandle)
    return _valueOrError(libcoreutil.xrtDeviceOpenFromXcl(xcldevhandler))

def xclOpen(deviceIndex, logFileName, level):
    """
    xclOpen(): Open a device and obtain its handle
    :param deviceIndex: (unsigned int) Slot number of device 0 for first device, 1 for the second device...
    :param logFileName: (const char pointer) Log file to use for optional logging
    :param level: (int) Severity level of messages to log
    :return: device handle
    """
    libc.xclOpen.restype = ctypes.POINTER(xclDeviceHandle)
    libc.xclOpen.argtypes = [ctypes.c_uint, ctypes.c_char_p, ctypes.c_int]
    return libc.xclOpen(deviceIndex, logFileName, level)

def xrtXclbinGetUUID(xcldevhandler, ret_uuid):
    """
    xrtXclbinGetUUID(): Close an device handle opened with xrtDeviceOpen()
    :param handle: XRT device handle
    :return: 0 on success or appropriate error number
    """
    libcoreutil.xrtXclbinGetUUID.restype = ctypes.c_int
    libcoreutil.xrtXclbinGetUUID.argTypes = [ctypes.POINTER(xclDeviceHandle), ctypes.c_void_p]
    return _valueOrError(libcoreutil.xrtXclbinGetUUID(xcldevhandler, ret_uuid))

def xrtDeviceClose(handle):
    """
    xrtDeviceClose(): Close an device handle opened with xrtDeviceOpen()
    :param handle: XRT device handle
    :return: 0 on success or appropriate error number
    """
    libcoreutil.xrtDeviceClose.restype = ctypes.c_int
    libcoreutil.xrtDeviceClose.argTypes = [xrtDeviceHandle]
    return _valueOrError(libcoreutil.xrtDeviceClose(handle))

def xclGetDeviceInfo2(handle, info):
    """
    xclGetDeviceInfo2() - Obtain various bits of information from the device

    :param handle: (xclDeviceHandle) device handle
    :param info: (xclDeviceInfo pointer) Information record
    :return: 0 on success or appropriate error number
    """

    libc.xclGetDeviceInfo2.restype = ctypes.c_int
    libc.xclGetDeviceInfo2.argtypes = [xclDeviceHandle, ctypes.POINTER(xclDeviceInfo2)]
    return libc.xclGetDeviceInfo2(handle, info)

def xclGetUsageInfo(handle, info):
    """
    xclGetUsageInfo() - Obtain usage information from the device
    :param handle: Device handle
    :param info: Information record
    :return: 0 on success or appropriate error number
    """
    libc.xclGetUsageInfo.restype = ctypes.c_int
    libc.xclGetUsageInfo.argtypes = [xclDeviceHandle, ctypes.POINTER(xclDeviceInfo2)]
    return libc.xclGetUsageInfo(handle, info)

def xrtDeviceLoadXclbin(handle, buf):
    """
    xrtDeviceLoadXclbin(): Load an xclbin image
    :param handle: XRT device handle
    :param buf: Pointer to complete axlf in memory image
    :return: 0 on success or appropriate error number
    """
    libcoreutil.xrtDeviceLoadXclbin.restype = ctypes.c_int
    libcoreutil.xrtDeviceLoadXclbin.argTypes = [xrtDeviceHandle, ctypes.c_void_p]
    return _valueOrError(libcoreutil.xrtDeviceLoadXclbin(handle, buf))

def xrtBOAlloc(handle, size, flags, grp):
    """
    Allocate a BO of requested size with appropriate flags.
    :param handle: Device handle
    :param size: Size of buffer
    :param flags: Specify bank information, etc
    :param grp: Specify memory bank group ID
    :return: xrtBufferHandle on success or NULL
    """
    libc.xrtBOAlloc.restype = xrtBufferHandle
    libc.xrtBOAlloc.argtypes = [xclDeviceHandle, ctypes.c_size_t, xrtBufferFlags, xrtMemoryGroup]
    return libc.xrtBOAlloc(handle, size, flags, grp)

def xrtBOAllocUserPtr(handle, userptr, size, flags, grp):
    """
    Allocate a BO using userptr provided by the user.
    :param handle: Device handle
    :param userptr: Pointer to 4K aligned user memory
    :param size: Size of buffer
    :param flags: Specify bank information, etc
    :param grp: Specify memory bank group ID
    :return: xrtBufferHandle on success or NULL
    """
    libcoreutil.xrtBOAllocUserPtr.restype = xrtBufferHandle
    libcoreutil.xrtBOAllocUserPtr.argtypes = [xclDeviceHandle, ctypes.c_void_p, ctypes.c_size_t, xrtBufferFlags, xrtMemoryGroup]
    return libcoreutil.xrtBOAllocUserPtr(handle, userptr, size, flags, grp)

def xrtBOSubAlloc(parent, size, offset):
    """
    Allocate a sub buffer from a parent buffer
    :param parent: Parent buffer handle
    :param size: Size of sub buffer
    :param offset: Offset into parent buffer
    :return: xrtBufferHandle on success or NULL
    """
    libcoreutil.xrtBOSubAlloc.restype = xrtBufferHandle
    libcoreutil.xrtBOSubAlloc.argtypes = [xclDeviceHandle, ctypes.c_size_t, ctypes.c_size_t]
    return libcoreutil.xrtBOSubAlloc(parent, size, offset)

def xrtBOFree(bufhandle):
    """
    Free a previously allocated BO
    :param bufhandle: Buffer handle
    :return: 0 on success, or err code on error
    """
    libcoreutil.xrtBOFree.restype = ctypes.c_int
    libcoreutil.xrtBOFree.argtypes = [xrtBufferHandle]
    return _valueOrError(libcoreutil.xrtBOFree(bufhandle))

def xrtBOWrite(bufhandle, src, size, seek):
    """
    Copy-in user data to host backing storage of BO
    :param bufhandle: Buffer handle
    :param src: Source data pointer
    :param size: Size of data to copy
    :param seek: Offset within the BO
    :return: 0 on success, or err code on error
    Copy host buffer contents to previously allocated device
    memory. ``seek`` specifies how many bytes to skip at the beginning
    of the BO before copying-in ``size`` bytes of host buffer.
    """
    libcoreutil.xrtBOWrite.restype = ctypes.c_int
    libcoreutil.xrtBOWrite.argtypes = [xrtBufferHandle, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t]
    return _valueOrError(libcoreutil.xrtBOWrite(bufhandle, src, size, seek))

def xrtBORead(bufhandle, dst, size, skip):
    """
    Copy-out user data from host backing storage of BO
    :param bufhandle: Buffer handle
    :param src: Destination data pointer
    :param size: Size of data to copy
    :param skip: Offset within the BO
    :return: 0 on success, or err code on error
    Copy contents of previously allocated device memory to host buffer.
    ``skip`` specifies how many bytes to skip from the beginning of the BO
    before copying-out ``size`` bytes of device buffer.
    """
    libcoreutil.xrtBORead.restype = ctypes.c_int
    libcoreutil.xrtBORead.argtypes = [xrtBufferHandle, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t]
    return _valueOrError(libcoreutil.xrtBORead(bufhandle, dst, size, skip))

def xrtBOMap(bufhandle):
    """
    Memory map BO into user's address space
    :param bufhandle: Buffer handle
    :return: Memory mapped buffer, or NULL on error
    Map the contents of the buffer object into host memory
    To unmap the buffer call xclUnmapBO().
    """
    libcoreutil.xrtBOMap.restype = ctypes.c_void_p
    libcoreutil.xrtBOMap.argtypes = [xrtBufferHandle]
    return libcoreutil.xrtBOMap(bufhandle)

def xrtBOSync(bufhandle, direction, size, offset):
    """
    Synchronize buffer contents in requested direction
    :param bufhandle: Buffer handle
    :param direction: To device or from device
    :param size: Size of data to synchronize
    :param offset: Offset within the BO
    :return: 0 on success, or err code on error
    Synchronize the buffer contents between host and device. Depending
    on the memory model this may require DMA to/from device or CPU
    cache flushing/invalidation.
    """
    libcoreutil.xrtBOSync.restype = ctypes.c_int
    libcoreutil.xrtBOSync.argtypes = [xrtBufferHandle, ctypes.c_int, ctypes.c_size_t, ctypes.c_size_t]
    return _valueOrError(libcoreutil.xrtBOSync(bufhandle, direction, size, offset))

def xclGetBOProperties(handle, boHandle, properties):
    """
    Obtain xclBOProperties struct for a BO

    :param handle: (xclDeviceHandle) device handle
    :param boHandle: (unsigned int) BO handle
    :param properties: BO properties struct pointer
    :return: 0 on success
    """
    libc.xclGetBOProperties.restype = ctypes.c_int
    libc.xclGetBOProperties.argtypes = [xclDeviceHandle, ctypes.c_uint, ctypes.POINTER(xclBOProperties)]
    return libc.xclGetBOProperties(handle, boHandle, properties)

def xclWrite(handle, space, offset, hostBuf, size):
    """
    Perform register write operation
    :param handle:  Device handle
    :param space: Address space
    :param offset: Offset in the address space
    :param hostBuf: Source data pointer
    :param size: Size of data to copy
    :return: size of bytes written or appropriate error number

    This API may be used to write to device registers exposed on PCIe BAR. Offset is relative to the
    the address space. A device may have many address spaces.
    This API will be deprecated in future. Please use this API only for IP bringup/debugging. For
    execution management please use XRT Compute Unit Execution Management APIs defined below
    """
    libc.xclWrite.restype = ctypes.c_size_t
    libc.xclWrite.argtypes = [xclDeviceHandle, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_size_t]
    return libc.xclWrite(handle, space, offset, hostBuf, size)

def xclRead(handle, space, offset, hostBuf, size):
    """
    Perform register write operation
    :param handle:  Device handle
    :param space: Address space
    :param offset: Offset in the address space
    :param hostBuf: Destination data pointer
    :param size: Size of data to copy
    :return: size of bytes written or appropriate error number

    This API may be used to write to device registers exposed on PCIe BAR. Offset is relative to the
    the address space. A device may have many address spaces.
    This API will be deprecated in future. Please use this API only for IP bringup/debugging. For
    execution management please use XRT Compute Unit Execution Management APIs defined below
    """
    libc.xclRead.restype = ctypes.c_size_t
    libc.xclRead.argtypes = [xclDeviceHandle, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_size_t]
    return libc.xclRead(handle, space, offset, hostBuf, size)

def xclExecBuf(handle, cmdBO):
    """
    xclExecBuf() - Submit an execution request to the embedded (or software) scheduler
    :param handle: Device handle
    :param cmdBO: BO handle containing command packet
    :return: 0 or standard error number

    Submit an exec buffer for execution. The exec buffer layout is defined by struct ert_packet
    which is defined in file *ert.h*. The BO should been allocated with DRM_XOCL_BO_EXECBUF flag.
    """
    libc.xclExecBuf.restype = ctypes.c_int
    libc.xclExecBuf.argtypes = [xclDeviceHandle, ctypes.c_uint]
    return libc.xclExecBuf(handle, cmdBO)

def xclExecBufWithWaitList(handle, cmdBO, num_bo_in_wait_list, bo_wait_list):
    """
    Submit an execution request to the embedded (or software) scheduler
    :param handle: Device handle
    :param cmdBO:BO handle containing command packet
    :param num_bo_in_wait_list: Number of BO handles in wait list
    :param bo_wait_list: BO handles that must complete execution before cmdBO is started
    :return:0 or standard error number

    Submit an exec buffer for execution. The BO handles in the wait
    list must complete execution before cmdBO is started.  The BO
    handles in the wait list must have been submitted prior to this
    call to xclExecBufWithWaitList.
    """
    libc.xclExecBufWithWaitList.restype = ctypes.c_int
    libc.xclExecBufWithWaitList.argtypes = [xclDeviceHandle, ctypes.c_uint, ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint)]
    return libc.xclExecBufWithWaitList(handle, cmdBO, num_bo_in_wait_list, bo_wait_list)

def xrtKernelRun(khandle):
    """
    Start a kernel execution
    :param khandle: Handle to the kernel to run
    :return: Run handle which must be closed with xrtRunClose()
    A run handle is specific to one execution of a kernel. Once execution
    completes, the run handle can be re-used to execute the same kernel again.
    When no longer needed, then run handle must be closed with xrtRunClose()
    """
    libcoreutil.xrtKernelRun.restype = xrtRunHandle
    libcoreutil.xrtKernelRun.argtypes = [xrtKernelHandle]
    return libcoreutil.xrtKernelRun(khandle)

def xrtRunOpen(khandle):
    """
    Open a new run handle for a kernel without starting kernel
    :param khandle: Handle to the kernel to run
    :return: Run handle which must be closed with xrtRunClose()
    The handle can be used repeatedly to start an execution of the associated
    kernel. This API allows application to manage run handles without
    maintaining corresponding kernel handle.
    """
    libcoreutil.xrtRunOpen.restype = ctypes.c_int
    libcoreutil.xrtRunOpen.argtypes = [xrtKernelHandle]
    return libcoreutil.xrtRunOpen(khandle)

def xrtRunStart(rhandle):
    """
    Start existing run handle
    :param rhandle: Handle to the run object to start
    :return: 0 on success, -1 on error
    Use this API when re-using a run handle for more than one execution of
    the kernel associated with the run handle.
    """
    libcoreutil.xrtRunStart.restype = ctypes.c_int
    libcoreutil.xrtRunStart.argtypes = [xrtRunHandle]
    return libcoreutil.xrtRunStart(rhandle)

def xrtRunClose(rhandle):
    """
    Close a run handle
    :param rhandle: kernel run handle obtained in xrtKernelRun()
    :return: 0 or throw OSError with error code
    """
    libcoreutil.xrtRunClose.restype = ctypes.c_int
    libcoreutil.xrtRunClose.argtypes = [xrtRunHandle]
    res = libcoreutil.xrtRunClose(rhandle)
    if (res):
        res = errno.EINVAL
    return _valueOrError(-res)

def xrtRunWait(rhandle):
    """
    Wait for a kernel execution to finish
    :param rhandle: kernel run handle obtained in xrtKernelRun()
    :return: ert_cmd_state code
    Blocks current thread until job has completed
    """
    libcoreutil.xrtRunWait.restype = ctypes.c_int
    libcoreutil.xrtRunWait.argtypes = [xrtRunHandle]
    return libcoreutil.xrtRunWait(rhandle)

def xrtRunWaitFor(rhandle, timeout):
    """
    Wait for a run to complete
    :param rhandle: kernel run handle obtained in xrtKernelRun()
    :param timeout: timeout in millisecond
    :return: Run command state for completed run, or current status if timeout.
    Blocks current thread until job has completed
    """
    libcoreutil.xrtRunWaitFor.restype = ctypes.c_int
    libcoreutil.xrtRunWaitFor.argtypes = [xrtRunHandle, ctypes.c_uint]
    return libcoreutil.xrtRunWaitFor(rhandle, timeout)

def xrtRunState(rhandle):
    """
    Check the current state of a run
    :param rhandle: kernel run handle obtained in xrtKernelRun()
    :return: The underlying command execution state per ert.h
    """
    libcoreutil.xrtRunState.restype = ctypes.c_int
    libcoreutil.xrtRunState.argtypes = [xrtRunHandle]
    return libcoreutil.xrtRunState(rhandle, timeout)

def _valueOrError(res):
    """
    Validate return code from XRT C library and raise an exception if necessary
    """
    # check if result is some kind of integer
    # can't do a direct comparison with an int since some
    # functions return long and Python3 dropped support for long

    if isinstance(res, Integral):
        if res < 0:
            raise OSError(abs(res), os.strerror(abs(res)))
    # check if result type is a pointer. Python3 doesn't support pointer and int comparison
    elif isinstance(res.contents, ctypes.c_void_p) and res is None:
        raise OSError(errno.ENODEV, os.strerror(errno.ENODEV))
    return res

def xclIPName2Index(handle, name):
    """
    Obtain index of a kernel given its name.
    :param handle: Device handle
    :param name: Name of PL kernel
    :return: index of Kernel

    The index is used in APIs like xclOpenContext(), etc.
    """
    libc.xclIPName2Index.restype = ctypes.c_int
    libc.xclIPName2Index.argtypes = [xclDeviceHandle, ctypes.c_char_p]
    return _valueOrError(libc.xclIPName2Index(handle, name.encode()))

def xrtXclbinAllocFilename(filename):
    """
    xrtXclbinAllocFilename(): Allocate a xclbin using xclbin filename
    :param filename: path to the xclbin file
    :return: xrtXclbinHandle on success or NULL with errno set
    """
    libcoreutil.xrtXclbinAllocFilename.restype = xrtXclbinHandle
    libcoreutil.xrtXclbinAllocFilename.argTypes = ctypes.c_char_p
    return _valueOrError(libcoreutil.xrtXclbinAllocFilename(filename))

def xrtXclbinGetNumKernelComputeUnits(handle):
    """
    xrtXclbinGetNumKernelComputeUnits(): Get number of CUs in xclbin
    :param handle: Xclbin handle obtained from an xrtXclbinAlloc function
    :return: The number of compute units Compute units are associated with kernels. This function returns the total number of compute units as the sum of compute units over all kernels.
    """
    libcoreutil.xrtXclbinGetNumKernelComputeUnits.restype = ctypes.c_int
    libcoreutil.xrtXclbinGetNumKernelComputeUnits.argTypes = xrtXclbinHandle
    return _valueOrError(libcoreutil.xrtXclbinGetNumKernelComputeUnits(handle))

def xrtXclbinGetNumKernels(handle):
    """
    xrtXclbinGetNumKernels(): Get number of PL kernels in xclbin
    :param handle: Xclbin handle obtained from an xrtXclbinAlloc function
    :return: The number of PL kernels in the xclbin
    """
    libcoreutil.xrtXclbinGetNumKernels.restype = ctypes.c_int
    libcoreutil.xrtXclbinGetNumKernels.argTypes = xrtXclbinHandle
    return _valueOrError(libcoreutil.xrtXclbinGetNumKernels(handle))

def xrtPLKernelOpen(handle, xclbinId, name):
    """
    Open a PL kernel and obtain its handle
    :param handle: Device handle
    :param xclbinId: UUID of the xclbin image running on the device
    :param name: Name of PL kernel
    :return: Kernel handle which must be closed with xrtKernelClose()
    """
    libcoreutil.xrtPLKernelOpen.restype = ctypes.POINTER(xrtKernelHandle)
    libcoreutil.xrtPLKernelOpen.argtypes = [xclDeviceHandle, ctypes.c_char_p, ctypes.c_char_p]
    if isinstance(name, str):
        nm = str.encode(name)
    else:
        nm = name
    return _valueOrError(libcoreutil.xrtPLKernelOpen(handle, xclbinId.bytes, nm))

def xrtPLKernelOpenExclusive(handle, xclbinId, name):
    """
    Open a PL kernel and obtain its handle, exclusive access
    :param handle: Device handle
    :param xclbinId: UUID of the xclbin image running on the device
    :param name: Name of PL kernel
    :return: Kernel handle which must be closed with xrtKernelClose()
    """
    libcoreutil.xrtPLKernelOpenExclusive.restype = ctypes.POINTER(xrtKernelHandle)
    libcoreutil.xrtPLKernelOpenExclusive.argtypes = [xclDeviceHandle, ctypes.c_char_p, ctypes.c_char_p]
    if isinstance(name, str):
        nm = str.encode(name)
    else:
        nm = name
    return _valueOrError(libcoreutil.xrtPLKernelOpenExclusive(handle, xclbinId.bytes, nm))

def xrtKernelClose(khandle):
    """
    Close an opened kernel
    :param khandle: Kernel handle obtained in xrtPLKernelOpen()
    :return: 0 or raises an OSError exception
    """
    libcoreutil.xrtKernelClose.restype = ctypes.c_int
    libcoreutil.xrtKernelClose.argtypes = [xrtKernelHandle]
    res = libcoreutil.xrtKernelClose(khandle)
    if (res):
        res = errno.EINVAL
    return _valueOrError(-res);

def xrtKernelArgGroupId(khandle, argno):
    """
    Acquire bank group id for kernel argument
    :param khandle: Handle to kernel previously opened with xrtKernelOpen
    :param argno: Index of kernel argument
    :Return: Group id or negative error code on error
    A valid group id is a non-negative integer.  The group id is required
    when constructing a buffer object.
    The kernel argument group id is ambiguous if kernel has multiple kernel
    with different connectivity for specified argument.  In this case the
    API returns error.
    """
    libcoreutil.xrtKernelArgGroupId.restype = ctypes.c_int
    libcoreutil.xrtKernelArgGroupId.argtypes = [xrtKernelHandle, ctypes.c_int]
    return _valueOrError(libcoreutil.xrtKernelArgGroupId(khandle, argno))

def xrtKernelArgOffset(khandle, argno):
    """
    Get the offset of kernel argument
    :param khandle: Handle to kernel previously opened with xrtKernelOpen
    :param argno: Index of kernel argument
    :Return: The kernel register offset of the argument with specified index
    A valid group id is a non-negative integer.  The group id is required
    Use with :c:func:`xrtKernelReadRegister()` and 
    :c:func:`xrtKernelWriteRegister()` if manually reading or writing kernel
    registers for explicit arguments.
    """
    libcoreutil.xrtKernelArgOffset.restype = ctypes.c_int
    libcoreutil.xrtKernelArgOffset.argtypes = [xrtKernelHandle, ctypes.c_int]
    return _valueOrError(libcoreutil.xrtKernelArgOffset(khandle, argno))

def xrtKernelReadRegister(khandle, offset, data):
    """
    Read data from kernel address range
    :param khandle: Handle to kernel previously opened with xrtKernelOpen
    :param offset: Offset in register space to read from
    :param offset: Offset in register space to read from
    :Return: data: Pointer to location where to write data
    The kernel must be associated with exactly one kernel instance
    (compute unit), which must be opened for exclusive access.
    """
    libcoreutil.xrtKernelReadRegister.restype = ctypes.c_size_t
    libcoreutil.xrtKernelReadRegister.argtypes = [xrtKernelHandle, ctypes.c_uint32, ctypes.c_void_p]
    return _valueOrError(libcoreutil.xrtKernelReadRegister(khandle, offset, data))

def xrtKernelWriteRegister(khandle, offset, data):
    """
    Read data from kernel address range
    :param khandle: Handle to kernel previously opened with xrtKernelOpen
    :param offset: Offset in register space to read from
    :param offset: Offset in register space to read from
    :Return: data: Data to write
    The kernel must be associated with exactly one kernel instance
    (compute unit), which must be opened for exclusive access.
    """
    libcoreutil.xrtKernelWriteRegister.restype = ctypes.c_size_t
    libcoreutil.xrtKernelWriteRegister.argtypes = [xrtKernelHandle, ctypes.c_uint32, ctypes.c_uint32]
    return _valueOrError(libcoreutil.xrtKernelWriteRegister(khandle, offset, data))

def xrtKernelGetFunc(*args):
    """
    Obtain the callback function as defined below to start a kernel execution:
        First argument is kernel handle obtained in xrtPLKernelOpen()
        Followed by variable number of kernel arguments
        Returns run handle which must be closed with xrtRunClose()
    After obtain the callback function, it can be called as:
        func(kernel_handle, arg0, arg1, ...)
    :param args: variable number of kernel argument ctypes for this kernel
                 (kernel handle is not included)
    :return: python function that can be called with specific kernel arguments
             to start the kernel specified by the kernel handle
    """
    types = [xrtKernelHandle]
    for argtype in args:
        types.append(argtype)
    proto = ctypes.CFUNCTYPE(xrtKernelRunHandle, *types)
    func = proto(("xrtKernelRun", libcoreutil))
    return func
