# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:38:40 2018

@author: Administrator
"""
import pygal
from country import get_country_code
import json
import pygal_maps_world.maps

#将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#创建一个字典存储国别码和人口数量
cc_populations = {}

for pop_dict in pop_data:
    #遍历pop_data中的每个元素，每个元素都是一个字典，包含四个键值对
    if pop_dict['Year'] =='2010':
        country = pop_dict['Country Name']
        #人口数据是字符串，先转换成浮点数，再转换成整形。int会丢掉浮点数的小数部分
        population =int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            #如果返回了国别码，就将国别码和人口数量分别作为键和值填充字典
            cc_populations[code] = population

wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')