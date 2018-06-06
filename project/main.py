import os
import numpy as np
import cv2 as cv
import getMatrix
import undistort
import grayImage
import kernelConv

def main():
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
    kernelConv.kernelConvLeft(imageLeft)
    kernelConv.kernelConvRight(imageRight)
    print('images convolution')

if __name__ == "__main__":
    main()
