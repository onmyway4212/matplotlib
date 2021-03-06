# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 18:12:37 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points 
        #随机漫步经过的每个点的x坐标和y坐标，从（0,0）点出发
        self.x_values=[0]
        self.y_values=[0]
    
    def fill_walk(self):
        #不断漫步，直到列表中的数的长度大于指定的5000步
        while len(self.x_values) < self.num_points:
            #决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1,-1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            #拒绝原地踏步
            if x_step == 0 and y_step ==0:
                continue
            
            #计算下一个点的x和y值，列表中最右边的数位置加上移动距离，生成新的位置
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            #把新的x和y坐标位置加入到列表中
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
while True:           
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.title('RandomWalk', fontsize=24)
    plt.xlabel('x-value', fontsize=14)
    plt.ylabel('y-value', fontsize=14)
    #将c设置成point_numbers列表，指定的列表只包含1到5000，步数小的时候颜色浅，步数大的时候颜色变深
    #cmap=plt.cm.Blues设置成蓝色渐变色
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,\
                edgecolor='none', cmap=plt.cm.Blues, s=5)
    #突出起点和终点
    plt.scatter(0,0, c= 'green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1],rw.y_values[-1], c= 'red', edgecolors='none', s=50)
    plt.show()
    
    keep_running = input('make another walk?(y/n):')
    if keep_running == 'n':
        break