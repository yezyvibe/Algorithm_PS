#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minNum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER samDaily
#  2. INTEGER kellyDaily
#  3. INTEGER difference
#

def minNum(samDaily, kellyDaily, difference):
    # Write your code here
    
    samSolved = difference
    kellySolved = 0
    days = 0
    if kellySolved > samSolved:
        return days
    if samDaily >= kellyDaily:
        return - 1
    while samSolved >= kellySolved:
        days += 1
        samSolved += samDaily
        kellySolved += kellyDaily
    return days
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    samDaily = int(input().strip())

    kellyDaily = int(input().strip())

    difference = int(input().strip())

    result = minNum(samDaily, kellyDaily, difference)

    fptr.write(str(result) + '\n')

    fptr.close()
