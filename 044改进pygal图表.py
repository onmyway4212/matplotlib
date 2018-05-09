# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:03:06 2018

@author: Administrator
"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url ='https://api.github.com/search/repositories?q=language:python&sort=stars'
r= requests.get(url)
print('status code:', r.status_code)

#将api以json格式的信息存储，转化为一个python字典
response_dict=r.json()
#打印字典的键
print('total repositories:', response_dict['total_count'])

repo_dicts = response_dict['items']
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#基色设置为深蓝色
my_style = LS('#333366', base_style=LCS)
#创建一个pygal类config实例，修改属性可以定制图表的外观
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend =False
my_config.title_font_size =24
my_config.label_font_size = 14
my_config.margin_label_font_size =18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000            
#用BAR创建一个条形图，让标签绕x轴转45度，隐藏了图例
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
#将标签设置成了空的字符串，就没有标签
chart.add('', stars)
chart.render_to_file('python_repos2.svg')