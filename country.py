# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:20:57 2018

@author: Administrator
"""

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    #根据指定的国家，返回pygal使用的两个字母的国别码
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.  
    if country_name == 'Korea, Republic of':
        return 'kr'
    elif country_name == "Korea, Democratic People's Republic of":
        return 'kp'
    elif country_name == 'Bolivia, Plurinational State of':
        return 'bo'
    elif country_name == 'Venezuela, Bolivarian Republic of':
        return 've'
    elif country_name == 'Yemen':
        return 'ye'
    elif country_name == 'Congo, the Democratic Republic of the':
        return 'cd'
    elif country_name == 'Tanzania, United Republic of':
        return 'tz'
    elif country_name == 'Iran, Islamic Republic of':
        return 'ir'
    elif country_name == 'Egypt':
        return 'eg'
    else:
        return None

    '''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code      
        elif name == 'Korea, Republic of':
            return 'kr'
        elif name == "Korea, Democratic People's Republic of":
            return 'kp'
        elif name == 'Bolivia, Plurinational State of':
            return 'bo'
        elif name == 'Venezuela, Bolivarian Republic of':
            return 've'
        elif name == 'Yemen':
            return 'ye'
        elif name == 'Congo, the Democratic Republic of the':
            return 'cd'
        elif name == 'Tanzania, United Republic of':
            return 'tz'
        elif name == 'Iran, Islamic Republic of':
            return 'ir'
        elif name == 'Egypt':
            return 'eg'
        else:
            return None
        '''