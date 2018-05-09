# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:30:07 2018

@author: Administrator
"""

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)   #设置绘制线条的粗细
plt.title('square numbers', fontsize=24)   #设置图形标题
plt.xlabel('value', fontsize=14)           #设置x轴名称和字体大小
plt.ylabel('square of value', fontsize=14) #设置y轴名称和字体大小

plt.tick_params(axis='both', labelsize=14) #设置刻度标记的大小

plt.show()