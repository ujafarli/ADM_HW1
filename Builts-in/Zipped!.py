#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    a, b = map(int, input().split()) 

# New array and append inputs
    arr = []
    for _ in range(a):
        arr.append(list(map(int, input().rstrip().split())))
# Sorting
    k = int(input())
    arr.sort(key=lambda x: x[k])
# Print line by line
    for i in arr:
        print(*i, sep=' ')
