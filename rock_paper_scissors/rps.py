#!/usr/bin/python

import sys
import math
import copy

options = [['rock'], ['paper'], ['scissors']]


def rock_paper_scissors(n):
    global options
    if n == 0:
        return [[]]
    if n == 1:
        return options

    else:
        rock = rock_paper_scissors(n-1)
        paper = copy.deepcopy(rock)
        scissors = copy.deepcopy(rock)
        for i in range(len(rock)):
            rock[i].insert(0, 'rock')
            paper[i].insert(0, 'paper')
            scissors[i].insert(0, 'scissors')

        answer = []

        answer.extend(rock)
        answer.extend(paper)
        answer.extend(scissors)

        return answer


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

# ````````````````````````````````````````````
        # for j in paper:
        #     j.insert(0, 'paper')
        # for k in scissors:
        #     j.insert(0, 'scissors')
# ````````````````````````````````````````````
        # for i in working_list[:len(working_list)/3]:

        # combos = []

        # for i in range(3**n):
        #     combos.append([])

        # while n > 0:
        #     for i in range(len(combos)):
        #         combos[i].append(options[math.floor(i/(3**n)) if math.floor(i/(3**n)) < 2 else math.floor(i/(3**n)) // 3])
        #     n -= 1

# print(rock_paper_scissors(5))
# print(rock_paper_scissors(4))
# print(rock_paper_scissors(3))
# print(rock_paper_scissors(4))
# print(rock_paper_scissors(1))
# print(rock_paper_scissors(0))
