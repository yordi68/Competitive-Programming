#!/bin/python3

import math
import os
import random
import re
import sys
def insertionSort1(n, arr):
    # Write your code here
    n = len(arr) - 1
    tmp = arr[len(arr) - 1]
    for j in range(n,0,-1):
        if tmp > arr[j -1]:
            arr[j] = tmp
            for item in arr:
                print(item,end=" ")
            print("")
            break
        else:
            arr[j] = arr[j -1]
            for item in arr:
                print(item,end=" ")
            print("")
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
