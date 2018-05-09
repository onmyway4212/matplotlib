# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 13:21:56 2018

@author: Administrator
"""
from datetime import datetime
import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #两个空列表，用于存储提取的日期和最高气温
    dates, highs = [], []
    #遍历余下的各行，这个循环从第二行开始
    for row in reader:
        #将包含日期信息的数据row[0]转换为datetime对象
        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(current_date)
        #将字符串转换为数字
        high = int(row[1])
        highs.append(high)

fig = plt.figure(dpi=128, figsize=(10, 6))
#将日期和最高气温的值传递给plot()
plt.plot(dates, highs, c='red')

plt.title('daily high temperatures, july 2014', fontsize=16)
plt.xlabel('',fontsize=6)
#autofmt_xdate()来绘制倾斜的日期标签，以免它们彼此重叠
fig.autofmt_xdate()
plt.ylabel('temperature (F)', fontsize=12)
plt.tick_params(axis='both', which = 'major', labelsize=12)
plt.show()