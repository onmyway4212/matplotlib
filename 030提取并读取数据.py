# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 12:42:25 2018

@author: Administrator
"""

import csv
from matplotlib import pyplot as plt
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    #next()函数返回的是第一行的数据
    header_row = next(reader)
    
    highs = []
    #遍历余下的各行，这个循环从第二行开始
    for row in reader:
        #将字符串转换为数字
        high = int(row[1])
        highs.append(high)

#fig = plt.figure(dpi=128, figsize=(10, 6))
#将最高气温的列表highs传递给plot()
plt.plot(highs, c='red')

plt.title('daily high temperatures, july 2014', fontsize=16)
plt.xlabel('',fontsize=6)
plt.ylabel('temperature (F)', fontsize=12)
plt.tick_params(axis='both', which = 'major', labelsize=12)
plt.show()