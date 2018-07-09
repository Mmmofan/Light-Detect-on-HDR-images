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
    #getMat_tic = time.clock()
    mtx_Left, dist_Left = getMatrix.getMatrix('intrinsic_Matrix_Left', 'distort_Matrix_Left')
    mtx_Right, dist_Right = getMatrix.getMatrix('intrinsic_Matrix_Right', 'distort_Matrix_Right')
    #getMat_tac = time.clock()
##Undistort images
    undist_tic = time.clock()
    imageLeft =  undistort.undistortLeft(imageLeft, mtx_Left, dist_Left)
    imageRight =  undistort.undistortRight(imageRight, mtx_Right, dist_Right)
    undist_tac = time.clock()
    print('images undistorted time cost: ', undist_tac-undist_tic,'s')
##Translate images to gray images
    #gray_tic = time.clock()
    imageLeft = grayImage.transToGray(imageLeft)
    imageRight = grayImage.transToGray(imageRight)
    #gray_tac = time.clock()
    #print('images gray time cost: ', gray_tac-gray_tic,'s')
##detect bright points
    conv_tic = time.clock()
    point1 = kernelConv.kernelConvLeft(imageLeft)
    conv_tac1 = time.clock()
    point2 = kernelConv.kernelConvRight(imageRight)
    conv_tac2 = time.clock()
    print('Left images convolution time cost: ', conv_tac1 - conv_tic, 's')
    print('Right images convolution time cost: ', conv_tac2 - conv_tac1, 's')
##calculate the distance
    #calc_tic = time.clock()
    distance = distanceCalculate.distanceCalculate(point1, point2)
    #calc_tac = time.clock()
    #print('calculate time cost: ',calc_tac-calc_tic,'s')
    print('Distance is: ', distance, "mm")
    end_tac = time.clock()
    print('Time cost: ', end_tac - start_tic, 's')

if __name__ == "__main__":
    main()
