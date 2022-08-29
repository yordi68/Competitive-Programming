#!/bin/python3

import math
import os
import random
import re
import sys



def countSwaps(a):
    
    i = 0
    numSwaps = 0
    while i <= n -1:
        j = i + 1
        while j <= n - 1:
            if a[j] < a[i]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
                numSwaps += 1
            j += 1
        i += 1
    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a) - 1]}")


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
