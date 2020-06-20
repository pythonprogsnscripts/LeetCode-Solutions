import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    up = 0
    level = 0
    for u in s:
        if u == 'U':
            up += 1
            print("Up -->",up)
        else:
            up -= 1
            print("Down -->",up)
        if up == 0 and u == 'U':
            level += 1    
    return level


if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)