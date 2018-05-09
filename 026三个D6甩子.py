# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 09:37:58 2018

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
die_3 = Die()

results = []

for roll_num in range(5000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):          
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title="挣5000次三个D6面的甩子的结果."
hist.x_labels = ['3', '4', '5', '6', '7','8','9','10','11','12','13','14','15','16','17','18']
hist.x_title = '出现的结果'
hist.y_title = '次数累积'


hist.add('D6*3', frequencies)
hist.render_to_file('die_visual4.svg')   