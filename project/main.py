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
    start_tic = time.clock()
##Images Reading
    imageLeft = cv.imread('HDR_Left.jpg',cv.IMREAD_GRAYSCALE)
    imageRight = cv.imread('HDR_Right.jpg', cv.IMREAD_GRAYSCALE)
##Get Matrix which come from C++
    getMat_tic = time.clock()
    mtx_Left, dist_Left = getMatrix.getMatrixLeft()
    mtx_Right, dist_Right = getMatrix.getMatrixRight()
    getMat_tac = time.clock()
    print('get Matrix time cost: ', getMat_tac-getMat_tic, 's')
##Undistort images
    undist_tic = time.clock()
    imageLeft =  undistort.undistortLeft(imageLeft, mtx_Left, dist_Left)
    imageRight =  undistort.undistortRight(imageRight, mtx_Right, dist_Right)
    undist_tac = time.clock()
    print('images undistorted time cost: ', undist_tac-undist_tic,'s')
##Translate images to gray images
    gray_tic = time.clock()
    imageLeft = grayImage.transToGray(imageLeft)
    imageRight = grayImage.transToGray(imageRight)
    gray_tac = time.clock()
    print('images gray time cost: ', gray_tac-gray_tic,'s')
##detect bright points
    point1 = kernelConv.kernelConvLeft(imageLeft)
    point2 = kernelConv.kernelConvRight(imageRight)
    print('images convolution')
##calculate the distance
    calc_tic = time.clock()
    distance = distanceCalculate.distanceCalculate(point1, point2)
    calc_tac = time.clock()
    print('calculate time cost: ',calc_tac-calc_tic,'s')
    print('Distance is: ', distance, "mm")
    end_tac = time.clock()
    print('Time cost: ', end_tac - start_tic, 's')

if __name__ == "__main__":
    main()
