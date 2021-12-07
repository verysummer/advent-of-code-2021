# -*- coding: utf-8 -*-

# AoC 2021 Day 3

import os

os.chdir('C:/Users/Profil/Documents/adventofcode/2021/advent-of-code-2021/')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')


# open input
f = open('input3.txt','r')
lines  = f.readlines()

# sum occurences of 1
sums = []
for digit in range(len(lines[0])-1): # -1 because \n
    curr_sum = 0
    for line in lines:
        curr_sum += int(line[digit]) # sum up all numbers at that digit -> how many 1s
    #print(curr_sum)
    # save all sums
    sums.append(curr_sum)
        
# gamma and epsilon rates (most and least common bit)
gamma = ''
epsilon = ''
for num_ones in sums:
    # if sum is larger than half of lines -> more 1s than 0s
    if num_ones > len(lines)/2:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'

power = int(gamma,2) * int(epsilon,2)
print(power)


# part 2 

new_lines = []
for bit in range(len(gamma)):
    for line in lines: 
        if line[bit] == gamma[bit]:
            


