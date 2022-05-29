# -*- coding: utf-8 -*-
"""
Created on Thu May 12 14:50:00 2022

@author: salman
"""
import numpy as np


def max_contig_subarr(arg):
    if len(arg) == 1:
        return 0, 0
    left = 0
    right = 0
    curr_left = 0
    curr_right = 0
    curr_max = -9999
    curr_sum = arg[curr_left]
    sum_arr = [0]*len(arg)
    sum_arr[0] = arg[0]
    for i in range(1, len(arg)):
        sum_arr[i] = sum_arr[i - 1] + arg[i]
    print(sum_arr)
    for i in range(1, len(arg)):
        curr_sum += arg[i]
        if curr_sum >= curr_max:
            curr_right = i
            curr_max = curr_sum
            left = curr_left
            right = curr_right
        elif curr_sum <= 0:
            curr_left = i
            curr_right = i
            curr_sum = arg[i]
    return left, right


if __name__ == '__main__':
    arg = list(np.random.randint(-50, 30, 20))
    print(arg)
    left, right = max_contig_subarr(arg)
    print(left, right)
    print(arg[left:right + 1])
    print(np.sum(arg[left:right + 1]))
