from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'marseval._mask',
        sources=['../common/maskApi.c', 'marseval/_mask.pyx'],
        include_dirs = [np.get_include(), '../common'],
        extra_compile_args=[] # previously: ['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    name='marseval',
    packages=['marseval'],
    package_dir = {'marseval': 'marseval'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0'
    ],
    version='2.0',
    ext_modules= cythonize(ext_modules)
)
