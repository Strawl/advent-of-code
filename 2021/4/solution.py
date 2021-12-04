import numpy as np
import re
with open("input.txt", "r") as f:
    bingo_input = [int(x) for x in f.readline().strip().split(",")]
    bingoboards = [[int(i) for i in re.sub(' +', ' ',x.strip()).split(" ")] for x in f.readlines() if x.strip() != '']
    bingoboards = np.reshape(np.array(bingoboards),(int(len(bingoboards)/5),5,5))
    marking = np.zeros(shape=bingoboards.shape)
    for num in bingo_input:
        marking = np.where(bingoboards == num, 1, marking)
        bingo_vertical = np.where(np.sum(marking,axis=1) == 5)
        bingo_horizontal = np.where(np.sum(marking,axis=2) == 5)
        if bingo_vertical[0].size != 0:
            sum = np.sum(bingoboards[bingo_vertical[0][0]],where=marking[bingo_vertical[0][0]] == 0)
            print(sum*num)
            break
        if bingo_horizontal[0].size != 0:           
            sum = np.sum(bingoboards[bingo_horizontal[0][0]],where=marking[bingo_horizontal[0][0]] == 0)
            print(sum*num)
            break

with open("input.txt", "r") as f:
    # read input 
    bingo_input = [int(x) for x in f.readline().strip().split(",")]
    bingoboards = [[int(i) for i in re.sub(' +', ' ',x.strip()).split(" ")] for x in f.readlines() if x.strip() != '']
    # put it into numpy
    bingoboards = np.reshape(np.array(bingoboards),(int(len(bingoboards)/5),5,5))
    marking = np.zeros(shape=bingoboards.shape)
    last = 0
    for num in bingo_input:
        # get all the boards, where someone has won vertically
        bingo_vertical = np.where(np.sum(marking,axis=1) == 5)

        # delete all those boards
        bingoboards = np.delete(bingoboards,bingo_vertical[0],axis=0)
        marking = np.delete(marking,bingo_vertical[0], axis=0)

        # get all the boards, where someone has won horizontally
        bingo_horizontal = np.where(np.sum(marking,axis=2) == 5)

        # delete all those boards
        bingoboards = np.delete(bingoboards,bingo_horizontal[0],axis=0)
        marking = np.delete(marking,bingo_horizontal[0],axis=0)

        # Cross every number, that has the 'num' number
        marking = np.where(bingoboards == num, 1, marking)

        # If it's the last board, start calculating the score
        if marking.shape[0] == 1:
            last = np.sum(bingoboards,where=marking == 0) * num
    print(last)