# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:07:24 2018

@author: Administrator
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#edgecolor='none'删除数据点的轮廓,c='red'指定点的颜色,c=(0,0,0.8)表示红绿蓝色分量
#plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)    
plt.scatter(x_values, y_values, c=(0.5,0.5,0.8), edgecolor='none', s=40)    
plt.title('square numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)
#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()