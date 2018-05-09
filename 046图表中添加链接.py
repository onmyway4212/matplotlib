# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:06:09 2018

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
print('number of items:', len(repo_dicts))
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
            'value':repo_dict['stargazers_count'],
            #'label':repo_dict['description'],
            'xlink':repo_dict['html_url'],
            }
    plot_dicts.append(plot_dict)

#基色设置为深蓝色
my_style = LS('#333366', base_style=LCS)
#用BAR创建一个条形图，让标签绕x轴转45度，隐藏了图例
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
#将标签设置成了空的字符串，就没有标签
chart.add('', plot_dicts)
chart.render_to_file('python_repos3.svg')
