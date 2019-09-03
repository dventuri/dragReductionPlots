# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:28:43 2018

@author: livio
"""
import locale
locale.setlocale(locale.LC_NUMERIC, "de_DE")
#importar pacotes
import numpy as np
import matplotlib.pyplot as plt


# Tell matplotlib to use the locale we set above
plt.rcParams['axes.formatter.use_locale'] = True

# make the figure and axes
fig,ax = plt.subplots(1)

# Some example data
x=np.array([1.5, 2.5, 3.5])#np.arange(100)
y=4e-18*x**2

# plot the data
ax.plot(x,y,'b-')

plt.show()