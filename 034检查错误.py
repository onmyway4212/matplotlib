# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:04:28 2018
death_valley_2014.csv
@author: Administrator
"""

from datetime import datetime
import csv
from matplotlib import pyplot as plt

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')          
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, highs, c='red', alpha=0.5)  #alpha值设置颜色的透明度，0为完全透明
plt.plot(dates, lows, c='blue', alpha=0.5)
#fill_between传递了一个x值：列表dates和两个y值：highs和lows
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('daily high and low temperatures, 2014\n death valley', fontsize=16)
plt.xlabel('',fontsize=6)
fig.autofmt_xdate()
plt.ylabel('temperature (F)', fontsize=12)
plt.tick_params(axis='both', which = 'major', labelsize=12)
plt.show()