import numpy as np

def transToGray(image):
    image = np.array(image)
    image[image<210] = 0
    image[image>=210] = 255
    grayImage = image
    return grayImage
