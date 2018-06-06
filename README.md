# Light-Detect-on-HDR-images

School project

This is post-process when the stereo cameras are calibrated through my last repository

This can detect the main light on the dark background, and ignore the small ones

But I also believe it has drawbacks if used in some pictures which has so many light areas, so it's just a sample

The algorithm of detect the light is self-design and some parameters can be fixed(I cannot give a guide to adjust these parameters)

Any suggestion or advice is welcomed

I'm a new conqueror of coding, hope I can do bette

------------------------------------------Descriptions Below------------------------------------------------------------

Four(4) Matrix file is created by my last C++ program(my last repository)

The processes are as below:
    1st: Read images which created by HDR process in C++ (HDR_Left.jpg && HDR_Right.jpg)
    2nd: Get Matrix of these 4 files, and transit to ndarray, use file [ getMatrix.py ]
    3rd: Undistort images use [ undistort,py ]
    4th: Transit gray images into dark/white (I defined this) use [ grayImage.py ]
    5th: Use kernel to calculate images value and get results use [ kernelConv.py ], which based on kernel set through [ setKernel.py ]
    6th: There should be 6th step to calculate the distance, but it has not done yet.
 
