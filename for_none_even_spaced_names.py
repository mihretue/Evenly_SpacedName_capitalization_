import sys
import os
import random
import re
import math


def solve(s):
    # Write your code here
    capital_names = [char.upper() if (i == 0 or s[i-1]==' ') else char for i, char in enumerate(s)]
    
    fullname_after_capitalization = ''.join(capital_names)
    
    return fullname_after_capitalization

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    
    fptr.close()