# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:39:01 2018

@author: Administrator
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=10)    

plt.title('cube numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('cube of value', fontsize=14)

plt.axis([0, 5000, 0, 125000000000])
plt.show()