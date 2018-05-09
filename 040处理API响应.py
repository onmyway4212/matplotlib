# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 09:37:59 2018

@author: Administrator
"""

import requests

url ='https://api.github.com/search/repositories?q=language:python&sort=stars'
r= requests.get(url)
print('status code:', r.status_code)

#将api以json格式的信息存储，转化为一个python字典
response_dict=r.json()
#打印字典的键
print('total repositories:', response_dict['total_count'])

repo_dicts = response_dict['items']
#len(repo_dicts)获得了多少个仓库的信息
print('repositories returned:', len(repo_dicts))

#研究第一个仓库
repo_dict = repo_dicts[0]
#打印这个字典的键数
print('\nKeys:', len(repo_dict))
#打印所有键，sorted() 函数对所有可迭代的对象进行排序操作。
for key in sorted(repo_dict.keys()):
    print(key)

