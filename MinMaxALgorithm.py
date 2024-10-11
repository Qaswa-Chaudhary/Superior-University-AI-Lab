# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 07:55:04 2024

@author: TOSHIBA
"""

import math

scores = [1, 2, 3, 4, 5, 6, 7, 8]
tree_depth = math.log(len(scores), 2)

def minmax(curr_depth, curr_index, ismax):
    if curr_depth == tree_depth:
        return scores[curr_index]
    if ismax:
        return max(minmax(curr_depth + 1,  curr_index*2, False), minmax(curr_depth + 1, curr_index*2 + 1, False))
    else:
        return min(minmax(curr_depth + 1,  curr_index*2, True), minmax(curr_depth + 1, curr_index*2 + 1, True))

result = minmax(0, 0, True)
print(result)