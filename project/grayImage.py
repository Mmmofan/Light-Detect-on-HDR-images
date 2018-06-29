import numpy as np

def transToGray(image):
    image = np.array(image)
    image[image<200] = 0
    image[image>=200] = 255
    grayImage = image
    return grayImage
