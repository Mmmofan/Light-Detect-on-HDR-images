import numpy as np

def setKernel(x,y):
  z = np.exp((-(x-9)**2-(y-9)**2)/20)
  return z
