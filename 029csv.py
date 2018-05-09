# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 12:22:51 2018

@author: Administrator
"""

import csv
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    #next()函数返回的是第一行的数据
    header_row = next(reader)
    
    #利用enumerate()来获取每个元素的索引及其值
    for index, column_header in enumerate(header_row):
        print(index, column_header)