import os
import time
import numpy as np
import cv2 as cv
from DistCalcu import DistCalcu

def main():
    start_tic = time.clock()

##Images Reading
    imageLeft = '../HDR_Left.jpg'
    imageRight = '../HDR_Right.jpg'
    intrinMatrix = ['../Matrix/intrinsic_Matrix_Left', '../Matrix/distort_Matrix_Left', '../Matrix/intrinsic_Matrix_Right', '../Matrix/distort_Matrix_Right']
    Tfile = '../Matrix/q_matrix'

    calculator = DistCalcu(imageLeft, imageRight, intrinMatrix)

##Undistort images
    undist_tic = time.clock()
    calculator.imageLeft = calculator.undistortLeft()
    calculator.imageRight = calculator.undistortRight()
    undist_tac = time.clock()
    print('images undistorted time cost: ', undist_tac-undist_tic,'s')

##Translate images to gray images
    #gray_tic = time.clock()
    calculator.imageLeft = calculator.transToGray(calculator.imageLeft)
    calculator.imageRight = calculator.transToGray(calculator.imageRight)
    #gray_tac = time.clock()
    #print('images gray time cost: ', gray_tac-gray_tic,'s')

##detect bright points
    #conv_tic = time.clock()
    point1 = calculator.kernelConvLeft(calculator.imageLeft)
    #conv_tac1 = time.clock()
    point2 = calculator.kernelConvRight(calculator.imageRight)
    #conv_tac2 = time.clock()
    #print('Left images convolution time cost: ', conv_tac1 - conv_tic, 's')
    #print('Right images convolution time cost: ', conv_tac2 - conv_tac1, 's')
##calculate the distance
    #calc_tic = time.clock()

    distance = calculator.distanceCalculate(point1, point2, Tfile)
    #calc_tac = time.clock()
    #print('calculate time cost: ',calc_tac-calc_tic,'s')
    print('Distance is: ', distance, "mm")
    end_tac = time.clock()
    print('Time cost: ', end_tac - start_tic, 's')

if __name__ == "__main__":
    main()
