# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:32:15 2018

@author: Administrator
"""

import json

#将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    #遍历pop_data中的每个元素，每个元素都是一个字典，包含四个键值对
    if pop_dict['Year'] =='2010':
        country_name = pop_dict['Country Name']
        #人口数据是字符串，先转换成浮点数，再转换成整形。int会丢掉浮点数的小数部分
        population =int(float(pop_dict['Value']))
        print(country_name + ' : ' + str(population))