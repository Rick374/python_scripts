#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    counter = 0
    for i in range(len(q)):
        if q[i] > abs(i+3):
            return(print ("Too chaotic"))
        if q[i] != i+1:
            counter += 1
    if q[len(q)-1] == len(q)/2
        counter += 1
    return (print(counter-2))

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
