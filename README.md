# Light-Detect-on-HDR-images

### Description
School small project, need: Python3.5.4 + numpy, cv2.
This is post-process when the stereo cameras are calibrated through my last repository which can detect the main light on the dark background, and ignore the small ones.
But I also believe it has drawbacks if used in some pictures which has so many light areas, so it's just a sample.
The algorithm of detect the light is self-design and some parameters can be fixed(I cannot give a guideline to adjust these parameters).
Any suggestion or advice is welcomed.

### How to use
Run this code

```
python main.py
```

and you will see the calculated distance.
If you are using your own camera, after calibration I believe you will have some matrix files and you need to replace line11-14 in main.py with your own.
In this repository, those four Matrix files are created by my last C++ program (see my last repository),

### Methodology
The processes are as below:
​    1st: Read images which created by HDR process in C++ (HDR_Left.jpg && HDR_Right.jpg);
​    2nd: Get Matrix of these 4 files, and transit to ndarray;
​    3rd: Undistort images;
​    4th: Transit gray images into dark/white (I defined this);
​    5th: Use kernel to calculate images value and get results , which based on kernel set through [ setKernel];
​    6th: Calculate the distance;

### Over
This is when I first learned Computer Vision and tried to implement some simple works, as I look the code I wrote, it's very ugly so I impoved something.
Let it be my first experience and laid here, so I can come back some day to see how I  naive then.
Haha!
