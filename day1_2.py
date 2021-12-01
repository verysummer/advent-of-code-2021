# -*- coding: utf-8 -*-

# AoC 2021 Day 1

import os

os.chdir('C:/Users/Profil/Documents/adventofcode/2021/advent-of-code-2021/')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')


# open input
f = open('input1.txt','r')
lines  = f.readlines()

data = list(map(int, lines)) 


sum_of_3 = []
for i in range(1,len(data)-1):
    sum_of_3.append(data[i-1] + data[i] + data[i+1])

cnt = 0
for sumi in range(len(sum_of_3)-1):    
    if sum_of_3[sumi] < sum_of_3[sumi+1]:
        cnt += 1
        
        
print(cnt)