# -*- coding: utf-8 -*-

# AoC 2021 Day 2

import os

os.chdir('C:/Users/Profil/Documents/adventofcode/2021/advent-of-code-2021/')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')


# open input
f = open('input2.txt','r')
lines  = f.readlines()

data = []
for line in lines:
    data.append(line.split())

horizontal = 0
depth = 0
aim = 0
for instruction in data:
    if instruction[0] == 'forward':
        horizontal += int(instruction[1])
        depth += (aim * int(instruction[1]))
    elif instruction[0] == 'down':
        aim += int(instruction[1])
    elif instruction[0] == 'up':
        aim -= int(instruction[1])
    
print(horizontal*depth)