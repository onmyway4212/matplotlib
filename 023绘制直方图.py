# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 08:35:35 2018

@author: Administrator
"""
#pypal用来生成可缩放的矢量图形文件，用于在不同尺寸的屏幕上显示
import pygal
from random import randint

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    
    def roll(self):
        return randint(1, self.num_sides)


die = Die()

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):          
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()
#设置图形的标题，x轴y轴的名称和数字
hist.title="results of rolling one d6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'result'
hist.y_title = 'frequency of result'

#用add()将一系列值添加到图表中
hist.add('D6', frequencies)
#将图表生成一个svg文件。扩展名只能为svg
hist.render_to_file('die_visual.svg')   
