# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:29:05 2018

@author: Administrator
"""

import matplotlib.pyplot as plt

#从颜色渐变到结束颜色
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
 
#将c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射，将y值较小的点显示为浅蓝色，y值较大的点显示为深蓝色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40) 

   
plt.title('square numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)
#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

#第一个参数是图片保存的路径，第二个参数bbox_inches='tight'表示将图标多余的空白部分剪掉。如果要保留周围多余的空白区域，这个参数可以省略
plt.savefig('d:/squares_plot.png', bbox_inches='tight')