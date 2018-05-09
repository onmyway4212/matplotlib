# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:32:36 2018

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

print('\nseleected information about first repository:')
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Reponsitory:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
