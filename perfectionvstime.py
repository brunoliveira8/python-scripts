# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 23:06:01 2016

@author: bruno
"""

import math

def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab

x = np.arange(-10., 10., 0.2)
sig = sigmoid(x)
plt.plot(x,sig)
plt.plot([x[50], x[50]],[-0.05, sig[50]], 'b--')
plt.plot([x[0], x[50]],[sig[50], sig[50]], 'b--')
plt.plot([x[65], x[65]],[-0.050, sig[65]], 'b--')
plt.plot([x[0], x[65]],[sig[65], sig[65]], 'b--')
plt.plot([x[57], x[57]],[-0.05, sig[57]], 'g--')
plt.plot([x[0], x[57]],[sig[57], sig[57]], 'g--')  
plt.plot(x[57], sig[57], 'go', label ='optimal point')    
plt.ylabel('Perfection')
plt.xlabel('Time Spent')
frame = pylab.gca()
#frame.axes.get_xaxis().set_ticks([])
plt.annotate('optimal region', xy=(x[57]+1, 0.5), xytext=(x[57]+3, 0.6),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.axis([-10, 10, -.05, 1.05])
#plt.legend()
plt.show()