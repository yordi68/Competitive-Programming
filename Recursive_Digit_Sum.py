#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    
    def new(n,k):
        if len(n) == 1:
            m = int(n) * k
            m = str(m)
            val = 0
            for char in m:
                val += int(char)
            return val
        val = 0
        for char in n:
            val += int(char)

        num = new(str(val) , k)
        return num
            
        
    return new(n , k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
