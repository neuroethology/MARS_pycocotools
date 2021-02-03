### About
This fork of pycocotools from the COCO API was made to allow evaluation of mouse pose estimates that use the MARS keypoint definitions:

![](MARS_kpt_reference.png)

The code is largely unchanged, however the sigmas used for Object Keypoint Similarity have been modified to reflect the values estimated from the MARS dataset; this change was made in pycocotools/cocoeval.py. The Matlab and Lua versions of the original CoCo API have been removed for simplicity.

The original COCO API can be found [here](https://github.com/cocodataset/cocoapi).

### Installation
Note: in the future, this will come pre-installed in the `mars_dev` conda environment of [https://github.com/neuroethology/MARS_Developer](https://github.com/neuroethology/MARS_Developer).

#### Linux
In progress.

#### Windows
If you don't have them, install:
* Microsoft Visual C++ Build Tools- download from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
* Cython - call `pip install cython`.

then, call:
```
pip install git+https://github.com/neuroethology/MARS_pycocotools.git#egg=pycocotools^&subdirectory=PythonAPI
```


TODO:
* Jupyter notebooks have not yet been updated.
