import os
import time

import cv2 as cv
import numpy as np

from DistCalcu import DistCalcu


def main():
    start_tic = time.clock()

    ## Matrix files Reading
    imageLeft = '../HDR_Left.jpg'
    imageRight = '../HDR_Right.jpg'
    intrinMatrix = ['../Matrix/intrinsic_Matrix_Left', '../Matrix/distort_Matrix_Left', 
                    '../Matrix/intrinsic_Matrix_Right', '../Matrix/distort_Matrix_Right']
    Tfile = '../Matrix/q_matrix'

    calculator = DistCalcu(imageLeft, imageRight, intrinMatrix)

    ## Undistort images
    calculator.imageLeft = calculator.undistortLeft()
    calculator.imageRight = calculator.undistortRight()

    ## Translate images to gray images
    calculator.imageLeft = calculator.transToGray(calculator.imageLeft)
    calculator.imageRight = calculator.transToGray(calculator.imageRight)

    ## detect bright points
    point1 = calculator.kernelConvLeft(calculator.imageLeft)
    point2 = calculator.kernelConvRight(calculator.imageRight)

    ## Calculate distance
    distance = calculator.distanceCalculate(point1, point2, Tfile)
    print('Distance is: ', distance, "mm")

    end_tac = time.clock()
    print('Time cost: ', end_tac - start_tic, 's')

if __name__ == "__main__":
    main()
