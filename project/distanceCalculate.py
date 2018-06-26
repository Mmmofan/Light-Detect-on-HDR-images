import numpy as np
import math

def distanceCalculate(p1, p2):
    coord_abs = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    #print(coord_abs)
    getTfileName = 'q_matrix'
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
