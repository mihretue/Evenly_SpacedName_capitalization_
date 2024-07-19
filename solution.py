import sys
import os
import random
import re
import math
def solve(s):
    names = s.split()
    #giving capital for each word
    capital_names = [name.capitalize() for name in names]
    # print(capital_names)
    
    
    #new format after they are capitalized
    each_name = []
    for word in capital_names:
        each_name.append(word)
    full_name = ' '.join(each_name)
    #printing the full name basestring
    return(full_name)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    
    fptr.close()