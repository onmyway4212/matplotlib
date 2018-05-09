# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 08:15:26 2018

@author: Administrator
"""

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
for value in range(1, die.num_sides+1):              #range(1,6)是1到5的数字
    #计算每种点数在results中出现了多少次
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)      
