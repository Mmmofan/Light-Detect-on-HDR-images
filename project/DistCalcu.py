import numpy as np
import cv2 as cv
import math

class DistCalcu(object):

    def __init__(self, imgLeft, imgRight, intrinsic_Matrix):
        self.imageLeft = cv.imread(imgLeft, cv.IMREAD_GRAYSCALE)
        self.imageRight = cv.imread(imgRight, cv.IMREAD_GRAYSCALE)

        ##Get Matrix which come from C++
        self.mtx_Left, self.dist_Left = self.getMatrix(intrinsic_Matrix[0], intrinsic_Matrix[1])
        self.mtx_Right, self.dist_Right = self.getMatrix(intrinsic_Matrix[2], intrinsic_Matrix[3])


    def getMatrix(self, intrinMatName, distortMatName):
        #intrinMatName = 'intrinsic_Matrix_Left'
        inStream = open(intrinMatName, 'r')
        intrinMatrix = []
        for line in open(intrinMatName):
            line = inStream.readline().split()
            intrinMatrix.append(line)
        intrinMatrix = np.array(intrinMatrix).reshape(3,3)
        inStream.close()

        #distortMatName = 'distort_Matrix_Left'
        inStream = open(distortMatName, 'r')
        distMatrix = []
        for line in open(distortMatName):
            line = inStream.readline().split()
            distMatrix.append(line)
        inStream.close()
        distMatrix = np.array(distMatrix).reshape(1,5)
        intrinMatrix = intrinMatrix.astype(np.float32)
        distMatrix = distMatrix.astype(np.float32)
        return intrinMatrix, distMatrix

    def undistortLeft(self):
        h,w = self.imageLeft.shape[:2]
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(self.mtx_Left, self.dist_Left, (w,h), 1, (w,h))  
        dst = np.array([])
        dst = cv.undistort(self.imageLeft, self.mtx_Left, self.dist_Left, dst, self.mtx_Left)
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]
        #cv.imwrite('undistortImageLeft.jpg',dst)
        #cv.imshow('result',dst)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
        return dst

    def undistortRight(self):
        h,w = self.imageRight.shape[:2]
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(self.mtx_Right, self.dist_Right, (w,h),1, (w,h))
        dst = np.array([])
        dst = cv.undistort(self.imageRight, self.mtx_Right, self.dist_Right, dst, self.mtx_Right)
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]
        #cv.imwrite('undistortImageRight.jpg',dst)
        #cv.imshow('result',dst)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
        return dst

    def transToGray(self, image):
        image = np.array(image)
        image[image<210] = 0
        image[image>=210] = 255
        grayImage = image
        return grayImage

    ##Use Kernel to calculate the bright points
    def kernelConvLeft(self, image):
        H1,W1 = image.shape
        ##kernel form
        x = np.arange(0, 19, 1)
        y = np.arange(0, 19, 1)
        x, y = np.meshgrid(x, y)
        K = self.setKernel(x, y).reshape(19,19)
        resMatrix = np.array([[0,0]])
        ##convolution
        for i in range(0, H1-20, 5):
            for j in range(0, W1-20, 5):
                newnum = np.sum(K*((image[i:i+19, j:j+19])/255))
                if(newnum > 62.51):
                    #print("i: ",i," j: ",j," newnum: ",newnum)
                    temp = np.array([j,i])
                    resMatrix = np.row_stack((resMatrix, temp))
        matIndex = resMatrix.shape
        #print(matIndex)
        resMatrix = np.delete(resMatrix, 0, 0)
        rowmax = resMatrix.max(0)
        rowmin = resMatrix.min(0)
        xmin = rowmin[0]
        ymin = rowmin[1]
        xmax = rowmax[0]
        ymax = rowmax[1]
        centerPoint_x = (xmin + xmax)/2
        centerPoint_y = (ymin + ymax)/2
        print("Px:",centerPoint_x," Py:", centerPoint_y)
        #cv.rectangle(image, (xmin,ymin), (xmax,ymax),(0,0,0), 3)
        #cv.imwrite("convImageLeft.jpg", image)
        #cv.imshow("image",image)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
        return [centerPoint_x, centerPoint_y]

    def kernelConvRight(self, image):
        H1,W1 = image.shape
        x = np.arange(0, 19, 1)
        y = np.arange(0, 19, 1)
        x, y = np.meshgrid(x, y)
        K = self.setKernel(x, y).reshape(19,19)
        resMatrix = np.array([[0,0]])
        for i in range(0, H1-20, 5):
            for j in range(0, W1-20, 5):
                newnum = np.sum(K*((image[i:i+19, j:j+19])/255))
                if(newnum > 62.51):
                    #print("i: ",i," j: ",j," newnum: ",newnum)
                    temp = np.array([j,i])
                    resMatrix = np.row_stack((resMatrix, temp))
        matIndex = resMatrix.shape
        #print(matIndex)
        resMatrix = np.delete(resMatrix, 0, 0)
        rowmax = resMatrix.max(0)
        rowmin = resMatrix.min(0)
        xmin = rowmin[0]
        ymin = rowmin[1]
        xmax = rowmax[0]
        ymax = rowmax[1]
        centerPoint_x = (xmin + xmax)/2
        centerPoint_y = (ymin + ymax)/2
        print("Px:", centerPoint_x," Py:", centerPoint_y)
        #cv.rectangle(image, (xmin,ymin), (xmax,ymax),(0,0,0), 3)
        #cv.imwrite("convImageRight.jpg", image)
        #cv.imshow("image",image)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
        return [centerPoint_x, centerPoint_y]

    def distanceCalculate(self, p1, p2, Tfile):
        coord_abs = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        #print(coord_abs)
        getTfileName = Tfile
        q_matrix = []
        inStream = open(getTfileName, 'r')
        for line in open(getTfileName):
            line = inStream.readline().split()
            q_matrix.append(line)
        q_matrix = np.array(q_matrix).reshape(4,4).astype(np.float32)
        Trans = 1 / q_matrix[3][2]
        focal_length = q_matrix[2][3]
        h = Trans * focal_length / coord_abs
        return h

    def setKernel(self, x, y):
        z = np.exp((-(x-9)**2-(y-9)**2)/20)
        return z
