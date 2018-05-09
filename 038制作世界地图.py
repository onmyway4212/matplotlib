# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 18:06:13 2018

@author: Administrator
"""

import pygal_maps_world.maps

#创建一个maps实例
wm = pygal_maps_world.maps.World()
wm.title = 'North, Central, and South America'

#add()方法接受一个标签和一个列表
wm.add('North America', {'ca':34126000,'mx':113423000,'us':309349000})
wm.add('Central America', ['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America', ['ar','bo','br','cl','co','ec','gf',\
                         'gy','pe','py','sr','uy', 've'])
#创建一个包含图表的.svg
wm.render_to_file('Americas.svg')