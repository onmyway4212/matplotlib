# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:54:33 2018

@author: Administrator
"""

from pygal.maps.world import COUNTRIES

#打印每个国家的2个字母的国别码
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])