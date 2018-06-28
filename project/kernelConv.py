#import cv2 as cv
import numpy as np
import setKernel
import time

##Use Kernel to calculate the bright points
def kernelConvLeft(image):
    H1,W1 = image.shape
    ##kernel form
    x = np.arange(0, 19, 1)
    y = np.arange(0, 19, 1)
    x, y = np.meshgrid(x, y)
    K = setKernel.setKernel(x, y).reshape(19,19)
    resMatrix = np.array([[0,0]])
##convolution
    for i in range(0, H1-20, 4):
        for j in range(0, W1-20, 4):
            newnum = K*((image[i:i+19, j:j+19])/255)
            newnum = np.sum(newnum)
            if(newnum > 62.51):
                #print("i: ",i," j: ",j," newnum: ",newnum)
                temp = np.array([j,i])
                resMatrix = np.row_stack((resMatrix, temp))
    matIndex = resMatrix.shape
    #print(matIndex)
    resMatrix = np.delete(resMatrix, 0, 0)
    rowmax = resMatrix.max(0)
    rowmin = resMatrix.min(0)
    p1x = resMatrix[1][0]
    p1y = rowmin[1]
    p2x = resMatrix[matIndex[0]-2][0]
    p2y = rowmax[1]
    centerPoint_x = (p1x+p2x)/2
    centerPoint_y = (p1y+p2y)/2
    print("Px:",centerPoint_x," Py:", centerPoint_y)
    #cv.rectangle(image, (p1x,p1y), (p2x,p2y),(0,0,0), 3)
    #cv.imwrite("convImageLeft.jpg", image)
    #cv.imshow("image",image)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    return [centerPoint_x, centerPoint_y]

def kernelConvRight(image):
    H1,W1 = image.shape
    x = np.arange(0, 19, 1)
    y = np.arange(0, 19, 1)
    x, y = np.meshgrid(x, y)
    K = setKernel.setKernel(x, y).reshape(19,19)
    resMatrix = np.array([[0,0]])
    for i in range(0, H1-20, 4):
        for j in range(0, W1-20, 4):
            newnum = K*((image[i:i+19, j:j+19])/255)
            newnum = np.sum(newnum)
            if(newnum > 62.51):
                #print("i: ",i," j: ",j," newnum: ",newnum)
                temp = np.array([j,i])
                resMatrix = np.row_stack((resMatrix, temp))
    matIndex = resMatrix.shape
    #print(matIndex)
    resMatrix = np.delete(resMatrix, 0, 0)
    rowmax = resMatrix.max(0)
    rowmin = resMatrix.min(0)
    p1x = resMatrix[1][0]
    p1y = rowmin[1]
    p2x = resMatrix[matIndex[0]-2][0]
    p2y = rowmax[1]
    centerPoint_x = (p1x+p2x)/2
    centerPoint_y = (p1y+p2y)/2
    print("Px:", centerPoint_x," Py:", centerPoint_y)
    #cv.rectangle(image, (p1x,p1y), (p2x,p2y),(0,0,0), 3)
    #cv.imwrite("convImageRight.jpg", image)
    #cv.imshow("image",image)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    return [centerPoint_x, centerPoint_y]