def mystery_function(word):
    start = 0
    end = len(word) - 1
    
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1

    return True

word = "kayak"
result = mystery_function(word)

print(result)

def sum_matrix(matrix):
    total = 0  # Initialize total
    row_length = len(matrix[0]) 
    for row in matrix:
        for j in range(row_length):
            if row[j] > 0:  # Check if the number is positive
                total += row[j]
    return total




def get_sum_of_odds(matrix):
    # Write your code here
    total_num_odds = 0
    total_sum = 0
    if not matrix:
        return [0, 0]
    row_length = len(matrix[0])

    for row in matrix:
        for i in range(row_length):
            if row[i] % 2 == 1:
                total_num_odds += 1
                total_sum += row[i]
    return [total_num_odds, total_sum]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(get_sum_of_odds(matrix))

matrix = [
    [10, -2],
    [-3, 5],
    [4, 8]
]
print(get_sum_of_odds(matrix))

matrix = []
print(get_sum_of_odds(matrix))


#!/bin/python3

from itertools import filterfalse
import math
import os
import random
import re
import sys
import ast
from tabnanny import check

#
# Complete the 'can_place_flowers' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY flowerbed
#  2. INTEGER n
#

def can_place_flowers(flowerbed, n):
    # Write your code here
    if not flowerbed:
        return False

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i-1] == 0)
            empty_right = (i == (len(flowerbed) - 1)) or (flowerbed[i + 1] == 0)
            if empty_left and empty_right:
                n -=1
                flowerbed[i] = 1
                if n == 0:
                    return True
    return False

flowerbed = [1,0,0,0,1]
n = 1 # true
print(can_place_flowers(flowerbed, n))

flowerbed = [1,0,0,0,1]
n = 2 # false
print(can_place_flowers(flowerbed, n))



#!/bin/python3

import math
import os
import random
import re
import sys
import ast

#
# Complete the 'merge_sorted_lists' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY lst1
#  2. INTEGER_ARRAY lst2
#

def merge_sorted_lists(lst1, lst2):
    # Write your code here
    nums1_pointer = 0
    nums2_pointer = 0
    mergedlst = []

    while nums1_pointer < len(lst1) and nums2_pointer < len(lst2):
        if lst1[nums1_pointer] < lst2[nums2_pointer]:
            mergedlst.append(lst1[nums1_pointer])
            nums1_pointer += 1
        else:
            mergedlst.append(lst2[nums2_pointer])
            nums2_pointer += 1

    while nums1_pointer < len(lst1):
        mergedlst.append(lst1[nums1_pointer])
        nums1_pointer += 1
    while nums2_pointer < len(lst2):
        mergedlst.append(lst2[nums2_pointer])
        nums2_pointer += 1
    return mergedlst

lst1 = [1,3,5]
lst2 = [2,4,6]
print(merge_sorted_lists(lst1, lst2))

string1 = "yellow"
string2 = "screaming"

final_string1 = string1[:4] + string2[-3:]
print(final_string1)

def check_pal(s):
    left,right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

result = check_pal("racecar")
print(result)

result = check_pal(" ")
print(result)

def seq_function(s):
    sequence = "aeiouAEIOU"
    result =""

    for char in s:
        if char not in sequence:
            result += char

    return result
result = seq_function("CodePath")
print(result)

#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'rotate_matrix' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY matrix as parameter.
#

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_matrix(matrix))


# The function accepts following parameters:
#  1. STRING word1
#  2. STRING word2

def merge_alternately(word1, word2):
    mergedlst = []
    word1_pointer = 0
    word2_pointer = 0
    
    while word1_pointer < len(word1) and word2_pointer < len(word2):
        mergedlst.append(word1[word1_pointer])
        word1_pointer += 1
        mergedlst.append(word2[word2_pointer])
        word2_pointer += 1
    
    while word1_pointer < len(word1):
        mergedlst.append(word1[word1_pointer])
        word1_pointer += 1
    
    while word2_pointer < len(word2):
        mergedlst.append(word2[word2_pointer])
        word2_pointer += 1
    
    return ''.join(mergedlst)

# Test cases
print(merge_alternately("abc", "zyx"))  # Expected output: "azbycx"
print(merge_alternately("abcd", "xyz"))  # Expected output: "axbyczd"
print(merge_alternately("abc", "wxyz"))  # Expected output: "awbxcxyz"
print(merge_alternately("", "xyz"))  # Expected output: "xyz"
print(merge_alternately("abc", ""))  # Expected output: "abc"

#!/bin/python3

import math
import os
import random
import re
import sys
import ast
# Complete the 'find_value_index' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY matrix
#  2. INTEGER value

def find_value_index(matrix, value):
    # Write your code here
    n = len(matrix)
    for i in range(n):
        for j in range(len(matrix[i])):  
            if matrix[i][j] == value:
                return [i,j]
   
    return [-1,-1]

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
value = 12
print(find_value_index(matrix, value)) # ouput [2,3]