import cv2 as cv
import numpy as np

def transToGray(image):
    rows, cols = image.shape
    for r in range(rows):
        for c in range(cols):
            if image[r][c] < 210:
                image[r][c] = 0
            else:
                image[r][c] = 255
    grayImage = image
    return grayImage
