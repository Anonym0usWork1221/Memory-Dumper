#! /usr/bin/env python
from glob import glob
from sys import platform
from ctypes import CDLL, c_char_p
from os import environ, system, getuid, path, mkdir, chmod, remove
from sys import exit
from shutil import copy
from subprocess import check_output
try:
    from androidMemoryTool import AndroidMemoryTool
    from rich import print
    from art import tprint
except ImportError:
    system("pip3 install -r ./requirements.txt")
    exit()

clear = lambda: system("clear")


class MemoryDumper:
    _lib = None
    _pkg = None
    _PID = None
    _android_tool = None
    _initial_glob = ''
    _android_glob = ''
    _fixer_path_android = "/data/data/lib-fixer/"
    _dump_path = "./dumped_lib/"

    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        # initialization directory and decoration
        if path.exists(self._dump_path):
            pass
        else:
            mkdir(self._dump_path)

        if path.exists('./build/'):
            self._initial_glob = glob('./build/*/fixer_lib*.pyd')[0]
        else:
            print("[*] Run setup file")
            exit(0)

        self._set_lib()
        self._init_return_types()
        self.main_loop()

    @staticmethod
    def _get_platform() -> str:
        if check_output(['uname', '-o']).strip() == b'Android':
            return 'android'
        elif platform == "linux" or platform == "linux2":
            return 'linux'
        else:
            return 'other'

    def _init_return_types(self) -> None:
        self._lib.fixer_so.restype = None  # return types
        self._lib.fixer_so.argtypes = (c_char_p, c_char_p, c_char_p)

    def _path_validator(self) -> None:
        if path.exists(self._fixer_path_android):
            self._android_glob = glob(f'{self._fixer_path_android}fixer_lib*.pyd')[0]
            chmod(path=self._android_glob, mode=0o0777)
        else:
            mkdir(self._fixer_path_android)
            copy(self._initial_glob, self._fixer_path_android)
            self._android_glob = glob(f'{self._fixer_path_android}fixer_lib*.pyd')[0]
            chmod(path=self._android_glob, mode=0o0777)

    def _set_lib(self) -> None:
        plt = self._get_platform()
        if plt == 'android':
            if self._initial_glob == '':
                print("[*] Setup is not build")
                exit(0)
            else:
                self._is_rooted_acquired()
                self._path_validator()
                if self._android_glob == '':
                    print("[*] Root required to initialize glob")
                    exit(0)
                self._lib = CDLL(self._android_glob)

        elif plt == 'linux':
            self._lib = CDLL(self._initial_glob)
        else:
            print('[*] Platform not supported')
            exit(0)

    @staticmethod
    def _is_rooted_acquired() -> None:
        if getuid() != 0:
            print("[*] Root Required")
            print("[*] Reboot script as root")
            exit(0)
        else:
            print("Root Acquired")

    @staticmethod
    def _decoration() -> None:
        tprint(text="DUMPER", chr_ignore=True)

    def _fixer_so(self, inFile: bytes, outFile: bytes, baseAddr: bytes) -> None:
        self._lib.fixer_so(c_char_p(inFile), c_char_p(outFile),
                           c_char_p(baseAddr))

    def _is_game_running(self) -> bool:
        self._PID = AndroidMemoryTool.get_pid(self._pkg)
        if not self._PID == "":
            return True
        else:
            return False

    def main_loop(self) -> None:
        clear()
        self._decoration()
        print("[*] 1. Dump from Memory")
        print("[*] 2. Fix Dump File")
        print("[*] 3. Exit")
        ans = input(">>>> ")
        ans = int(ans)
        if ans == 1:
            self._pkg = input("Enter package name: ")
            game = self._is_game_running()
            if game:
                self._android_tool = AndroidMemoryTool(PKG=self._pkg)
            else:
                print("[*] PID not found")
                exit(0)

            clear()
            self._decoration()
            while True:
                print("[*] 1. Raw Dump from memory")
                print("[*] 2. Fixed Dump from memory")
                print("[*] 3. Exit and release memory")
                ans = input(">>>> ")
                ans = int(ans)
                if ans == 1:
                    lib_id = input("Enter Lib Name: ")
                    dump = self._android_tool.raw_dump(lib_name=lib_id, path=self._dump_path)
                    if dump:
                        print("\n[*] Lib Dumped successfully: %s" % self._dump_path)
                elif ans == 2:
                    lib_id = input("Enter Lib Name: ")
                    dump = self._android_tool.raw_dump(lib_name=lib_id, path=self._dump_path)
                    if dump:
                        file_path = glob(f"{self._dump_path}*{lib_id}*")[0]
                        unrefined_file_name = path.basename(file_path)
                        file_name = unrefined_file_name.replace('.bin', '')
                        base_addr = file_name.split('-')[0]

                        self._fixer_so(file_path.encode("ASCII"), f"{self._dump_path}{file_name}".encode("ASCII"),
                                       base_addr.encode("ASCII"))
                        remove(path=file_path)
                    else:
                        print("[*] Unable to get dump file")

                elif ans == 3:
                    print("[*] Exiting")
                    exit(0)

        elif ans == 2:
            bin_name = input("Enter bin file name: ")
            out_file_name = input("Enter output file name: ")
            base_address_of_file = input("Enter base address (0x0 if you dont know): ")
            self._fixer_so(bin_name.encode("ASCII"), out_file_name.encode("ASCII"),
                           base_address_of_file.encode("ASCII"))
        elif ans == 3:
            exit(0)
        else:
            print("[*] Choose given options")


if __name__ == '__main__':
    MemoryDumper().__int__()
