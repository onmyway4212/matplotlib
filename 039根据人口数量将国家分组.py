# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:32:40 2018

@author: Administrator
"""

import pygal
from country import get_country_code
#pygal样式存储在模块style中；lightcolorizedstyle加亮地图的颜色
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
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

#根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
#遍历cc_populations,检查每个国家人口的数量，进行人口数量分组
for cc, pop in cc_populations.items():
    #cc国别码，pop人口数量。将每个国别码-人口数量对加入到合适的字典
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] =pop
    else:
        cc_pops_3[cc] =pop

#看看每个分组包含多少个国家,打印字典的长度
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population2.svg')