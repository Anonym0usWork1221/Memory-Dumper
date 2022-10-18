from os import environ
from sys import platform
from ctypes import CDLL, c_char_p
import glob

# find the shared library, the path depends on the platform and Python version
_lib_file = glob.glob('build/*/fixer_lib*.pyd')[0]

_lib = CDLL(_lib_file)  # loading ctypes
_lib.fixer_so.restype = None  # return types
_lib.fixer_so.argtypes = (c_char_p, c_char_p, c_char_p)


def _get_platform():
    if 'ANDROID_STORAGE' in environ:
        return 'android'
    elif platform == "linux" or platform == "linux2":
        return 'linux'
    else:
        return 'other'


def fixer_so(inFile: bytes, outFile: bytes, baseAddr: bytes):
    global _lib
    _lib.fixer_so(c_char_p(inFile), c_char_p(outFile),
                  c_char_p(baseAddr))


fixer_so(b'./test.bin', b'./t.so', b'0x7d68d9e000')
