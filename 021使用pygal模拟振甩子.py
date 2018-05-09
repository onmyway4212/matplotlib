# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 20:05:53 2018

@author: Administrator
"""

from random import randint

#表示一个甩子的类
class Die(): 
    #__init__方法接受一个可选参数，面数默认为6.如果指定了实参，这个值将用于设置股子的面数
    def __init__(self, num_sides=6):
        #甩子默认为6个面
        self.num_sides = num_sides
    
    def roll(self):
        return randint(1, self.num_sides)


die = Die()

results = []
#甩子投振次数为100
for roll_num in range(100):
    result = die.roll()
    results.append(result)
    
print(results)
    