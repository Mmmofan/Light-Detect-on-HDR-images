# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:17:13 2015

@author: Van_Mo
"""

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(0, 19, 1)
Y = np.arange(0, 19, 1)
X, Y = np.meshgrid(X, Y)
Z = np.exp((-(X-9)**2-(Y-9)**2)/25)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
print(Z)
plt.show()
