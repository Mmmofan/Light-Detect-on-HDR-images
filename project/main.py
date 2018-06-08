import os
import time
import numpy as np
import cv2 as cv
import getMatrix
import undistort
import grayImage
import kernelConv
import distanceCalculate

def main():
    start = time.clock()
##Images Reading
    imageLeft = cv.imread('HDR_Left.jpg',cv.IMREAD_GRAYSCALE)
    imageRight = cv.imread('HDR_Right.jpg', cv.IMREAD_GRAYSCALE)
##Get Matrix which come from C++
    mtx_Left, dist_Left = getMatrix.getMatrixLeft()
    mtx_Right, dist_Right = getMatrix.getMatrixRight()
##Undistort images
    imageLeft =  undistort.undistortLeft(imageLeft, mtx_Left, dist_Left)
    imageRight =  undistort.undistortRight(imageRight, mtx_Right, dist_Right)
    print('images undistorted')
##Translate images to gray images
    imageLeft = grayImage.transToGray(imageLeft)
    imageRight = grayImage.transToGray(imageRight)
    print('images gray')
##detect bright points
    point1 = kernelConv.kernelConvLeft(imageLeft)
    point2 = kernelConv.kernelConvRight(imageRight)
    print('images convolution')
##calculate the distance
    distance = distanceCalculate.distanceCalculate(point1, point2)
    print('distance is: ', distance)
    end = time.clock()
    print(end-start)

if __name__ == "__main__":
    main()
