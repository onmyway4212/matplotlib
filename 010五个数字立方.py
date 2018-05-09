# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:34:56 2018

@author: Administrator
"""

import matplotlib.pyplot as plt

#要绘制一系列的点，可向scatter()转递两个分别包含x值和y值的列表
x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]   
plt.scatter(x_values, y_values, s=100)    

plt.title('cube numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('cube of value', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()