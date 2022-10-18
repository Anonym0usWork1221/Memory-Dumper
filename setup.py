from distutils.command.build_ext import build_ext as build_ext_orig
from distutils.dist import Distribution
from setuptools import setup, Extension


class BuildExt(build_ext_orig):

    def __init__(self, dist: Distribution):
        super().__init__(dist)
        self._ctypes = None

    def build_extension(self, ext):
        self._ctypes = isinstance(ext, Extension)
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)

    def get_ext_filename(self, ext_name):
        if self._ctypes:
            return ext_name + '.pyd'
        return super().get_ext_filename(ext_name)


req = open("./requirements.txt", "r").readlines()

setup(
    name='MemoryDumper',
    version='0.1',
    license="MIT license",
    author='Abdul Moez',
    author_email='abdulmoez123456789@gmail.com',
    description='Dump/Fix android/linux Dumped libs',
    zip_safe=False,
    ext_modules=[
        Extension(
            "fixer_lib",
            ["./ElfFixer/test_fix.cpp",
             "./ElfFixer/fix.cpp"],
        ),
    ],
    install_requires=req,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],

    cmdclass={'build_ext': BuildExt},
)
