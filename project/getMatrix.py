import os
import numpy as np


def getMatrix(intrinMatName, distortMatName):
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