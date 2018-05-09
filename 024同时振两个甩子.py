# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 08:54:29 2018

@author: Administrator
"""

import pygal
from random import randint

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    
    def roll(self):
        return randint(1, self.num_sides)


die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):          
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title="挣1000两个都是6面的甩子的结果."
hist.x_labels = ['2', '3', '4', '5', '6', '7','8','9','10','11','12']
hist.x_title = '出现的结果'
hist.y_title = '次数累积'


hist.add('D6*2', frequencies)
hist.render_to_file('die_visual2.svg')   