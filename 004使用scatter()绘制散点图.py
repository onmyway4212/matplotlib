# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:48:27 2018

@author: Administrator
"""

import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)       #s=200圆点的直径变大
#设置标题，x轴和y轴
plt.title('square numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

#设置标度计的大小，axis=‘both‘ 表示指定的实参影响 x 轴和 y 轴上的刻度，默认是major表示主刻度，后面分布为次刻度及主次刻度都显示
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()