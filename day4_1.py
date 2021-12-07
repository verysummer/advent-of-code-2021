# -*- coding: utf-8 -*-

# AoC 2021 Day 4

import os
import numpy as np

os.chdir('C:/Users/Profil/Documents/adventofcode/2021/advent-of-code-2021/')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')


# open input
f = open('input4.txt','r')
lines  = f.readlines()

numbers = lines[0]

# prepare dict with boards 

boards = {}
curr_board = []
board_cnt = -1

for line in lines:
    if line != '\n':
        if ',' in line:
            numbers = list(map(int,line.split(','))) # numbers to draw
        else:
            curr_board.append(line.split())        
    else:
        curr_board = np.array(curr_board)
        #curr_board = curr_board.astype(int)
        boards[board_cnt] = curr_board
        curr_board = []
        board_cnt += 1
        continue
del boards[-1]

# draw numbers
bingo = False

for number in numbers:
    if not(bingo):
        for board in boards.keys():
            curr_board = boards[board]
            # find number in board and if found substitute with 'x'
            if str(number) in curr_board:
                curr_board = np.where(curr_board==str(number), 'x', curr_board) 
                
                # check whether bingo
                [row,col] = np.where(curr_board=='x') # coordinates for 'x'
                # if same number occurs 5 times in a row or column
                if 5 in np.bincount(row) or 5 in np.bincount(col):
                    print('BINGO!')
                    bingo = True
                    my_number = number
                    break
                
                # save changed board to boards
                boards[board] = curr_board
    else:
        break
    
# calculate score
score = 0
for number in np.nditer(curr_board):
    if np.char.isnumeric(number):
        #print(number)
        score += int(number)
print(score*my_number)