This fork of pycocotools from the COCO API was made to allow evaluation of mouse pose estimates that use the MARS keypoint definitions:
<p align=center>
<img src=MARS_kpt_reference.png height=200>
</p>
The code is largely unchanged, however the sigmas used for Object Keypoint Similarity have been modified to reflect the values estimated from the MARS dataset; this change was made in pycocotools/cocoeval.py. The Matlab and Lua versions of the original CoCo API have been removed for simplicity.

To install, run "make" from this directory.

TODO:
* Jupyter notebooks have not yet been updated.

The original COCO API can be found [here](https://github.com/cocodataset/cocoapi).
