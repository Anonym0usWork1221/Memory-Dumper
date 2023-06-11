import os
import sys
import warnings
from setuptools.command.build_ext import build_ext as build_ext_orig
from setuptools import setup, Extension
from setuptools.command.install import install


# Define a helper function to redirect output to /dev/null
def silence_output(func):
    def wrapper(*args, **kwargs):
        with open(os.devnull, "w") as devnull:
            original_stdout = sys.stdout
            sys.stdout = devnull
            try:
                return func(*args, **kwargs)
            finally:
                sys.stdout = original_stdout

    return wrapper


class BuildExt(build_ext_orig):
    def __init__(self, dist):
        super().__init__(dist)
        self._ctypes = None

    @silence_output
    def build_extension(self, ext):
        self._ctypes = isinstance(ext, Extension)
        return super().build_extension(ext)

    @silence_output
    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)

    @silence_output
    def get_ext_filename(self, ext_name):
        if self._ctypes:
            return ext_name + '.pyd'
        return super().get_ext_filename(ext_name)


class InstallCommand(install):
    def run(self):
        super().run()
        self.build_package()

    def build_package(self):
        self.run_command("build_ext")


req = open("./requirements.txt", "r").readlines()

# Disable warning logs
warnings.filterwarnings("ignore")

setup(
    name='MemoryDumper',
    version='0.2',
    license="MIT license",
    author='Abdul Moez',
    author_email='abdulmoez123456789@gmail.com',
    description='Dump/Fix android/linux Dumped libs',
    zip_safe=False,
    ext_modules=[
        Extension(
            "fixer_lib",
            sources=["./ElfFixer/fix_executor.cpp", "./ElfFixer/fix.cpp"],
            # extra_compile_args=['-Wno-error']
        ),
    ],
    install_requires=req,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],

    cmdclass={
        'build_ext': BuildExt,
        'install': InstallCommand,
    },
)
print("[*] Build Complete")
