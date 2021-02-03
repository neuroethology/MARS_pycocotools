from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'MARSeval._mask',
        sources=['../common/maskApi.c', 'MARSeval/_mask.pyx'],
        include_dirs = [np.get_include(), '../common'],
        extra_compile_args=[] # previously: ['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    name='MARSeval',
    packages=['MARSeval'],
    package_dir = {'MARSeval': 'MARSeval'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0'
    ],
    version='1.0',
    ext_modules= cythonize(ext_modules)
)
