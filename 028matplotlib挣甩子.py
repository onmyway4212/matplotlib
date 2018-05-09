# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 10:52:16 2018

@author: Administrator
"""
import matplotlib.pyplot as plt
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


input_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
plt.plot(input_values, frequencies, linewidth=5)
plt.title('two D6 in 1000 times', fontsize=16)  
plt.xlabel('value', fontsize=12)           
plt.ylabel('result', fontsize=12)

plt.tick_params(axis='both', labelsize=12) 
plt.show() 