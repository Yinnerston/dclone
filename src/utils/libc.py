import ctypes
import ctypes.util
import os

class LibcWrapper():
    # static variable for libc util
    libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
    libc.mount.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_ulong, ctypes.c_char_p)

    def __init__(self) -> None:
        pass

    def mount(source, target, fs, options=''):
        ret = LibcWrapper.libc.mount(source.encode(), target.encode(), fs.encode(), 0, options.encode())
        if ret < 0:
            errno = ctypes.get_errno()
            raise OSError(errno, f"Error mounting {source} ({fs}) on {target} with options '{options}': {os.strerror(errno)}")
    
    def unmount(device, options=0):
        ret = ctypes.CDLL('libc.so.6', use_errno=True).umount2(device, options)
        if ret < 0:
            errno = ctypes.get_errno()
            raise RuntimeError("Error umounting {} with options '{}': {}".format(device, options, os.strerror(errno)))